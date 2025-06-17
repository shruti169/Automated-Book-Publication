Automated Book Publication Workflow 

 1. Introduction
 This project is a part of an Automated Book Publication Workflow system that integrates AI-generated writing,AI reviewing, and Human-in-the-Loop (HITL) editing into one streamlined workflow.It allows an
editor to view spun chapters, review feedback, make improvements, and track changes. Past versions are stored and compared using ChromaDB.
 
Automated Book Publication Workflow - HITL Editing System

 Step 1: Clone the repository
 $ git clone <your-repo-url>
 
 Step 2: Create virtual environment and activate it
 $ python -m venv venv
 $ source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
 
 Step 3: Install dependencies
 $ pip install -r requirements.txt
 
 Step 4: Run Streamlit app
 $ streamlit run editor_gui.py
 
 5. Workflow Steps
 Step 1: Load AI-spun content and AI-reviewed feedback.
 Step 2: Show editor panel to refine the reviewed version.
 Step 3: Editor checks grammar, clarity, tone, applies suggestions.
 Step 4: Editor provides name and notes, then saves final version.
 Step 5: Save version to file, log the action, and store in ChromaDB.
 Step 6: Allow comparison of past approved versions side-by-side.


 7. How to Use
 1. Launch the Streamlit app using the command.
 2. Review the AI-written content and AI feedback.
 3. Edit the reviewed version to improve readability and tone.
 4. Complete the checklist and fill in your name and change summary.
 5. Click 'Save Final Approved Version' to log and store changes.
 6. Scroll down to compare previous approved versions.
 7. Final Note
    
![Screenshot 2025-06-16 211955](https://github.com/user-attachments/assets/0d18931b-cc77-429e-bbf4-4044994e0c06)
![Screenshot 2025-06-16 211941](https://github.com/user-attachments/assets/fe65b1e2-2a1d-437f-abb5-5c03a1d7ab4c)
![Screenshot 2025-06-16 211923](https://github.com/user-attachments/assets/9196c8e9-e5a0-4e47-bc4f-1d0e1e78991a)
