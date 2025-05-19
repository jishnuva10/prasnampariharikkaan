

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import streamlit as st
import random
from streamlit.components.v1 import html

# ========== CONFIGURATION ==========
SENDER_EMAIL = "jishnupaaru6@gmail.com"
SENDER_PASSWORD = "djifhhmtxnodgzyr"  # App password
RECEIVER_EMAIL = "archanaoppa@gmail.com"
CC_EMAIL = "jishnuva10@gmail.com"
YT_LINKS = [
    'https://www.youtube.com/shorts/q3Nj9ZMSw4I',
    'https://www.youtube.com/shorts/auOkm_cRLRs',
    'https://www.youtube.com/shorts/AfLMDBPCNZw',
    'https://www.youtube.com/shorts/V5_6UZlyE78',
    'https://www.youtube.com/shorts/vsBBgKri7lY',
    'https://www.youtube.com/shorts/MplgciJ_yl4',
    'https://www.youtube.com/shorts/xFpzo9yqICU',
    'https://www.youtube.com/shorts/XtzKPfM9dZo',
    'https://www.youtube.com/shorts/wdW4TcuQ0R4',
    'https://www.youtube.com/shorts/yK8WruDdXpI',
    'https://www.youtube.com/shorts/L-itTxuQDeY',
    'https://www.youtube.com/shorts/JY0sf5BVPNw',
    'https://www.youtube.com/shorts/cr4MbL06Ss8',
    'https://www.youtube.com/shorts/ytQb8Hb8X_c',
    'https://www.youtube.com/shorts/CO0JThyeCpk',
    'https://www.youtube.com/shorts/rX4M0E6zZ0s',
    'https://www.youtube.com/shorts/xLMszPzJbSU',
    'https://www.youtube.com/shorts/Jwdt5dE1MbY',
    'https://www.youtube.com/shorts/5ofunM5Jef8',
    'https://www.youtube.com/shorts/fYRtBD4lP7w',
    'https://www.youtube.com/shorts/GONIiCa0oAc',
    'https://www.youtube.com/shorts/jIi4BPJE-zU',
    'https://www.youtube.com/shorts/1CBHltCErZc',
    'https://www.youtube.com/shorts/q3OTehN1ulM',
    'https://www.youtube.com/shorts/xLbXDy3LvdU',
    'https://www.youtube.com/shorts/1HCtOWgJOFY',
    'https://www.youtube.com/shorts/JW8LmQlcjmM',
    'https://www.youtube.com/shorts/1Bjj_MJNzZs',
    'https://www.youtube.com/shorts/cnNqtPB6vBA',
    'https://www.youtube.com/shorts/KiXXdGxInR0',
    'https://www.youtube.com/shorts/7MVWvpqQKfg',
    'https://www.youtube.com/shorts/jVKOwccS2Fw',
    'https://www.youtube.com/shorts/NHeofs_1WhQ',
    'https://www.youtube.com/shorts/T3In7w-Lgk8',
    'https://www.youtube.com/shorts/zqnFQX-swbw',
    'https://www.youtube.com/shorts/qgui9jtTFXI',
    'https://www.youtube.com/shorts/v5X79vo7j5c',
    'https://www.youtube.com/shorts/v5X79vo7j5c',
    'https://www.youtube.com/shorts/v5X79vo7j5c',
    'https://www.youtube.com/shorts/v5X79vo7j5c',
    'https://www.youtube.com/shorts/v5X79vo7j5c'


]

# ========== COLOR SCHEME MANAGEMENT ==========
if 'color_scheme' not in st.session_state:
    st.session_state.color_scheme = {
        'primary': '#3498db', 
        'secondary': '#2980b9', 
        'accent': '#e74c3c', 
        'bg': '#f8f9fa',
        'name': "Blue Energy"
    }

