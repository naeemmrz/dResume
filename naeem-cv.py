from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Naeem - Compact Curriculum Citae.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Naeem A"
PAGE_ICON = ":lab_coat:"
NAME = "Naeem A."
DESCRIPTION = """
I am a molecular biologist with a specialization in vaccinology. My research passion encompasses the convergence of immunology, molecular biology, and informatics.
Beyond my academic pursuits, I find solace in outdoor camping and I have a profound interest in discovering new destinations and immersing myself in diverse cultures. 
"""
EMAIL = "mailto:merzanaeem007@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/naeemmrz/",
    "GitHub": "https://github.com/naeemmrz/",
    "Instagram": "https://www.instagram.com/naeemmrz/",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

	
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([0.4, 0.5])
with col1:
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.image(profile_pic, width=250)

with col2:
    st.header(NAME)
    st.markdown(f"<div style='text-align: justify;'>{DESCRIPTION}</div>", unsafe_allow_html=True)
    st.write("\n")

    st.download_button(
        label=" 📄 Download Compact Curriculum Vitae",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(f"[![Repo](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]({SOCIAL_MEDIA['LinkedIn']})", "--", f"[![Repo](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]({SOCIAL_MEDIA['GitHub']})", "--", f"[![repo](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)]({EMAIL})")


st.write('\n')
# --- SOCIAL LINKS ---
#st.write('\n')
#cols = st.columns(len(SOCIAL_MEDIA))
#for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#    cols[index].write(f"[{platform}]({link})")


st.write('\n')
# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    """
- :white_check_mark: Extensive hands-on experience in mammalian cell culture
- :white_check_mark: Good understanding of computational drug discovery methodologies
- :white_check_mark: Proficient in academic English writing and presenting
- :white_check_mark: Unwaveringly reliable with a strong drive for excellence
"""
)

st.write('\n')
st.write('\n')
# --- THE MENU BAR ---
selected = option_menu(menu_title=None,
			options=[ "Education & Experience", "Awards & Accomplishments", "Publications & Proceedings"],
			icons=["buildings", "trophy", "newspaper"],
			menu_icon="cast",
			default_index=1,
			orientation="horizontal",
			styles={
			"container": {"height": "70px", "font-size": "16px", "padding": "2px!important", "background-color": "#002b36"}, # Menu BG color
			"icon": {"font-size": "18px"}, 
			"nav-link": {"margin-top": "6px!important", "font-size": "18px", "text-align": "center", "margin":"2px", "--hover-color": "#B64003"}, # Hover-over Menu color
            "nav-link-selected": {"background-color": "#B64003"} # Selected Menu color
            })

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

if selected == "Education & Experience":
    
    
    st.write('\n')
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Technical Skills")
    st.write("---")
    st.write(
        """
    🥇 High level proficiency in the following areas:
    - 🧫 Mammalian cell culture: MTT, qRT-PCR, DNA/RNA extraction, gel electrophoresis, etc.
    - 👩‍💻 Machine learning: Python (Scikit-learn, Pandas, streamlit)
    - ⚗️ Cheminformatics: Drug discovery (RDKit, QSAR, Vina, NAMD)
    - 📝 Academic writing: Manuscript/poster drafting (MS, Canva, Mendeley)
    """
    )
    st.write('\n')
    st.write(
        """
    🥈 Foundational knowledge in the following areas:
    - 🔬 Immuno-assays: Western blot, ELISA, IHC, immunoassays
    - 👩‍💻 Programming: R/RStudio (Statistical testing)
    - 🦾 Deep Learning: Tensor/Keras
    - 📊 Data Visualization: Matplotlib, Seaborn, GraphPad Prism 

    """
    )

    st.write('\n')
    st.write('\n')
    # --- EDUCATION & WORK HISTORY ---
    st.write('\n')
    st.write('\n')
    st.subheader("Education & Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Erasmus Mundus Joint Master's Degree | [🔗 Leading International Vaccinology Education](https://www.uantwerpen.be/en/about-uantwerp/faculties/fbd/international/international-programmes/vaccinology-master/)** - ES, BE, & FR")
    st.write("09/2023 - Present")
    st.write(
        """
    - ► A comprehensive and interdisciplinary joint master’s program delivered jointly by a consortium of European universities including Universidad de Barcelona, Universitat Autònoma de Barcelona, Universiteit Antwerpen, Université de Saint-Etienne & Université Claude Bernard Lyon.
    - ► Completed the first semester of lectures and practical’s in field of immunology and immunopathology at Universidad de Barcelona & Universitat Autònoma de Barcelona.
    - ► Currently under taking courses and practical’s in infectious disease, advanced data analysis, and clinical drug research.
    - ► Participated in a 2 week education program and a hackathon at GlaxoSmithKline (GSK, Wavre)  
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write('\n')
    st.write("🚧", "**Master of Science (Candidate) | [🔗 Molecular Biology & Genetics](http://www.fenbilimleri.mu.edu.tr/en)**, Mugla S. K. University - TR")
    st.write("09/2022 - Present")
    st.write(
        """
    - ► Co-authored a research proposal that earned funding from the Research Support & Funding Office of the university (Investigating drug repurposing for wild MDM2-p53 cancers)
    - ► Co-authored a research proposal that earned funding from the Scientific and Technological Research Council of Turkey (ABacAPP, ML platform for antibiotic screening)
    - ► Performed cheminformatics and computational drug discovery analysis
    - ► Independently worked in cell culture laboratory, routinely performed cytotoxicity, gene expression, and molecular biology assays
    - ► Supervised 2 undergraduate student's research project
    - ► CGPA 3.91/4.00 & thesis defense is scheduled at the end of summer 2023

    """
    )

    # --- JOB 3
    st.write('\n')
    st.write('\n')
    st.write("🚧", "**Bachelor of Science | [🔗 Molecular Biology & Genetics](https://mbg.mu.edu.tr/en), Mugla S. K. Univeristy - TR**")
    st.write("09/2018 - 09/2021")
    st.write(
        """
    - ► Graduated in the top 1% of the class as a High Honors student with a CGPA of 3.68/4.00
    - ► Co-authored an undergraduate research project on natural plant-products that was funded by the Scientific and Technological Research Council of Turkey
    - ► Participated as an Erasmus+ Exchange Student for 1 semester at the Bydgoszcz University of Science and Technology 
    - ► Completed an internships in a cell biology laboratory (10 months), computational drug discovery (10 months), and plant tissue culture (3 months).
    - ► Co-authored 3 peer-reviewed articles, 2 posters and 1 oral presentation

    """
    )


    st.write('\n')
    st.write('\n')
    # --- WORKSHOPS ---
    st.write('\n')
    st.write('\n')
    st.subheader("Workshops")
    st.write("---")
    st.write(
        """
            🛡️ 2023   
            - 🔰    ICH-GCP E6R2 Antwerp University Hospital Certification
            - 🔰    GlaxoSmithKline Hackathon (Wavre)
            \n
            🛡️ 2022 
            - 🔰    Academic IELTS (C2 Proficient)
            - 🔰    VaxInLIVE Symposium
            \n
            🛡️ 2021
            - 🔰    RSG Turkey Computational Structural Biology Virtual Workshop
            - 🔰    Introduction to Machine Learning, Duke University (Coursera)
            - 🔰    Welcome to Game Theory, the University of Tokyo (Coursera)
            - 🔰    Introduction to Python, Global AI hub, Turkey
            - 🔰    1st National Structural Biology Workshop, Koc University, Turkey
        """
    )


    st.write('\n')
    st.write('\n')
    # --- LANGUAGES ---
    st.write('\n')
    st.write('\n')
    st.subheader("Languages")
    st.write("---")
    st.write(
        """
            - 🌏 English - Advanced (C2) level
            - 🧿 Turkish - Advanced (C1) level
            - 🌙 Arabic  - Native speaker
            - 📜 Persian - Native speaker
            - 🥐 French  - Currently learning (A1)
        """
    )


    # --- JOB 4
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.subheader("🚧 **Non-Relevant Work Experiences**")
    st.write("---")
    st.write("2016 - 2023")
    st.write(
        """
            - ► Worked in catering and waitressing at different locations on & off during weekends throughout my undergraduate
            - ► Worked in a game arcade, a cinema reception, a bowling reception, etc. during undergraduate summer breaks
            - ► Worked as an assistant for the logistics team in a Carpet company after high school for 9 months

        """ 
    )

    
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

if selected == "Awards & Accomplishments":


    st.write('\n')
    # --- AWARDS & ACCOMPLISHMENTS ---
    st.write('\n')
    st.subheader("Awards & Accomplishments")
    st.write("---")

    st.write("🏆", "European Education and Culture Executive Agency Scholarship - 2022")
    st.markdown("<div style='text-align: justify;'>Full EACEA scholarship for 2 years to participate in Erasmus Mundus Joint Master's Degree in Leading International Vaccinology Education.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.write("🏆", "High Honors Degree - 2021")
    st.markdown("<div style='text-align: justify;'>A statutory award given to undergraduate students who graduate with remarkably high CGPA.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.write("🏆", "Best Poster Award - 2021")
    st.markdown("<div style='text-align: justify;'>First place in the International Conference 'Environment-Animal-Human' Young Scientists Session's poster competition, organized by the West Pomeranian University of Technology, Szczecin, Poland.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.write("🏆", "Academic Incentive Award - 2021")
    st.markdown("<div style='text-align: justify;'>Monetary award by the Turkish Scientific and Technological Research Council for co-authoring a manuscript in a well-reputed journal (PLoS ONE).</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.write("🏆", "Excellence Scholarship - 2021")
    st.markdown("<div style='text-align: justify;'>Merit-based scholarship awarded by Turkey's Directorate General of Foundations for distinctive academic performance. </div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

if selected == "Publications & Proceedings":


    st.write('\n')
    # --- PUBLICATIONS  ---
    st.write('\n')
    st.subheader("Articles & Preprints")
    st.write("---")

    st.markdown("<div style='text-align: justify;'> 📰 <u>Abdul Ghafoor, N.</u> & Yildiz, A. Targeting MDM2-p53 Axis Through Drug Repurposing for Cancer Therapy: A Multidisciplinary Approach. (2023) <i>Preprint</i>. <br><a href='https://doi.org/10.21203/rs.3.rs-2907077/v1'>🔗https://doi.org/10.21203/rs.3.rs-2907077/v1</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>My contribution</b>: I designed the study, performed the experiments and analysis, and drafted the manuscript.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 📰 <u>Abdul Ghafoor, N.</u> & Sitkowska, B. Computational repurposing of FDA-approved drugs against specific mastitis-causing pathogens. (2022) <i>Acta Scientiarum Polonorum Zootechnica</i>. <br><a href='http://dx.doi.org/10.21005/asp.2021.20.4.02'>🔗http://dx.doi.org/10.21005/asp.2021.20.4.02</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>My contribution</b>: I designed the study, performed the experiments and analysis, and drafted the manuscript.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 📰 <u>Abdul Ghafoor, N.</u>, Galatali, S., Yeniocak, S., Kaya, E., Sarac, N. & Uğur, A. Investigating anticancer potency of in vitro propagated endemic Thymus cilicicus Boiss. & Bal. extract on human lung, breast, and prostate cancer cell lines. (2022) <i>Biologia</i>. <br><a href='https://doi.org/10.1007/s11756-022-01168-7'>🔗https://doi.org/10.1007/s11756-022-01168-7</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>My contribution</b>: I performed the experiments and drafted the manuscript.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 📰 <u>Abdul Ghafoor, N.</u> & Sitkowska, B. MasPA: A Machine Learning Application to Predict Risk of Mastitis in Cattle from AMS Sensor Data. (2021) <i>AgriEngineering</i>. <br><a href='https://doi.org/10.3390/agriengineering3030037'>🔗https://doi.org/10.3390/agriengineering3030037</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>My contribution</b>: I designed the study, performed the experiments and analysis, and drafted the manuscript.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 📰 Kivrak Kiran, S., Galatali, S., Yeniocak, S., Ozkaya, D. E., Mercan, T., Guldag, S., Celik, O., <u>Abdul Ghafoor, N.</u>, & Kaya, E. Investigation of modified WPM medium for the best meristem proliferation of Corylus avellana L. (2021) <i>Advances in Horticultural Science</i>. <br><a href='https://doi.org/10.36253/ahsc-10536'>🔗https://doi.org/10.36253/ahsc-10536</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>My contribution</b>: I translated (from Turkish to English), compiled and proofread the manuscript.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 📰 Baysal, Ö., <u>Abdul Ghafoor, N.</u>, Silme, RS., Ignatov, AN., Kniazeva, V. Molecular dynamics analysis of N-acetyl-D-glucosamine against specific SARS-CoV-2’s pathogenicity factors. (2021) <i>PLoS ONE</i>. <br><a href='http://dx.doi.org/10.1371/journal.pone.0252571'>🔗http://dx.doi.org/10.1371/journal.pone.0252571</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>My contribution</b>: I performed the computational experiments and contributed to the writing of the manuscript.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 📰 Galatali, S., <u>Abdul Ghafoor, N.</u>, Kaya, E. Characterization of Olive (Olea Europaea L.) Genetic Resources via PCR-Based Molecular Marker Systems. (2021) <i>European Journal of Biology and Biotechnology</i>. <br><a href='http://dx.doi.org/10.24018/ejbio.2021.2.1.146'>🔗http://dx.doi.org/10.24018/ejbio.2021.2.1.146</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>My contribution</b>: I translated (from Turkish to English), compiled and proofread the manuscript.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')


    st.write('\n')
    st.subheader("Posters & Conference Abstracts")
    st.write("---")

    st.markdown("<div style='text-align: justify;'> 👨‍🏫 Yildiz, A. <u>Abdul Ghafoor, N.</u> & Tanrıverdi, Ö. Re-evaluation of FDA Approved Drugs for Cancer Research. (2022) <i>5th Muğla Multidisciplinary Oncology Research Conference.</i> Remote, Turkey. <br><a href='https://amorecongress2022.com/tr#:~:text=Bildiri%20Kitab%C4%B1n%C4%B1%20%C4%B0ndirmek%20%C4%B0%C3%A7in%20T%C4%B1klay%C4%B1n%C4%B1z'>🔗https://amorecongress2022.com/tr</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>Oral presentation</b>.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n') 

    st.markdown("<div style='text-align: justify;'> 👨‍🏫 <u>Abdul Ghafoor, N.</u>, Galatali, S., Yeniocak, S., Saman, Z., Kaya, E., & Sarac, N. Cytotoxicity, wound healing & anti-cancer potency of in vitro cultured Thymus cilicicus Boiss. & Bal. ethanolic extracts. (2022) <i>1st International Conference on Experimental Sciences and Biotechnology.</i> Mugla, Turkey. <br><a href='https://www.researchgate.net/publication/356193661_Cytotoxicity_Wound_Healing_Anti-cancer_Potency_of_in_vitro_Cultured_Thymus_cilicicus_Boiss_Bal_Ethanolic_Extracts'>🔗https://www.researchgate.net/publication/356193661</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>Oral presentation</b>.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 👨‍🏫 <u>Abdul Ghafoor, N.</u> & Yildiz, A. A Machine Learning Approach to Predict in Vitro Efficacy of Human Lung Adenocarcinoma Proliferation Inhibitors. (2021) <i>5th International Symposium on Bioinformatics (InSyB2021).</i> Istanbul, Turkey. <br><a href='http://dx.doi.org/10.13140/RG.2.2.21710.38725'>🔗http://dx.doi.org/10.13140/RG.2.2.21710.38725</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>Poster presentation</b>.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')

    st.markdown("<div style='text-align: justify;'> 👨‍🏫 <u>Abdul Ghafoor, N.</u> & Sitkowska, B. Computational Repurposing of FDA-approved Drugs Against Specific Mastitis-causing Pathogens. (2021) <i>International Conference Environment - Animal - Human.</i> Remote, Poland. <br><a href='http://dx.doi.org/10.13140/RG.2.2.26908.36480'>🔗http://dx.doi.org/10.13140/RG.2.2.26908.36480</a> </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify;'><b>Poster presentation</b>.</div>", unsafe_allow_html=True)
    st.write('\n')
    st.write('\n')
