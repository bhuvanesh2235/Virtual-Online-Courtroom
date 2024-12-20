# Virtual Online Courtroom

## Project Overview
The **Virtual Online Courtroom** is an innovative solution aimed at digitizing judicial proceedings. It comprises:
- A **web application** for managing case details, user information, and generating reports.
- An **Android application (Courtup App)** for conducting video conferencing between users and judges. The video calls are recorded and analyzed using AI to predict deception through face recognition.

The project integrates various modules to streamline courtroom operations and provide a seamless experience for users, judges, and lawyers.

---

## Key Features
### **Web Application**
1. **Welcome Page**: Includes links to the user page, cases page, uploads page, reports page, and lawyers page.
2. **User Page**: 
   - Collects user details such as First Name, Last Name, Gender, Email, Password, and Place.
   - Stores the data in a MySQL database.
3. **Cases Page**:
   - Collects case details: Case Number, User ID, Description, and Status (Open/Closed).
4. **Uploads Page**:
   - Allows users to upload files related to a specific case.
   - Inputs include Case ID and associated files, stored in a separate drive.
5. **Reports Page**:
   - Allows input of case reports by Case ID.
   - Generates reports and emails them to both the user and the judge.
6. **Lawyers Page**:
   - Displays details of lawyers, including Case ID, Specialization, Experience, and Expected Price.
   - Allows clients to choose lawyers based on their requirements.

### **Android Application (Courtup App)**
1. Video conferencing between users and judges.
2. Recorded video calls are analyzed by an AI deception prediction model.
3. Meeting IDs are generated via the web application.
4. Output of the AI model is provided to the judge for better judgment.

---

## Technologies Used
- **Frontend**: Node.js
- **Backend**: Django
- **Database**: MySQL
- **AI Model**: Face Recognition for deception prediction
- **Other Libraries**: Axios for connecting frontend and backend
- **Cloud Storage**: Separate drive for storing uploaded files

---

## Project Workflow
1. Users log in or sign up through the web application.
2. Case details, user data, and uploads are managed through respective web pages.
3. Lawyers can be selected by clients based on specialization and experience.
4. Judges and users connect through the Courtup App for video conferencing.
5. Video call recordings are analyzed for deception using AI.
6. Case reports are generated and sent via email.

---

## Demo Images and Video
Click on the links below to view images and demo videos of the project:

### **Android Application**
- [![Courtup App Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Courtup%20App%20Pic.png)](https://youtu.be/1d-SEfJMSxs) 
- ![App Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/App%20Pic.png)
- ![App Video Call Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/App_Video_Call%20Pic.png)

### **Web Application**
- [![Website Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website%20Pic.png)](https://youtu.be/zti8aR7Ro-c) 
- ![Website Case Page Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website_Case_Page%20Pic.png)
- ![Website Drive Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website_Drive%20Pic.png)
- ![Website Lawyers Page Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website_Lawyers_Page%20Pic.png)
- ![Website Lawyers Page 1 Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website_Lawyers_Page_1%20Pic.png)
- ![Website Reports Page Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website_Reports_Page%20Pic.png)
- ![Website Uploads Page Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website_Uploads_Page%20Pic.png)
- ![Website User Page Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/Website_User_Page%20Pic.png)

### **Database**
- ![SQL Database Pic](https://github.com/bhuvanesh2235/Virtual-Online-Courtroom/blob/main/Images/SQL%20Database%20Pic.png)

---