def get_random_color_scheme():
    schemes = [
        {'primary': '#3498db', 'secondary': '#2980b9', 'accent': '#e74c3c', 'bg': '#f8f9fa', 'name': "Blue Energy"},
        {'primary': '#2ecc71', 'secondary': '#27ae60', 'accent': '#e67e22', 'bg': '#ecf0f1', 'name': "Green Growth"},
        {'primary': '#9b59b6', 'secondary': '#8e44ad', 'accent': '#f1c40f', 'bg': '#f9f9f9', 'name': "Purple Passion"},
        {'primary': '#1abc9c', 'secondary': '#16a085', 'accent': '#d35400', 'bg': '#f0f3f4', 'name': "Teal Serenity"},
        {'primary': '#34495e', 'secondary': '#2c3e50', 'accent': '#c0392b', 'bg': '#f5f6f7', 'name': "Dark Professional"},
        {'primary': '#e74c3c', 'secondary': '#c0392b', 'accent': '#3498db', 'bg': '#fef5f5', 'name': "Red Alert"},
        {'primary': '#f39c12', 'secondary': '#d35400', 'accent': '#9b59b6', 'bg': '#fff9e6', 'name': "Sunshine"}
    ]
    return random.choice(schemes)

def inject_custom_css(color_scheme):
    st.markdown(f"""
    <style>
        .stApp {{
            background-color: {color_scheme['bg']};
            transition: all 0.5s ease;
        }}
        h1, h2, h3 {{
            color: {color_scheme['primary']} !important;
        }}
        .stTextInput input, .stTextArea textarea {{
            border: 1px solid {color_scheme['secondary']} !important;
        }}
        .stSelectbox:first-of-type div {{
            border: 1px solid {color_scheme['secondary']} !important;
        }}
        .stButton>button {{
            background-color: {color_scheme['primary']} !important;
            color: white !important;
            border: none !important;
        }}
        .stButton>button:hover {{
            background-color: {color_scheme['secondary']} !important;
        }}
        .stForm {{
            border: 1px solid {color_scheme['secondary']} !important;
            border-radius: 10px;
            padding: 20px;
            background-color: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        .stAlert {{
            border-left: 4px solid {color_scheme['accent']} !important;
        }}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        .yt-container {{
            margin: 20px 0;
            text-align: center;
        }}
        .yt-link {{
            display: inline-block;
            background-color: #FF0000;
            color: white !important;
            padding: 10px 15px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 10px;
        }}
    </style>
    """, unsafe_allow_html=True)

