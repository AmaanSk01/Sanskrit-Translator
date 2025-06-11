# Sanskrit-Translator

![image](https://github.com/user-attachments/assets/11ba6625-5f65-4ace-91b3-581172733504)
Sanskrit, one of the oldest and most culturally significant languages, poses challenges in understanding and translation due to its complexity and limited accessibility. To address this, the AI-Powered Sanskrit Translator offers an intelligent solution that extracts and translates Sanskrit texts into multiple modern languages. By integrating OCR technology (Tesseract) with AI-based translation (Google Translate API), the system can process scanned documents, PDFs, and images, providing real-time translation and downloadable results through a user-friendly interface. Developed using Python (Flask), HTML, and libraries like Poppler, PyPDF2, and SQLite, this tool delivers accurate and accessible Sanskrit translations, making it highly beneficial for researchers, students, and scholars engaged in Sanskrit literature.

Scope:
The Sanskrit Translator project supports automatic translation of Sanskrit text into multiple languages, ensuring users can easily understand and interpret ancient literature with contextual accuracy and linguistic integrity. It integrates Optical Character Recognition (OCR) to extract text from scanned images and handwritten documents, aiding in the digitization of old manuscripts and inscriptions. With multi-language support, the system caters to a global audience by offering translations in languages like English, Hindi, and more. To enhance usability, it includes features for downloading or copying translated content, which is especially useful for researchers and educators. The user-friendly and interactive interface ensures smooth navigation for users of all backgrounds. Additionally, the project leverages AI and NLP techniques to deliver accurate, context-aware translations and continuously improves through machine learning, making it a dependable tool for language analysis and preservation.

Library Used:
Flask – A lightweight Python web framework used to build the backend, manage routes, handle requests, and render HTML templates.
Googletrans – A Python library that interfaces with Google Translate API to perform real-time, multi-language text translation.
Pytesseract – A wrapper for Tesseract OCR that extracts editable text from images and scanned documents in multiple languages.
pdf2image – Converts PDF pages into image formats like PNG or JPG for OCR-based text extraction from scanned PDFs.
OS – Provides functions to handle file paths, directories, and system-level operations essential for managing uploads and processing.
PIL (Pillow) – A library for opening, manipulating, and preprocessing images to improve OCR accuracy and image handling.
indic_transliteration.sanscript – Enables transliteration of Sanskrit text between scripts like Devanagari and IAST for improved readability and processing.

API Used (Google Translate API):
The Google Translate API is a powerful machine translation service that enables real-time conversion of text across over 100 languages, making it ideal for translating Sanskrit into widely spoken languages like English, Hindi, German, and French. It uses neural machine translation (NMT) to enhance accuracy by understanding context rather than relying on word-for-word translation. The API supports automatic language detection and provides a RESTful interface, allowing seamless integration with Flask-based applications for sending and receiving translated text via HTTP requests. In this project, when users input Sanskrit text, the app.py file sends it to the Google Translate API, which processes it using deep learning models and returns high-quality, context-aware translations. The translated output is then displayed on the user interface with options to copy or download, ensuring an efficient and user-friendly translation experience.

Future Scope:
Integration of Advanced AI/ML Models – Incorporate deep learning-based NLP models trained on Sanskrit to improve translation accuracy and context understanding.
Offline Translation Capability – Enable offline translation using pre-trained models or dictionaries for use without internet access.
Text-to-Speech and Speech-to-Text – Add TTS and STT features to allow users to listen to translations and provide voice input.
Mobile Application Development – Create a dedicated Android/iOS app to offer translation services on-the-go.
Grammar Correction and Contextual Editing – Introduce tools for manual grammar correction and contextual refinement of translations.
Support for More File Formats – Expand support to DOCX, PPTX, XLSX, multi-page PDFs, ZIP files, and multilingual documents.
Collaborative Learning and Dictionary Building – Implement user-feedback features and build a shared Sanskrit dictionary to enhance translation quality over time.

References:
Google Translate API Documentation – https://cloud.google.com/translate/docs (Used for implementing real-time language translation functionalities).
Tesseract OCR Engine – https://github.com/tesseract-ocr/tesseract (Used for extracting text from scanned documents and image files).
Flask – Python Web Framework – https://flask.palletsprojects.com/ (Used to build the backend server and manage translation requests).
W3Schools (HTML, CSS, JavaScript Docs) – https://www.w3schools.com/ (Used for designing the frontend and integrating interactivity).
Sanskrit Documents Collection – https://sanskritdocuments.org/ (Used for understanding Sanskrit grammar and linguistic structure).
Bootstrap Framework – https://getbootstrap.com/ (Used to design responsive and professional UI components).
Natural Language Toolkit (NLTK) – https://www.nltk.org/ (Planned for future implementation of grammar and linguistic features in Sanskrit translation).
Research Articles on Sanskrit Digitization – Various online papers on computational linguistics and Sanskrit language digitization.

Conclusion:
The Sanskrit Translator project marks a major technological advancement in making ancient Sanskrit literature accessible to modern users by integrating AI and OCR technologies. With tools like Tesseract OCR for text extraction and the Google Translate API for multilingual translation, the system bridges the gap between the ancient and digital worlds, enabling users to translate scanned documents, images, PDFs, and typed text into various modern languages. Its user-friendly interface, support for multiple formats, real-time translation, and download options make it highly practical for students, researchers, scholars, and language enthusiasts. Beyond digitizing Sanskrit content, the project sets a solid foundation for future developments like speech-to-text, offline translation, mobile apps, and cloud integration. The inclusion of translation history and downloadable content further enhances its value as a long-term academic and cultural resource, promoting the preservation and global reach of one of the world’s most classical languages.

