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
        about_me_text = """
        I am Sergio Pessoa, a Brazilian Computer Engineer who graduated from UFPE, currently working as a Data Scientist for the Brazilian football club Atletico Mineiro.
        
        In the past 5 years, I've been working as a Data Scientist on top-level projects. My main technical skills are Python, Machine Learning, Data Visualization, and Statistics, and I have experience with data problems in various areas, such as financial markets and sports.
        
        Studying the state-of-the-art of Data Science and Analytics is more than a job for me, it's also a hobby. I'm a big enthusiast of research and I like to develop a lot of side projects to train my skills.
        """
        st.header("About Me")
        st.write(about_me_text)

# Function to load the "Resume" tab
def load_resume():
    with tab2:
        st.header("Resume")
        
        st.subheader("Experience")
        # Clube Atlético Mineiro
        st.write("**Data Scientist** at **Clube Atlético Mineiro** | February 2024 - Now | Belo Horizonte - MG, Brazil")
        st.write("- **Statistical Data Analysis**: Development of an algorithm to calculate probabilities of winning a football championship, and development of a dashboard to track the results, using Python and Statistical concepts.")
        st.write("- **Machine Learning**: Using Python and SkLearn, I developed an algorithm to estimate the valuation of a football player, based on Machine Learning Algorithms such as random forest and linear regression.")
        st.write("- **Monte Carlo Simulation**: Developed a Monte Carlo Simulation model to estimate how many points a team deserved to win in a past game.")
        
        # Insight Sport
        st.write("**Data Scientist** at **Insight Sport** | December 2022 - February 2024 | London, UK (Remote)")
        st.write("- **Data Engineering**: Collection and preprocessing of Skillcorner and Statsbomb data. This resulted in the creation of a unified Database stored in Amazon AWS, with Event and Tracking Data from football games ready to be used in the modeling.")
        st.write("- **Data Analysis**: Development of a Streamlit App containing the view of football plays, created in chart format with Matplotlib.")
        
        # XP Inc.
        st.write("**Data Analysis Intern** at **XP Inc.** | August 2021 - November 2022 | São Paulo - SP, Brazil (Remote)")
        st.write("- **Natural Language Processing**: Developed an algorithm to standardize the ticker names of companies listed on the Brazilian Stock Exchange.")
        st.write("- **Data Analysis**: Used Python to automate the generation of a pdf report, using the libraries Fpdf and Matplotlib.")
        
        # Pernambuco Brewery - Ambev
        st.write("**Data Science Intern** at **Pernambuco Brewery - Ambev** | April 2021 - August 2021 | Itapissuma - PE, Brazil")
        st.write("- **Deep Learning**: Developed a Convolutional Neural Network to count the number of beer cans lost during the line of production.")
        
        # Reciprev/UFPE project
        st.write("**Data Researcher** at **Reciprev/UFPE project** | January 2020 - February 2021 | Recife - PE, Brazil")
        st.write("- **Data Analysis**: Development of a dashboard using R, containing analysis of financial derivatives data and portfolio optimization techniques, such as Markowitz. The dashboard was bought by a Brazilian company that works with pension funds.")
        
        st.subheader("Education")
        st.write("Bachelor in **Computer Engineering** | 2017 - 2022 | Federal University of Pernambuco (UFPE), Recife, Brazil")
        st.write("- Average: 8.42 of 10")

# Function to load the "Portfolio" tab
def load_portfolio():
    with tab3:
        st.header("Projects")
        
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
    st.set_page_config(layout="wide", page_title="Sergio Pessoa", page_icon=":briefcase:")

    # Load profile picture
    profile_pic = Image.open("images/profile_pic.jpg")  # Replace with your profile picture path

    # Load sidebar
    load_sidebar(profile_pic)

    # Centered section with tabs
    global tab1, tab2, tab3, tab4
    tab1, tab2, tab3, tab4 = st.tabs(["About Me", "Resume", "Projects", "Contact"])

    # Load tabs
    load_about_me()
    load_resume()
    load_portfolio()
    load_contact()

# Run the app
if __name__ == "__main__":
    main()