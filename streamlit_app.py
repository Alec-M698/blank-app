import streamlit as st

# The title
st.title("Introduction to HTML")

# Some text
st.write("HTML is a markup language used for building websites. HTML is also used to build web apps, e.g. web platforms (Facebook, Instagram, Twitter, etc.).")


# Examples of what HTML can do (written in the Markdown counterpart of HTML, as Streamlit doesn't support HTML)
st.write("**HTML Examples:**")
st.write("**DISCLAIMER:** This code is rendered using Streamlit's `markdown` function as Streamlit does not have HTML-first support.")

# Headings
st.write("**1. Headings:**")
st.write("Headings are used to create titles and subtitles on a webpage. HTML provides six levels of headings, from `<h1>` to `<h6>`, with `<h1>` being the highest (or most important) level and `<h6>` the least.")
st.write("**Code:** `<h1 style='color: red;'>Hello, Streamlit!</h1>`")
st.markdown(
    "<h1 style='color: red;'>Hello, Streamlit!</h1>",
    unsafe_allow_html=True
)

# Paragraphs
st.write("**2. Paragraphs:**")
st.write("Paragraphs are used to define blocks of text. The `<p>` tag is used to create a paragraph. You can style paragraphs using CSS within the `style` attribute.")
st.write("**Note:** This does the same things as the markdown equivalent of typing without a specified prefix, e.g. `Hello Streamlit` and ***not*** `# Hello Streamlit`")
st.write("**Code:** `<p style='color: red;'>Hello Streamlit!</p>`")
st.markdown(
    "<p style='color: red;'>Hello, Streamlit!</p>",
    unsafe_allow_html=True
)

# Links
st.write("**3. Links:**")
st.write("Links are used to navigate from one webpage to another. The `<a>` tag defines a hyperlink, which is used to link from one page to another. The `href` attribute specifies the URL of the page the link goes to.")
st.write("**Code:** `<a href='https://streamlit.io' style='color: red;'>Streamlit</a>`")
st.markdown(
    "<a href='https://streamlit.io' style='color: red;'>Streamlit Link</a>",
    unsafe_allow_html=True
)

# Images
st.write("**4. Images:**")
st.write("Images are used to add visual content to a webpage. The `<img>` tag is used to embed an image in an HTML page. The `src` attribute specifies the path to the image, and the `alt` attribute provides alternative text for the image.")
st.write("**Code:** `<img src='https://via.placeholder.com/150' alt='Placeholder Image'>`")
st.markdown(
    "<img src='https://via.placeholder.com/150' alt='Placeholder Image'>",
    unsafe_allow_html=True
)

# Tables
st.write("**5. Tables:**")
st.write("Tables are used to display data in a tabular format. The `<table>` tag defines a table, `<tr>` defines a table row, `<th>` defines a table header, and `<td>` defines a table cell.")
st.write("**Code:** `<table><tr><th>Header 1</th><th>Header 2</th></tr><tr><td>Data 1</td><td>Data 2</td></tr></table>`")
st.markdown(
    """
    <table>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
        </tr>
    </table>
    """,
    unsafe_allow_html=True
)

# Forms
st.write("**6. Forms:**")
st.write("Forms are used to collect user input. The `<form>` tag is used to create an HTML form for user input. Inside the form, you can use various input elements like text fields, checkboxes, radio buttons, and submit buttons.")
st.write("**Code:** `<form><input type='text' placeholder='Enter text'><input type='submit'></form>`")
st.markdown(
    """
    <form>
        <input type='text' placeholder='Enter text'>
        <input type='submit'>
    </form>
    """,
    unsafe_allow_html=True
)

# Lists
st.write("**7. Lists:**")
st.write("Lists are used to group related items. HTML supports ordered lists (`<ol>`) and unordered lists (`<ul>`). Each list item is defined with the `<li>` tag.")
st.write("**Code:** `<ul><li>Item 1</li><li>Item 2</li></ul>`")
st.markdown(
    """
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
    """,
    unsafe_allow_html=True
)

# Div and Span
st.write("**8. Div and Span:**")
st.write("The `<div>` tag is a block-level container for grouping HTML elements, while the `<span>` tag is an inline container. Both can be styled using CSS.")
st.write("**Code:** `<div style='color: blue;'>This is a div</div>` and `<span style='color: green;'>This is a span</span>`")
st.markdown(
    """
    <div style='color: blue;'>This is a div</div>
    <span style='color: green;'>This is a span</span>
    """,
    unsafe_allow_html=True
)

# Quiz
st.write("**9. Quiz:**")
st.write("Test your knowledge of HTML with this quiz!")

