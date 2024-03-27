import streamlit as st
from PIL import Image
from ultralytics import YOLO
import io
import json

with open('treat.json', 'r') as file:
    disease_data = json.load(file)
def home():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(to bottom, #f6f6f6, #ffffff);
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('🌿 Welcome to Plant Disease Detection App 🌿')
    st.markdown(
        """
        <div style='text-align: center;'>
        <h2 style='color: #006600;'>Identify Plant Diseases with Ease</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.write("This application is designed to help identify diseases in plant leaves using the latest deep learning techniques.")
    st.image('./static/l.png', use_column_width=True)

    st.markdown("---")
    st.header("Why Use Our App? 🌟")
    st.markdown("""
        - <span style='color: #006600;'>**Accuracy**: Our model is trained on a large dataset to provide accurate detection results. :dart:</span>
        - <span style='color: #006600;'>**Ease of Use**: Simply upload an image, and our app will analyze it for you. :computer:</span>
        - <span style='color: #006600;'>**Fast**: Get instant results without any delays. ⏱️</span>
        - <span style='color: #006600;'>**Accessibility**: Our app is accessible on various devices and platforms. 📱💻</span>
        - <span style='color: #006600;'>**Free to Use**: Our application is completely free for all users. 💰</span>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.header("How It Works 🧠")
    st.write("Our application uses a state-of-the-art deep learning model, specifically YOLOv8, to detect diseases in plant leaves. The model has been trained on a diverse dataset of plant diseases to ensure robust performance. Once you upload an image, the model processes it and identifies any present diseases.")
    st.image('./static/h.png', use_column_width=True)

    st.markdown("---")
    st.header("Benefits 🌱")
    st.markdown("""
        - <span style='color: #006600;'>**Early Detection**: Detect diseases early to prevent widespread damage to crops. :seedling:</span>
        - <span style='color: #006600;'>**Remote Accessibility**: Access the application from anywhere, anytime. :globe_with_meridians:</span>
        - <span style='color: #006600;'>**Cost-effective**: Eliminate the need for manual inspection, saving time and resources. :money_with_wings:</span>
        - <span style='color: #006600;'>**User Community**: Join our community to share insights and learn from others. 👥🌍</span>
        - <span style='color: #006600;'>**Educational Resources**: Access educational materials to learn more about plant diseases. 📚🌱</span>
    """, unsafe_allow_html=True)
    st.image('./static/b.jpg', use_column_width=True)

    st.markdown("---")
    st.header("Additional Features 🚀")
    st.markdown("""
        - <span style='color: #006600;'>**Multiple Plant Species**: Our model can detect diseases across various plant species. :deciduous_tree:</span>
        - <span style='color: #006600;'>**User-Friendly Interface**: The app is designed to be intuitive and easy to use for all users. :iphone:</span>
        - <span style='color: #006600;'>**Continuous Improvement**: We're constantly updating and improving our model to enhance performance. :chart_with_upwards_trend:</span>
        - <span style='color: #006600;'>**Customization**: Customize the app settings to suit your preferences. ⚙️</span>
        - <span style='color: #006600;'>**Real-time Updates**: Get real-time updates on new features and improvements. 🔄</span>
    """, unsafe_allow_html=True)
    st.image('./static/train_batch2.jpg', use_column_width=True)

    st.markdown("---")
    st.header("Customer Feedback 📣")
    st.markdown("""
        - <span style='color: #006600;'>\"I've been using this app for a while now, and it's been a game-changer for my farming practices!\"</span> - John
        - <span style='color: #006600;'>\"The accuracy of disease detection is impressive, and the interface is very user-friendly.\"</span> - Mary
        - <span style='color: #006600;'>\"I love how easy it is to access the app from my phone and get instant results.\"</span> - David
    """, unsafe_allow_html=True)
    st.image('./static/labels.jpg', use_column_width=True)

    st.markdown("---")
    st.header("Case Studies 📊")
    st.markdown("""
        - Case Study 1: Increased crop yield through early disease detection
        - Case Study 2: Optimizing pesticide use with accurate disease diagnosis
        - Case Study 3: Sustainable agriculture practices using our app
    """)

    st.markdown("---")
    st.header("Research Publications 📄")
    st.markdown("""
        - Publication 1: Deep learning for plant disease detection
        - Publication 2: YOLOv8 architecture for object detection in agriculture
        - Publication 3: Impact of technology on modern agriculture
    """)

    st.markdown("---")
    st.header("FAQs ❓")
    st.markdown("""
        - How accurate is the disease detection?
        - Can I use the app for different types of plants?
        - Is my data secure when using the app?
    """)

    st.markdown("---")
    st.header("Video Tutorials 🎥")
    st.markdown("""
        - Tutorial 1: Uploading an image and interpreting the disease detection results
        - Tutorial 2: Understanding the different features and settings of the app
        - Tutorial 3: Tips and tricks for maximizing the app's effectiveness
    """)

    st.markdown("---")
    st.header("Glossary 📖")
    st.markdown("""
        - Glossary Term 1: Phytopathology
        - Glossary Term 2: Fungicide Resistance
        - Glossary Term 3: Pathogen Identification
    """)

    st.markdown("---")
    st.header("News and Updates 📰")
    st.markdown("""
        - Announcement 1: New features added to the app
        - Announcement 2: Webinar on advancements in plant disease detection
        - Announcement 3: Collaboration with leading agricultural organizations
    """)

    st.markdown("---")
    st.header("Partnerships and Collaborations 🤝")
    st.markdown("""
        - Partner 1: Agricultural Research Institute
        - Partner 2: Farmers Cooperative Association
        - Partner 3: International Agricultural Development Fund
    """)

    st.markdown("---")
    st.header("Testimonials 🌟")
    st.markdown("""
        - Testimonial 1: Improved crop yield and reduced losses
        - Testimonial 2: User-friendly interface and accurate results
        - Testimonial 3: Collaborative approach to solving agricultural challenges
    """)

    st.markdown("---")
    st.write('Please select "Detection" from the sidebar to start detecting plant diseases.')

def detection():
    st.title('🔍 Plant Disease Detection 🔍')
    st.write('Upload an image of a plant leaf below to detect diseases.')
    st.image('./static/l.png', use_column_width=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file)
        
        model = YOLO("./model/best.pt")  
        results = model(pil_image)  
        
        names = model.names  
        for r in results:
            for c in r.boxes.cls:
                object_name = names[int(c)]
                st.title(f"Disease: {object_name}")
                st.image(r.plot(), caption='Detected Object', use_column_width=True)
                disease_found = False
                for disease in disease_data['diseases']:
                    if disease['name'].lower() == object_name.lower():
                        disease_found = True
                        st.success("Disease detected!")
                        st.subheader("Symptoms:")
                        st.write(disease['symptoms'])
                        st.subheader("Causes:")
                        st.write(disease['causes'])
                        st.subheader("Treatment:")
                        st.write(disease['treatment'])
                        st.subheader("Pesticides:")
                        st.write(', '.join(disease['pesticides']))
                        st.subheader("Prevention:")
                        st.write(disease['prevention'])
                        
                if not disease_found:
                    st.warning("No disease information found for this object.")

def about():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(to bottom, #f6f6f6, #ffffff);
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('ℹ️ About the Project ℹ️')
    st.write('Welcome to our plant disease detection project!')

    st.header("Project Overview 🌱")
    st.write("This project aims to provide an interactive platform for detecting plant diseases. We utilize the YOLOv8 model, trained on the PlantDoc dataset, to achieve accurate detection. Our goal is to assist farmers and agronomists in identifying and managing plant diseases effectively.")
    st.image('./static/l.png', use_column_width=True)

    st.header("Our Mission 🚀")
    st.write("Our mission is to revolutionize the way plant diseases are detected and managed. By leveraging cutting-edge technology, we aim to empower farmers and agronomists with accurate and timely information to protect their crops and ensure food security.")

    st.header("Model Architecture 🧠")
    st.write("Our model architecture is based on YOLOv8, a state-of-the-art object detection algorithm. YOLOv8 offers a balance between accuracy and speed, making it ideal for real-time applications like plant disease detection. With its ability to detect multiple diseases simultaneously, our model provides comprehensive insights for farmers.")

    st.header("Dataset 📊")
    st.write("We have curated a comprehensive dataset, known as PlantDoc, consisting of thousands of images of plant leaves affected by various diseases. The dataset is meticulously annotated to facilitate model training and validation. We continuously update and expand the dataset to improve the robustness of our model.")

    st.header("Collaboration 🤝")
    st.write("We collaborate with agricultural experts, researchers, and farmers to ensure the relevance and effectiveness of our solution. By working closely with the agricultural community, we gather valuable insights and feedback to drive innovation and address real-world challenges.")

    st.header("Future Directions 🎯")
    st.write("In the future, we envision expanding our platform to include additional features such as disease severity assessment, personalized recommendations for disease management, and integration with agricultural machinery for automated field monitoring. We are committed to leveraging technology to create sustainable solutions for agriculture.")

    st.header("Impact 🌍")
    st.write("Our project has the potential to have a significant impact on agriculture and food security. By enabling early detection and effective management of plant diseases, we can minimize crop losses, increase agricultural productivity, and ensure a more sustainable food supply for future generations.")

    st.header("Ethical Considerations 🛡️")
    st.write("We are committed to ethical principles in the development and deployment of our technology. We prioritize data privacy, transparency, and fairness in our algorithms. Additionally, we strive to address any potential biases and ensure equitable access to our solution for all stakeholders.")

    st.header("Community Engagement 👥")
    st.write("We actively engage with the agricultural community through workshops, webinars, and outreach programs. By fostering collaboration and knowledge-sharing, we aim to build a supportive ecosystem that enables continuous improvement and innovation in agriculture.")

    st.header("Team 👩‍💼👨‍💼")
    st.write("Our team consists of passionate individuals with diverse backgrounds in agriculture, data science, and software engineering. Together, we are dedicated to leveraging our expertise to make a positive impact on agriculture and society.")

    st.header("Acknowledgments 🙏")
    st.write("We would like to express our gratitude to all the organizations and individuals who have contributed to this project, including our partners, collaborators, and supporters. Your contributions are invaluable in driving our mission forward.")

    st.header("Contact Us 📧")
    st.write("If you have any questions, suggestions, or collaboration opportunities, please feel free to reach out to us at contact@example.com.")

    st.header("Results Image")
    results_img = Image.open("./static/results.png")
    st.image(results_img, caption="Results Image", use_column_width=True)

    st.header("Training Batch Image")
    train_batch_img = Image.open("./static/train_batch2.jpg")
    st.image(train_batch_img, caption="Training Batch Image", use_column_width=True)

    st.header("Validation Batch Image")
    val_batch_img = Image.open("./static/val_batch2_labels.jpg")
    st.image(val_batch_img, caption="Validation Batch Image", use_column_width=True)

    st.header("F1 Curve Plot")
    f1_curve_img = Image.open("./static/F1_curve.png")
    st.image(f1_curve_img, caption="F1 Curve Plot", use_column_width=True)

    st.header("PR Curve Plot")
    pr_curve_img = Image.open("./static/PR_curve.png")
    st.image(pr_curve_img, caption="PR Curve Plot", use_column_width=True)

    st.header("Confusion Matrix")
    confusion_matrix_img = Image.open("./static/confusion_matrix.png")
    st.image(confusion_matrix_img, caption="Confusion Matrix Plot", use_column_width=True)


def contact():
    st.title('📞 Contact Us 📞')
    st.write('For any inquiries or feedback, please feel free to contact us using the form below. We value your input and will respond to you as soon as possible.')

    st.header("Contact Form 📝")
    name = st.text_input("Name")
    email = st.text_input("Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")
    if st.button("Submit"):
        st.success("Thank you for reaching out! We'll get back to you shortly.")

    st.header("Other Ways to Reach Us 🌐")
    st.write("You can also reach us through the following channels:")
    st.write("- Email: contact@example.com")
    st.write("- Phone: +1234567890")
    st.write("- Social Media:")
    st.write("  - Twitter: [@example](https://twitter.com/example)")
    st.write("  - Facebook: [ExamplePage](https://www.facebook.com/examplepage)")
    st.write("- Online Chat: Visit our website and chat with our support team.")

    st.header("Visit Us 📍")
    st.write("Feel free to visit us at our office:")
    st.write("123 Example Street, City, Country")
    st.write("Our office hours are from Monday to Friday, 9:00 AM to 5:00 PM.")
    st.write("You can schedule an appointment by contacting us in advance.")

    st.header("Feedback Form 📣")
    st.write("We value your feedback! Please take a moment to fill out our feedback form:")
    st.write("[Feedback Form](https://forms.example.com)")

def main():
    st.sidebar.title('🌐 Navigation 🌐')
    page = st.sidebar.selectbox("Select a page", ["Home", "Detection", "About", "Contact Us"])

    if page == "Home":
        home()
    elif page == "Detection":
        detection()
    elif page == "About":
        about()
    elif page == "Contact Us":
        contact()

if __name__ == "__main__":
    main()
