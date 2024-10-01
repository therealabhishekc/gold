import streamlit as st
import streamlit.components.v1 as html
from streamlit_option_menu import option_menu
import base64
from render_page import render_gold_breakdown, render_gold_scrap, render_dia_breakdown, render_ant_breakdown, render_hyd_breakdown

# page setup
st.set_page_config(
    page_title="Govindji's",
    page_icon="🌟",
    layout="wide"
)


# Function to load CSS from a file
def load_css(css_file):
    with open(css_file, "r") as file:
        css = file.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


def displayPDF(file):

    # download button
    with open(file, "rb") as f:
        st.download_button("Download Report", f, file)

    st.write()

    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    #Embedding PDF in HTML and centering it
    pdf_display = f'''
    <div style="display: flex; justify-content: center;">
        <iframe
            src="data:application/pdf;base64,{base64_pdf}#zoom=145" 
            width="1300" 
            height="1020" 
            type="application/pdf">
        </iframe>
    </div>
    '''
    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


# Function to render the content on each page
def render_page(page_name):
    if page_name == "scrap_gold":
        return render_gold_scrap()
    elif page_name == "gold_breakdown":
        return render_gold_breakdown()
    elif page_name == "hyd_breakdown":
        return render_hyd_breakdown()
    elif page_name == "ant_breakdown":
        return render_ant_breakdown()
    elif page_name == "dia_breakdown":
        return render_dia_breakdown()


# on_change callback
def on_change(key):
    pass


# Main function to set up the Streamlit app
def main():

    # Load the CSS file
    load_css("styles.css")

    output = st.query_params.get("output", None)

    if output:
        displayPDF('output.pdf')

    else:
        _, col, _ = st.columns([4,3,4])
        with col:
            st.image("images/logo.png")
            hide_img_fs = '''
            <style>
            button[title="View fullscreen"]{
                visibility: hidden;}
            </style>
            '''
            st.markdown(hide_img_fs, unsafe_allow_html=True)
            st.write("")

        view_pdf = False

        # Initialize selected3 in session_state if not already set
        if 'selected_option' not in st.session_state:
            st.session_state.selected_option = 0

        options_list = ["Scrap\nGold", "Gold\nBreakdown", "Hyderabadi\nBreakdown", "Antique\nBreakdown", "Diamond\nBreakdown"]

        selected3 = option_menu(
            menu_title=None,
            options=options_list, 
            icons=[None, None, None, None],
            menu_icon=None, 
            default_index=st.session_state.selected_option, 
            orientation="horizontal",
            on_change=on_change,
            key='nav_bar',
            styles={
                "container": {"padding": "0!important", 
                              "background-color": "#fafafa"},
                "icon": {"display": "none"}, 
                "nav-link": {"font-size": "15px", 
                             "font-family": "sans-serif",
                             "text-align": "center", 
                             "margin":"2px", 
                             "white-space": "pre-wrap",
                             "border-radius" : "10px",
                             "--hover-color": "#eee",
                             "padding" : "7px"
                },
                "nav-link-selected": {
                    "background": "linear-gradient(to right, #005C97 , #363795)", 
                    "font-weight": "bold", 
                    "color": "white" 
                },
            }
        )

        st.session_state.selected_option = options_list.index(selected3)

        if st.session_state.selected_option == 0:
            view_pdf = render_page('scrap_gold')
        if st.session_state.selected_option == 1:
            view_pdf = render_page('gold_breakdown')
        if st.session_state.selected_option == 2:
            view_pdf = render_page('hyd_breakdown')
        if st.session_state.selected_option == 3:
            view_pdf = render_page('ant_breakdown')
        if st.session_state.selected_option == 4:
            view_pdf = render_page('dia_breakdown')

        if view_pdf:
            st.link_button(
                "View Report",
                url=f"http://localhost:8501/?output={view_pdf}"
                #url=f"https://cu4k7r7zzzwfe8ru8skepo.streamlit.app/?output={view_pdf}"
            )


if __name__ == "__main__":
    main()

