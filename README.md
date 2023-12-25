# diabetes prediction flask app

Live Now:- https://diabetes-prediction-2.onrender.com/

Abstract
Type 2 diabetes mellitus (T2DM) is a widespread chronic metabolic disorder that necessitates 
early prediction and effective management for optimal patient outcomes. This research examined 
the performance of various machine learning algorithms in predicting T2DM risk using a dataset 
comprising relevant features. Logistic Regression (LR), Support Vector Machine (SVM), Decision 
Tree (DT), Random Forest (RF), and Artificial Neural Networks (ANN) were evaluated. The study 
utilized the Pima Indians Diabetes Database as the primary data source, supplemented by data 
from Akkaraipattu Hospital to ensure a comprehensive analysis of diabetes-related factors, 
outcomes, and interventions. This collaborative approach increased the validity and 
generalizability of the findings, offering a robust understanding of diabetes in the study population, 
including male patients.
The dataset encompassed a substantial number of T2DM patients, enabling multiple experiments 
to assess algorithm performance. Initially, LR, SVM, DT, and RF were trained and evaluated using 
various performance metrics such as testing accuracy, precision, recall, F1-score, and AUC. RF 
achieved the highest performance, with a testing accuracy of 0.7798, closely followed by LR and 
SVM with accuracies of 0.7738 and 0.7798, respectively. DT demonstrated relatively lower 
performance, with a testing accuracy of 0.7321.
To further enhance predictive accuracy, ANN models were developed with different 
hyperparameters, including epochs, batch size, hidden layers, and dropout layers. Eight ANN 
models were created with varying hyperparameter combinations, and their performance was 
assessed using diverse metrics. Results indicated significant variations in the performance of ANN 
models based on the utilized hyperparameters. Among the ANN models, Model 1 exhibited 
relatively better performance, employing higher epochs (500) and a smaller batch size (20), 
achieving testing accuracies of 0.7440 and 0.7619 with epochs (200) and a larger batch size (40), 
respectively. In contrast, Model 2 and Model 3, utilizing higher epochs (500) and a larger batch 
size (40), demonstrated comparatively lower performance, with accuracies of 0.6845 and 0.6785, 
respectively.
Additionally, the inclusion of dropout layers in ANN models influenced performance, with models 
lacking dropout layers displaying better testing accuracy and F1-score. Moreover, the number of 
vi
hidden layers impacted performance, as models with 3 hidden layers outperformed those with 4 or 
5 layers. The findings underscore the necessity for meticulous hyperparameter tuning, 
encompassing epochs, batch size, hidden layers, and dropout layers, to optimize the performance 
of ANN models in T2DM risk prediction.

4.4 Model selection and web application development
The RF model, which was identified as the best-performing model among the models evaluated, 
has yielded promising results in the predict of T2DM. With an accuracy of 77%, an AUC value of 
0.84, precision of 0.79, recall of 0.78, and an f1-score of 0.78, this RF model has demonstrated 
notable performance. Subsequently, the model was saved as a file with the ".pkl" extension 
utilizing the Python pickle library, and was seamlessly integrated into the Flask web app for further 
deployment and utilization in practical applications.
In the development of the Flask web application, the initial step involved the creation of a basic 
plan for the HTML page layout, as depicted in Figure 42, 43. Subsequently, the HTML page was 
crafted in the second stage, following the established layout. The Flask app was installed using the 
"pip install flask" command, and the required environment was configured accordingly. The 
index.html page was then added to the default route by Flask. Within the index.html page, a form 
was implemented to capture the attributes necessary for measuring diabetes. The information 
obtained from the form was then transmitted to the Flask backend through the post method. In the 
backend, the RF model was imported and diabetes was predicted by incorporating the obtained 
attributes.
Upon receiving a diabetes diagnosis, the system will generate a response indicating "Diabetic 
(Positive)." The importance of seeking prompt medical treatment is strongly emphasized, as 
depicted in Figure 46. Conversely, if the absence of diabetes is determined, the system will display 
the message "Good news! You do not have diabetes." Furthermore, maintaining a healthy lifestyle 
is highlighted as crucial for optimizing overall health

![Screenshot 2023-03-12 004616](https://user-images.githubusercontent.com/70307019/224507531-dbf6d2ad-ba1b-4dd0-bef0-7d46452913d4.png)
![Screenshot 2023-03-12 004738](https://user-images.githubusercontent.com/70307019/224507552-87094b02-0759-44d8-9472-702b971d44f8.png)
