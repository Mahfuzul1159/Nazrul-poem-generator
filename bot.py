import streamlit as st
import google.generativeai as genai
import time

# ==============================
# Configure the Gemini API
# ==============================
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("API Key not found. Please add your GEMINI_API_KEY to the Streamlit secrets file.")
    st.stop()


# ==============================
# Core Poem Generation Function
# ==============================
def generate_poem_gemini(seed_line: str, max_tokens: int, temperature: float):
    """
    Generates a Bengali poem using the Gemini API with a specific poetic style.
    Instead of true streaming, we fetch the full poem first, then reveal line by line.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    আপনি একজন বাঙালি কবি, কাজী নজরুল ইসলামের বিদ্রোহী ঢঙে কবিতা লিখবেন।
    নিয়ম:
    1. প্রতিটি লাইন আলাদা লাইনে লিখবেন।
    2. কোনো লাইন ভেঙে অসম্পূর্ণ রাখবেন না।
    3. কবিতার শেষ লাইন অবশ্যই সম্পূর্ণ বাক্যে শেষ করবেন।

    You are a Bengali poet. Write a poem in strong, Nazrul-style language.
    Generate the poem one line at a time, like this:
    First line of poem
    Second line of poem
    
    ...
    Use this seed line to start:
    '{seed_line}'
    """

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "max_output_tokens": max_tokens,
                "temperature": temperature,
            },
            stream=False  
        )
        return response.text
    except Exception as e:
        st.error(f"API Error: {e}")
        return None


# ==============================
# Streamlit App
# ==============================
def main():
    st.set_page_config(page_title="বিদ্রোহী AI", page_icon="✍️", layout="wide")
    st.title("Create Poems like Kazi Nazrul Islam")
    st.markdown("---")
    st.markdown("Give a starting line, and the AI will generate a rebellious Nazrul-style poem.")

    if "full_poem" not in st.session_state:
        st.session_state.full_poem = ""

    seed_line = st.text_area("Write the first line of the poem:", height=70,
                             placeholder="যেমন: বল বীর, বল উন্নত মম শির!")

    st.sidebar.header("Settings")
    max_tokens = st.sidebar.slider("Length of the poem:", 100, 500, 300)
    temperature = st.sidebar.slider("Creativity:", 0.0, 1.0, 0.8)

    if st.button("Generate Poem", use_container_width=True, type="primary"):
        if not seed_line:
            st.error("Please enter a starting line.")
            return

        with st.spinner("Generating poem..."):
            full_text = generate_poem_gemini(seed_line, max_tokens, temperature)

            if full_text:
                # Reset previous poem
                st.session_state.full_poem = ""
                poem_placeholder = st.empty()

                # Clean + split into lines
                lines = [l.strip() for l in full_text.strip().split("\n") if l.strip()]
                for line in lines:
                    st.session_state.full_poem += line + "\n"
                    poem_placeholder.markdown(f"```\n{st.session_state.full_poem}\n```")
                    time.sleep(0.5)  # Reveal effect

                st.success("The poem is complete!")
            else:
                st.error("Could not create poem. Please try again.")

    

    
    # 👇 Signature at the bottom of sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div style='text-align: center; color: gray; font-size: 14px;'>
             Developed by <br>
            <a href="https://mahfuzul-islam-rafi-portfolio.netlify.app/#home" target="_blank">
            <b>Sheikh Mahfuzul Islam Rafi</b>
            </a>
        </div>
    """,
    unsafe_allow_html=True
    )

 

if __name__ == "__main__":
    main()
