import streamlit as st
st.set_page_config(layout="wide")
def display_roadmap():
    st.title("📈 60-Day Intensive Tech Mastery Roadmap")
    st.markdown("""
    ### **Focus Areas**  
    - **Data Science/AI**: Python (NumPy, Pandas, Scikit-learn, TensorFlow) → Real-world ML pipelines  
    - **Systems Programming**: C → C++ → DSA → Competitive Coding (ICPC/GSOC prep)  
    - **Full-Stack Web**: Modern CSS → JavaScript → Node.js → Angular.js  
    """)
    
    st.markdown("---")
    
    # Phase 1: Foundations (Days 1-15)
    st.header("🔰 Phase 1: Foundations (Days 1-15)")
    
    with st.expander("🧠 Python Data Science (9 days)", expanded=True):
        cols = st.columns(3)
        with cols[0]:
            st.subheader("📅 Days 1-3: NumPy Mastery")
            st.markdown("""
            **Core Concepts**:  
            - ND arrays, broadcasting, universal functions  
            - Matrix operations, linear algebra  
            
            **Resources**:  
            📺 [FreeCodeCamp Crash Course](https://youtu.be/rN0TREjYYGk) (3.5hr)  
            📖 [NumPy Official Docs](https://numpy.org/doc/stable/user/absolute_beginners.html)  
            
            **Practice**:  
            💻 30 exercises from [PracticePython NumPy](https://www.practicepython.org/)  
            🧩 Solve 5 problems on [HackerRank NumPy](https://www.hackerrank.com/domains/python/numpy)  
            
            **Project**:  
            🛠️ Matrix Calculator CLI
            """)
        
        with cols[1]:
            st.subheader("📅 Days 4-6: Pandas Pro")
            st.markdown("""
            **Core Concepts**:  
            - DataFrames, Series, indexing  
            - GroupBy, merging, handling missing data  
            
            **Resources**:  
            📺 [Data School Playlist](https://youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)  
            📖 [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)  
            
            **Practice**:  
            💼 Clean [COVID-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  
            
            **Project**:  
            🛠️ CLI Data Analyzer
            """)
        
        with cols[2]:
            st.subheader("📅 Days 7-9: Data Visualization")
            st.markdown("""
            **Core Concepts**:  
            - Matplotlib figures/axes  
            - Seaborn statistical plots  
            
            **Resources**:  
            📺 [Matplotlib Tutorial](https://youtu.be/3Xc3CA655Y4)  
            📖 [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)  
            
            **Project**:  
            🛠️ Interactive Plot
            """)
    
    with st.expander("🌐 Web Dev Basics (6 days)"):
        cols = st.columns(2)
        with cols[0]:
            st.subheader("📅 Days 10-12: Modern CSS")
            st.markdown("""
            **Core Concepts**:  
            - Flexbox, Grid, responsive design  
            - CSS variables, animations  
            
            **Resources**:  
            📺 [Kevin Powell Playlist](https://youtube.com/playlist?list=PL4-IK0AVhVjM0xE0K2uZ2vsKen7UBAi3K)  
            🎮 [CSS Grid Garden](https://cssgridgarden.com/)  
            
            **Project**:  
            🛠️ Responsive Portfolio Page
            """)
        
        with cols[1]:
            st.subheader("📅 Days 13-15: JavaScript DOM")
            st.markdown("""
            **Core Concepts**:  
            - Event listeners, DOM manipulation  
            - Local storage, async JS  
            
            **Resources**:  
            🎓 [JavaScript30 Course](https://javascript30.com/)  
            📖 [Eloquent JavaScript](https://eloquentjavascript.net/)  
            
            **Project**:  
            🛠️ Todo App with Persistence
            """)
    
    st.markdown("---")
    
    # Phase 2: Core Development (Days 16-35)
    st.header("⚙️ Phase 2: Core Development (Days 16-35)")
    
    with st.expander("🤖 Advanced Python & AI (9 days)", expanded=True):
        cols = st.columns(3)
        with cols[0]:
            st.subheader("📅 Days 16-18: Scientific Python")
            st.markdown("""
            **Core Concepts**:  
            - Scipy stats, optimization  
            - Numerical integration, FFTs  
            
            **Resources**:  
            📺 [Edureka Tutorial](https://youtu.be/jmX4FOUEfgQ)  
            📖 [Scipy Lecture Notes](https://scipy-lectures.org/)  
            
            **Project**:  
            🛠️ Recommendation Engine
            """)
        
        with cols[1]:
            st.subheader("📅 Days 19-21: ML Foundations")
            st.markdown("""
            **Core Concepts**:  
            - Linear regression, classification  
            - Model evaluation metrics  
            
            **Resources**:  
            🧠 [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)  
            📊 [Sklearn Tutorial](https://scikit-learn.org/stable/tutorial/basic/tutorial.html)  
            
            **Project**:  
            🛠️ Housing Price Predictor
            """)
        
        with cols[2]:
            st.subheader("📅 Days 22-24: Streamlit Dashboards")
            st.markdown("""
            **Core Concepts**:  
            - Widgets, layout, caching  
            - Plot integration  
            
            **Resources**:  
            📺 [Streamlit Docs](https://docs.streamlit.io/)  
            🎨 [Streamlit Components](https://streamlit.io/components)  
            
            **Project**:  
            🛠️ Interactive Data Explorer
            """)
    
    with st.expander("💻 C/C++ & DSA (11 days)"):
        cols = st.columns(3)
        with cols[0]:
            st.subheader("📅 Days 25-27: C Programming")
            st.markdown("""
            **Core Concepts**:  
            - Pointers, memory management  
            - File I/O, structs  
            
            **Resources**:  
            🎓 [CS50 Week 1-3](https://cs50.harvard.edu/x/2023/)  
            🧩 [C Exercises](https://www.w3resource.com/c-programming-exercises/)  
            
            **Project**:  
            🛠️ Text Adventure Game
            """)
        
        with cols[1]:
            st.subheader("📅 Days 28-30: C++ OOP")
            st.markdown("""
            **Core Concepts**:  
            - Classes, inheritance  
            - STL containers  
            
            **Resources**:  
            📺 [The Cherno Playlist](https://youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)  
            📖 [Learn C++](https://www.learncpp.com/)  
            
            **Project**:  
            🛠️ Library Management System
            """)
        
        with cols[2]:
            st.subheader("📅 Days 31-33: Basic DSA")
            st.markdown("""
            **Core Concepts**:  
            - Arrays, strings, sorting  
            - Time complexity analysis  
            
            **Resources**:  
            📺 [Abdul Bari Playlist](https://youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)  
            ⚔️ [LeetCode Easy](https://leetcode.com/problemset/all/?difficulty=EASY)  
            
            **Project**:  
            🛠️ Sorting Visualizer
            """)
    
    st.markdown("---")
    
    # Phase 3: Specialization (Days 36-50)
    st.header("🎯 Phase 3: Specialization (Days 36-50)")
    
    with st.expander("🧠 AI & Data Science (6 days)"):
        cols = st.columns(2)
        with cols[0]:
            st.subheader("📅 Days 36-38: Scikit-learn")
            st.markdown("""
            **Core Concepts**:  
            - Pipelines, hyperparameter tuning  
            - Feature engineering  
            
            **Resources**:  
            📺 [Data School Tutorials](https://youtube.com/playlist?list=PL5-da3qGB5ICeMbQuqbbCOQWcS6OYBr5A)  
            📖 [Sklearn Docs](https://scikit-learn.org/stable/user_guide.html)  
            
            **Project**:  
            🛠️ Twitter Sentiment Analyzer
            """)
        
        with cols[1]:
            st.subheader("📅 Days 39-41: Deep Learning")
            st.markdown("""
            **Core Concepts**:  
            - Neural networks basics  
            - TensorFlow/Keras API  
            
            **Resources**:  
            📺 [TensorFlow YouTube](https://www.youtube.com/@TensorFlow)  
            🖼️ [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)  
            
            **Project**:  
            🛠️ Handwritten Digit Recognizer
            """)
    
    with st.expander("⚔️ Competitive Coding (6 days)"):
        cols = st.columns(2)
        with cols[0]:
            st.subheader("📅 Days 42-44: Intermediate DSA")
            st.markdown("""
            **Core Concepts**:  
            - Trees, graphs, recursion  
            - Dynamic programming  
            
            **Resources**:  
            📺 [takeUforward Playlist](https://youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz)  
            ⚔️ [LeetCode Medium](https://leetcode.com/problemset/all/?difficulty=MEDIUM)  
            """)
        
        with cols[1]:
            st.subheader("📅 Days 45-47: C++ for CP")
            st.markdown("""
            **Core Concepts**:  
            - Advanced STL usage  
            - Bit manipulation  
            
            **Resources**:  
            📚 [CP-Algorithms](https://cp-algorithms.com/)  
            🏆 [Codeforces Div3](https://codeforces.com/)  
            """)
    
    with st.expander("🌐 Full Stack (5 days)"):
        st.subheader("📅 Days 48-50: Angular.js")
        st.markdown("""
        **Core Concepts**:  
        - Directives, controllers  
        - Services, routing  
        
        **Resources**:  
        📖 [AngularJS Guide](https://docs.angularjs.org/guide)  
        📺 [Node.js Crash Course](https://youtu.be/fBNz5xF-Kx4)  
        
        **Project**:  
        🛠️ Todo SPA with Node Backend
        """)
    
    st.markdown("---")
    
    # Phase 4: Integration (Days 51-60)
    st.header("🚀 Phase 4: Integration (Days 51-60)")
    
    with st.expander("🔄 Cross-Domain Projects (3 days)"):
        st.subheader("📅 Days 51-53: Full-Stack Data App")
        st.markdown("""
        **Project Components**:  
        - Flask backend with Pandas/NumPy  
        - Angular.js frontend  
        - Streamlit admin dashboard  
        
        **Resources**:  
        🐍 [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)  
        🚀 [Render Deployment Guide](https://render.com/docs/deploy-flask)  
        
        **Deliverables**:  
        ✅ Deployed web app  
        ✅ Clean GitHub repo with docs  
        """)
    
    with st.expander("🤖 AI Microservices (3 days)"):
        st.subheader("📅 Days 54-56: ML as a Service")
        st.markdown("""
        **Project Components**:  
        - TensorFlow model in Python  
        - Node.js API wrapper  
        - Docker containerization  
        
        **Resources**:  
        🐳 [Docker Get Started](https://docs.docker.com/get-started/)  
        📦 [FastAPI Tutorial](https://fastapi.tiangolo.com/)  
        
        **Deliverables**:  
        ✅ Docker image on Docker Hub  
        ✅ Postman API documentation  
        """)
    
    with st.expander("🎓 Portfolio Polish (4 days)"):
        cols = st.columns(2)
        with cols[0]:
            st.subheader("📅 Days 57-58: GitHub Portfolio")
            st.markdown("""
            **Tasks**:  
            - Organize all projects in GitHub  
            - Create READMEs with screenshots  
            - Set up GitHub Pages  
            
            **Resources**:  
            📚 [GitHub Guides](https://guides.github.com/)  
            🎨 [README Templates](https://github.com/othneildrew/Best-README-Template)  
            """)
        
        with cols[1]:
            st.subheader("📅 Days 59-60: Demo Prep")
            st.markdown("""
            **Tasks**:  
            - Record 2-min project demos  
            - Prepare ICPC code samples  
            - GSOC application materials  
            
            **Resources**:  
            🎥 [Loom](https://www.loom.com/) for recording  
            📝 [GSOC Tips](https://google.github.io/gsocguides/student/)  
            """)

if __name__ == "__main__":
    display_roadmap()
