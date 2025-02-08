import streamlit as st
from PIL import Image
import base64
from io import BytesIO

github_link = 'https://img.icons8.com/?size=30&id=62856&format=png&color=000000'
linkedin_link = 'https://img.icons8.com/?size=30&id=98960&format=png&color=000000'
medium_logo = "https://img.icons8.com/color/30/medium-logo.png"
kaggle_logo = "https://img.icons8.com/?size=30&id=1iP83OYM1FL-&format=png&color=000000"
twitter_logo = "https://img.icons8.com/?size=30&id=phOKFKYpe00C&format=png&color=000000"

linkedin_me = 'https://www.linkedin.com/in/sergio-pessoa-079317187/'
medium_me = 'https://medium.com/@sslp23'
github_me = 'https://github.com/sslp23'
kaggle_me = 'https://www.kaggle.com/sslp23/code'
twitter_me = 'https://x.com/sergiopessoa23'


# Function to convert image to base64
def profile_pic_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to load and display the sidebar
def load_sidebar(profile_pic):
    with st.sidebar:
        # Display rounded and centered profile picture
        st.markdown(
            """
            <style>
            .profile-img-container {
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }
            .profile-img {
                border-radius: 50%;
                width: 150px;
                height: 150px;
                object-fit: cover;
            }
            .centered-text {
                text-align: center;
                width: 100%;
            }
            .social-media-icons {
                text-align: center;
                width: 100%;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        # Use st.image to display the profile picture
        st.markdown(
            '<div class="profile-img-container">'
            f'<img src="data:image/png;base64,{profile_pic_to_base64(profile_pic)}" class="profile-img">'
            '</div>',
            unsafe_allow_html=True
        )

        # Centered name, email, and location
        st.markdown('<div class="centered-text"><h1>Sergio Pessoa</h1></div>', unsafe_allow_html=True)
        st.markdown('<div class="centered-text">Data Scientist</div>', unsafe_allow_html=True)
        #st.markdown('<div class="centered-text">Location: Brazil </div>', unsafe_allow_html=True)
        
        # Social media icons
        # Social media icons side by side
        
        st.markdown(
            f"""
            <div class="social-media-icons">
                <a href={linkedin_me}><img src={linkedin_link} alt="LinkedIn"></a>
                <a href={medium_me}><img src={medium_logo} alt="Medium"></a>
                <a href={kaggle_me}><img src={kaggle_logo} alt="Kaggle"></a>
                <a href={github_me}><img src={github_link} alt="GitHub"></a>
                <a href={twitter_me}><img src={twitter_logo} alt="GitHub"></a>
            </div>
            """,
            unsafe_allow_html=True
        )

# Function to load the "About Me" tab
def load_about_me():
    with tab1:
        st.header("About Me")
        st.write("""
        This is a mock-up text about me. In the future, I will replace this with the actual information.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """)

# Function to load the "Resume" tab
def load_resume():
    with tab2:
        st.header("Resume")
        
        st.subheader("Experience")
        st.write("""
        - Mock Job Title 1 at Mock Company 1 (2020-2022)
        - Mock Job Title 2 at Mock Company 2 (2018-2020)
        - Mock Job Title 3 at Mock Company 3 (2016-2018)
        - Mock Job Title 4 at Mock Company 4 (2014-2016)
        """)
        
        st.subheader("Education")
        st.write("""
        - Mock Degree 1 from Mock University 1 (2010-2014)
        - Mock Degree 2 from Mock University 2 (2008-2010)
        - Mock Degree 3 from Mock University 3 (2006-2008)
        - Mock Degree 4 from Mock University 4 (2004-2006)
        """)

# Function to load the "Portfolio" tab
def load_portfolio():
    with tab3:
        st.header("Portfolio")
        
        # Create a grid layout for projects
        cols = st.columns(3)
        
        for i in range(15):
            with cols[i % 3]:
                st.image("https://via.placeholder.com/150", width=100)
                st.write(f"Project {i+1}")
                st.markdown("[View Project](#)")

# Function to load the "Contact" tab
def load_contact():
    with tab4:
        st.header("Contact")
        st.write("Feel free to reach me anytime!")
        st.markdown(
            """
            <style>
            .social-media-left {
                text-align: left;
                width: 100%;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div class="social-media-left">
                <a href={linkedin_me}><img src={linkedin_link} alt="LinkedIn"></a>
                <a href={medium_me}><img src={medium_logo} alt="Medium"></a>
                <a href={kaggle_me}><img src={kaggle_logo} alt="Kaggle"></a>
                <a href={github_me}><img src={github_link} alt="GitHub"></a>
                <a href={twitter_me}><img src={twitter_logo} alt="GitHub"></a>
            </div>
            """,
            unsafe_allow_html=True
        )

# Main function
def main():
    # Set page configuration
    st.set_page_config(layout="wide", page_title="My Portfolio", page_icon=":briefcase:")

    # Load profile picture
    profile_pic = Image.open("images/profile_pic.jpg")  # Replace with your profile picture path

    # Load sidebar
    load_sidebar(profile_pic)

    # Centered section with tabs
    global tab1, tab2, tab3, tab4
    tab1, tab2, tab3, tab4 = st.tabs(["About Me", "Resume", "Portfolio", "Contact"])

    # Load tabs
    load_about_me()
    load_resume()
    load_portfolio()
    load_contact()

# Run the app
if __name__ == "__main__":
    main()