def send_email(problem, details, category, solution):
    subject = f"Problem Resolution: {problem[:30]}..." if len(problem) > 30 else f"Problem Resolution: {problem}"
    random_yt_link = random.choice(YT_LINKS)
    
    html_body = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: {st.session_state.color_scheme['bg']};
                }}
                .header {{
                    color: {st.session_state.color_scheme['primary']};
                    border-bottom: 2px solid {st.session_state.color_scheme['accent']};
                    padding-bottom: 10px;
                }}
                .card {{
                    background-color: #fff;
                    padding: 15px;
                    border-radius: 8px;
                    margin-bottom: 15px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    border-left: 4px solid {st.session_state.color_scheme['secondary']};
                }}
                .accent {{
                    color: {st.session_state.color_scheme['accent']};
                }}
                .yt-container {{
                    margin: 20px 0;
                    text-align: center;
                }}
                .yt-link {{
                    display: inline-block;
                    background-color: #FF0000;
                    color: white !important;
                    padding: 10px 15px;
                    border-radius: 5px;
                    text-decoration: none;
                    font-weight: bold;
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div style="padding: 20px;">
                <h2 class="header">Aakramanam Onninum Oru Parihaaram Alla</h2>
                
                <div class="card">
                    <h3 style="color: {st.session_state.color_scheme['primary']};">Problem Details</h3>
                    <p><strong>Entha Paaru vaave prasnam:</strong> {problem}</p>
                    <p><strong>Details:</strong> {details}</p>
                </div>
                
                <div class="card">
                    <h3 style="color: {st.session_state.color_scheme['primary']};">Analysis</h3>
                    <p><strong>Category:</strong> <span class="accent">{category}</span></p>
                </div>
                
                <div class="card" style="background-color: rgba({int(st.session_state.color_scheme['secondary'][1:3], 16)}, {int(st.session_state.color_scheme['secondary'][3:5], 16)}, {int(st.session_state.color_scheme['secondary'][5:7], 16)}, 0.1);">
                    <h3 style="color: {st.session_state.color_scheme['primary']};">Solution Proposed</h3>
                    <p>{solution}</p>
                </div>
                
                <div class="yt-container">
                    <h3 style="color: {st.session_state.color_scheme['primary']};">Here's something to cheer you up! ❤️</h3>
                    <a href="{random_yt_link}" class="yt-link" target="_blank">Watch YouTube Short</a>
                </div>
                
                <div style="text-align: center; margin-top: 30px; color: #7f8c8d; font-size: 0.9em;">
                    <p>With love,<br>Jishnu V A<br>+91 9995355951</p>
                    <p style="font-style: italic; color: {st.session_state.color_scheme['secondary']};">"Namukk Paranj Theerkkaam"</p>
                </div>
            </div>
        </body>
    </html>
    """
    
    text_body = f"""
    Problem: {problem}
    Details: {details}
    Category: {category}
    Solution: {solution}
    
    Cheer up video: {random_yt_link}
    
    Thanks and Regards,
    Jishnu V A
    +91 9995355951
    """
    
    try:
        message = MIMEMultipart("alternative")
        message["From"] = SENDER_EMAIL
        message["To"] = RECEIVER_EMAIL
        message["Subject"] = subject
        message["Cc"] = CC_EMAIL
        
        message.attach(MIMEText(text_body, "plain"))
        message.attach(MIMEText(html_body, "html"))
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(
                SENDER_EMAIL, 
                [RECEIVER_EMAIL, CC_EMAIL], 
                message.as_string()
            )
        return True, random_yt_link
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False, None

# ========== STREAMLIT UI ==========
st.set_page_config(page_title="Problem Solver", page_icon="💌", layout="centered")
inject_custom_css(st.session_state.color_scheme)

# Main form
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("Akramanam onninum oru parihaaram alla")
    st.markdown(f"""
    <div style="color:{st.session_state.color_scheme['secondary']}; font-style:italic; text-align:center;">
        Namukk Paranj Theerkkaam
    </div>
    """, unsafe_allow_html=True)

    with st.form("problem_form", clear_on_submit=True):
        problem = st.text_input("Entha Paaru vaave prasnam???", key="problem")
        details = st.text_area("Paruuttyyy Detail aayi para", height=100, key="details")
        
        options = [
            "Njan cheytha mandatharam", 
            "Oorkkenda karyam marannu poi", 
            "Pand paranjatho cheythatho kuthipokkal", 
            "Mood Swings", 
            "Veruthe Oru Rasathinu",
            "Paranja karyam cheyyathath",
            "Cheytha karyam Parayaathath"
        ]
        category = st.selectbox("Eth category aanu vaave ee prasnam????", options, key="category")
        
        solution = st.text_area("❤️❤️❤️❤️Namukk Pariharikkande... Entha Ippo solve Cheyyaan cheyya Paaaru vaave❤️❤️❤️❤️!!!!", height=100, key="solution")
        
        submitted = st.form_submit_button("Submit", type="primary", use_container_width=True)
        
        if submitted:
            if not all([problem, details, solution]):
                st.warning("Please fill all fields!")
            else:
                with st.spinner(f"Sending in {st.session_state.color_scheme['name']} theme..."):
                    success, yt_link = send_email(problem, details, category, solution)
                    if success:
                        st.success("Email sent successfully! Namukk ee issue vegam pariharikkaam... Love Youu!")
                        st.balloons()
                        
                        st.markdown(f"""
                        <div style="padding:15px; border-radius:10px; 
                                    border-left:4px solid {st.session_state.color_scheme['accent']};
                                    background:white; box-shadow:0 2px 8px rgba(0,0,0,0.1); margin-top:20px;">
                            <h3 style="color:{st.session_state.color_scheme['primary']};">Summary</h3>
                            <p><b>Problem:</b> {problem}</p>
                            <p><b>Details:</b> {details}</p>
                            <p><b>Category:</b> <span style="color:{st.session_state.color_scheme['accent']}">{category}</span></p>
                            <p><b>Solution:</b> {solution}</p>
                            <div class="yt-container">
                                <p><b>Video shared:</b> <a href="{yt_link}" target="_blank">{yt_link}</a></p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

# Theme changer button
st.markdown("""
<div style="position: fixed; bottom: 10px; right: 10px;">
    <button onclick="window.parent.document.querySelector('.stButton button').click()" 
            style="background-color: #f0f2f6; border: none; border-radius: 50%; width: 40px; height: 40px; cursor: pointer;">
        🎨
    </button>
</div>
""", unsafe_allow_html=True)

if st.button("Change Theme", key="theme_changer", help="Change color theme"):
    st.session_state.color_scheme = get_random_color_scheme()
    st.rerun()
