import gradio as gr
from main import chain
from vector import retriver

def get_answer(question):
    if question.lower() == "q":
        return "👋 Exiting..."
    try:
        reviews = retriver.invoke(question)
        result = chain.invoke({"reviews": reviews, "question": question})
        return result
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

iface = gr.Interface(
    fn=get_answer,
    inputs=gr.Textbox(lines=2, placeholder="Ask about vegan options, offers, etc..."),
    outputs="text",
    title="🍕 Pizza Review Assistant",
    description="Ask anything about the pizza restaurant. The AI reads real reviews to answer!"
)

iface.launch()
