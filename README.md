
<p align="center">
  <img src="https://altaml.com/media/ul4ibm45/logo-for-dark.png?">
</p>

# AltaML Hackathon-2022 
# THEME: Empowering Ethical AI practices
# Project title: AI4HealthyStaff

## Description
This project is going to help with detecting burnout and fatigue in call centre agents based on emetion detection. Emotion detection is done by utilizing the BERT (Bidirectional Encoder Representations from Transformers) model. The trained model will give five emotions as outputs which will be used to create a curve representing each employee's change of emotions.

Due to the limitation of Github, not all components are presented in the repository.

## Installation & Usage
1. In order to setup the conda environment, run `make setup-environment` from bash in the root directory of the repository.
2. The created virtual environment is labeled based on the name saved in `environment.yaml`. Run `conda activate hackathon2022-scale` to work from the virtual environment.
3. In order to use Azure services, you need to create a `access_key.env` file in the root directory and set `SUBSCRIPTION_KEY="your_subscription_key"` and `REGION="your_azure_service_region"` in separate lines. To connect to File Share Storage, add `AZURE_STORAGE_CONNECTION_STRING=your_string_connection`. This should be implemented prior to the following instructions.
4. Make sure you have the `BERT` pretrained model accessible in `model/` directory. Both `.h5` and `.preproc` files are required. Due to the git repo size constraint, the model is mounted on `Azure File Share Storage` and can be accessed on the `Azure Compute Machine`. 
  <img src=".gitimages/model.png" width="600" height="300"/>
7. Two options exist for emotion detection:
    - pass in data pipeline address: loop through data files -> speech to text -> detect emotion from text. Run `make predict-emotion-data-pipeline`
    - pass in one audio file: speech to text -> detect emotion from text. Run `make predict-emotion-file`
8. The results are passed to the `power apps` api that can be viewed by the supervisor.



## Technology

<img src="https://user-images.githubusercontent.com/37459996/196521698-01cbe418-6389-454b-8ddf-d140ee9c1e5a.png" width="600" height="600"/>


## Results
A curve representing emotions for individuals working in the call centre. 

    Joy: 4

    Neutral: 3

    Sadness: 2

    Fear: 1

    Anger: 1

We also propose a notification system to recommend checking on agents who are experiencing burnout or depression. The picture below shows the user interface designed by Power Apps.
        
        
<img src="https://user-images.githubusercontent.com/37459996/196503217-37334144-3691-4277-b0ad-67cac1edac1e.png" width="1000" height="500"/>


<img src="https://user-images.githubusercontent.com/37459996/196529553-d6558de6-2094-4d0a-baf1-829984419227.JPG" width="300" height="100"/>


## MSFT outlined 6 responsible AI core values

1. Fairness- AI systems should treat all people fairly 

      - Problem: 
         
         * Speaking English with accent can cause issues with Speech to Text service 
      - Solutions: 
          * Covered by Microsoft Azure Speech to Text 
          * Optimize the model using datasets including various accents such as Indian Accent and Foreign Accented English [1][2]. 
      - Problem: 
         * Non-native English speakers might have a limited vocabulary of positive words compared to native English speaker. 
      - Solution:
          * We propose using speech analyzer to help with that [3].
      - Problem: 
          * misusing the product as a rating system. 
      - Solution: 
          * In the contract, it will be stated that the service is provided only for detecting burnout and not for rating. The clients are not allowed to use it as a rating system based on our terms of service.


2. Reliability & Safety – AI systems should perform reliably and safely 

      - Problem: 
          * The probability of each emotions might show uncertinty in the output. For example: 50% joy and 50% neutral
      - Solution: 
          * we use the help of speech analyzer and also the preference of the client. Each use case of this system can have its own needs. Morover, the help of a second model considering emotion mining using speech can help in uncertain situations.
          
          
3. Privacy & Security – AI systems should be secure and respect privacy 



      - Problem:
          * Customers should have consent for their voices to be recorded.
      - Solution: 
          * It should be announced that the calls will be recorded for quality purposes.
      - Problem:
          * Recording the personal and sensitive information has no value for the product and will come with a high responsibility.
      - Solution: 
          * Automatically removing name and account information from voices
          * Text files are not stored at all and are just used as the input of the model
      - Implemented Azure Key Vault to ensure a secure practice of key management
      - Data storage and security: using microsoft cloud storage
      - The data should not be sold and its solo use is to improve the performance of the model
  


4. Inclusiveness – AI systems should empower everyone and engage people 


      - Problem: The accuracy of converting female or minority voices with accent to text should not be lower than native English speakers.
      - Solution: Speech to Text is handled by microsoft speech to text service [4] and the model will be improved by using datasets including various accents such as Indian Accent and Foreign Accented English [1][2]


5. Transparency – AI systems should be understandable 
      - The ML pipeline (shown below) is clear and easy to understand.
    
        <img src="https://user-images.githubusercontent.com/37459996/196529747-e6e04fdc-1e4d-451d-b36c-dcdd95387243.png" width="500" height="600"/>

      - Transparency does not mean disclosing intellectual property [5].

      - The features that are used in the model should be explained to the manager and with permission, to the employees.
      
  
6. Accountability – People should be accountable for AI systems
    - There is a built-in feedback system where management can report issues and recommendations.
    - Using the provided feedback, the model will be updated and imporved.
    - Performance monitooring is done on a weekly basis by managers and monthly basis by the product producers or when requested [6]
____________________________


### Data Source: 
[1] https://github.com/AI4Bharat/NPTEL2020-Indian-English-Speech-Dataset

[2] https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP2/K7EQTE

http://yanran.li/dailydialog.html

https://www.site.uottawa.ca/~diana/resources/emotion_stimulus_data/

www.affective-sciences.org/index.php/download_file/view/395/296/



#### Additional Sources:

[The BERT model]([https://github.com/amtwo/Data-Blogger-Resource-Kit/wiki/Demo-data-repositories-&-Mock-data-creation](https://github.com/lukasgarbas/nlp-text-emotion/blob/master/bert.ipynb)

[3] https://github.com/MiteshPuthran/Speech-Emotion-Analyzer

[4] https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/speech-to-text/guidance-integration-responsible-use

[5] https://www.forbes.com/sites/aparnadhinakaran/2021/09/10/overcoming-ais-transparency-paradox/?sh=17b4e8c44b77
[6] https://hbr.org/2021/08/how-to-build-accountability-into-your-ai
[Ethical AI document] https://docs.google.com/document/d/11sS1JN46QPuiOZ1dH6zHxr4ifee7regMMEXlxbnfOIs/edit#
