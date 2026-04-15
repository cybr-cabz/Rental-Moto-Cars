import streamlit as st
import os

FLEET_DATA = {
    "Cars": [
        {"name": "2011 Bugatti Veyron", "img": "Cars/5.jpg", "speed": "257.8 MPH", "condition": "Excellent", "engine": "8.0L W16 Quad-Turbo"},
        {"name": "2010 Koenigsegg CCXR", "img": "Cars/6.jpg", "speed": "254.6 MPH", "condition": "Pristine", "engine": "4.8L V8 Twin-Supercharged"},
        {"name": "2014 Lykan Hypersport", "img": "Cars/7.jpg", "speed": "245 MPH", "condition": "New", "engine": "3.7L Twin-Turbo Flat-Six"},
        {"name": "2011 Lexus LFA", "img": "Cars/8.jpg", "speed": "202 MPH", "condition": "Excellent", "engine": "4.8L V10"}
    ],
    "Motorcycles": [
        {"name": "Ninja H2 Carbon", "img": "Motors/1.jpg", "condition": "Track Ready", "engine": "998cc Supercharged Inline-4"},
        {"name": "Ducati Panigale V4R", "img": "Motors/2.jpg", "condition": "Pristine", "engine": "998cc Desmosedici Stradale V4"},
        {"name": "Suzuki GSX-R1000R", "img": "Motors/3.jpg", "condition": "Excellent", "engine": "999.8cc Inline-4"},
        {"name": "BMW S1000 RR", "img": "Motors/4.jpg", "condition": "Excellent", "engine": "999cc Inline-4"}
    ]
}

def rental_css():
    st.markdown("""
        <style>
        .stApp { background-color: #001f3f; color: #ffffff; }
        [data-testid="stHeader"] { background-color: #262626; }
        .main-title { color: #ff9800; font-family: 'Arial Black'; font-size: 48px; text-align: center; }
        .body-text { font-size: 20px; line-height: 1.6; }
        
        /* Card Styling */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #262626 !important;
            border: 1px solid #444 !important;
            border-radius: 15px !important;
            padding: 20px !important;
            transition: transform 0.3s;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: #ff9800 !important;
        }
                
        div[data-testid="stImage"],
        div[data-testid="stImage"] img {
            background-color: transparent !important;
            box-shadow: none !important;
        }
                
        p { font-size: 20px !important; }
        span { font-size: 22px !important; }
        </style>
    """, unsafe_allow_html=True)

@st.dialog("Login Required")
def login_dialog():
    st.write(f"You must be logged in to rent a vehicle. Please log in to continue.")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    st.write("---")
    col1, col2 = st.columns(2)
    if col1.button("Login", use_container_width=True):
        if user.lower() == "admin" and pwd == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials.")
    
    if col2.button("Sign Up", use_container_width=True):
        st.info("Sign-up is currently disabled.")

def dashboard():
    rental_css()
    st.markdown('<h1 class="main-title">RENTAL MOTO-CARS</h1>', unsafe_allow_html=True)

    category = st.radio("Select Category", ["Cars", "Motorcycles"], horizontal=True)
    st.divider()

    items = FLEET_DATA[category]
    cols = st.columns(2)

    for idx, item in enumerate(items):
        with st.container(border=True):
            st.subheader(item["name"])

            if os.path.exists(item["img"]):
                st.image(item["img"], width="stretch")
            else:
                st.warning(f"Image for {item['name']} not found.")

            with st.expander("View Details"):
                st.write(f"**Condition:** {item['condition']}")
                st.write(f"**Engine:** {item['engine']}")
                if "speed" in item:
                    st.write(f"**Top Speed:** {item['speed']}")
            
            if st.button(f"Rent {item['name']}", key=f"btn_{idx}_{category}"):
                    if not st.session_state.logged_in:
                        login_dialog()
                    else:
                        st.success(f"Successfully booked {item['name']}!")
                        st.balloons()

def main():
    st.set_page_config(page_title="Rental Moto-Cars", layout="centered")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar Navigation
    st.sidebar.title("")
    page = st.sidebar.radio("", ["Home", "About", "Contact", "Services"], key="nav")
    st.session_state.page = page

    # Sidebar Logout
    if st.session_state.logged_in:
        st.sidebar.success("Logged in as Admin")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # Page routing
    if st.session_state.page == "Home":
        dashboard()
    elif st.session_state.page == "About":
        about_page()
    elif st.session_state.page == "Contact":
        contact_page()
    elif st.session_state.page == "Services":
        services_page()

def about_page():
    rental_css()
    st.markdown('<h1 class="main-title">ABOUT US</h1>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Rental Moto-Cars was established with a clear mission to provide high-performance, reliable, and affordable transportation for every type of journey.</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">We specialize in a diverse fleet that bridges the gap between luxury and utility, offering everything from high-end sports sedans to rugged, track ready motorcycles.</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">As a proud member of the National Rental Association, we prioritize the safety and satisfaction of our clients by ensuring every vehicle in our collection from the record breaking Bugatti Veyron to the precision engineered Ninja H2 Carbon undergoes rigorous mechanical verification.</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">Whether you are navigating city streets on a scooter or seeking an adrenaline filled adventure touring the coast, our team is dedicated to delivering a premium rental experience grounded in trust and excellence.</p>', unsafe_allow_html=True)

def contact_page():
    rental_css()
    st.markdown('<h1 class="main-title">CONTACT US</h1>', unsafe_allow_html=True)
    st.write("Email: info@rentalmotocars.com")
    st.write("Phone: +6312456800-MOTO-CARS")

def services_page():
    rental_css()
    st.markdown('<h1 class="main-title">OUR SERVICES</h1>', unsafe_allow_html=True)
    st.write('<p class="body-text">- <span style = "color: #007bff;font-weight: bold;">Verified Vehicle Condition</span>: Every car and motorcycle, from our high speed Bugatti Veyron to our precision engineered Ninja H2, undergoes a rigorous multi-point inspection to ensure peak engine performance and safety.</p>', unsafe_allow_html=True)
    st.write('<p class="body-text">- <span style = "color: #007bff;font-weight: bold;">Privacy & Data Protection</span>: We manage your browsing experience with the same care as our fleet. Our platform utilizes advanced tracking prevention and secure data management to ensure your search history, passwords, and personal cookies remain private within your profile.</p>', unsafe_allow_html=True)
    st.write('<p class="body-text">- <span style = "color: #007bff;font-weight: bold;">Secure Connected Experiences</span>: We provide a seamless, continuous browsing session by safely saving necessary site data on your device, allowing you to facilitate effortless transitions between vehicle categories and booking sessions.</p>', unsafe_allow_html=True)
    st.write('<p class="body-text">- <span style = "color: #007bff;font-weight: bold;">Enhanced Site Security</span>: Your digital safety is paramount. We actively manage security settings and site permissions across our entire platform to protect your information while you browse our premium collection.</p>', unsafe_allow_html=True)
    st.write('<p class="body-text">- <span style = "color: #007bff;font-weight: bold;">Expert Roadside Support</span>: To ensure you are never alone on the journey, our dedicated dispatch team offers real-time assistance and professional support for any issues you may encounter on the road.</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()