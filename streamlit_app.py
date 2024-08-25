import streamlit as st

# The title
st.title("Introduction to HTML")

# Some text
st.write("HTML is a markup language used for building websites. HTML is also used to build web apps, e.g. web platforms (FaceBook, Instagram, Twitter, etc.).")

# Examples of what HTML can do (written in the Markdown counterpart of HTML, as Streamlit doesn't support HTML)

st.write("**HTML Examples:**")
st.write("**DISCLAMER:** This code is rendered using Streamlit's `markdown` function as Streamlit does not have HTML-first support.")
st.write("**1. Headings:**")
st.write("**Code:** `<h1 style='color: red;'>Hello, Streamlit!</h1>`4")
st.markdown(
    "<h1 style='color: red;'>Hello, Streamlit!</h1>",
    unsafe_allow_html=True
)

st.write("**2. Paragraphs:**")
st.write("**Note:** This does the same things as the markdown equivalent of typing without a specified prefix, e.g. `Hello Streamlit` and ***not*** `# Hello Streamlit`")
st.write("**Code:** `<p style='color: red';>Hello Streamlit!</p>`")
st.markdown(
    "<p style='color: red';>Hello, Streamlit!</p>",
    unsafe_allow_html=True
)

st.write("**3. Links:**")
st.write("**Code:** `<a href='https://streamlit.io' style='color: red;'>Streamlit</a>`")
st.markdown(
    "<a href='https://streamlit.io' style='color: red;'>Streamlit</a>",
    unsafe_allow_html=True
)

st.write("**4. Lists:**")
st.write("**Code:**\n
```html
<!-- Unordered List-->
<ul>
  <li style="color: red";> List Item </li>
</ul>
```
")
st.markdown(
    "<p style='color: red';>Hello, Streamlit!</p>",
    unsafe_allow_html=True
)