# Question 1
st.write("**Question 1:** What does HTML stand for?")
answer1 = st.text_input("Your answer for Question 1:")

# Question 2
st.write("**Question 2:** Which tag is used to create a hyperlink in HTML?")
answer2 = st.text_input("Your answer for Question 2:")

# Question 3
st.write("**Question 3:** How many levels of headings does HTML provide?")
answer3 = st.text_input("Your answer for Question 3:")

# Question 4
st.write("**Question 4:** Which tag is used to define a table row?")
answer4 = st.text_input("Your answer for Question 4:")

# Question 5
st.write("**Question 5:** What attribute is used to specify the URL of a link?")
answer5 = st.text_input("Your answer for Question 5:")

# Question 6
st.write("**Question 6:** Which tag is used to create an unordered list?")
answer6 = st.text_input("Your answer for Question 6:")

# Question 7
st.write("**Question 7:** What tag is used to embed an image in an HTML page?")
answer7 = st.text_input("Your answer for Question 7:")

# Question 8
st.write("**Question 8:** Which tag is used to create a form in HTML?")
answer8 = st.text_input("Your answer for Question 8:")

# Question 9
st.write("**Question 9:** What is the difference between `<div>` and `<span>` tags?")
answer9 = st.text_input("Your answer for Question 9:")

# Question 10
st.write("**Question 10:** Which tag is used to define a list item?")
answer10 = st.text_input("Your answer for Question 10:")

# Question 11
st.write("**Question 11:** How do you specify alternative text for an image?")
answer11 = st.text_input("Your answer for Question 11:")

# Question 12
st.write("**Question 12:** What tag is used to create a table header?")
answer12 = st.text_input("Your answer for Question 12:")

# Question 13
st.write("**Question 13:** Which attribute is used to style HTML elements?")
answer13 = st.text_input("Your answer for Question 13:")

# Question 14
st.write("**Question 14:** What tag is used to create an ordered list?")
answer14 = st.text_input("Your answer for Question 14:")

# Question 15
st.write("**Question 15:** How do you create a text input field in a form?")
answer15 = st.text_input("Your answer for Question 15:")

if st.button("Submit"):
    if answer1.lower() == "hypertext markup language":
        st.success("Question 1: Correct!")
    else:
        st.error("Question 1: Wrong answer. Try again!")

    if answer2.lower() == "a" or answer2.lower() == "<a>":
        st.success("Question 2: Correct!")
    else:
        st.error("Question 2: Wrong answer. Try again!")

    if answer3 == "6":
        st.success("Question 3: Correct!")
    else:
        st.error("Question 3: Wrong answer. Try again!")

    if answer4.lower() == "tr" or answer4.lower() == "<tr>":
        st.success("Question 4: Correct!")
    else:
        st.error("Question 4: Wrong answer. Try again!")

    if answer5.lower() == "href":
         st.success("Question 5: Correct!")
    else:
        st.error("Question 5: Wrong answer. Try again!")

    if answer6.lower() == "ul" or answer6.lower() == "<ul>":
        st.success("Question 6: Correct!")
    else:
        st.error("Question 6: Wrong answer. Try again!")

    if answer7.lower() == "img" or answer7.lower() == "<img>":
        st.success("Question 7: Correct!")
    else:
        st.error("Question 7: Wrong answer. Try again!")

    if answer8.lower() == "form" or answer8.lower() == "<form>":
        st.success("Question 8: Correct!")
    else:
        st.error("Question 8: Wrong answer. Try again!")

    if "block-level" in answer9.lower() and "inline" in answer9.lower():
        st.success("Question 9: Correct!")
    else:
        st.error("Question 9: Wrong answer. Try again!")

    if answer10.lower() == "li" or answer10.lower() == "<li>":
        st.success("Question 10: Correct!")
    else:
        st.error("Question 10: Wrong answer. Try again!")

    if answer11.lower() == "alt attribute" or answer11.lower() == "alt":
        st.success("Question 11: Correct!")
    else:
        st.error("Question 11: Wrong answer. Try again!")

    if answer12.lower() == "th" or answer12.lower() == "<th>":
        st.success("Question 12: Correct!")
    else:
        st.error("Question 12: Wrong answer. Try again!")

    if answer13.lower() == "style":
        st.success("Question 13: Correct!")
    else:
        st.error("Question 13: Wrong answer. Try again!")

    if answer14.lower() == "ol" or answer14.lower() == "<ol>":
        st.success("Question 14: Correct!")
    else:
        st.error("Question 14: Wrong answer. Try again!")

    if answer15.lower() == "input" or answer15.lower() == "<input>":
        st.success("Question 15: Correct!")
    else:
        st.error("Question 15: Wrong answer. Try again!")

    
