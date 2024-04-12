import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import webbrowser
from sharepy import connect


# page config
st.set_page_config(page_title="MEU LABS", page_icon="New Logo.png", layout="wide")


custom_sidebar = """
<div class="sidebar-container" style="padding: 0px; margin-top: -60px;">
<img src="https://meulabs.org/wp-content/uploads/2022/08/STEM-1.webp" alt="Image" style="width: 100px; height: 40px; margin-left:-10px;"> 

<h1 style="margin-top: 0;color: #F98F26;text-align: left; font-family: 'Arial', Times: serif; font-size: 40px;">MeuProject</h1>    
</div>
"""
# <img src="https://meulabs.org/wp-content/uploads/2022/08/STEM-1.webp" alt="Image" style="width: 100px; height: 40px; margin-top:-70px;  margin-right:700px;">
st.sidebar.markdown(custom_sidebar, unsafe_allow_html=True)

# Def subjects and homework
program_homework = {
    "Knowledge Explorers": {
        "KX1E40": [
            {"Homework": "3D Rocket Designing", "Deadline": "2024 - 04 - 07", "Resources": "http://tinyurl.com/ys4pmmhm","Sample":"t725.png"},
            {"Homework": "3D Rocket Designing - Team","Deadline": "2024-04-10", "Resources": "http://tinyurl.com/ys4pmmhm", "Video":"Rocket_Design_3D.mp4"},
            {"Homework": "Dance Party Programming","Deadline": "2024-04-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Ed6tedRykjhFk5qwx8kuLMsBavmYv9rmBD-FJvfJ7MQUWw?e=54ZDSv", "Video":"DanceParty.mp4"},
            {"Homework": "Name Animation Programming","Deadline": "2024-04-28", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"https://youtu.be/snVFZeRJAsw?si=RZjOIPMG02oGrggb"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-07", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O","Video":"RocketNG.mp4"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-14", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"RocketNG.mp4"},
            {"Homework": "Crew selection simulation", "Deadline": "2024-05-21", "Resources": "https://meulabslk.sharepoint.com/:p:/s/content/Ea9IWg1B7EZEsYNZt9j_NdIBZfWA5jK_ZMv6VnT9e8WNBg?e=PEvnSl","Sample":"CSG.PNG"},
            {"Homework": "Video Animation Story Board", "Deadline": "2024-05-28", "Resources":"", "Sample":"storyboard.png"},
            {"Homework": "Video Animation", "Deadline": "2024-06-07", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Video Editing", "Deadline": "2024-06-14", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Rover Stage 1", "Deadline": "2024-06-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/ESfnL-6SnG9OuEsykfxdsLMBDVD0HkyzkzElrozwWDQkig?e=eRfqGU","Video":"Rover stage 1.mp4"},
            {"Homework": "Rover Stage 2", "Deadline": "2024-06-28", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EZsHoRCn7OBOvg5GMs-otnEBCz40dmes5te4j-Gm7Wu0zw?e=pOszJv","Video":"Stage2.mp4"},
            {"Homework": "Rover Stage 3", "Deadline": "2024-07-07", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Eb4ufzD31iFKuTzWbEWBa7EBv4EOMFRHMnxZY1p2JHHTvw?e=HSfTGc","Video":"Stage4.mp4"},
            {"Homework": "Rover Stage 4", "Deadline": "2024-07-14", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EVanVe5qj39LmpySIAJtCmwBAJmlrDZSHe-W-4Fwqk7Z1g?e=HdBLYX","Video":"Stage4.mp4"},
            {"Homework": "Testimonial Video", "Deadline": "2024-07-21", "Resources": "","Video":"https://www.youtube.com/watch?v=PB9vafi87No"},
            #{"Homework": "Refelection", "Deadline": "2024-06-21", "Resources": "","Video":""}
        ],
        "KX1E41": [
           {"Homework": "3D Rocket Designing", "Deadline": "2024 - 04 - 07", "Resources": "http://tinyurl.com/ys4pmmhm","Sample":"t725.png"},
            {"Homework": "3D Rocket Designing - Team","Deadline": "2024-04-10", "Resources": "http://tinyurl.com/ys4pmmhm", "Video":"Rocket_Design_3D.mp4"},
            {"Homework": "Dance Party Programming","Deadline": "2024-04-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Ed6tedRykjhFk5qwx8kuLMsBavmYv9rmBD-FJvfJ7MQUWw?e=54ZDSv", "Video":"DanceParty.mp4"},
            {"Homework": "Name Animation Programming","Deadline": "2024-04-28", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"https://youtu.be/snVFZeRJAsw?si=RZjOIPMG02oGrggb"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-07", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O","Video":"RocketNG.mp4"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-14", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"RocketNG.mp4"},
            {"Homework": "Crew selection simulation", "Deadline": "2024-05-21", "Resources": "https://meulabslk.sharepoint.com/:p:/s/content/Ea9IWg1B7EZEsYNZt9j_NdIBZfWA5jK_ZMv6VnT9e8WNBg?e=PEvnSl","Sample":"CSG.PNG"},
            {"Homework": "Video Animation Story Board", "Deadline": "2024-05-28", "Resources":"", "Sample":"storyboard.png"},
            {"Homework": "Video Animation", "Deadline": "2024-06-07", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Video Editing", "Deadline": "2024-06-14", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Rover Stage 1", "Deadline": "2024-06-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/ESfnL-6SnG9OuEsykfxdsLMBDVD0HkyzkzElrozwWDQkig?e=eRfqGU","Video":"Rover stage 1.mp4"},
            {"Homework": "Rover Stage 2", "Deadline": "2024-06-28", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EZsHoRCn7OBOvg5GMs-otnEBCz40dmes5te4j-Gm7Wu0zw?e=pOszJv","Video":"Stage2.mp4"},
            {"Homework": "Rover Stage 3", "Deadline": "2024-07-07", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Eb4ufzD31iFKuTzWbEWBa7EBv4EOMFRHMnxZY1p2JHHTvw?e=HSfTGc","Video":"Stage4.mp4"},
            {"Homework": "Rover Stage 4", "Deadline": "2024-07-14", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EVanVe5qj39LmpySIAJtCmwBAJmlrDZSHe-W-4Fwqk7Z1g?e=HdBLYX","Video":"Stage4.mp4"},
            {"Homework": "Testimonial Video", "Deadline": "2024-07-21", "Resources": "","Video":"https://www.youtube.com/watch?v=PB9vafi87No"},
            #{"Homework": "Refelection", "Deadline": "2024-06-21", "Resources": "","Video":""}
        ],
        "KX1E42": [
            {"Homework": "3D Rocket Designing", "Deadline": "2024 - 04 - 07", "Resources": "http://tinyurl.com/ys4pmmhm","Sample":"t725.png"},
            {"Homework": "3D Rocket Designing - Team","Deadline": "2024-04-10", "Resources": "http://tinyurl.com/ys4pmmhm", "Video":"Rocket_Design_3D.mp4"},
            {"Homework": "Dance Party Programming","Deadline": "2024-04-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Ed6tedRykjhFk5qwx8kuLMsBavmYv9rmBD-FJvfJ7MQUWw?e=54ZDSv", "Video":"DanceParty.mp4"},
            {"Homework": "Name Animation Programming","Deadline": "2024-04-28", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"https://youtu.be/snVFZeRJAsw?si=RZjOIPMG02oGrggb"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-07", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O","Video":"RocketNG.mp4"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-14", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"RocketNG.mp4"},
            {"Homework": "Crew selection simulation", "Deadline": "2024-05-21", "Resources": "https://meulabslk.sharepoint.com/:p:/s/content/Ea9IWg1B7EZEsYNZt9j_NdIBZfWA5jK_ZMv6VnT9e8WNBg?e=PEvnSl","Sample":"CSG.PNG"},
            {"Homework": "Video Animation Story Board", "Deadline": "2024-05-28", "Resources":"", "Sample":"storyboard.png"},
            {"Homework": "Video Animation", "Deadline": "2024-06-07", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Video Editing", "Deadline": "2024-06-14", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Rover Stage 1", "Deadline": "2024-06-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/ESfnL-6SnG9OuEsykfxdsLMBDVD0HkyzkzElrozwWDQkig?e=eRfqGU","Video":"Rover stage 1.mp4"},
            {"Homework": "Rover Stage 2", "Deadline": "2024-06-28", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EZsHoRCn7OBOvg5GMs-otnEBCz40dmes5te4j-Gm7Wu0zw?e=pOszJv","Video":"Stage2.mp4"},
            {"Homework": "Rover Stage 3", "Deadline": "2024-07-07", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Eb4ufzD31iFKuTzWbEWBa7EBv4EOMFRHMnxZY1p2JHHTvw?e=HSfTGc","Video":"Stage4.mp4"},
            {"Homework": "Rover Stage 4", "Deadline": "2024-07-14", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EVanVe5qj39LmpySIAJtCmwBAJmlrDZSHe-W-4Fwqk7Z1g?e=HdBLYX","Video":"Stage4.mp4"},
            {"Homework": "Testimonial Video", "Deadline": "2024-07-21", "Resources": "","Video":"https://www.youtube.com/watch?v=PB9vafi87No"},
            #{"Homework": "Refelection", "Deadline": "2024-06-21", "Resources": "","Video":""}
        ],
        "KX1E43": [
            {"Homework": "3D Rocket Designing", "Deadline": "2024 - 04 - 07", "Resources": "http://tinyurl.com/ys4pmmhm","Sample":"t725.png"},
            {"Homework": "3D Rocket Designing - Team","Deadline": "2024-04-10", "Resources": "http://tinyurl.com/ys4pmmhm", "Video":"Rocket_Design_3D.mp4"},
            {"Homework": "Dance Party Programming","Deadline": "2024-04-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Ed6tedRykjhFk5qwx8kuLMsBavmYv9rmBD-FJvfJ7MQUWw?e=54ZDSv", "Video":"DanceParty.mp4"},
            {"Homework": "Name Animation Programming","Deadline": "2024-04-28", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"https://youtu.be/snVFZeRJAsw?si=RZjOIPMG02oGrggb"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-07", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O","Video":"RocketNG.mp4"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-14", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"RocketNG.mp4"},
            {"Homework": "Crew selection simulation", "Deadline": "2024-05-21", "Resources": "https://meulabslk.sharepoint.com/:p:/s/content/Ea9IWg1B7EZEsYNZt9j_NdIBZfWA5jK_ZMv6VnT9e8WNBg?e=PEvnSl","Sample":"CSG.PNG"},
            {"Homework": "Video Animation Story Board", "Deadline": "2024-05-28", "Resources":"", "Sample":"storyboard.png"},
            {"Homework": "Video Animation", "Deadline": "2024-06-07", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Video Editing", "Deadline": "2024-06-14", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Rover Stage 1", "Deadline": "2024-06-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/ESfnL-6SnG9OuEsykfxdsLMBDVD0HkyzkzElrozwWDQkig?e=eRfqGU","Video":"Rover stage 1.mp4"},
            {"Homework": "Rover Stage 2", "Deadline": "2024-06-28", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EZsHoRCn7OBOvg5GMs-otnEBCz40dmes5te4j-Gm7Wu0zw?e=pOszJv","Video":"Stage2.mp4"},
            {"Homework": "Rover Stage 3", "Deadline": "2024-07-07", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Eb4ufzD31iFKuTzWbEWBa7EBv4EOMFRHMnxZY1p2JHHTvw?e=HSfTGc","Video":"Stage4.mp4"},
            {"Homework": "Rover Stage 4", "Deadline": "2024-07-14", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EVanVe5qj39LmpySIAJtCmwBAJmlrDZSHe-W-4Fwqk7Z1g?e=HdBLYX","Video":"Stage4.mp4"},
            {"Homework": "Testimonial Video", "Deadline": "2024-07-21", "Resources": "","Video":"https://www.youtube.com/watch?v=PB9vafi87No"},
            #{"Homework": "Refelection", "Deadline": "2024-06-21", "Resources": "","Video":""}
        ],
        "KX3E44": [
            {"Homework": "3D Rocket Designing", "Deadline": "2024 - 04 - 07", "Resources": "http://tinyurl.com/ys4pmmhm","Sample":"t725.png"},
            {"Homework": "3D Rocket Designing - Team","Deadline": "2024-04-10", "Resources": "http://tinyurl.com/ys4pmmhm", "Video":"Rocket_Design_3D.mp4"},
            {"Homework": "Dance Party Programming","Deadline": "2024-04-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Ed6tedRykjhFk5qwx8kuLMsBavmYv9rmBD-FJvfJ7MQUWw?e=54ZDSv", "Video":"DanceParty.mp4"},
            {"Homework": "Name Animation Programming","Deadline": "2024-04-28", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"https://youtu.be/snVFZeRJAsw?si=RZjOIPMG02oGrggb"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-07", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O","Video":"RocketNG.mp4"},
            {"Homework": "Rocket Navigation game", "Deadline": "2024-05-14", "Resources": "https://meulabslk.sharepoint.com/:t:/s/content/EYqUa8akonlPmedoc1OOpv4BUkGQuQJ40j4yRn3Nepv5Ww?e=D89N7O", "Video":"RocketNG.mp4"},
            {"Homework": "Crew selection simulation", "Deadline": "2024-05-21", "Resources": "https://meulabslk.sharepoint.com/:p:/s/content/Ea9IWg1B7EZEsYNZt9j_NdIBZfWA5jK_ZMv6VnT9e8WNBg?e=PEvnSl","Sample":"CSG.PNG"},
            {"Homework": "Video Animation Story Board", "Deadline": "2024-05-28", "Resources":"", "Sample":"storyboard.png"},
            {"Homework": "Video Animation", "Deadline": "2024-06-07", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Video Editing", "Deadline": "2024-06-14", "Resources": "", "Video":"Team Alpha plotagon.mp4"},
            {"Homework": "Rover Stage 1", "Deadline": "2024-06-21", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/ESfnL-6SnG9OuEsykfxdsLMBDVD0HkyzkzElrozwWDQkig?e=eRfqGU","Video":"Rover stage 1.mp4"},
            {"Homework": "Rover Stage 2", "Deadline": "2024-06-28", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EZsHoRCn7OBOvg5GMs-otnEBCz40dmes5te4j-Gm7Wu0zw?e=pOszJv","Video":"Stage2.mp4"},
            {"Homework": "Rover Stage 3", "Deadline": "2024-07-07", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/Eb4ufzD31iFKuTzWbEWBa7EBv4EOMFRHMnxZY1p2JHHTvw?e=HSfTGc","Video":"Stage4.mp4"},
            {"Homework": "Rover Stage 4", "Deadline": "2024-07-14", "Resources": "https://meulabslk.sharepoint.com/:b:/s/content/EVanVe5qj39LmpySIAJtCmwBAJmlrDZSHe-W-4Fwqk7Z1g?e=HdBLYX","Video":"Stage4.mp4"},
            {"Homework": "Testimonial Video", "Deadline": "2024-07-21", "Resources": "","Video":"https://www.youtube.com/watch?v=PB9vafi87No"},
            #{"Homework": "Refelection", "Deadline": "2024-06-21", "Resources": "","Video":""}
        ],
#     }, "Analytics": {
#         "AN1E09": [
#             # {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "http://tinyurl.com/ys4pmmhm"},
#             # {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "http://tinyurl.com/ys4pmmhm"},
#             # {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "http://tinyurl.com/ys4pmmhm"},
#             # {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "http://tinyurl.com/ys4pmmhm"}
#         ],
#         "AN1E10": [
#             # {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#          "AN1E11": [
#             # {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Samples"}
#         ],
#          "AN1E12": [
#             # {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             # {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#          "AN1E13": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ]

#     },
#         "Product Design": {
#         "PD1E04": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-08", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#         "PD1E05": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#          "PD1E06": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#          ]
# }, 
#     "Embeded Systems": {
#         "ES1E01": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#         "ES1E02": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#          "ES1E03": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#          ]
# },
#     "Software Engineering": {
#         "SE1E03": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#         "SE1E04": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#          "SE1E05": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#          ]
# },
#     "Data Science": {
#         "DS1E01": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#         "DS1E02": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#         ],
#          "DS1E03": [
#             {"Homework": "Sample1", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample2", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample3", "Deadline": "2024-02-07", "Resources": "Sample"},
#             {"Homework": "Sample4", "Deadline": "2024-02-08", "Resources": "Sample"}
#          ]
 }
}



 # Sidebar navigation
with st.sidebar:
    st.sidebar.markdown("<h2 style='font-family: Arial, sans-serif;margin-top:-10px; margin-bottom:-40px;'>Program</h2>", unsafe_allow_html=True)
    selected_program = st.sidebar.selectbox("", list(program_homework.keys()))

    st.sidebar.markdown("<h2 style='font-family: Arial, sans-serif;margin-bottom:-40px'>Classes</h2>", unsafe_allow_html=True)
    selected_class = st.sidebar.selectbox("", list(program_homework[selected_program].keys()))

    # Add radio buttons for selecting the week
    st.sidebar.markdown("<h2 style='font-family: Arial, sans-serif;margin-bottom:-40px'>Week</h2>", unsafe_allow_html=True)
    selected_week = st.sidebar.radio("", ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15"])



with st.container():
    # Nested container for the header
            with stylable_container(
        key="markdown_container1",
        css_styles="""{
             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
             background-color:rgb(0, 0, 51);
              width: 1200px;
              height: 260px;                  
             padding:4em;
             position:fixed;
             z-index: 1;
             margin-top:-100px;
             margin-left:-190px;
             
         }
         """,
    ):
                st.markdown("""
    <style>
        .image-container {
            float: left;
            margin-left: 300px;
        }
    </style>
""", 
unsafe_allow_html=True)
                
                st.image("Logo- on dark.png", width=400)
                st.markdown(
    "<h2 style=\"text-align: right; font-family: 'Times New Roman', Times, serif; margin-top:-40px;\"> Students Homework Tracker  <span style='font-size: 40px;'>📚</span></h2>",
    unsafe_allow_html=True
)


# ---------------------------------------------

        
st.markdown("""
    <style>
        .trackgap {
            margin-bottom: 80px; 
            
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="trackgap"></div>', unsafe_allow_html=True)

st.markdown("""
    <style>
        .gap {
            margin-bottom: 50px;
        }
    </style>
""",
 unsafe_allow_html=True)

st.markdown('<div class="gap"></div>', unsafe_allow_html=True)

# columns to create a two-column layout
col1, col2= st.columns([1, 0.1])


# Display homework for the selected week
with col1:
    with stylable_container(
        key="markdown_container",
        css_styles="""{
         height:700px;
         width: 800px;
         border-radius:5px;
         border:solid;
         border-color:#4D5559;
         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
         padding:0.0010em;
         margin-left:-20px;
         text-margin:150px;
         }
         """
    ):
        
        homework_data = program_homework[selected_program][selected_class]

        if selected_week == "Week 1":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-04-07"]
        elif selected_week == "Week 2":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-04-14" and hw["Deadline"] > "2024-04-07"]
        elif selected_week == "Week 3":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-04-21" and hw["Deadline"] > "2024-04-14"]
        elif selected_week == "Week 4":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-04-28" and hw["Deadline"] > "2024-04-21"]
        elif selected_week == "Week 5":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-05-07" and hw["Deadline"] > "2024-04-28"]
        elif selected_week == "Week 6":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-05-14" and hw["Deadline"] > "2024-05-07"]
        elif selected_week == "Week 7":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-05-21" and hw["Deadline"] > "2024-05-14"]
        elif selected_week == "Week 8":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-05-28" and hw["Deadline"] > "2024-05-21"]
        elif selected_week == "Week 9":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-06-07" and hw["Deadline"] > "2024-05-28"]
        elif selected_week == "Week 10":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-06-14" and hw["Deadline"] > "2024-06-07"]
        elif selected_week == "Week 11":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-06-21" and hw["Deadline"] > "2024-06-14"]
        elif selected_week == "Week 12":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-06-28" and hw["Deadline"] > "2024-06-21"]
        elif selected_week == "Week 13":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-07-07" and hw["Deadline"] > "2024-06-28"]
        elif selected_week == "Week 14":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-07-14" and hw["Deadline"] > "2024-07-07"]
        elif selected_week == "Week 15":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-07-21" and hw["Deadline"] > "2024-07-14"]
        elif selected_week == "Week 16":
            homework_data = [hw for hw in homework_data if hw["Deadline"] <= "2024-07-28" and hw["Deadline"] > "2024-07-21"]



# Display homework for the selected week
# with col1:
#     with stylable_container(
#         key="markdown_container",
#         css_styles="""{
#          height:700px;
#          width: 800px;
#          border-radius:5px;
#          border:solid;
#          border-color:#4D5559;
#          box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#          padding:0.0005em;
#          margin-left:-20px;
#          text-margin:50;
#          }
#          """
#     ):
      
        # st.markdown(f"<h2 style='font-family: Arial, sans-serif; font-size: 30px;'>{selected_week} {selected_week} - {selected_class}</h2>", unsafe_allow_html=True)st.markdown(f"<span style='font-family: Arial, sans-serif; font-size: 29px;'>Week 1 {hw['Homework']} </span>", unsafe_allow_html=True)
        for hw in homework_data:
            st.markdown(f"<span style='font-family: Arial, sans-serif; font-size: 29px; margin-left: 20px;'> {selected_week} - {hw['Homework']} - {selected_class}  </span>", unsafe_allow_html=True)
            st.markdown(f"<div style='margin-bottom: 20px; margin-top: 40px; margin-left: 18px; font-size: 20px; font-family: Arial, sans-serif;'>Homework:  <span style='font-size: 16px;'>{hw['Homework'] }</span></div>", unsafe_allow_html=True)
            # st.markdown(f"<div style='margin-bottom: 20px; margin-left: 20px; font-size: 18px; font-family: Arial, sans-serif;'>Instructions:  <span style='font-size: 16px;'>{hw['Instructions']}</span></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='margin-bottom: 20px; margin-left: 20px; font-size: 18px; font-family: Arial, sans-serif;'>Deadline: <span style='font-size: 16px;'>{hw['Deadline']}</span></div>", unsafe_allow_html=True)
            st.markdown(f"<div style='margin-bottom: 20px; margin-left: 20px; font-size: 18px;  font-family: Arial, sans-serif;'>Resources: <a href='{hw['Resources']}' target='_blank'>Credentials</a></div>", unsafe_allow_html=True)
            # st.markdown(f"<div style='margin-bottom: 20px;'><strong>Resources:</strong> <a href='{hw['Resources']}' target='_blank'>Sample</a></div>", unsafe_allow_html=True)
        if "Sample" in hw:
            
            # st.markdown(f"<div style='margin-bottom: 20px; margin-left: 20px; font-size: 20px;'>Example Project: <span style='font-size: 18px;'>{hw['Sample']}</span></div>", unsafe_allow_html=True)
            st.image(hw["Sample"], caption="Tinkercad 3D design", use_column_width=False)
        
        if "Video" in hw:
                
            # st.markdown(f"<div style='margin-bottom: 20px; margin-left: 20px; font-size: 20px;'>Example Project: <span style='font-size: 18px;'>{hw['Video']}</span></div>", unsafe_allow_html=True)
            st.video(hw["Video"])
            # image_path = "t725.png"
            # st.image(image_path, caption='', use_column_width=False)

        
        
    # Display video if available
        
            # Add custom CSS styling
        
            # st.markdown(
            # """
            # <style>
            # /* Add your custom CSS styles here */
            # /* Adjust the font size of the caption */
            # .element-container .caption span {
            # font-size: 100px; /* Adjust the font size as needed */
            # }
            # </style>
            # """,
            # unsafe_allow_html=True
            # )


# if st.button(f"Submit {hw['Homework']} Homework", key=f"submit_{hw['Homework']}"):
#          google_form_url = "https://forms.gle/n5SyyEqqqyTWpVsD6"
#          webbrowser.open_new_tab(google_form_url)
                
uploaded_file=col1.file_uploader("UPLOAD YOUR HOMEWORK")
                 

st.markdown(
            """
            <style>
            /* Add your custom CSS styles here */
            /* For example, adjust the width of the image */
            img {
                width: 400px;
                border-radius: 8%;
                margin-left: 70px;
            }

            
            </style>
            """,
            unsafe_allow_html=True
        )

st.markdown(
            """
            <style>
            /* Add your custom CSS styles here */
            /* For example, adjust the width of the image */
            video {
                width: 400px;
                border-radius: 8%;
                margin-left: 0px;
                height:400px;
            }

            
            </style>
            """,
            unsafe_allow_html=True
        )





# Add footer
footer = """
<style>
    .footer {
        position: fixed;
        bottom: -10px;
        left: 100px;
        width: 100%;
        background-color: #333333;
        color: white;
        text-align: center;
        padding: -70px;
    }
</style>
<div class="footer">
    <p>Developed by <a style="color: #F98F26; text-decoration: none;" href="https://meulabs.org">MEU LABS</a></p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
