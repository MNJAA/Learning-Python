from ANSI import CR,C,SL
print(C,CR)


TESTING = [
    {"question": "What is true about bilayer in the cell membrane?",
     "correct_answer": "Hydrophilic is always in the outer layer",
     "wrong_answers": ["Hydrophobic is always in the outer layer", "Both layers are hydrophobic",
                       "Hydrophilic is always in the inner layer"]
     },
]



#premid 1 Theoretical 

Anatomy_questions = [
    {
        'question': "Stab in 1st IC space, what major vessel is injured?",
        'correct_answer': "SVC",
        'wrong_answers': ["Aorta", "Pulmonary artery", "Brachiocephalic vein"]
    },
    {
        'question': "Which is correct about lactating?",
        'correct_answer': "Oxytocin is for milk secretion",
        'wrong_answers': [
            "Prolactin is for uterine contractions",
            "Estrogen is for bone development",
            "Testosterone is for breast growth"
        ]
    },
    {
        'question': "Which is correct about vasa privata and publica of the lung?",
        'correct_answer': "Privata for the lung, publica for the whole body",
        'wrong_answers': [
            "Privata for the whole body, publica for the lung",
            "Both privata and publica for the whole body",
            "Both privata and publica for the lung"
        ]
    },
    {
        'question': "Chest drainage: Monaldi: 2nd IC space midclavicular, Bulau: 5th Ic space midaxillary",
        'correct_answer': "True",
        'wrong_answers': ["False"]
    },
    {
        'question': "Which is correct about anatomical positions?",
        'correct_answer': "Big toe is superior during inversion",
        'wrong_answers': [
            "Thumb is superior during eversion",
            "Heel is superior during dorsiflexion",
            "Index finger is superior during pronation"
        ]
    },
    {
        'question': "Atypical feature of the first rib?",
        'correct_answer': "One facet on the head",
        'wrong_answers': [
            "Two facets on the head",
            "No facets on the head",
            "Three facets on the head"
        ]
    },
    {
        'question': "The left 5th posterior IC vein drained by what?",
        'correct_answer': "Accessory hemiazygos",
        'wrong_answers': [
            "Superior vena cava",
            "Inferior vena cava",
            "Brachiocephalic vein"
        ]
    },
    {
        'question': "Patient came and complained of change in voice. Caused by a tumor between the aortic arch and pulmonary trunk. Which nerve?",
        'correct_answer': "Left recurrent laryngeal",
        'wrong_answers': [
            "Right recurrent laryngeal",
            "Vagus nerve",
            "Phrenic nerve"
        ]
    },
    {
        'question': "Manubriosternal joint damaged. Which rib is likely to be damaged?",
        'correct_answer': "2nd",
        'wrong_answers': ["5th", "8th", "12th"]
    },
    {
        'question': "Layers penetrated during intercostal nerve block? External intercostal muscle -> internal intercostal membrane",
        'correct_answer': "True",
        'wrong_answers': ["False"]
    },
    {
        'question': "Pregnant woman and put anesthesia. Which position?",
        'correct_answer': "Standard fowler",
        'wrong_answers': [
            "Lower fowler",
            "Supine",
            "Prone"
        ]
    },
    {
        'question': "Deepest structure in the thorax that is sensitive to pain?",
        'correct_answer': "Parietal pleura",
        'wrong_answers': [
            "Visceral pleura",
            "Pericardium",
            "Diaphragm"
        ]
    },
    {
        'question': "What is not found in the posterior mediastinum?",
        'correct_answer': "Thyroid gland",
        'wrong_answers': [
            "Descending aorta",
            "Thoracic duct",
            "Esophagus"
        ]
    },
    {
        'question': "Vertebra of sympathetic trunk?",
        'correct_answer': "C8/T1 - L3",
        'wrong_answers': [
            "C1/C2 - C7",
            "L4 - S4",
            "Sacral vertebrae"
        ]
    },
    {
        'question': "Inferior attachment of fibrous pericardium?",
        'correct_answer': "Pericardiacophrenic ligaments",
        'wrong_answers': [
            "Central tendon of diaphragm",
            "Costal cartilages of ribs 2-6",
            "Sternum"
        ]
    },
    {
        'question': "Ductus venosus becomes what?",
        'correct_answer': "Ligamentum venosum",
        'wrong_answers': [
            "Ligamentum arteriosum",
            "Round ligament of liver",
            "Falciform ligament"
        ]
    },
    {
        'question': "2nd left ICS which valve?",
        'correct_answer': "Pulmonary valve",
        'wrong_answers': [
            "Aortic valve",
            "Tricuspid valve",
            "Mitral valve"
        ]
    },
    {
        'question': "4th left ICS which valve?",
        'correct_answer': "Tricuspid valve",
        'wrong_answers': [
            "Aortic valve",
            "Pulmonary valve",
            "Mitral valve"
        ]
    },
    {
        'question': "Coronary groove separates what?",
        'correct_answer': "Atrium from ventricle",
        'wrong_answers': [
            "Left atrium from right atrium",
            "Right ventricle from left ventricle",
            "Aorta from pulmonary artery"
        ]
    },
    {
        'question': "Function of the cardiac skeleton?",
        'correct_answer': "Insulation of ventricular and atrial muscles",
        'wrong_answers': [
            "Providing support to the heart",
            "Promoting blood flow through the heart",
            "Preventing valve prolapse"
        ]
    },
    {
        'question': "What is true about the innervation of the pericardium?",
        'correct_answer': "Sensitively innervated by phrenic nerve",
        'wrong_answers': [
            "Mainly innervated by the vagus nerve",
            "Receives sympathetic innervation only",
            "Has no direct nerve supply"
        ]
    },
    {
        'question': "Function of papillary muscles?",
        'correct_answer': "Keep the AV valves closed",
        'wrong_answers': [
            "Contract to open the AV valves",
            "Aid in ventricular contraction",
            "Regulate blood flow in the coronary arteries"
        ]
    },
    {
        'question': "Sinoatrial nodal branch that supplies SA node in ⅔ of the cases originates from where?",
        'correct_answer': "Right coronary artery",
        'wrong_answers': [
            "Left coronary artery",
            "Circumflex artery",
            "Left anterior descending artery"
        ]
    },
    {
        'question': "Right and left coronary arteries originate from?",
        'correct_answer': "Aorta above aortic valve",
        'wrong_answers': [
            "Aorta below aortic valve",
            "Pulmonary artery",
            "Superior vena cava"
        ]
    },
    {
        'question': "Cough muscle",
        'correct_answer': "Latissimus muscle",
        'wrong_answers': [
            "Diaphragm",
            "Intercostal muscles",
            "Rectus abdominis"
        ]
    },
    {
        'question': "Why do we need foramen ovale in the fetus?",
        'correct_answer': "Lung is closed",
        'wrong_answers': [
            "To facilitate blood flow from the right atrium to the left atrium",
            "To allow oxygen exchange in the lungs",
            "To regulate blood flow to the liver"
        ]
    },
    {
        'question': "What happens if the ductus arteriosus is closed?",
        'correct_answer': "Blood will flow from aorta to pulmonary",
        'wrong_answers': [
            "Blood will flow from pulmonary artery to aorta",
            "Blood circulation will stop",
            "The heart will pump blood backward into the veins"
        ]
    },
    {
        'question': "Musculophrenic artery is damaged. Which part of the diaphragm is not supplied?",
        'correct_answer': "Costal part of diaphragm",
        'wrong_answers': [
            "Central tendon of diaphragm",
            "Crural part of diaphragm",
            "Sternal part of diaphragm"
        ]
    },
    {
        'question': "Phrenic nerve originated from?",
        'correct_answer': "C3 C4 C5",
        'wrong_answers': [
            "C6 C7 C8",
            "C1 C2 C3",
            "T1 T2 T3"
        ]
    },
    {
        'question': "Which of the following structures does not penetrate the diaphragm?",
        'correct_answer': "Left recurrent laryngeal nerve",
        'wrong_answers': [
            "Inferior vena cava",
            "Esophagus",
            "Aorta"
        ]
    },
    {
        'question': "Right dome is at T8. Left dome at?",
        'correct_answer': "T9",
        'wrong_answers': [
            "T10",
            "T7",
            "T6"
        ]
    },
    {
        'question': "Milk flows in the following direction?",
        'correct_answer': "Lobules -> lactiferous duct -> lactiferous sinus -> papilla",
        'wrong_answers': [
            "Papilla -> lactiferous sinus -> lactiferous duct -> lobules",
            "Lobules -> papilla -> lactiferous duct -> lactiferous sinus",
            "Lactiferous duct -> papilla -> lactiferous sinus -> lobules"
        ]
    },
    {
        'question': "Most important lymphatic drainage?",
        'correct_answer': "Axillary lymphatic drainage",
        'wrong_answers': [
            "Inguinal lymphatic drainage",
            "Cervical lymphatic drainage",
            "Popliteal lymphatic drainage"
        ]
    },
    {
        'question': "Sensory innervation of the breast?",
        'correct_answer': "Intercostal nerves 2nd-6th",
        'wrong_answers': [
            "Phrenic nerve",
            "Brachial plexus",
            "Femoral nerve"
        ]
    },
    {
        'question': "How can we increase the pleural space?",
        'correct_answer': "Diaphragm contracts and pulls down to enlarge the pleural cavity",
        'wrong_answers': [
            "Intercostal muscles contract and lift the ribcage",
            "Diaphragm relaxes and moves upward to reduce the pleural cavity",
            "Pleural space cannot be increased"
        ]
    },
    {
        'question': "Right bronchial artery originates from?",
        'correct_answer': "3rd right intercostal artery",
        'wrong_answers': [
            "Aorta",
            "Left subclavian artery",
            "Pulmonary artery"
        ]
    },
    {
        'question': "Cartilage and gland can be found in which of the following?",
        'correct_answer': "Trachea",
        'wrong_answers': [
            "Esophagus",
            "Bronchus",
            "Larynx"
        ]
    },
    {
        'question': "Which of the following is a primary cartilagenous joint?",
        'correct_answer': "Xhipsternal joint",
        'wrong_answers': [
            "Sternoclavicular joint",
            "Intervertebral joint",
            "Pubic symphysis"
        ]
    },
    {
        'question': "Which of the following is not part of the anatomical dead space?",
        'correct_answer': "Alveolar sac",
        'wrong_answers': [
            "Trachea",
            "Bronchi",
            "Bronchioles"
        ]
    },
    {
        'question': "What happens in pneumothorax?",
        'correct_answer': "Lung cannot follow the respiratory movements of the thoracic wall resulting in lack of ventilation for the respective lung",
        'wrong_answers': [
            "Accumulation of fluid in the pleural cavity",
            "Collapse of the lung",
            "Inflammation of the pleura"
        ]
    },
    {
        'question': "Fluid in the pericardial cavity around the heart?",
        'correct_answer': "Pericardial effusion",
        'wrong_answers': [
            "Pleural effusion",
            "Ascites",
            "Cerebrospinal fluid"
        ]
    },
    {
        'question': "Largest reserve space?",
        'correct_answer': "Costodiaphragmatic",
        'wrong_answers': [
            "Costomediastinal",
            "Costovertebral",
            "Costosternal"
        ]
    },
    {
        'question': "Effective during inspiration?",
        'correct_answer': "Diaphragm",
        'wrong_answers': [
            "Intercostal muscles",
            "Abdominal muscles",
            "Accessory muscles of the neck"
        ]
    },
    {
        'question': "What of the following is not a feature of typical ribs?",
        'correct_answer': "They must bind to the sternum",
        'wrong_answers': [
            "They have a costal groove",
            "They articulate with the thoracic vertebrae",
            "They have a head, neck, and tubercle"
        ]
    },
    {
        'question': "What type of joint is interchondral joint?",
        'correct_answer': "Synovial",
        'wrong_answers': [
            "Cartilaginous",
            "Fibrous",
            "Suture"
        ]
    },
    {
        'question': "Muscle needed for yawning?",
        'correct_answer': "External intercostal muscle",
        'wrong_answers': [
            "Diaphragm",
            "Internal intercostal muscle",
            "Sternocleidomastoid muscle"
        ]
    },
    {
        'question': "Heart and pericardium part of which mediastinum?",
        'correct_answer': "Middle",
        'wrong_answers': [
            "Superior",
            "Anterior",
            "Posterior"
        ]
    },
    {
        'question': "What is not true about the esophagus?",
        'correct_answer': "Originates from T3",
        'wrong_answers': [
            "Passes through the diaphragm at the esophageal hiatus",
            "Contains upper and lower sphincters",
            "Conducts food to the stomach"
        ]
    },
    {
        'question': "Parietal pleura?",
        'correct_answer': "Costal pleura + diaphragmatic pleura + mediastinal pleura + cervical pleura",
        'wrong_answers': [
            "Covers the outer surface of the lungs",
            "Is sensitive to pain",
            "Contains the pleural cavity"
        ]
    },
    {
        'question': "What is not true about lung?",
        'correct_answer': "Right lung has lingula",
        'wrong_answers': [
            "Contains bronchi, bronchioles, and alveoli",
            "Divided into lobes",
            "Covered by pleura"
        ]
    },
    {
        'question': "There is a fire and you’re running. What nervous system will help you?",
        'correct_answer': "Sympathetic nervous system will expand bronchi (Bronchodilation) and allow you to run faster",
        'wrong_answers': [
            "Parasympathetic nervous system",
            "Central nervous system",
            "Peripheral nervous system"
        ]
    },
    {
        'question': "Montgomery glands’ function?",
        'correct_answer': "Create airtight seal between baby’s oral cavity and mother’s nipple so no air is drawn by baby",
        'wrong_answers': [
            "Produce milk",
            "Facilitate breastfeeding",
            "Aid in nipple sensitivity"
        ]
    },
    {
        'question': "Apex formed by which borders?",
        'correct_answer': "Left and inferior",
        'wrong_answers': [
            "Right and superior",
            "Anterior and posterior",
            "Superior and inferior"
        ]
    },
    {
        'question': "Thoracic outlet syndrome caused by compression on which artery?",
        'correct_answer': "Subclavian",
        'wrong_answers': [
            "Aortic",
            "Brachial",
            "Carotid"
        ]
    },
    {
        'question': "What is true about the brachiocephalic trunk?",
        'correct_answer': "Passes posterior to the left brachiocephalic vein",
        'wrong_answers': [
            "Arises from the aorta",
            "Supplies the right common carotid artery",
            "Has a short course before dividing into its branches"
        ]
    },
    {
        "question": "A surgeon cuts through the sternum in a child and sees a lobulated structure, called?",
        "correct_answer": "Thymus",
        "wrong_answers": ["Spleen", "Liver", "Pancreas"]
    },
    {
        "question": "The artery in the 9th anterior intercostal space is supplied by?",
        "correct_answer": "Musculophrenic Artery",
        "wrong_answers": ["Internal Thoracic Artery", "Intercostal Artery", "Superior Epigastric Artery"]
    },
    {
        "question": "Which thoracic vertebra has one complete facet on the body and a demifacet?",
        "correct_answer": "T1",
        "wrong_answers": ["T2", "T3", "T4"]
    },
    {
        "question": "What structure is compressed by a tumor between the aortic arch and pulmonary trunk that causes loss of voice?",
        "correct_answer": "Left recurrent laryngeal",
        "wrong_answers": ["Vagus nerve", "Phrenic nerve", "Glossopharyngeal nerve"]
    },
    {
        "question": "Which rib is affected if the manubriosternal joint (sternal angle) is damaged?",
        "correct_answer": "2nd Rib",
        "wrong_answers": ["3rd Rib", "4th Rib", "5th Rib"]
    },
    {
        "question": "Movement of the knee towards the thigh?",
        "correct_answer": "Flexion",
        "wrong_answers": ["Extension", "Abduction", "Adduction"]
    },
    {
        "question": "What is true about the left brachiocephalic vein?",
        "correct_answer": "Passes anterior to the left common carotid and the left subclavian artery",
        "wrong_answers": ["Passes posterior to the left common carotid", "Joins with the right brachiocephalic vein", "Forms the superior vena cava"]
    },
    {
        "question": "If the costal margin is damaged, what ribs will be affected?",
        "correct_answer": "7th – 10th Ribs",
        "wrong_answers": ["1st – 3rd Ribs", "4th – 6th Ribs", "11th – 12th Ribs"]
    },
    {
        "question": "The doctor asks the patient to lie on his chest for a spinal check, which position will the patient be in?",
        "correct_answer": "Prone",
        "wrong_answers": ["Supine", "Lateral recumbent", "Fowler's position"]
    },
    {
        "question": "What additional feature is found in the second rib?",
        "correct_answer": "Tuberosity for serratus anterior muscle",
        "wrong_answers": ["Costal groove", "Articular facet for the tubercle of the rib", "Angle of the rib"]
    },
    {
        "question": "Which layer is responsible for thermal insulation?",
        "correct_answer": "Superficial fascia",
        "wrong_answers": ["Deep fascia", "Muscle tissue", "Subcutaneous tissue"]
    },
    {
        "question": "A patient is experiencing difficulty in swallowing (dysphagia) due to compression on the esophagus, what structure is responsible?",
        "correct_answer": "Left Atrium",
        "wrong_answers": ["Aortic arch", "Trachea", "Left ventricle"]
    },
    {
        "question": "Diminished radial pulse, paranesthesia, pale cold fingers indicates?",
        "correct_answer": "Thoracic outlet syndrome",
        "wrong_answers": ["Carpal tunnel syndrome", "Rotator cuff injury", "Peripheral artery disease"]
    },
    {
        "question": "What is caudal?",
        "correct_answer": "Towards the tail",
        "wrong_answers": ["Towards the head", "Towards the midline", "Away from the body"]
    },
    {
        "question": "Rib number 7 articulate with?",
        "correct_answer": "T6 & T7",
        "wrong_answers": ["T5 & T6", "T7 & T8", "T8 & T9"]
    },
    {
        "question": "Not a part of the posterior mediastinum?",
        "correct_answer": "Thyroid gland",
        "wrong_answers": ["Descending aorta", "Thoracic duct", "Esophagus"]
    },
    {
        "question": "Sympathetic trunk location?",
        "correct_answer": "C8/T1 – L3",
        "wrong_answers": ["C1/C2 – T4", "T5 – L1", "L4 – S3"]
    },
    {
        "question": "A person is given thoracostomy near the sternal margin. Which layers does it penetrate?",
        "correct_answer": "Internal intercostal muscle, external intercostal membrane and transversus thoracis muscle",
        "wrong_answers": ["Parietal pleura", "Innermost intercostal muscle", "Endothoracic fascia"]
    },
    {
        "question": "How does parasympathetic innervation affect peristalsis?",
        "correct_answer": "Increases peristalsis",
        "wrong_answers": ["Decreases peristalsis", "Has no effect on peristalsis", "Causes irregular peristalsis"]
    },
    {
        "question": "What is true about the Vagus nerve (CN X)?",
        "correct_answer": "Largest parasympathetic innervation",
        "wrong_answers": ["Smallest parasympathetic innervation", "Predominantly sympathetic innervation", "No autonomic innervation"]
    },
    {
        "question": "What is false about the intercostal nerves?",
        "correct_answer": "Collateral branch runs on the inferior surface of the rib above",
        "wrong_answers": ["Collateral branch runs on the superior surface of the rib below", "Anterior cutaneous branch supplies the skin", "Posterior cutaneous branch supplies the skin"]
    },
    {
        "question": "What is not true about the nerve block?",
        "correct_answer": "It is given on the upper border of the rib",
        "wrong_answers": ["It is given on the lower border of the rib", "It involves injecting anesthetic near a nerve", "It is used for pain relief"]
    },
    {
        "question": "Where is the external muscle replaced by external membrane?",
        "correct_answer": "At the level of costochondral joint",
        "wrong_answers": ["At the level of costovertebral joint", "At the level of costotransverse joint", "At the level of costosternal joint"]
    },
    {
        "question": "Type of joint that allows pronation and supination?",
        "correct_answer": "Pivot",
        "wrong_answers": ["Hinge", "Ball and socket", "Saddle"]
    },
    {
        "question": "Which artery supplies the 2nd ICS?",
        "correct_answer": "Superior intercostal artery",
        "wrong_answers": ["Internal thoracic artery", "Posterior intercostal artery", "Anterior intercostal artery"]
    },
    {
        "question": "Number of intercostal arteries?",
        "correct_answer": "58",
        "wrong_answers": ["12", "24", "36"]
    },
    {
        "question": "41cm down the esophagus what causes constriction?",
        "correct_answer": "Diaphragmatic",
        "wrong_answers": ["Aortic arch", "Left main bronchus", "Inferior vena cava"]
    },
    {
        "question": "Most important feature in thoracic vertebrae?",
        "correct_answer": "Presence of articular facets (costal facets) and demifacets",
        "wrong_answers": ["Prominent spinous process", "Large vertebral foramen", "Transverse foramen"]
    },
    {
        "question": "Most deep sensitive layer in the chest?",
        "correct_answer": "Parietal pleura",
        "wrong_answers": ["Visceral pleura", "Endothoracic fascia", "Superficial fascia"]
    },
    {
        "question": "Where do the 9th IC arteries arise directly from?",
        "correct_answer": "Musculophrenic Artery",
        "wrong_answers": ["Internal thoracic artery", "Subcostal artery", "Anterior intercostal artery"]
    },
    {
        "question": "A patient fractured the 6th rib, the doctor will do intercostal nerve block, which structure will it puncture?",
        "correct_answer": "Internal intercostal membrane",
        "wrong_answers": ["External intercostal muscle", "Parietal pleura", "Endothoracic fascia"]
    },
    {
        "question": "A patient diagnosed with thoracic outlet syndrome, which signs and symptoms are mostly related to compression on the nerve?",
        "correct_answer": "Numbness and paresthesia",
        "wrong_answers": ["Pain in the chest", "Shortness of breath", "Cyanosis"]
    },
    {
        "question": "What do the facets on the head of a typical rib articulate (attach) to?",
        "correct_answer": "Corresponding vertebrae and vertebrae above",
        "wrong_answers": ["Costal cartilage of the same rib", "Costal cartilage of the rib below", "Transverse process of the same vertebra"]
    },
    {
        "question": "Where is the sinus venorum located?",
        "correct_answer": "Right Atrium",
        "wrong_answers": ["Left Atrium", "Right Ventricle", "Left Ventricle"]
    },
    {
        "question": "Which is not true about the marked part of the heart (Image; Atrioventricular node was marked)?",
        "correct_answer": "It accelerated the frequency of the signal so that the ventricles and atria contract together",
        "wrong_answers": ["It conducts the electrical impulses from the atria to the ventricles", "It is located in the interatrial septum", "It is responsible for the delay in impulse conduction"]
    },
    {
        "question": "The physician heard a murmur in the 2nd ICS left parasternal, which valve is affected?",
        "correct_answer": "Pulmonary Valve",
        "wrong_answers": ["Aortic Valve", "Mitral Valve", "Tricuspid Valve"]
    },
    {
        "question": "What does the umbilical vein become after birth?",
        "correct_answer": "Round ligament of the liver",
        "wrong_answers": ["Ligamentum teres hepatis", "Ductus venosus", "Ligamentum venosum"]
    },
    {
        "question": "What does the ductus venosum become after birth?",
        "correct_answer": "Ligamentum Venosum",
        "wrong_answers": ["Ligamentum teres hepatis", "Round ligament of the liver", "Umbilical ligament"]
    },
    {
        "question": "Where do the coronary arteries originate from?",
        "correct_answer": "Aorta above the aortic valve",
        "wrong_answers": ["Pulmonary artery", "Superior vena cava", "Left atrium"]
    },
    {
        "question": "What branch is not a branch of the left coronary artery?",
        "correct_answer": "Sinuatrial nodal branch",
        "wrong_answers": ["Anterior interventricular branch", "Circumflex branch", "Left marginal branch"]
    },
    {
        "question": "What is true about the innervation of the heart?",
        "correct_answer": "The phrenic nerve is responsible for sensitive innervation of the pericardium (parietal)",
        "wrong_answers": ["Vagus nerve is responsible for sympathetic innervation", "The sympathetic nerves are responsible for parasympathetic innervation", "The cardiac plexus is not involved in cardiac innervation"]
    },
    {
        "question": "What is the function of the cardiac skeleton?",
        "correct_answer": "It isolates the valves and stabilizes them",
        "wrong_answers": ["It provides structural support to the myocardium", "It conducts electrical impulses in the heart", "It regulates blood flow through the coronary arteries"]
    },
    {
        "question": "Why is the foramen ovale present in the embryo?",
        "correct_answer": "Because the lungs are closed",
        "wrong_answers": ["To allow blood flow from the right atrium to the left atrium", "To facilitate gas exchange in the fetal lungs", "To maintain the patency of the ductus arteriosus"]
    },
      {
        "question": "Computed Tomography (CT) scan showed accumulation of fluid around the heart in the pericardial cavity, what is the most possible diagnosis?",
        "correct_answer": "Pericardial effusion",
        "wrong_answers": ["Myocardial infarction", "Aortic dissection", "Pulmonary embolism"]
    },
    {
        "question": "What are the labeled parts in the picture?",
        "correct_answer": "Aorta and Right Ventricle",
        "wrong_answers": ["Left Atrium and Left Ventricle", "Pulmonary Artery and Left Ventricle", "Right Atrium and Pulmonary Artery"]
    },
    {
        "question": "What is the function of papillary muscles?",
        "correct_answer": "Closes the atrioventricular valves",
        "wrong_answers": ["Pumps blood into the pulmonary artery", "Regulates blood flow into the coronary arteries", "Conducts electrical impulses in the heart"]
    },
    {
        "question": "Damage of the sinuatrial node because of occlusion in the sinuatrial nodal artery, which artery does the sinuatrial node branch arise from?",
        "correct_answer": "Right Coronary Artery",
        "wrong_answers": ["Left Coronary Artery", "Circumflex artery", "Anterior interventricular artery"]
    },
    {
        "question": "What is the marked structure in the X-ray scan?",
        "correct_answer": "Right Atrium",
        "wrong_answers": ["Left Atrium", "Right Ventricle", "Left Ventricle"]
    },
    {
        "question": "What happens if the ductus arteriosus does not close?",
        "correct_answer": "The blood travels from the aorta to the pulmonary trunk",
        "wrong_answers": ["The blood travels from the pulmonary trunk to the aorta", "The blood travels from the left atrium to the right atrium", "The blood travels from the right ventricle to the left ventricle"]
    },
    {
        "question": "What is the marked structure?",
        "correct_answer": "Transverse pericardial sinus",
        "wrong_answers": ["Oblique pericardial sinus", "Coronary sinus", "Fossa ovalis"]
    },
    {
        "question": "The pericardium is attached inferiorly by which ligament?",
        "correct_answer": "Pericardiacophrenic ligament",
        "wrong_answers": ["Fibrous pericardium", "Transverse pericardial sinus", "Oblique pericardial sinus"]
    },
    {
        "question": "Which structure opens in the right atrium?",
        "correct_answer": "Coronary Sinus",
        "wrong_answers": ["Inferior vena cava", "Superior vena cava", "Azygos vein"]
    },
    {
        "question": "What does the coronary groove separate?",
        "correct_answer": "Atria and ventricles",
        "wrong_answers": ["Right atrium and right ventricle", "Left atrium and left ventricle", "Aorta and pulmonary trunk"]
    }
]


Biology_questions = [
      {
        "question": "What is the difference between meiosis I and mitosis?",
        "correct_answer": "Sister chromatids remain joined at their centromeres throughout meiosis I but are apart completely in anaphase in mitosis",
        "wrong_answers": [
            "During meiosis I, sister chromatids separate in anaphase similar to mitosis, and they remain joined at their centromeres throughout mitosis.",
            "In both meiosis I and mitosis, sister chromatids separate during anaphase, and they are always apart completely from prophase through telophase."
        ],
    },
    {
        "question": "IVF uses?",
        "correct_answer": "Phase contrast",
        "wrong_answers": ["SEM", "TEM", "LM"],
    },
    {
        "question": "Mucus secretion of vagina happens or is produced from?",
        "correct_answer": "Mucous from the cervix",
        "wrong_answers": ["Uterus lining", "Fallopian tubes", "Ovaries"],
    },
    {
        "question": "Which is a part of internal female genitalia?",
        "correct_answer": "Vagina",
        "wrong_answers": ["Uterus", "Ovaries", "Cervix"],
    },
    {
        "question": "Maturation of tissue and stuff occurs at which stage of embryological development?",
        "correct_answer": "Fetal",
        "wrong_answers": ["Embryonic", "Neonatal", "Adolescent"],
    },
    {
        "question": "What is responsible for dilated pupils?",
        "correct_answer": "Oculomotor",
        "wrong_answers": ["Optic nerve", "Trochlear nerve", "Abducens nerve"],
    },
    {
        "question": "What is one correct statement about kidneys?",
        "correct_answer": "Ureter is the most posterior structure in the root",
        "wrong_answers": ["Renal artery is anterior to the renal vein", "The renal pelvis is located in the cortex", "The nephron is the smallest functional unit"],
    },
    {
        "question": "Nephron consist of?",
        "correct_answer": "Renal corpuscle and renal tubules",
        "wrong_answers": ["Collecting ducts only", "Glomerulus only", "Renal pelvis and ureter"],
    },
    {
        "question": "Integral membrane proteins? - span all over phospholipid membrane",
        "correct_answer": "Span all over phospholipid membrane",
        "wrong_answers": ["Are only found in the cytoplasm", "Are soluble in water", "Are located outside the cell"],
    },
    {
        "question": "What factors affect Passive transport?",
        "correct_answer": "Concentration gradient",
        "wrong_answers": ["Energy input", "Carrier proteins", "ATP hydrolysis"],
    },
    {
        "question": "The main principle of fluid mosaic of plasma membrane?",
        "correct_answer": "Phospholipid bilayer",
        "wrong_answers": ["Protein monolayer", "Cholesterol layer", "Glycoprotein mesh"],
    },
    {
        "question": "What is a membrane protein that uses active transport?",
        "correct_answer": "Na+K+ pump",
        "wrong_answers": ["Facilitated diffusion protein", "Ion channel protein", "Aquaporin"],
    },
    {
        "question": "Air in pleural cavity is:",
        "correct_answer": "Pneumothorax",
        "wrong_answers": ["Hemothorax", "Hydrothorax", "Atelectasis"],
    },
    {
        "question": "Gonadotroph affected, what gland is impacted?",
        "correct_answer": "Ovary",
        "wrong_answers": ["Testis", "Pituitary gland", "Thyroid gland"],
    },
    {
        "question": "Hormones that stimulate the posterior pituitary gland to secrete hormones are?",
        "correct_answer": "Stimulating hormones",
        "wrong_answers": ["Inhibiting hormones", "Tropic hormones", "Releasing hormones"],
    },
    {
        "question": "Which of the following is true about the nervous system?",
        "correct_answer": "31 spinal nerve segments",
        "wrong_answers": ["12 cranial nerves", "42 spinal nerve segments", "24 thoracic nerve segments"],
    },
    {
        "question": "A CT scan for abdomino pelvic... how is the scan taken?",
        "correct_answer": "Coronal plane",
        "wrong_answers": ["Sagittal plane", "Axial plane", "Transverse plane"],
    },
    {
        "question": "CT scan of a patient of the vertebral column... how is the picture taken?",
        "correct_answer": "Transverse",
        "wrong_answers": ["Sagittal", "Coronal", "Oblique"],
    },
    {
        "question": "Which lymphoid organ is responsible for filtering antigens circulating in the blood?",
        "correct_answer": "Spleen",
        "wrong_answers": ["Thymus", "Lymph nodes", "Tonsils"],
    },
    {
        "question": "What of the following is responsible for bone resorption?",
        "correct_answer": "Osteoclasts",
        "wrong_answers": ["Osteoblasts", "Chondrocytes", "Fibroblasts"],
    },
    {
        "question": "What is inductive reasoning?",
        "correct_answer": "Drawing a general conclusion from specific observations",
        "wrong_answers": ["Drawing specific conclusions from general observations", "Making predictions based on assumptions", "Deducing specific facts from unrelated observations"],
    },
    {
        "question": "Which of the following describes astrocytes?",
        "correct_answer": "Prevents harmful substances from passing into the brain",
        "wrong_answers": ["Promotes the passage of harmful substances", "Has no role in substance regulation", "Is not present in the brain"],
    },
    {
        "question": "Collection of neural bodies inside the CNS:",
        "correct_answer": "Nucleus",
        "wrong_answers": ["Ganglion", "Cortex", "Tract"],
    },
    {
        "question": "What is the best description of the sensory system?",
        "correct_answer": "From skin to spinal nerves through dorsal root",
        "wrong_answers": ["From muscles to spinal nerves through ventral root", "From brain to peripheral nerves", "From eyes to optic nerve"],
    },
    {
        "question": "A patient suffers from motor weakness in facial nerves? Part C, Lower part anterior sulcus",
        "correct_answer": "False",
        "wrong_answers": ["True", "Depends on the specific condition", "Motor weakness is not associated with facial nerves"],
    },
    {
        "question": "DNA wrapped around a core of 8 histones:",
        "correct_answer": "Nucleosome",
        "wrong_answers": ["Chromatin", "Centromere", "Nuclear envelope"],
    },
    {
        "question": "Patient suffers from touch, position, as well as pain and temperature on the left side. Which area is affected?",
        "correct_answer": "Right side of the brain",
        "wrong_answers": ["Left side of the brain", "Spinal cord", "Peripheral nerves in the left side"],
    },
    {
        "question": "Patient suffers from touch and position in the left side. Which area of the spinal cord is affected? (Ignore the circle)",
        "correct_answer": "Right side of the spinal cord",
        "wrong_answers": ["Left side of the spinal cord", "Cervical region", "Lumbar region"],
    },
    {
        "question": "What is the function of the cell?",
        "correct_answer": "Receives/transmits impulses",
        "wrong_answers": ["Produces energy", "Stores genetic information", "Synthesizes proteins"],
    },
    {
        "question": "Development of tissue and stuff occurs at which stage of embryological development?",
        "correct_answer": "Fetal",
        "wrong_answers": ["Embryonic", "Neonatal", "Adulthood"],
    },
    {
        "question": "True about cell theory?",
        "correct_answer": "All made of 1 or more cells",
        "wrong_answers": ["Each cell is independent", "Cells do not have genetic material", "Cells do not have specific functions"],
    },
    {
        "question": "A cross-section of the spinal cord, which part is affected that causes dysfunction of the heart?",
        "correct_answer": "Lateral horn",
        "wrong_answers": ["Dorsal horn", "Ventral horn", "Central canal"],
    },
    {
        "question": "Which part of the spinal cord has somatic neurons controlling muscle?",
        "correct_answer": "Ventral horn (anterior)",
        "wrong_answers": ["Dorsal horn", "Lateral horn", "Central canal"],
    },
    {
        "question": "Where does ovulation occur?",
        "correct_answer": "Uterine tube",
        "wrong_answers": ["Ovary", "Uterus", "Cervix"],
    },
    {
        "question": "What kind of structure is found in the electron microscope but not the light microscope?",
        "correct_answer": "Vacuole",
        "wrong_answers": ["Mitochondrion", "Nucleus", "Endoplasmic reticulum"],
    },
    {
        "question": "Blood in the plural space",
        "correct_answer": "Hemothorax",
        "wrong_answers": ["Pneumothorax", "Pericarditis", "Hemopericardium"]
    },
    {
        "question": "Cell structure that secretes estrogen",
        "correct_answer": "Ovaries",
        "wrong_answers": ["Testes", "Pancreas", "Thyroid"]
    },
    {
        "question": "Anterior pituitary produces hormones",
        "correct_answer": "Trophic hormone",
        "wrong_answers": ["Growth hormone", "Prolactin", "Adrenocorticotropic hormone"]
    },
    {
        "question": "Correct statement about main bronchi",
        "correct_answer": "Right bronchi is vertical and wider",
        "wrong_answers": ["Left bronchi is vertical and wider", "Both bronchi are horizontal", "Not specified"]
    },
    {
        "question": "Diagram/point at afferent part of lymph node",
        "correct_answer": "B, afferent vessel (one at top) enters the cell",
        "wrong_answers": ["A, efferent vessel (one at bottom) exits the cell", "C, lymphoid follicle", "Not specified"]
    },
    {
        "question": "Kidney location: T12-L3",
        "correct_answer": "T12-L3",
        "wrong_answers": ["C7-T1", "L4-L5", "Not specified"]
    },
    {
        "question": "Cells theory",
        "correct_answer": "All living things are composed of one or more cells",
        "wrong_answers": ["Only animals are composed of cells", "Only plants are composed of cells", "Not specified"]
    },
    {
        "question": "Women sex organ that secretes hormones",
        "correct_answer": "Ovary",
        "wrong_answers": ["Uterus", "Vagina", "Not specified"]
    },
    {
        "question": "Site of gas exchange",
        "correct_answer": "Capillaries",
        "wrong_answers": ["Alveoli", "Arteries", "Not specified"]
    },
    {
        "question": "Not part of the kidney system",
        "correct_answer": "Loop of Henle",
        "wrong_answers": ["Glomerulus", "Renal tubule", "Not specified"]
    },
    {
        "question": "In the medullary region of the kidney",
        "correct_answer": "Loop of Henle",
        "wrong_answers": ["Cortex", "Collecting duct", "Not specified"]
    },
    {
        "question": "Cell that coagulates blood",
        "correct_answer": "Platelets",
        "wrong_answers": ["Red blood cells", "White blood cells", "Not specified"]
    },
    {
        "question": "Cell that changes to plasma cells when activated",
        "correct_answer": "B lymphocytes",
        "wrong_answers": ["T lymphocytes", "Natural killer cells", "Not specified"]
    },
    {
        "question": "Cell that secretes surfactant in lungs",
        "correct_answer": "Type II alveolar",
        "wrong_answers": ["Type I alveolar", "Bronchial cells", "Not specified"]
    },
    {
        "question": "Woman in Asia with parasitic worms",
        "correct_answer": "Eosinophils",
        "wrong_answers": ["Neutrophils", "Basophils", "Not specified"]
    },
    {
        "question": "Tonsillitis infection",
        "correct_answer": "Palatine",
        "wrong_answers": ["Pharyngeal", "Lingual", "Not specified"]
    },
    {
        "question": "A pain in the abdominal wall causes the patient to vomit and feel pain due to food not going into the duodenum, which structure is obstructed?",
        "correct_answer": "Pyloric sphincter",
        "wrong_answers": ["Ileocecal valve", "Cardiac sphincter", "Not specified"]
    },
    {
        "question": "Which of the following is responsible for the passage of food from the stomach to the small intestine? ",
        "correct_answer": "Pylorus",
        "wrong_answers": ["Duodenum", "Jejunum", "Not specified"]
    },
    {
        "question": "Which part of the nephron is in the medulla?",
        "correct_answer": "Loop of Henle",
        "wrong_answers": ["Glomerulus", "Bowman's capsule", "Not specified"]
    },
    {
        "question": "A radiologist wants to image a scan that is parallel to the vertebral column, which plane is the best?",
        "correct_answer": "Sagittal",
        "wrong_answers": ["Frontal", "Transverse", "Not specified"]
    }
    
      
]


Chemistry_questions = [
    {"question": "What is true about bilayer in the cell membrane?",
     "correct_answer": "Hydrophilic is always in the outer layer",
     "wrong_answers": ["Hydrophobic is always in the outer layer", "Both layers are hydrophobic",
                       "Hydrophilic is always in the inner layer"]
     },
    {
        "question": "What can't be oxidized?",
     "correct_answer": "Tertiary alcohol",
     "wrong_answers": ["Primary alcohol", "Secondary alcohol", "Quaternary alcohol"]
     },
    {
        "question": "Which one of the following tests positive for Tollen's reagent?",
     "correct_answer": "Aldehyde",
     "wrong_answers": ["Ketone", "Carboxylic acid", "Ester"]
     },
    {
        "question": "Definition of heterocyclic?",
     "correct_answer": "A ring that has atoms other than carbons",
     "wrong_answers": ["A ring composed only of carbon atoms", "A ring with a single type of atom",
                       "A ring with alternating single and double bonds"]
     },
    {
        "question": "Aldehyde oxidation?",
     "correct_answer": "Carboxylic acid",
     "wrong_answers": ["Ketone", "Alcohol", "Ester"]
     },
    {
        "question": "Primary amine attaches to how many carbons?",
     "correct_answer": "One",
     "wrong_answers": ["Two", "Three", "Four"]
     },
    {
        "question": "Ch3(OH)CH(OH) is?",
     "correct_answer": "Diol",
     "wrong_answers": ["Triol", "Monol", "Tetrol"]
     },
    {
        "question": "Oxidation of secondary alcohol?",
     "correct_answer": "Ketone",
     "wrong_answers": ["Aldehyde", "Carboxylic acid", "Ester"]
     },
    {
        "question": "Which of the following has the correct order of boiling points?",
     "correct_answer": "ethanoic acid > ethanol > ethane",
     "wrong_answers": ["ethane > ethanol > ethanoic acid", "ethanol > ethane > ethanoic acid",
                       "ethanoic acid > ethane > ethanol"]
     },
    {
        "question": "Solid at room temperature?",
     "correct_answer": "octadecane",
     "wrong_answers": ["propanol", "acetone", "butanoic acid"]
     },
    {
        "question": "General formula of alkanes?",
     "correct_answer": "CnH2n+2",
     "wrong_answers": ["CnH2n", "CnH2n-2", "CnH2n+1"]
     },
    {
        "question": "How many litres of CH4 react with 20 litres of O2 if it is at STP?",
     "correct_answer": "10 liters",
     "wrong_answers": ["5 liters", "15 liters", "20 liters"]
     },
    {
        "question": "Buffer system?",
     "correct_answer": "CH3COOH/CH3COO-",
     "wrong_answers": ["HCl/NaOH", "H2SO4/Na2CO3", "NH3/NH4Cl"]
     },
    {
        "question": "Why do alkanes undergo few reactions?",
     "correct_answer": "Lack of functional groups",
     "wrong_answers": ["High reactivity", "Presence of double bonds", "Strong acidity"]
     },
    {
        "question": "Which serum protein stores water in the blood?",
     "correct_answer": "Serum albumin",
     "wrong_answers": ["Hemoglobin", "Fibrinogen", "Globulin"]
     },
    {
        "question": "What is the product of the reaction of a carboxylic acid and alcohol?",
     "correct_answer": "Ester",
     "wrong_answers": ["Aldehyde", "Ketone", "Acid anhydride"]
     },
    {
        "question": "Hydrogen bonds occur because hydrogen binds to?",
     "correct_answer": "Electronegative",
     "wrong_answers": ["Metallic", "Positive", "Neutral"]
     },
    {
        "question": "What is the pOH of the solution if the pH is 7.5?",
     "correct_answer": "6.5",
     "wrong_answers": ["7.5", "8.5", "5.5"]
     },
    {
        "question": "5.4mg in 2.5g, what is the ppm?",
     "correct_answer": "2160 ppm",
     "wrong_answers": ["1080 ppm", "4320 ppm", "8640 ppm"]
     },
    {
        "question": "Atoms of strontium differ from strontium ions by?",
     "correct_answer": "Electrons",
     "wrong_answers": ["Protons", "Neutrons", "Nucleons"]
     },
     {
         "question": "Which bond is polar?",
     "correct_answer": "C=O",
     "wrong_answers": ["C-C", "C=C", "C#C"]
     },
    {
        "question": "According to Brønsted-Lowry, which of the following is true?",
     "correct_answer": "Acids are proton donors",
     "wrong_answers": ["Bases are proton donors", "Acids are proton acceptors", "Bases are proton acceptors"]
     },
    {
        "question": "In an aqueous solution, which is correct?",
     "correct_answer": "True",
     "wrong_answers": ["False", "The higher the pH, the stronger the acid", "pH is not related to acid strength"]
     },
    {
        "question": "Which has the lowest melting point? Hexane (choices all alkenes versus one alkane)",
     "correct_answer": "Alkane",
     "wrong_answers": ["Alkene", "Alkyne", "Aromatic hydrocarbon"]
     },
    {
        "question": "454g of NH4NO3 decomposes to NO2 and H2O, how much H2O is formed? NH4NO3–>N2O + 2H2O 204g",
     "correct_answer": "204g",
     "wrong_answers": ["100g", "300g", "400g"]
     },
    {
        "question": "Which type of decay releases ONLY He (helium atom)?",
     "correct_answer": "Alpha",
     "wrong_answers": ["Beta", "Gamma", "Neutron"]
     },
    {
        "question": "2 Mg + O2 -› 2 MgO ... This reaction is an example of which type of reaction?",
     "correct_answer": "Combination",
     "wrong_answers": ["Decomposition", "Single Replacement", "Double Replacement"]
     },
    {
        "question": "Adding one chlorine to a benzene ring resulting in chlorobenzene. What is the product named?",
     "correct_answer": "A monosubstituted benzene halide",
     "wrong_answers": ["Dichlorobenzene", "Trichlorobenzene", "Chloromethane"]
     },
    {
        "question": "Which one has the lowest melting point?",
        "correct_answer": "Oleic acid",
        "wrong_answers": [
            "The one with a double bond",
            "Saturated with single bonds",
            "Not specified"]
    },
    {
        "question": "The half-life of cesium-137 is 30 years. If you had 1g at the beginning, how many grams would be left after 90 years?",
        "correct_answer": "0.125g",
        "wrong_answers": [
            "0.25g",
            "0.5g",
            "1g"]
    },
    {
        "question": "What is a strong base?",
        "correct_answer": "Calcium hydroxide",
        "wrong_answers": [
            "Sodium chloride",
            "Ammonium hydroxide",
            "Hydrochloric acid"]
    },
    {
        "question": "What is NOT a factor that affects solubility?",
        "correct_answer": "Empirical formula",
        "wrong_answers": [
            "Temperature",
            "Pressure",
            "Nature of solute and solvent"]
    },
    {
        "question": "What happens to the solubility of O2 as temperature increases?",
        "correct_answer": "Decreases",
        "wrong_answers": [
            "Increases",
            "Remains constant",
            "Not specified"]
    },
    {
        "question": "Which type of alcohol is the most soluble?",
        "correct_answer": "Propandiol (the one with 2 OH’s)",
        "wrong_answers": [
            "Methanol",
            "Ethanol",
            "Butanol"]
    },
    {
        "question": "2-methylbutene + HCl =?",
        "correct_answer": "2-chloro-2-methylbutane",
        "wrong_answers": [
            "1-chloro-2-methylbutane",
            "2-methylbutane",
            "Not specified"]
    },
    {
        "question": "Which factors decide Gibbs Free Energy?",
        "correct_answer": "Enthalpy, Entropy, Temperature",
        "wrong_answers": [
            "Pressure, Volume, Temperature",
            "Heat, Work, Temperature",
            "Not specified"]
    },
    {
        "question": "Percentage of O is 72% which compound ___?",
        "correct_answer": "CO2",
        "wrong_answers": [
            "H2O",
            "O2",
            "Not specified"]
    },
    {
        "question": "Electron configuration of C?",
        "correct_answer": "1s2 2s2 2p2",
        "wrong_answers": [
            "1s2 2s2 2p6",
            "1s2 2s1",
            "Not specified"]
    },
    {
        "question": "What is true about endothermic reactions?",
        "correct_answer": "ΔG is positive",
        "wrong_answers": [
            "ΔH is negative",
            "ΔS is negative",
            "Not specified"]
    },
    {
        "question": "Baeyer test is for...?",
        "correct_answer": "Alkene",
        "wrong_answers": [
            "Alkyne",
            "Alkane",
            "Aromatic compounds"]
    },
    {
        "question": "Benzene preferred reaction is...?",
        "correct_answer": "Substitution",
        "wrong_answers": [
            "Addition",
            "Elimination",
            "Polymerization"]
    },
    {
        "question": "Concentration of H is 3.6x10^-3 M. What is the concentration of OH? 2.78x10^-12 and the solution is acidic.",
        "correct_answer": "2.78x10^-12 M",
        "wrong_answers": [
            "3.6x10^-3 M",
            "Neutral solution",
            "Not specified"]
    },
    {
        "question": "Nylon is a polyamide. What two functional groups reacted to form the amide linkage?",
        "correct_answer": "Carboxylic acid + Amine group",
        "wrong_answers": [
            "Alcohol + Aldehyde",
            "Ketone + Alcohol",
            "Carboxylic acid + Alcohol"]
    }
]


NIT_questions = [
    {
        "question": "What type of data is blood type?",
        "correct_answer": "Qualitative",
        "wrong_answers": ["Quantitative", "Continuous", "Categorical"]
    },
    {
        "question": "What is the average of 15-x, 15, 15+x?",
        "correct_answer": "15",
        "wrong_answers": ["x", "x+15", "45"]
    },
    {
        "question": "If 1L = 1000cm^3, what is the cube of 50cm?",
        "correct_answer": "125 liters",
        "wrong_answers": ["125cm^3", "625 liters", "625cm^3"]
    },
    {
        "question": "Find the length of arc AC if the area of the circle is 9π.",
        "correct_answer": "1.5π",
        "wrong_answers": ["3π", "4.5π", "6π"]
    },
    {
        "question": "All of the following are positive impacts on the fourth industrial revolution except?",
        "correct_answer": "Less hacking",
        "wrong_answers": ["Increased automation", "Enhanced connectivity", "Improved efficiency"]
    },
    {
        "question": "Definition of deep learning:",
        "correct_answer": "Subset of machine learning",
        "wrong_answers": ["Advanced artificial intelligence", "Complex data analysis", "High-level programming language"]
    },
    {
        "question": "What is a hype cycle?",
        "correct_answer": "Raise then come down then settle in the middle",
        "wrong_answers": ["Continuous rise", "Continuous decline", "Remain at the peak"]
    },
    {
        "question": "What is false about the fourth industrial revolution?",
        "correct_answer": "Use technology from 3rd industrial revolution without upgrading and enhancing them",
        "wrong_answers": ["Adopt completely new technologies", "Integrate digital and physical systems", "Focus on innovation and collaboration"]
    },
    {
        "question": "What is not a feature of the fourth industrial revolution?",
        "correct_answer": "High-level computing",
        "wrong_answers": ["Increased connectivity", "Advanced automation", "Intelligent data analysis"]
    },
    {
        "question": "What is not an example of the 4th industrial revolution?",
        "correct_answer": "4GB phone data",
        "wrong_answers": ["Machine learning algorithms", "Internet of Things (IoT)", "Blockchain technology"]
    },
    {
        "question": "The average number of days for 9 patients (frequency table, u calculate the average w bs)",
        "correct_answer": "5 days",
        "wrong_answers": ["4 days", "6 days", "7 days"]
    },
    {
        "question": "Leaf stem… find mode:",
        "correct_answer": "63",
        "wrong_answers": ["69", "75", "81"]
    },
    {
        "question": "Leaf stem… find median:",
        "correct_answer": "69",
        "wrong_answers": ["63", "75", "81"]
    },
    {
        "question": "26 meters in 13.8 seconds, how many meters in 4 minutes?",
        "correct_answer": "452 meters",
        "wrong_answers": ["408 meters", "520 meters", "576 meters"]
    },
    {
        "question": "⅕ cups of sugar used for 5/7 cups of flour, how many cups of sugar are needed for 5 cups of flour?",
        "correct_answer": "7/5",
        "wrong_answers": ["1", "1.25", "1.4"]
    },
    {
        "question": "What stayed the same from AI gen 1 and AI gen 2?",
        "correct_answer": "Classifier",
        "wrong_answers": ["Neural network architecture", "Training algorithms", "Processing speed"]
    },
    {
        "question": "40 is 80% of?",
        "correct_answer": "50",
        "wrong_answers": ["45", "55", "60"]
    },
    {
        "question": "What is an example of predictive analytics?",
        "correct_answer": "Forecast the spread of seasonal disease based on data from the previous year",
        "wrong_answers": ["Retroactive analysis of past events", "Real-time monitoring of current events", "Analyzing historical trends"]
    },
    {
        "question": "What is veracity?",
        "correct_answer": "The data quality, relevance, reliability",
        "wrong_answers": ["The speed of data processing", "The quantity of data", "The variety of data types"]
    },
    {
        "question": "What is K Health?",
        "correct_answer": "An app to track symptoms of diseases",
        "wrong_answers": ["A social networking app", "A fitness tracking app", "An online shopping platform"]
    },
    {
        "question": "Research related to Health Professions Education. What is the best way to narrow to the result?",
        "correct_answer": "Use relevant keywords",
        "wrong_answers": ["Broaden the search terms", "Exclude keywords", "Search without keywords"]
    },
    {
        "question": "Definition of point-of-care apps?",
        "correct_answer": "Resource for evidence-based clinical decision making",
        "wrong_answers": ["Entertainment applications", "Social networking tools", "Educational games"]
    },
    {
        "question": "Definition of information literacy?",
        "correct_answer": "Ability to find, evaluate, and use information effectively",
        "wrong_answers": ["Knowing everything about information", "Memorizing information", "Ignoring information"]
    },
    {
        "question": "Which benefit of information literacy is the best for a 6th-year medical student?",
        "correct_answer": "Critical thinking skills",
        "wrong_answers": ["Improved memory retention", "Faster reading speed", "Stronger physical endurance"]
    },
    {
        "question": "\"information\". Which type of citation?",
        "correct_answer": "In-text citation",
        "wrong_answers": ["Bibliography citation", "Footnote citation", "Endnote citation"]
    },
    {
        "question": "Real 3D cadaver of gross anatomy? Ackland",
        "correct_answer": "Medical databases",
        "wrong_answers": ["Social media", "News articles", "Government websites"]
    },
    {
        "question": "Picture of Acland’s video for human anatomy.",
        "correct_answer": "Visual resource",
        "wrong_answers": ["Audio resource", "Text resource", "Interactive resource"]
    },
    {
        "question": "Picture of Lecturio.",
        "correct_answer": "Online learning platform",
        "wrong_answers": ["Healthcare facility", "Bookstore", "Fitness app"]
    },
    {
        "question": "Picture of primal pictures.",
        "correct_answer": "Anatomy source",
        "wrong_answers": ["Art gallery", "Photography studio", "Cooking school"]
    },
    {
        "question": "Which of the following is an anatomy source?",
        "correct_answer": "Primal Pictures",
        "wrong_answers": ["YouTube", "Facebook", "Twitter"]
    },
    {
        "question": "If you want to build a 3D image of the thoracic cage. Which app would you use?",
        "correct_answer": "Primal Pictures",
        "wrong_answers": ["Facebook", "YouTube", "Twitter"]
    },
    {
        "question": "After 2 weeks of the COVID outbreak. Which type of resource will you use?",
        "correct_answer": "News articles",
        "wrong_answers": ["Scientific journals", "Government websites", "Educational websites"]
    },
    {
        "question": "After 5 months of the COVID outbreak. Which type of resource will you use?",
        "correct_answer": "Scientific journals",
        "wrong_answers": ["News articles", "Government websites", "Educational websites"]
    },
    {
        "question": "Patient wants to know more about treatment plans to decide. Which resource should the doctor recommend?",
        "correct_answer": "Medical information websites",
        "wrong_answers": ["Social media", "Personal blogs", "Entertainment websites"]
    },
    {
        "question": "Pathology book comparison?",
        "correct_answer": "Professional qualification of authors (book written by a scientist better than a writer)",
        "wrong_answers": ["Book cover design", "Number of pages", "Paper quality"]
    },
    {
        "question": "Which of the following is a learning tool?",
        "correct_answer": "Online tutorials",
        "wrong_answers": ["Coffee machine", "Televised cooking shows", "Board games"]
    },
    {
        "question": "Which of the following is a point of care tool?",
        "correct_answer": "UpToDate",
        "wrong_answers": ["Social media", "News websites", "Online shopping platforms"]
    },
    {
        "question": "Browzine is used to locate…?",
        "correct_answer": "Medical journals",
        "wrong_answers": ["Restaurants", "Bookstores", "Movie theaters"]
    },
    {
        "question": "An electrical engineer who woke up at night to vomit, he wants to find the causes, what is the best source?",
        "correct_answer": "Medical databases",
        "wrong_answers": ["Social media", "News articles", "Government websites"]
    },
    {
        "question": "What are LibGuides?",
        "correct_answer": "Collection of library resources that are useful for a particular study need",
        "wrong_answers": ["Guides for librarians", "Travel guides", "User manuals"]
    },
    {
        "question": "If you want to build a 3D image of the thoracic cage. Which app would you use?",
        "correct_answer": "Primal Pictures",
        "wrong_answers": ["Facebook", "YouTube", "Twitter"]
    },
    {
        "question": "After 2 weeks of the COVID outbreak. Which type of resource will you use?",
        "correct_answer": "News articles",
        "wrong_answers": ["Scientific journals", "Government websites", "Educational websites"]
    },
    {
        "question": "After 5 months of the COVID outbreak. Which type of resource will you use?",
        "correct_answer": "Scientific journals",
        "wrong_answers": ["News articles", "Government websites", "Educational websites"]
    },
    {
        "question": "Patient wants to know more about treatment plans to decide. Which resource should the doctor recommend?",
        "correct_answer": "Medical information websites",
        "wrong_answers": ["Social media", "Personal blogs", "Entertainment websites"]
    },
    {
        "question": "Pathology book comparison?",
        "correct_answer": "Professional qualification of authors (book written by a scientist better than a writer)",
        "wrong_answers": ["Book cover design", "Number of pages", "Paper quality"]
    },
    {
        "question": "Which of the following is a learning tool?",
        "correct_answer": "Online tutorials",
        "wrong_answers": ["Coffee machine", "Televised cooking shows", "Board games"]
    },
    {
        "question": "Which of the following is a point of care tool?",
        "correct_answer": "UpToDate",
        "wrong_answers": ["Social media", "News websites", "Online shopping platforms"]
    },
    {
        "question": "Browzine is used to locate…?",
        "correct_answer": "Medical journals",
        "wrong_answers": ["Restaurants", "Bookstores", "Movie theaters"]
    },
    {
        "question": "An electrical engineer who woke up at night to vomit, he wants to find the causes, what is the best source?",
        "correct_answer": "Medical databases",
        "wrong_answers": ["Social media", "News articles", "Government websites"]
    },
    {
        "question": "What are LibGuides?",
        "correct_answer": "Collection of library resources that are useful for a particular study need",
        "wrong_answers": ["Guides for librarians", "Travel guides", "User manuals"]
    },
    {
        "question": "A student wrote a research paper and submitted it to the editor. What is the next step?",
        "correct_answer": "Paper sent for peer review",
        "wrong_answers": ["Publication in a journal", "Presentation at a conference", "Submission to a library"]
    },
    {
        "question": "Submitted the research paper, got comments from peers, and made the changes. What is the next step?",
        "correct_answer": "Resubmitting the research",
        "wrong_answers": ["Acceptance without changes", "Rejection of the paper", "Withdrawal of the paper"]
    },
    {
        "question": "Which of the following is not a database for locating research papers?",
        "correct_answer": "Facebook",
        "wrong_answers": ["PubMed", "IEEE Xplore", "JSTOR"]
    },
    {
        "question": "Open access journals are?",
        "correct_answer": "Free for everyone to access",
        "wrong_answers": ["Available only for certain institutions", "Accessible only after payment", "Restricted to specific countries"]
    },
    {
        "question": "What can we find in PubMed?",
        "correct_answer": "Journal Articles",
        "wrong_answers": ["Movie reviews", "Travel guides", "Cooking recipes"]
    },
    {
        "question": "What is included in the in-text citation?",
        "correct_answer": "Author's last name and year of publication",
        "wrong_answers": ["Title of the paper", "Volume and issue number", "Page numbers"]
    },
    {
        "question": "Pharmac* will generate the following results?",
        "correct_answer": "Pharmacology, Pharmacy, Pharmaceutical, etc.",
        "wrong_answers": ["Physics, Phobia, Phosphorus, etc.", "Physical, Physician, Physiology, etc.", "Photography, Phrase, Phrenology, etc."]
    },
    {
        "question": "Which resource allows locating videos using the book matcher tool?",
        "correct_answer": "Lecturio",
        "wrong_answers": ["Google Scholar", "PubMed", "JSTOR"]
    },
    {
        "question": "Med student asked to add more references to a paper. In what citation style is that the easiest to do?",
        "correct_answer": "APA",
        "wrong_answers": ["MLA", "Chicago", "Vancouver"]
    },
    {
        "question": "Researcher writing a paper on a rare disease. They found one source only. What search strategy should they use to help find more?",
        "correct_answer": "Citation tracking",
        "wrong_answers": ["Keyword search", "Boolean operators", "Wildcard search"]
    },
]


PPC_questions = [
    {
        "question": "What is risk?",
        "correct_answer": "Probability to cause harm",
        "wrong_answers": [
            "Possibility of success",
            "Certainty of safety",
            "Likelihood of profit"
        ]
    },
    {
        "question": "The junior doctor hears an abnormal heartbeat; what should he say to the patient?",
        "correct_answer": "Something like we are going to check something (test)",
        "wrong_answers": [
            "What are you going to be alright",
            "Something like I’m going to go and come back",
            "Don't worry, it's probably nothing"
        ]
    },
    {
        "question": "Students only attend lectures and assignments; he does at night. On weekends he reviews everything he learned, how much will he remember by the end of the week?",
        "correct_answer": "30-49",
        "wrong_answers": ["Less than 30", "50-69", "More than 70"]
    },
    {
        "question": "Someone that has a viral infection stayed in bed all Sunday and wants to attend on Monday. What should they do?",
        "correct_answer": "Stay at home to avoid spreading the infection",
        "wrong_answers": [
            "Go to work or school as usual",
            "Wear a mask and attend",
            "Visit a crowded place to get fresh air"
        ]
    },
    {
        "question": "Leading cause of death in the UAE",
        "correct_answer": "Cardiovascular diseases (CVS)",
        "wrong_answers": ["Cancer", "Respiratory diseases", "Infectious diseases"]
    },
    {
        "question": "سالفة الطويلة بختصار Influenza?",
        "correct_answer": "Acute infectious disease",
        "wrong_answers": ["Chronic condition", "Autoimmune disorder", "Genetic disease"]
    },
    {
        "question": "Which of the following is a chronic and infectious disease?",
        "correct_answer": "AIDS",
        "wrong_answers": ["Influenza", "Tuberculosis", "Hepatitis A"]
    },
    {
        "question": "A final year medical student performed stitches without proper hygiene and only remembered that after the patient left. What should he do right after?",
        "correct_answer": "Immediately inform his senior supervisor",
        "wrong_answers": ["Nothing, it's not a big deal", "Inform the patient later", "Continue with other tasks"]
    },
    {
        "question": "Probability of something bad happening?",
        "correct_answer": "Risk",
        "wrong_answers": ["Certainty", "Possibility", "Safety"]
    },
    {
        "question": "likelihood of adverse effect occurring to people",
        "correct_answer": "Risk",
        "wrong_answers": ["Probability", "Chance", "Potential"]
    },
    {
    "question": "Definition: disease?.",
    "correct_answer": "Change in structure or function of any body part",
    "wrong_answers": ["Pathogen invasion", "Manifestation of illness", "Therapeutic intervention"]
    },
    {
        "question": "Uncontrollable risk factor of breast cancer ?",
        "correct_answer": "Family history",
        "wrong_answers": ["Diet", "Exercise", "Hormone replacement therapy"]
    },
    {
        "question": "A mother informed the doctor that her daughter is allergic to morphine. The doctor didn't write the information in a document, and when the daughter went to visit the hospital again they gave her morphine and she had an allergic reaction. What was the mistake done?",
        "correct_answer": "Not documenting the allergy information",
        "wrong_answers": [
            "Connection loop",
            "Not informing senior doctor",
            "Not signing consent paper"
        ]
    },
    {
        "question": "Alzheimer's is which type of disease?",
        "correct_answer": "Chronic",
        "wrong_answers": [
            "Acute",
            "Genetic",
            "Communicable"
        ]
    },
    {
        "question": "What is a symptom of COVID?",
        "correct_answer": "Fever",
        "wrong_answers": [
            "Cough",
            "Knee pain",
            "Sore throat"
        ]
    },
    {
        "question": "Which is a secondary prevention?",
        "correct_answer": "Mammogram for a 30-year-old",
        "wrong_answers": [
            "Annual check-up",
            "Blood test for cholesterol",
            "Vaccination"
        ]
    },
    {
        "question": "A child has fever, cough, etc., and his classmates have the same symptoms. What is the type of disease?",
        "correct_answer": "Acute infectious",
        "wrong_answers": [
            "Chronic non-infectious",
            "Genetic disorder",
            "Autoimmune"
        ]
    },
    {
        "question": "A woman has been in a coma for 4 years. What can identify if they should stop ventilation or something?",
        "correct_answer": "Brainstem death with 3 consultants, one has to be a neurologist",
        "wrong_answers": [
            "Blood test results",
            "Family's decision",
            "Doctor's assessment"
        ]
    },
    {
        "question": "Urine was spilled on the floor, and the doctor said they should clean it immediately because it is a hazard. What is the definition of hazard?",
        "correct_answer": "Something that poses a threat or danger",
        "wrong_answers": [
            "Normal occurrence",
            "Routine procedure",
            "Unnecessary task"
        ]
    },
    {
        "question": "When to breach confidentiality?",
        "correct_answer": "When there is a risk of harm to others",
        "wrong_answers": [
            "When patient requests",
            "Only if a crime is committed",
            "Only with family's consent"
        ]
    },
    {
        "question": "A patient got sickle cell and he has a family history of the disease, what is the type of disease?",
        "correct_answer": "Genetic",
        "wrong_answers": [
            "Autoimmune",
            "Infectious",
            "Degenerative"
        ]
    },
    {
        "question": "What is the first level of risk assessment?",
        "correct_answer": "Identifying the hazard",
        "wrong_answers": [
            "Assessing the consequences",
            "Implementing safety measures",
            "Monitoring the risk"
        ]
    },
    {
        "question": "81dB noise coming from Computer tomography, and the radiologists were complaining from the noise? What type of hazard?",
        "correct_answer": "Physical",
        "wrong_answers": [
            "Chemical",
            "Biological",
            "Psychosocial"
        ]
    },
    {
        "question": "Highest infant mortality rate?",
        "correct_answer": "Afghanistan",
        "wrong_answers": [
            "Norway",
            "Japan",
            "Canada"
        ]
    },
    {
        "question": "A 35-year-old woman was having a headache, what holistic care approach?",
        "correct_answer": "Addressing physical, emotional, and social aspects",
        "wrong_answers": [
            "Prescribing medication",
            "Referring to a specialist",
            "Providing only physical treatment"
        ]
    },
    {
        "question": "A man who was having a myocardial infarction, which holistic care approach?",
        "correct_answer": "Addressing physical, emotional, and social aspects",
        "wrong_answers": [
            "Performing surgery",
            "Prescribing medication",
            "Focusing only on the heart condition"
        ]
    },
    {
        "question": "A 23-year-old who refuses to get treatment and wants to go to the sheikh instead. What should the doctor do?",
        "correct_answer": "Ask about the reason, discuss risks and benefits",
        "wrong_answers": [
            "Force the patient to undergo treatment",
            "Refer the patient to another doctor",
            "Ignore the patient's preference"
        ]
    },
    {
        "question": "A father who had something, and the son doesn’t want to discuss the management of his disease with the patient. What should the doctor do?",
        "correct_answer": "Respect the son's decision",
        "wrong_answers": [
            "Force the son to discuss",
            "Convince the son to talk",
            "Ignore the son's preference"
        ]
    },
    {
        "question": "The mother who was 5 weeks pregnant had a heart disease, based on which Islamic principle applies?",
        "correct_answer": "Maintenance of life",
        "wrong_answers": [
            "Preservation of lineage",
            "Preservation of intellect",
            "Preservation of wealth"
        ]
    },
    {
        "question": "Controllable risk factor?",
        "correct_answer": "Obesity",
        "wrong_answers": [
            "Family history",
            "Age",
            "Gender"
        ]
    },
    {
        "question": "Noncontrollable risk factor?",
        "correct_answer": "Family history",
        "wrong_answers": [
            "Obesity",
            "Diet",
            "Exercise"
        ]
    },
    {
        "question": "Squelae definition:",
        "correct_answer": "Long-term consequences or complications following a disease or injury",
        "wrong_answers": [
            "Acute onset of symptoms",
            "Prevention of disease",
            "Treatment of symptoms"
        ]
    },
     {
        "question": "What is the UAE’s Law views on lethal injection?",
        "correct_answer": "Prohibited by law",
        "wrong_answers": [
            "Allowed with restrictions",
            "Depends on the circumstances",
            "Not addressed by law"
        ]
    },
    {
        "question": "What principle applies when the doctor refuses to give lethal injection?",
        "correct_answer": "Do no harm",
        "wrong_answers": [
            "Patient autonomy",
            "Beneficence",
            "Justice"
        ]
    },
    {
        "question": "Changes in diet because it was unappetizing?",
        "correct_answer": "Patient preference",
        "wrong_answers": [
            "Doctor's preference",
            "Family's preference",
            "Cultural preference"
        ]
    },
    {
        "question": "Type 2 diabetes is caused by?",
        "correct_answer": "Individual’s behavior",
        "wrong_answers": [
            "Genetic factors",
            "Environmental factors",
            "Societal factors"
        ]
    },
    {
        "question": "Debate question: they had clearer facts and statements",
        "correct_answer": "Factual and clear arguments",
        "wrong_answers": [
            "Emotional appeals",
            "Opinions without evidence",
            "Personal anecdotes"
        ]
    },
    {
        "question": "What to cite in a reference page?",
        "correct_answer": "All sources used for writing the essay, even background",
        "wrong_answers": [
            "Only direct quotes",
            "Only recent sources",
            "Only primary sources"
        ]
    },
    {
        "question": "Definition of plagiarism:",
        "correct_answer": "Using someone else's work without proper acknowledgment",
        "wrong_answers": [
            "Writing in a foreign language",
            "Rephrasing sentences",
            "Quoting with citation"
        ]
    },
    {
        "question": "Alcoholic patient who needs a knee surgery, but the doctor insisted on doing it the same day, and the patient agreed. What principle is violated?",
        "correct_answer": "Informed consent",
        "wrong_answers": [
            "Autonomy",
            "Beneficence",
            "Non-maleficence"
        ]
    },
    {
        "question": "Orthopedic surgeon needed surgery that was urgent but was too scared. He’s doing therapy and limiting exercise. Which ethical principle is in play?",
        "correct_answer": "Non-maleficence",
        "wrong_answers": [
            "Autonomy",
            "Justice",
            "Beneficence"
        ]
    },
    {
        "question": "How to achieve good teamwork?",
        "correct_answer": "Listen, be patient, be a good leader, manage time effectively",
        "wrong_answers": [
            "Work independently",
            "Compete with team members",
            "Ignore team communication"
        ]
    },
    {
        "question": "Comprehensive integrated patient care is provided by?",
        "correct_answer": "General hospital",
        "wrong_answers": [
            "Specialized clinic",
            "Emergency room",
            "Rehabilitation center"
        ]
    },
    {
        "question": "Definition of prevalence?",
        "correct_answer": "Total number of cases of a certain disease in a population",
        "wrong_answers": [
            "Percentage of deaths from a disease",
            "Number of new cases in a year",
            "Average duration of the disease"
        ]
    },
    {
        "question": "What is not a feature of academic writing?",
        "correct_answer": "Empathy",
        "wrong_answers": [
            "Clarity and precision",
            "Logical structure",
            "Citations and references"
        ]
    },
    {
        "question": "A doctor explaining how the patient will gradually start walking again, what is this?",
        "correct_answer": "Prognosis",
        "wrong_answers": [
            "Diagnosis",
            "Treatment plan",
            "Physical examination"
        ]
    },
    {
        "question": "The boy has 10-14% absences in a term and only studied at home as he did in high-school, and he needed to be learning actively, what should he do?",
        "correct_answer": "Participate in discussions during class",
        "wrong_answers": [
            "Continue studying at home",
            "Request more handouts",
            "Skip more classes"
        ]
    },
    {
        "question": "A patient had a fever or something and had been waiting for two hours, what should you say to demonstrate empathy?",
        "correct_answer": "It seems that you are upset",
        "wrong_answers": [
            "You should have come earlier",
            "The doctor is busy",
            "Waiting is part of the process"
        ]
    },
    {
        "question": "What is an unacceptable case of breaching confidentiality?",
        "correct_answer": "Informing the principal that she has a coronary heart disease",
        "wrong_answers": [
            "Informing the patient's family",
            "Discussing with other healthcare professionals",
            "Documenting in the patient's medical record"
        ]
    },
    {
        "question": "What demonstrates criminalism in a doctor?",
        "correct_answer": "Showing obvious neglect towards a patient",
        "wrong_answers": [
            "Prescribing appropriate medication",
            "Providing necessary information",
            "Following standard medical procedures"
        ]
    },
    {
        "question": "Pathogens definition",
        "correct_answer": "Microorganisms that cause disease",
        "wrong_answers": [
            "Antibodies produced by the immune system",
            "Cells responsible for phagocytosis",
            "Chemicals used in sterilization"
        ]
    }
]


#premid 1 practical

Anatomy_practical = [
    {
        "question": "What is the first/second arrow?",
        "correct_answer": "Internal Thoracic Artery and Transversus Thoracis Muscle",
        "wrong_answers": [
            "Superior Vena Cava and Left Atrium",
            "Descending Aorta and Esophagus",
            "Pulmonary Artery and Left Ventricle"
        ]
    },
    {
        "question": "What is the first/second arrow?",
        "correct_answer": "Superior Articular Facet and Spinous Process",
        "wrong_answers": [
            "Costal Facet and Rib Tubercle",
            "Transverse Process and Inferior Articular Facet",
            "Vertebral Body and Pedicle"
        ]
    },
    {
        "question": "Which muscle is this?",
        "correct_answer": "External Intercostal Muscle",
        "wrong_answers": [
            "Internal Intercostal Muscle",
            "Subcostal Muscle",
            "Diaphragm"
        ]
    },
    {
        "question": "What is the motor supply of this muscle?",
        "correct_answer": "Muscular branch of the intercostal nerves",
        "wrong_answers": [
            "Phrenic nerve",
            "Long thoracic nerve",
            "Spinal accessory nerve"
        ]
    },
    {
        "question": "What is the first/second arrow?",
        "correct_answer": "Trachea and Left Subclavian artery",
        "wrong_answers": [
            "Esophagus and Azygos Vein",
            "Vagus Nerve and Right Subclavian Artery",
            "Thoracic Duct and Thoracic Aorta"
        ]
    },
    {
        "question": "Which vertebra does this rib articulate with?",
        "correct_answer": "T7",
        "wrong_answers": [
            "T6",
            "T8",
            "T5"
        ]
    },
    {
        "question": "What is the name of the joint formed here?",
        "correct_answer": "Costotransverse joint",
        "wrong_answers": [
            "Costovertebral joint",
            "Sternocostal joint",
            "Costochondral joint"
        ]
    },
    {
        "question": "Identify the blood vessel",
        "correct_answer": "Brachiocephalic Trunk",
        "wrong_answers": [
            "Subclavian Artery",
            "Superior Vena Cava",
            "Pulmonary Trunk"
        ]
    },
    {
        "question": "Identify the blood vessel",
        "correct_answer": "Internal thoracic vein",
        "wrong_answers": [
            "Internal thoracic artery",
            "Azygos vein",
            "Inferior vena cava"
        ]
    },
    {
        "question": "What is the vertebral level for the bony body?",
        "correct_answer": "T10",
        "wrong_answers": [
            "T11",
            "T9",
            "T12"
        ]
    },
    {
        "question": "What is the vertebral level for the level on the arrow?",
        "correct_answer": "T4-T5",
        "wrong_answers": [
            "T3-T4",
            "T5-T6",
            "T2-T3"
        ]
    }
]


Chemistry_practical = [
    {
        "question": "What is this?",
        'correct_answer': "N,N-diethyl-m-toulamide",
        'wrong_answers': ["N,N-dimethyl-m-toulamide", "N-ethyl-m-toulamide", "N,N-dipropyl-m-toulamide"]
    },

    {
        "question": "What is this?",
        'correct_answer': "4-ethyl-5,6-dimethyldecane",
        'wrong_answers': ["2-methyl-3-propylhexane", "3-ethyl-4,5-dimethylheptane", "5,6-dimethyl-4-ethyldecane"]
    },
    {
        "question": "What is this?",
        'correct_answer': "2-ethyl-1-pentene",
        'wrong_answers': ["3-methyl-1-butene", "1,2-dimethylcyclohexane", "4-propyl-2-hexene"]
    },
    {
        "question": "What is this?",
        'correct_answer': "cis-5-chloro-2-hexene",
        'wrong_answers': ["trans-5-chloro-2-hexene", "3-methyl-1-butene", "1,2-dimethylcyclohexane"]
    }
]


#premid 2 Theoretical 

Anatomy2_questions = [
    {
        "question": "What's located at the transtubercular line?",
        "correct_answer": "Origin of IVC",
        "wrong_answers": [
            "Origin of the aorta",
            "Origin of the renal arteries",
            "Origin of the common iliac artery"
        ]
    },
    {
        "question": "What structures pass through the lacuna vasorum?",
        "correct_answer": "Femoral vein, femoral artery, genitofemoral nerve",
        "wrong_answers": [
            "Popliteal vein, popliteal artery, saphenous nerve",
            "Sciatic nerve, femoral nerve, obturator artery",
            "Saphenous vein, deep femoral artery, femoral nerve"
        ]
    },
    {
        "question": "Right suprarenal hilum?",
        "correct_answer": "Anterior border",
        "wrong_answers": [
            "Posterior border",
            "Medial border",
            "Lateral border"
        ]
    },
    {
        "question": "What structure helps you locate the appendix?",
        "correct_answer": "Tenia coli",
        "wrong_answers": [
            "Appendicular artery",
            "Haustra",
            "Peyer's patches"
        ]
    },
    {
        "question": "Ulcer of the posterior part of the 1st Duodenum which vessel will be damaged?",
        "correct_answer": "Gastroduodenal Artery",
        "wrong_answers": [
            "Superior mesenteric artery",
            "Celiac trunk",
            "Hepatic artery"
        ]
    },
    {
        "question": "Ulcer of the posterior part of the stomach, which main vessel will be affected?",
        "correct_answer": "Splenic Artery",
        "wrong_answers": [
            "Left gastric artery",
            "Common hepatic artery",
            "Gastroduodenal artery"
        ]
    },
    {
        "question": "Where does the McBurney's point located?",
        "correct_answer": "Right spino-umbilical line",
        "wrong_answers": [
            "Left spino-umbilical line",
            "Mid-clavicular line",
            "Right mid-clavicular line"
        ]
    },
    {
        "question": "If the 10th rib on the left was fractured which organ will be damaged?",
        "correct_answer": "Spleen",
        "wrong_answers": [
            "Liver",
            "Stomach",
            "Pancreas"
        ]
    },
    {
        "question": "Which of the following structures is retroperitoneal?",
        "correct_answer": "Adrenal glands",
        "wrong_answers": [
            "Liver",
            "Spleen",
            "Gallbladder"
        ]
    },
    {
        "question": "Which vessel is parallel to the inguinal ligament?",
        "correct_answer": "Deep circumflex iliac artery",
        "wrong_answers": [
            "Femoral artery",
            "External iliac artery",
            "Internal iliac artery"
        ]
    },
     {
        "question": "Which nerves constrict the pyloric sphincter to allow the stomach to fill with food first?",
        "correct_answer": "Sympathetic nerve fibers",
        "wrong_answers": [
            "Parasympathetic nerve fibers",
            "Vagus nerve",
            "Somatic nerve fibers"
        ]
    },
    {
        "question": "Removal of gall bladder will LEAST likely damage which of the following?",
        "correct_answer": "Left hepatic vein",
        "wrong_answers": [
            "Common bile duct",
            "Hepatic artery",
            "Portal vein"
        ]
    },
    {
        "question": "Liver fibrosis (overproduction of fibers that obstruct liver passageways). What structure that takes fluid directly away from the liver is damaged?",
        "correct_answer": "Common bile duct",
        "wrong_answers": [
            "Hepatic artery",
            "Hepatic portal vein",
            "Hepatic vein"
        ]
    },
    {
        "question": "What is true about the ileum?",
        "correct_answer": "Has lymphoid aggregations",
        "wrong_answers": [
            "Contains intestinal villi",
            "Has a thick muscular layer",
            "Reabsorbs most of the water and electrolytes"
        ]
    },
    {
        "question": "How to differentiate between jejunum and ileum?",
        "correct_answer": "Arterial arcades",
        "wrong_answers": [
            "Presence of Peyer's patches",
            "Thickness of muscular layer",
            "Length of the segment"
        ]
    },
    {
        "question": "Cancer in neck of pancreas affects which vessel?",
        "correct_answer": "Portal vein",
        "wrong_answers": [
            "Common bile duct",
            "Hepatic artery",
            "Superior mesenteric vein"
        ]
    },
    {
        "question": "What part of the lumbar plexus is on the posterior side of the kidney?",
        "correct_answer": "Ilioinguinal nerve",
        "wrong_answers": [
            "Femoral nerve",
            "Obturator nerve",
            "Genitofemoral nerve"
        ]
    },
    {
        "question": "Left gonadal vein drains in what?",
        "correct_answer": "Left renal vein",
        "wrong_answers": [
            "Inferior vena cava",
            "Left common iliac vein",
            "Superior mesenteric vein"
        ]
    },
    {
        "question": "Which branch of abdominal aorta is paired?",
        "correct_answer": "Suprarenal branch (paired branch)",
        "wrong_answers": [
            "Inferior phrenic artery",
            "Celiac trunk",
            "Superior mesenteric artery"
        ]
    },
    {
        "question": "Physiologic lobes of the liver are divided based on the distribution of what?",
        "correct_answer": "Portal vein",
        "wrong_answers": [
            "Hepatic artery",
            "Hepatic vein",
            "Hepatic portal vein"
        ]
    },
    {
        "question": "Cholecystitis?",
        "correct_answer": "Inflammation of gallbladder",
        "wrong_answers": [
            "Inflammation of liver",
            "Inflammation of pancreas",
            "Inflammation of stomach"
        ]
    },
    {
        "question": "Free margin of the lesser omentum damaged. Bleeding in the peritoneal cavity. Which vessel is damaged?",
        "correct_answer": "Hepatic artery",
        "wrong_answers": [
            "Gastroduodenal artery",
            "Left gastric artery",
            "Splenic artery"
        ]
    },
    {
        "question": "Posterior of epiploic foramen?",
        "correct_answer": "IVC",
        "wrong_answers": [
            "Aorta",
            "Common bile duct",
            "Pancreatic duct"
        ]
    },
    {
        "question": "As the ureter travels down from the abdomen to the pelvis it is constricted at?",
        "correct_answer": "Bifurcation of the common iliac artery",
        "wrong_answers": [
            "Iliac crest",
            "Ischial spine",
            "Sacral promontory"
        ]
    },
    {
        "question": "Inferior mesenteric artery damaged. Which structure is affected?",
        "correct_answer": "Descending colon",
        "wrong_answers": [
            "Ascending colon",
            "Transverse colon",
            "Sigmoid colon"
        ]
    },
    {
        "question": "Someone swallowed something. Upper part of the esophagus is stretched. Which nerve fibers send information to brain?",
        "correct_answer": "Vagus",
        "wrong_answers": [
            "Glossopharyngeal",
            "Hypoglossal",
            "Accessory"
        ]
    },
    {
        "question": "Esophageal variations, talking about the portosystemic anastomoses, if we close one vein forming these anastomoses, which one is it?",
        "correct_answer": "Left gastric",
        "wrong_answers": [
            "Inferior mesenteric",
            "Superior mesenteric",
            "Splenic"
        ]
    },
    {
        "question": "A blocked vessel that drains FLUID from the liver, causing liver fibrosis?",
        "correct_answer": "Common bile duct",
        "wrong_answers": [
            "Hepatic portal vein",
            "Hepatic vein",
            "Hepatic artery"
        ]
    },
    {
        "question": "What is the muscle that makes the inguinal canal?",
        "correct_answer": "External oblique",
        "wrong_answers": [
            "Internal oblique",
            "Transversus abdominis",
            "Rectus abdominis"
        ]
    },
    {
        "question": "If the gastroduodenal artery was ligated, which of the following will CONTINUE to supply the small intestine?",
        "correct_answer": "Superior mesenteric artery",
        "wrong_answers": [
            "Inferior mesenteric artery",
            "Celiac trunk",
            "Hepatic artery"
        ]
    },
    {
        "question": "Liver",
        "correct_answer": "Common bile duct",
        "wrong_answers": [
            "Hepatic portal vein",
            "Hepatic vein",
            "Hepatic artery"
        ]
    },
    {
        "question": "What is Cholelithiasis?",
        "correct_answer": "Stones in the gallbladder",
        "wrong_answers": [
            "Inflammation of the gallbladder",
            "Enlargement of the gallbladder",
            "Tumor in the gallbladder"
        ]
    },
    {
        "question": "Floor of inguinal canal?",
        "correct_answer": "Inguinal ligament",
        "wrong_answers": [
            "Transversalis fascia",
            "Internal oblique muscle",
            "Conjoint tendon"
        ]
    },
    {
        "question": "Ulcer in the posterior wall of the stomach opens it to?",
        "correct_answer": "Lesser sac/omental bursa",
        "wrong_answers": [
            "Greater sac/peritoneal cavity",
            "Peritoneal cavity",
            "Hepatorenal recess"
        ]
    },
    {
        "question": "How to find the tail of the pancreas?",
        "correct_answer": "Splenorenal ligament",
        "wrong_answers": [
            "Gastrocolic ligament",
            "Duodenorenal ligament",
            "Gastrosplenic ligament"
        ]
    },
    {
        "question": "The lesser sac connects the stomach to?",
        "correct_answer": "Liver",
        "wrong_answers": [
            "Spleen",
            "Pancreas",
            "Duodenum"
        ]
    },
    {
        "question": "Which of the following is intraperitoneal?",
        "correct_answer": "Stomach",
        "wrong_answers": [
            "Kidneys",
            "Ureters",
            "Bladder"
        ]
    },
    {
        "question": "What is found in Calot's triangle?",
        "correct_answer": "Cystic artery",
        "wrong_answers": [
            "Common bile duct",
            "Hepatic artery",
            "Hepatic duct"
        ]
    },
    {
        "question": "Earlier Abdominal pain around the umbilicus region, then it transferred to the right inferior quadrant, what’s the structure inflamed?",
        "correct_answer": "Vermiform appendix",
        "wrong_answers": [
            "Cecum",
            "Ascending colon",
            "Ileocecal valve"
        ]
    },
    {
        "question": "Where’s the normal constriction in the ureter of the kidney?",
        "correct_answer": "Pelviureteric junction",
        "wrong_answers": [
            "Ureterovesical junction",
            "Ureteropelvic junction",
            "Ureteral hiatus"
        ]
    },
    {
        "question": "What is true about the jejunum?",
        "correct_answer": "It has fewer blood arcades long (vasa recta)",
        "wrong_answers": [
            "It has more blood arcades",
            "It has no blood arcades",
            "It has more lymphatics"
        ]
    },
    {
        "question": "Which part of the pancreas cancer can cause jaundice?",
        "correct_answer": "Head",
        "wrong_answers": [
            "Body",
            "Tail",
            "Uncinate process"
        ]
    },
    {
        "question": "The appendix is not in its normal place, in which peritoneal recess do you expect to find it?",
        "correct_answer": "Retrocecal",
        "wrong_answers": [
            "Hepatorenal",
            "Paracolic",
            "Subhepatic"
        ]
    },
    {
        "question": "Where does the left suprarenal artery drain?",
        "correct_answer": "Left renal vein",
        "wrong_answers": [
            "Inferior vena cava",
            "Hepatic vein",
            "Left gonadal vein"
        ]
    }
]

PPC_terms = [
    {
        "question": "What does the term 'xanth/o' refer to?",
        "correct_answer": "yellow",
        "wrong_answers": ["red", "green", "purple"]
    },
    {
        "question": "What does the term 'melan/o' refer to?",
        "correct_answer": "black",
        "wrong_answers": ["white", "brown", "gray"]
    },
    {
        "question": "What does the term 'cyan/o' refer to?",
        "correct_answer": "blue",
        "wrong_answers": ["orange", "pink", "purple"]
    },
    {
        "question": "What medical condition is described as a 'black tumor of the skin'?",
        "correct_answer": "melanoma",
        "wrong_answers": ["leukemia", "cyanosis", "xanthoma"]
    },
    {
        "question": "What does the term 'cyanosis' refer to?",
        "correct_answer": "blueness may be due to cold or not enough oxygen in blood",
        "wrong_answers": ["overabundance of white blood cells", "yellow tumor", "black tumor of the skin"]
    },
    {
        "question": "What does the term 'xanthoma' refer to?",
        "correct_answer": "yellow tumor",
        "wrong_answers": ["leukemia", "cyanosis", "melanoma"]
    },
    {
        "question": "What medical condition is described as an 'overabundance of white blood cells'?",
        "correct_answer": "leukemia",
        "wrong_answers": ["melanoma", "cyanosis", "xanthoma"]
    },
    {
        "question": "What does the term 'Aden/o' refer to?",
        "correct_answer": "gland",
        "wrong_answers": ["fat", "muscle", "lymph tissue"]
    },
    {
        "question": "What does the term 'Lip/o' refer to?",
        "correct_answer": "fat",
        "wrong_answers": ["gland", "muscle", "lymph tissue"]
    },
    {
        "question": "What does the term 'My/o' refer to?",
        "correct_answer": "muscle",
        "wrong_answers": ["gland", "fat", "lymph tissue"]
    },
    {
        "question": "What does the term 'Lymph/o' refer to?",
        "correct_answer": "lymph tissue",
        "wrong_answers": ["gland", "fat", "muscle"]
    },
    {
        "question": "What does the term 'Carcin/o' refer to?",
        "correct_answer": "malignant",
        "wrong_answers": ["benign", "non-cancerous", "metastasis"]
    },
    {
        "question": "What does the term 'Osteo/o' refer to?",
        "correct_answer": "bone",
        "wrong_answers": ["muscle", "gland", "fat"]
    },
    {
        "question": "What does the prefix 'Endo-' mean?",
        "correct_answer": "within, inside of",
        "wrong_answers": ["around", "behind", "upon, on top"]
    },
    {
        "question": "What does the prefix 'Peri-' mean?",
        "correct_answer": "around",
        "wrong_answers": ["within, inside of", "behind", "through"]
    },
    {
        "question": "What does the prefix 'Circum-' mean?",
        "correct_answer": "around",
        "wrong_answers": ["within, inside of", "behind", "through"]
    },
    {
        "question": "What does the prefix 'Retro-' mean?",
        "correct_answer": "behind",
        "wrong_answers": ["within, inside of", "around", "through"]
    },
    {
        "question": "What does the prefix 'Epi-' mean?",
        "correct_answer": "upon, on top",
        "wrong_answers": ["within, inside of", "around", "behind"]
    },
    {
        "question": "What does the prefix 'Trans-' mean?",
        "correct_answer": "through",
        "wrong_answers": ["within, inside of", "around", "upon, on top"]
    },
    {
        "question": "What does the prefix 'Intra-' mean?",
        "correct_answer": "within",
        "wrong_answers": ["around", "behind", "through"]
    },
    {
        "question": "What does the prefix 'Sub-' mean?",
        "correct_answer": "below",
        "wrong_answers": ["around", "behind", "upon, on top"]
    },
    {
        "question": "What does the prefix 'Hem/o, -emia' mean?",
        "correct_answer": "blood",
        "wrong_answers": ["vein", "vessel", "heart"]
    },
    {
        "question": "What does the suffix '-cyte' mean?",
        "correct_answer": "cell",
        "wrong_answers": ["blood", "vein", "heart"]
    },
    {
        "question": "What does the suffix '-stasis' mean?",
        "correct_answer": "to stop",
        "wrong_answers": ["blood", "vein", "heart"]
    },
    {
        "question": "What does the prefix 'Veno/phlebo-' mean?",
        "correct_answer": "vein",
        "wrong_answers": ["blood", "vessel", "heart"]
    },
    {
        "question": "What does the prefix 'Angi/o-' mean?",
        "correct_answer": "vessel",
        "wrong_answers": ["blood", "vein", "heart"]
    },
    {
        "question": "What does the prefix 'Brady/tachy-' mean?",
        "correct_answer": "slow/fast",
        "wrong_answers": ["blood", "vein", "heart"]
    },
    {
        "question": "What does the prefix 'Cardi/o-' mean?",
        "correct_answer": "heart",
        "wrong_answers": ["blood", "vein", "vessel"]
    },
    {
        "question": "What type of cancer does 'adenoma' refer to?",
        "correct_answer": "glandular cancer",
        "wrong_answers": ["fat tissue cancer", "muscle tissue cancer", "lymph tissue cancer"]
    },
    {
        "question": "What type of cancer does 'lipoma' refer to?",
        "correct_answer": "fat tissue cancer",
        "wrong_answers": ["glandular cancer", "muscle tissue cancer", "lymph tissue cancer"]
    },
    {
        "question": "What type of cancer does 'myoma' refer to?",
        "correct_answer": "muscle tissue cancer",
        "wrong_answers": ["glandular cancer", "fat tissue cancer", "lymph tissue cancer"]
    },
    {
        "question": "What type of cancer does 'lymphoma' refer to?",
        "correct_answer": "lymph tissue cancer",
        "wrong_answers": ["glandular cancer", "fat tissue cancer", "muscle tissue cancer"]
    },
    {
        "question": "What type of cancer does 'carcinoma' refer to?",
        "correct_answer": "epithelial tissue cancer",
        "wrong_answers": ["glandular cancer", "fat tissue cancer", "muscle tissue cancer"]
    },
    {
        "question": "What type of cancer does 'osteoma' refer to?",
        "correct_answer": "bone cancer",
        "wrong_answers": ["glandular cancer", "fat tissue cancer", "muscle tissue cancer"]
    },
    {
        "question": "Endocarditis",
        "correct_answer": "inflammation of the lining of the heart",
        "wrong_answers": ["inflammation of the muscle layer of the heart", "inflammation of the outer layer of the heart", "heart attack"]
    },
    {
        "question": "Myocarditis",
        "correct_answer": "inflammation of the muscle layer of the heart",
        "wrong_answers": ["inflammation of the lining of the heart", "inflammation of the outer layer of the heart", "heart attack"]
    },
    {
        "question": "Pericarditis",
        "correct_answer": "inflammation of the outer layer of the heart",
        "wrong_answers": ["inflammation of the lining of the heart", "inflammation of the muscle layer of the heart", "heart attack"]
    },
    {
        "question": "What is Angiography?",
        "correct_answer": "X-ray of artery",
        "wrong_answers": ["MRI of artery", "Ultrasound of artery", "CT scan of artery"]
    },
    {
        "question": "What is Angiogram?",
        "correct_answer": "X-ray of artery",
        "wrong_answers": ["MRI of artery", "Ultrasound of artery", "CT scan of artery"]
    },
    {
        "question": "What is Venogram?",
        "correct_answer": "X-ray of veins",
        "wrong_answers": ["MRI of veins", "Ultrasound of veins", "CT scan of veins"]
    },
    {
        "question": "What is Phlebitis?",
        "correct_answer": "inflammation of veins",
        "wrong_answers": ["inflammation of arteries", "blood clot in veins", "heart disease"]
    },
    {
        "question": "What is Hemostasis?",
        "correct_answer": "to stop bleeding",
        "wrong_answers": ["to promote bleeding", "to prevent clotting", "to dilate blood vessels"]
    },
    {
        "question": "What is a Hemostat?",
        "correct_answer": "a clamp-like instrument",
        "wrong_answers": ["a surgical needle", "a syringe", "a scalpel"]
    },
    {
        "question": "What are Erythrocytes?",
        "correct_answer": "red blood cells",
        "wrong_answers": ["white blood cells", "platelets", "plasma"]
    },
    {
        "question": "What are Leukocytes?",
        "correct_answer": "white blood cells",
        "wrong_answers": ["red blood cells", "platelets", "plasma"]
    },
    {
        "question": "What is Hypoxemia?",
        "correct_answer": "low oxygen",
        "wrong_answers": ["high oxygen", "low carbon dioxide", "high carbon dioxide"]
    },
    {
        "question": "What is Hematosalpinx?",
        "correct_answer": "blood in the uterine tubes",
        "wrong_answers": ["blood in the uterus", "blood in the ovaries", "blood in the vagina"]
    },
    {
        "question": "What is Atherosclerosis?",
        "correct_answer": "Fatty deposits in arteries.",
        "wrong_answers": [
            "Irregular heartbeats.",
            "High blood pressure.",
            "Dilated blood vessels."
        ]
    },
    {
        "question": "What is Myocardial Infarction (MI)?",
        "correct_answer": "Heart attack.",
        "wrong_answers": [
            "Weak heart muscle.",
            "Increased heart rate.",
            "Malfunctioning heart valves."
        ]
    },
    {
        "question": "What are Mitral Prolapse, Stenosis, and Regurgitation?",
        "correct_answer": "Conditions affecting the mitral valve.",
        "wrong_answers": [
            "Conditions affecting the aorta.",
            "Conditions affecting the coronary arteries.",
            "Conditions affecting the pulmonary arteries."
        ]
    },
    {
        "question": "What is Angina Pectoris?",
        "correct_answer": "Chest pain due to insufficient blood flow to the heart.",
        "wrong_answers": [
            "Irregular heartbeats.",
            "Dilated blood vessels.",
            "Malfunctioning heart valves."
        ]
    },
    {
        "question": "What is Ischemia?",
        "correct_answer": "Restricted blood flow.",
        "wrong_answers": [
            "Excess blood flow.",
            "Low blood pressure.",
            "Dilated blood vessels."
        ]
    },
    {
        "question": "What is a Cardiologist?",
        "correct_answer": "Heart specialist.",
        "wrong_answers": [
            "Lung specialist.",
            "Kidney specialist.",
            "Liver specialist."
        ]
    },
    {
        "question": "What is Arrhythmia/Dysrhythmia?",
        "correct_answer": "Irregular heartbeat.",
        "wrong_answers": [
            "Difficulty breathing.",
            "Malfunctioning heart valves.",
            "Blood clots in the heart."
        ]
    },
    {
        "question": "What is an Electrocardiogram?",
        "correct_answer": "Heart's electrical activity test.",
        "wrong_answers": [
            "Heart structure test.",
            "Blood flow test.",
            "Blood vessel test."
        ]
    },
    {
        "question": "What is a Hematologist?",
        "correct_answer": "Blood specialist.",
        "wrong_answers": [
            "Heart specialist.",
            "Lung specialist.",
            "Kidney specialist."
        ]
    },
    {
        "question": "What is Echocardiography?",
        "correct_answer": "Heart ultrasound.",
        "wrong_answers": [
            "X-ray of the heart.",
            "MRI of the heart.",
            "Nuclear scan of the heart."
        ]
    },
    {
        "question": "What is Cardiac Catheterization?",
        "correct_answer": "Heart procedure with a catheter.",
        "wrong_answers": [
            "Lung procedure with a catheter.",
            "Kidney procedure with a catheter.",
            "Liver procedure with a catheter."
        ]
    },
    {
        "question": "What is a Phlebotomist/Venipuncturist?",
        "correct_answer": "Blood drawing professional.",
        "wrong_answers": [
            "Vaccine administrator.",
            "Surgeon.",
            "Dentist."
        ]
    },
    {
        "question": "What does the term 'Encephal/o' refer to?",
        "correct_answer": "Inside the head (brain)",
        "wrong_answers": ["Head", "Paralysis", "Development, formation, growth"]
    },
    {
        "question": "What does the term 'Cephal/o' refer to?",
        "correct_answer": "Head",
        "wrong_answers": ["Inside the head (brain)", "Paralysis", "Development, formation, growth"]
    },
    {
        "question": "What does the term '-plegia' refer to?",
        "correct_answer": "Paralysis",
        "wrong_answers": ["Inside the head (brain)", "Head", "Development, formation, growth"]
    },
    {
        "question": "What does the term '-plasia' refer to?",
        "correct_answer": "Development, formation, growth",
        "wrong_answers": ["Inside the head (brain)", "Head", "Paralysis"]
    },
    {
        "question": "What does the term '-pathy' refer to?",
        "correct_answer": "Disease, abnormality",
        "wrong_answers": ["Inside the head (brain)", "Head", "Paralysis"]
    },
    {
        "question": "What does the term '-cele' refer to?",
        "correct_answer": "Hernia, abnormal protrusion of structure out of normal anatomical position",
        "wrong_answers": ["Inside the head (brain)", "Head", "Paralysis"]
    },
    {
        "question": "What does the prefix 'Dys' refer to?",
        "correct_answer": "Difficult, painful, abnormal",
        "wrong_answers": ["Inside the head (brain)", "Head", "Paralysis"]
    },
    {
        "question": "What does the term 'Neur/o' refer to?",
        "correct_answer": "Nerve",
        "wrong_answers": ["Inside the head (brain)", "Head", "Paralysis"]
    },
    {
        "question": "What does the term 'Myel/o' refer to?",
        "correct_answer": "Spinal cord",
        "wrong_answers": ["Inside the head (brain)", "Head", "Paralysis"]
    },
    {
        "question": "What does the term 'Mening/o' refer to?",
        "correct_answer": "Membranes surrounding the brain and spinal cord",
        "wrong_answers": ["Inside the head (brain)", "Head", "Paralysis"]
    },
     {
        "question": "What does the term 'Cephalgia' refer to?",
        "correct_answer": "A headache",
        "wrong_answers": ["Paralysis of one side of the body", "No development", "Disease of the brain"]
    },
    {
        "question": "What does the term 'Hemiplegia' refer to?",
        "correct_answer": "Paralysis of one side of the body",
        "wrong_answers": ["A headache", "No development", "Disease of the brain"]
    },
    {
        "question": "What does the term 'Quadriplegia' refer to?",
        "correct_answer": "Paralysis of all four limbs",
        "wrong_answers": ["A headache", "No development", "Disease of the brain"]
    },
    {
        "question": "What does the term 'Aplasia' refer to?",
        "correct_answer": "No development",
        "wrong_answers": ["A headache", "Paralysis of one side of the body", "Disease of the brain"]
    },
    {
        "question": "What does the term 'Hyperplasia' refer to?",
        "correct_answer": "Over development",
        "wrong_answers": ["A headache", "Paralysis of one side of the body", "Disease of the brain"]
    },
    {
        "question": "What does the term 'Encephalopathy' refer to?",
        "correct_answer": "Disease of the brain",
        "wrong_answers": ["A headache", "Paralysis of one side of the body", "No development"]
    },
    {
        "question": "What does the term 'Neuropathy' refer to?",
        "correct_answer": "Disease of the nerves",
        "wrong_answers": ["A headache", "Paralysis of one side of the body", "No development"]
    },
    {
        "question": "What does the term 'Meningomyelocele' refer to?",
        "correct_answer": "Protrusion of membranes and spinal cord",
        "wrong_answers": ["A headache", "Paralysis of one side of the body", "No development"]
    },
    {
        "question": "What does the term 'Dyslexia' refer to?",
        "correct_answer": "Difficulty reading",
        "wrong_answers": ["Tumor", "Inflammation", "X-ray of the spinal cord"]
    },
    {
        "question": "What does the term 'Neuroma' refer to?",
        "correct_answer": "Tumor",
        "wrong_answers": ["Difficulty reading", "Inflammation", "X-ray of the spinal cord"]
    },
    {
        "question": "What does the term 'Neuritis' refer to?",
        "correct_answer": "Inflammation",
        "wrong_answers": ["Difficulty reading", "Tumor", "X-ray of the spinal cord"]
    },
    {
        "question": "What does the term 'Myelogram' refer to?",
        "correct_answer": "X-ray of the spinal cord",
        "wrong_answers": ["Difficulty reading", "Tumor", "Inflammation"]
    },
    {
        "question": "What does the term 'Meningitis' refer to?",
        "correct_answer": "Inflammation of the membranes",
        "wrong_answers": ["Difficulty reading", "Tumor", "X-ray of the spinal cord"]
    },
    {
        "question": "What does the term 'Encephalitis' refer to?",
        "correct_answer": "Inflammation of the brain",
        "wrong_answers": ["Difficulty reading", "Tumor", "X-ray of the spinal cord"]
    },
    {
        "question": "What does the term 'Anencephalic' refer to?",
        "correct_answer": "Born without a brain",
        "wrong_answers": ["Inflammation of the brain", "X-ray of the spinal cord", "Difficulty reading"]
    },
    {
        "question": "What is Multiple Sclerosis?",
        "correct_answer": "Autoimmune disease affecting the central nervous system.",
        "wrong_answers": [
            "Infectious disease affecting the brain.",
            "Genetic disorder affecting the muscles.",
            "Degenerative disease affecting the bones."
        ]
    },
    {
        "question": "What is Cerebrovascular Accident (CVA)?",
        "correct_answer": "Stroke caused by interruption of blood flow to the brain.",
        "wrong_answers": [
            "Brain infection caused by a virus.",
            "Brain tumor pressing on a nerve.",
            "Muscle spasm in the brain."
        ]
    },
    {
        "question": "What is Transient Ischemic Attack (TIA)?",
        "correct_answer": "Mini-stroke with temporary symptoms.",
        "wrong_answers": [
            "Temporary loss of consciousness.",
            "Sudden severe headache.",
            "Permanent loss of brain function."
        ]
    },
    {
        "question": "What is Epilepsy?",
        "correct_answer": "Neurological disorder characterized by recurrent seizures.",
        "wrong_answers": [
            "Inflammatory disorder of the spine.",
            "Degenerative disorder of the muscles.",
            "Vascular disorder affecting the heart."
        ]
    },
    {
        "question": "What is Aphasia?",
        "correct_answer": "Language disorder affecting comprehension or expression.",
        "wrong_answers": [
            "Visual disorder affecting sight.",
            "Hearing disorder affecting hearing.",
            "Motor disorder affecting movement."
        ]
    },
    {
        "question": "What is a Neurologist?",
        "correct_answer": "Medical doctor specializing in nervous system disorders.",
        "wrong_answers": [
            "Medical doctor specializing in heart disorders.",
            "Medical doctor specializing in lung disorders.",
            "Medical doctor specializing in kidney disorders."
        ]
    },
    {
        "question": "What is Lumbar (spinal) puncture or tap (LP)?",
        "correct_answer": "Procedure to collect cerebrospinal fluid from the lower back.",
        "wrong_answers": [
            "Procedure to inject medication into the spine.",
            "Procedure to remove bone tissue from the spine.",
            "Procedure to repair a herniated disc in the spine."
        ]
    },
    {
        "question": "What is a Brain scan?",
        "correct_answer": "Imaging test to visualize the brain's structure and function.",
        "wrong_answers": [
            "Blood test to analyze brain chemistry.",
            "Physical examination to assess brain health.",
            "Surgical procedure to remove brain tissue."
        ]
    },
    {
        "question": "What is Electroencephalography (EEG)?",
        "correct_answer": "Test to record electrical activity in the brain.",
        "wrong_answers": [
            "Test to measure blood flow in the brain.",
            "Test to assess nerve function in the brain.",
            "Test to evaluate hormone levels in the brain."
        ]
    },
    {
        "question": "What is Computed Tomography (CT)?",
        "correct_answer": "Imaging technique using X-rays to create cross-sectional images of the body.",
        "wrong_answers": [
            "Imaging technique using sound waves to visualize internal organs.",
            "Imaging technique using magnetic fields and radio waves to produce detailed images of the body.",
            "Surgical procedure to remove abnormal tissue from the body."
        ]
    },
    {
        "question": "What is Magnetic Resonance Imaging (MRI)?",
        "correct_answer": "Imaging technique using magnetic fields and radio waves to produce detailed images of the body.",
        "wrong_answers": [
            "Imaging technique using X-rays to create cross-sectional images of the body.",
            "Imaging technique using sound waves to visualize internal organs.",
            "Surgical procedure to remove abnormal tissue from the body."
        ]
    },
    {
        "question": "What does 'Gastr/o' refer to?",
        "correct_answer": "Stomach",
        "wrong_answers": ["Liver", "Gall, bile", "Vomit"]
    },
    {
        "question": "What does 'Hepat/o' refer to?",
        "correct_answer": "Liver",
        "wrong_answers": ["Stomach", "Gall, bile", "Vomit"]
    },
    {
        "question": "What does 'Chol/e' refer to?",
        "correct_answer": "Gall, bile",
        "wrong_answers": ["Stomach", "Liver", "Vomit"]
    },
    {
        "question": "What does 'Emes/o' refer to?",
        "correct_answer": "Vomit",
        "wrong_answers": ["Stomach", "Liver", "Gall, bile"]
    },
    {
        "question": "What does 'Lith/o' refer to?",
        "correct_answer": "Stone",
        "wrong_answers": ["Stomach", "Liver", "Gall, bile"]
    },
    {
        "question": "What does 'Lapar/o' refer to?",
        "correct_answer": "Abdominal wall",
        "wrong_answers": ["Stomach", "Liver", "Gall, bile"]
    },
    {
        "question": "What does '-centesis' mean?",
        "correct_answer": "To puncture",
        "wrong_answers": ["To crush", "Flow, discharge", "Abnormal condition"]
    },
    {
        "question": "What does '-tripsy' mean?",
        "correct_answer": "To crush",
        "wrong_answers": ["To puncture", "Flow, discharge", "Abnormal condition"]
    },
    {
        "question": "What does '-rrhea' mean?",
        "correct_answer": "Flow, discharge",
        "wrong_answers": ["To puncture", "To crush", "Abnormal condition"]
    },
    {
        "question": "What does '-iasis (-osis)' mean?",
        "correct_answer": "Abnormal condition",
        "wrong_answers": ["To puncture", "To crush", "Flow, discharge"]
    },
      {
        "question": "What does 'Gastr/o' refer to?",
        "correct_answer": "Stomach",
        "wrong_answers": ["Liver", "Gall, bile", "Vomit"]
    },
    {
        "question": "What does 'Hepat/o' refer to?",
        "correct_answer": "Liver",
        "wrong_answers": ["Stomach", "Gall, bile", "Vomit"]
    },
    {
        "question": "What does 'Chol/e' refer to?",
        "correct_answer": "Gall, bile",
        "wrong_answers": ["Stomach", "Liver", "Vomit"]
    },
    {
        "question": "What does 'Emes/o' refer to?",
        "correct_answer": "Vomit",
        "wrong_answers": ["Stomach", "Liver", "Gall, bile"]
    },
    {
        "question": "What does 'Lith/o' refer to?",
        "correct_answer": "Stone",
        "wrong_answers": ["Stomach", "Liver", "Gall, bile"]
    },
    {
        "question": "What does 'Lapar/o' refer to?",
        "correct_answer": "Abdominal wall",
        "wrong_answers": ["Stomach", "Liver", "Gall, bile"]
    },
    {
        "question": "What does '-centesis' mean?",
        "correct_answer": "To puncture",
        "wrong_answers": ["To crush", "Flow, discharge", "Abnormal condition"]
    },
    {
        "question": "What does '-tripsy' mean?",
        "correct_answer": "To crush",
        "wrong_answers": ["To puncture", "Flow, discharge", "Abnormal condition"]
    },
    {
        "question": "What does '-rrhea' mean?",
        "correct_answer": "Flow, discharge",
        "wrong_answers": ["To puncture", "To crush", "Abnormal condition"]
    },
    {
        "question": "What does '-iasis (-osis)' mean?",
        "correct_answer": "Abnormal condition",
        "wrong_answers": ["To puncture", "To crush", "Flow, discharge"]
    },
    {
        "question": "What is a cystoscopy?",
        "correct_answer": "Examining the lining of a bladder.",
        "wrong_answers": [
            "Surgical removal of bladder stones.",
            "Treatment of bladder infection.",
            "Measurement of bladder capacity."
        ]
    },
     {
        "question": "What is Gastroesophageal Reflux Disease (GERD)?",
        "correct_answer": "Stomach acid flowing back into the esophagus.",
        "wrong_answers": [
            "Inflammation of the stomach lining.",
            "Liver disorder causing yellowing of the skin.",
            "Inflammation of diverticula in the colon."
        ]
    },
    {
        "question": "What is Jaundice?",
        "correct_answer": "Yellowing of skin due to high bilirubin levels.",
        "wrong_answers": [
            "Stomach acid flowing back into the esophagus.",
            "Inflammation of diverticula in the colon.",
            "Liver disorder causing portal hypertension."
        ]
    },
    {
        "question": "What is Diverticulosis/diverticulitis?",
        "correct_answer": "Small pouches in the colon wall, with or without inflammation.",
        "wrong_answers": [
            "Liver disorder causing yellowing of the skin.",
            "Stomach acid flowing back into the esophagus.",
            "Liver disorder causing portal hypertension."
        ]
    },
    {
        "question": "What is Cirrhosis?",
        "correct_answer": "Chronic liver disease with scarring and loss of function.",
        "wrong_answers": [
            "Stomach acid flowing back into the esophagus.",
            "Inflammation of diverticula in the colon.",
            "Liver disorder causing portal hypertension."
        ]
    },
    {
        "question": "What is Portal Hypertension?",
        "correct_answer": "High blood pressure in portal vein system due to liver disease.",
        "wrong_answers": [
            "Stomach acid flowing back into the esophagus.",
            "Liver disorder causing yellowing of the skin.",
            "Inflammation of diverticula in the colon."
        ]
    },
    {
        "question": "What are Esophageal Varices?",
        "correct_answer": "Enlarged veins in the esophagus due to liver disease.",
        "wrong_answers": [
            "Stomach acid flowing back into the esophagus.",
            "Liver disorder causing yellowing of the skin.",
            "Inflammation of diverticula in the colon."
        ]
    },
    {
        "question": "What is Dysphagia?",
        "correct_answer": "Difficulty swallowing.",
        "wrong_answers": [
            "Stomach acid flowing back into the esophagus.",
            "Liver disorder causing yellowing of the skin.",
            "Inflammation of diverticula in the colon."
        ]
    },
    {
        "question": "What is Crohn’s Disease?",
        "correct_answer": "Chronic inflammatory bowel disease affecting any part of the digestive tract.",
        "wrong_answers": [
            "Stomach acid flowing back into the esophagus.",
            "Liver disorder causing yellowing of the skin.",
            "Inflammation of diverticula in the colon."
        ]
    },
    {
        "question": "What is Peritonitis?",
        "correct_answer": "Inflammation of the peritoneum, the lining of the abdominal cavity.",
        "wrong_answers": [
            "Stomach acid flowing back into the esophagus.",
            "Liver disorder causing yellowing of the skin.",
            "Chronic inflammatory bowel disease."
        ]
    },
    {
        "question": "What is Rhin/o?",
        "correct_answer": "Nose",
        "wrong_answers": [
            "Larynx",
            "Trachea",
            "Lung air passageways"
        ]
    },
    {
        "question": "What is Laryng/o?",
        "correct_answer": "Larynx, or 'voice box'.",
        "wrong_answers": [
            "Nose",
            "Trachea",
            "Lung air passageways"
        ]
    },
    {
        "question": "What is Trache/o?",
        "correct_answer": "Trachea, or 'windpipe'.",
        "wrong_answers": [
            "Nose",
            "Larynx",
            "Lung air passageways"
        ]
    },
    {
        "question": "What is Bronch/o?",
        "correct_answer": "Lung air passageways.",
        "wrong_answers": [
            "Nose",
            "Larynx",
            "Trachea"
        ]
    },
    {
        "question": "What is Pne/u, -pnea?",
        "correct_answer": "Breath, air, lung.",
        "wrong_answers": [
            "Nose",
            "Larynx",
            "Trachea"
        ]
    },
    {
        "question": "What is Pulmo/o?",
        "correct_answer": "Lung.",
        "wrong_answers": [
            "Nose",
            "Larynx",
            "Trachea"
        ]
    },
    {
        "question": "What is -ptysis?",
        "correct_answer": "Spitting (coughing).",
        "wrong_answers": [
            "Reconstruction",
            "Breath, air, lung",
            "Larynx"
        ]
    },
    {
        "question": "What is -plasty?",
        "correct_answer": "Reconstruction.",
        "wrong_answers": [
            "Spitting (coughing)",
            "Breath, air, lung",
            "Larynx"
        ]
    },
    {
        "question": "What is Rhinitis?",
        "correct_answer": "Inflammation of the nose.",
        "wrong_answers": [
            "Inflammation of the larynx.",
            "Inflammation of the trachea.",
            "Inflammation of the bronchi."
        ]
    },
    {
        "question": "What is Rhinorrhea?",
        "correct_answer": "Runny nose.",
        "wrong_answers": [
            "Cutting into the larynx.",
            "Looking into the bronchi.",
            "Accelerated breathing."
        ]
    },
    {
        "question": "What is Laryngotomy?",
        "correct_answer": "Cutting into the larynx.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Temporary opening into the trachea.",
            "Looking into the bronchi."
        ]
    },
    {
        "question": "What is Laryngectomy?",
        "correct_answer": "Surgical removal of the larynx.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Temporary opening into the trachea.",
            "Looking into the bronchi."
        ]
    },
    {
        "question": "What is Tracheotomy?",
        "correct_answer": "Creation of a temporary opening into the trachea.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Cutting into the larynx.",
            "Looking into the bronchi."
        ]
    },
    {
        "question": "What is Tracheostomy?",
        "correct_answer": "Creation of a permanent opening into the trachea.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Cutting into the larynx.",
            "Looking into the bronchi."
        ]
    },
    {
        "question": "What is Bronchoscopy?",
        "correct_answer": "Procedure to look into the bronchi.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Inflammation of the larynx.",
            "Surgical reconstruction of the nose."
        ]
    },
    {
        "question": "What is Tachypnea?",
        "correct_answer": "Accelerated breathing.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Inflammation of the larynx.",
            "Inflammation of the trachea."
        ]
    },
    {
        "question": "What is Dyspnea?",
        "correct_answer": "Difficult or painful breathing.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Inflammation of the larynx.",
            "Inflammation of the trachea."
        ]
    },
    {
        "question": "What is Apnea?",
        "correct_answer": "Cessation of breathing.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Inflammation of the larynx.",
            "Inflammation of the trachea."
        ]
    },
    {
        "question": "What is Pulmonary Artery?",
        "correct_answer": "Artery carrying blood from heart to lungs.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Inflammation of the larynx.",
            "Inflammation of the trachea."
        ]
    },
    {
        "question": "What is Hemoptysis?",
        "correct_answer": "Spitting or coughing up blood from lungs.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Inflammation of the larynx.",
            "Inflammation of the trachea."
        ]
    },
    {
        "question": "What is Rhinoplasty?",
        "correct_answer": "Surgical reconstruction of the nose.",
        "wrong_answers": [
            "Inflammation of the larynx.",
            "Temporary opening into the trachea.",
            "Looking into the bronchi."
        ]
    },
    
     {
        "question": "What is Pneumoconiosis?",
        "correct_answer": "Lung disease caused by inhalation of dust particles.",
        "wrong_answers": [
            "Inflammation of the nose.",
            "Surgical reconstruction of the nose.",
            "Cutting into or surgically removing the larynx."
        ]
    },
    {
        "question": "What is Epistaxis?",
        "correct_answer": "Bleeding from the nose.",
        "wrong_answers": [
            "Lung disease caused by inhalation of dust particles.",
            "Looking into the bronchi.",
            "Accelerated breathing."
        ]
    },
    {
        "question": "What is Cystic Fibrosis?",
        "correct_answer": "Inherited disorder causing mucus buildup in the lungs and digestive system.",
        "wrong_answers": [
            "Bleeding from the nose.",
            "Temporary opening into the trachea.",
            "Lung disease caused by inhalation of dust particles."
        ]
    },
    {
        "question": "What is Emphysema (COPD)?",
        "correct_answer": "Chronic lung disease characterized by damaged air sacs in the lungs.",
        "wrong_answers": [
            "Bleeding from the nose.",
            "Inherited disorder causing mucus buildup.",
            "Looking into the bronchi."
        ]
    },
    {
        "question": "What is Atelectasis?",
        "correct_answer": "Collapsed lung.",
        "wrong_answers": [
            "Chronic lung disease characterized by damaged air sacs.",
            "Inherited disorder causing mucus buildup.",
            "Surgical reconstruction of the nose."
        ]
    },
    {
        "question": "What is a Pulmonologist?",
        "correct_answer": "Doctor specializing in lung diseases.",
        "wrong_answers": [
            "Bleeding from the nose.",
            "Temporary opening into the trachea.",
            "Chronic lung disease characterized by damaged air sacs."
        ]
    },
    {
        "question": "What is a Respiratory Therapist?",
        "correct_answer": "Healthcare professional specializing in respiratory care.",
        "wrong_answers": [
            "Doctor specializing in lung diseases.",
            "Surgical reconstruction of the nose.",
            "Looking into the bronchi."
        ]
    },
    {
        "question": "What is Pulmonary Angiography?",
        "correct_answer": "Imaging test to visualize blood vessels in the lungs.",
        "wrong_answers": [
            "Chronic lung disease characterized by damaged air sacs.",
            "Bleeding from the nose.",
            "Inherited disorder causing mucus buildup."
        ]
    },
    {
        "question": "What is Laryngoscopy?",
        "correct_answer": "Procedure to examine the larynx.",
        "wrong_answers": [
            "Chronic lung disease characterized by damaged air sacs.",
            "Inherited disorder causing mucus buildup.",
            "Imaging test to visualize blood vessels in the lungs."
        ]
    },
    {
        "question": "What is Endotracheal Intubation?",
        "correct_answer": "Placement of a tube into the trachea to maintain an open airway.",
        "wrong_answers": [
            "Chronic lung disease characterized by damaged air sacs.",
            "Procedure to examine the larynx.",
            "Imaging test to visualize blood vessels in the lungs."
        ]
    },
    {
        "question": "What is Nephr/o or ren/o?",
        "correct_answer": "Kidney.",
        "wrong_answers": [
            "Water.",
            "Bladder.",
            "Renal collecting ducts."
        ]
    },
    {
        "question": "What is Hydro/o?",
        "correct_answer": "Water.",
        "wrong_answers": [
            "Kidney.",
            "Bladder.",
            "Renal collecting ducts."
        ]
    },
    {
        "question": "What is Cyst/o?",
        "correct_answer": "Bladder.",
        "wrong_answers": [
            "Kidney.",
            "Water.",
            "Renal collecting ducts."
        ]
    },
    {
        "question": "What is Pyel/o?",
        "correct_answer": "Renal collecting ducts.",
        "wrong_answers": [
            "Kidney.",
            "Water.",
            "Bladder."
        ]
    },
    {
        "question": "What is Ur/o or -uria?",
        "correct_answer": "Urine.",
        "wrong_answers": [
            "Kidney.",
            "Water.",
            "Bladder."
        ]
    },
    {
        "question": "What is Olig/o?",
        "correct_answer": "Scanty or less than normal.",
        "wrong_answers": [
            "Kidney.",
            "Water.",
            "Bladder."
        ]
    },
    {
        "question": "What is -pexy?",
        "correct_answer": "To surgically reattach or fix in normal position.",
        "wrong_answers": [
            "Kidney.",
            "Water.",
            "Bladder."
        ]
    },
    {
        "question": "What is Nephritis?",
        "correct_answer": "Inflammation of the kidney.",
        "wrong_answers": [
            "Renal artery.",
            "Abnormal condition involving back up of urine into the kidney.",
            "Inflammation of, removal of bladder."
        ]
    },
    {
        "question": "What is Hydronephrosis?",
        "correct_answer": "Abnormal condition involving back up of urine into the kidney.",
        "wrong_answers": [
            "Inflammation of the kidney.",
            "X-ray of the collecting ducts.",
            "Frequent urination, no urine formation."
        ]
    },
    {
        "question": "What is Cystitis?",
        "correct_answer": "Inflammation of the bladder.",
        "wrong_answers": [
            "X-ray of the collecting ducts.",
            "Abnormal condition involving back up of urine into the kidney.",
            "Reduced urine formation."
        ]
    },
    {
        "question": "What is Cystectomy?",
        "correct_answer": "Surgical removal of the bladder.",
        "wrong_answers": [
            "Inflammation of the bladder.",
            "Frequent urination, no urine formation.",
            "Surgically attach kidney in normal anatomical position."
        ]
    },
    {
        "question": "What is Pyelogram?",
        "correct_answer": "X-ray of the collecting ducts.",
        "wrong_answers": [
            "Inflammation of the kidney.",
            "Surgically attach kidney in normal anatomical position.",
            "Reduced urine formation."
        ]
    },
    {
        "question": "What is Polyuria?",
        "correct_answer": "Frequent urination.",
        "wrong_answers": [
            "Abnormal condition involving back up of urine into the kidney.",
            "Surgically attach kidney in normal anatomical position.",
            "Inflammation of the bladder."
        ]
    },
    {
        "question": "What is Anuria?",
        "correct_answer": "No urine formation.",
        "wrong_answers": [
            "Frequent urination.",
            "Abnormal condition involving back up of urine into the kidney.",
            "Inflammation of the kidney."
        ]
    },
    {
        "question": "What is Oliguria?",
        "correct_answer": "Reduced urine formation.",
        "wrong_answers": [
            "Surgical removal of the bladder.",
            "Inflammation of the bladder.",
            "No urine formation."
        ]
    },
    {
        "question": "What is Nephropexy?",
        "correct_answer": "Surgically attach kidney in normal anatomical position.",
        "wrong_answers": [
            "Inflammation of the bladder.",
            "X-ray of the collecting ducts.",
            "Frequent urination."
        ]
    },
    {
        "question": "What is Nephrosis?",
        "correct_answer": "Abnormal condition of the kidney.",
        "wrong_answers": [
            "Formation of kidney stones.",
            "Inflammation of the urethra.",
            "Frequent urination during the night."
        ]
    },
    {
        "question": "What is Nephrolith?",
        "correct_answer": "Kidney stone.",
        "wrong_answers": [
            "Abnormal condition of the kidney.",
            "Inflammation of the urethra.",
            "Frequent urination during the night."
        ]
    },
    {
        "question": "What is Urethritis?",
        "correct_answer": "Inflammation of the urethra.",
        "wrong_answers": [
            "Abnormal condition of the kidney.",
            "Formation of kidney stones.",
            "Frequent urination during the night."
        ]
    },
    {
        "question": "What is Nocturia?",
        "correct_answer": "Frequent urination during the night.",
        "wrong_answers": [
            "Abnormal condition of the kidney.",
            "Formation of kidney stones.",
            "Inflammation of the urethra."
        ]
    },
    {
        "question": "What is Enuresis?",
        "correct_answer": "Involuntary discharge of urine, especially at night; bed-wetting.",
        "wrong_answers": [
            "Abnormal condition of the kidney.",
            "Formation of kidney stones.",
            "Inflammation of the urethra."
        ]
    },
    {
        "question": "What is Nephrologist?",
        "correct_answer": "Medical specialist in kidney diseases.",
        "wrong_answers": [
            "Medical specialist in urinary tract diseases.",
            "Medical specialist in kidney stone removal.",
            "Medical specialist in urology."
        ]
    },
    {
        "question": "What is Urologist?",
        "correct_answer": "Medical specialist in urinary tract diseases and male reproductive system.",
        "wrong_answers": [
            "Medical specialist in kidney diseases.",
            "Medical specialist in kidney stone removal.",
            "Medical specialist in nephrology."
        ]
    },
    {
        "question": "What is Intravenous Pyelogram?",
        "correct_answer": "X-ray of kidneys and urinary tract after injection of contrast material.",
        "wrong_answers": [
            "X-ray of the bladder after injection of contrast material.",
            "X-ray of the kidneys without injection of contrast material.",
            "Ultrasound of the kidneys and urinary tract."
        ]
    },
    {
        "question": "What is Retrograde Pyelogram?",
        "correct_answer": "X-ray of kidneys and urinary tract after injection of contrast material through a catheter into the ureters.",
        "wrong_answers": [
            "X-ray of the kidneys without injection of contrast material.",
            "X-ray of the bladder after injection of contrast material.",
            "Ultrasound of the kidneys and urinary tract."
        ]
    },
    {
        "question": "What is Voiding Cystourethrogram?",
        "correct_answer": "X-ray of bladder and urethra during urination.",
        "wrong_answers": [
            "X-ray of the kidneys and urinary tract after injection of contrast material.",
            "Ultrasound of the kidneys and urinary tract.",
            "X-ray of the bladder after injection of contrast material."
        ]
    },
    {
        "question": "What is Dialysis?",
        "correct_answer": "Medical procedure to remove waste products and excess fluid from the blood when the kidneys are unable to do so.",
        "wrong_answers": [
            "Medical procedure to break down kidney stones.",
            "Medical procedure to examine the kidneys using sound waves.",
            "Surgical removal of the kidneys."
        ]
    },
    {
        "question": "What is Lithotripsy?",
        "correct_answer": "Medical procedure to break up kidney stones using shock waves.",
        "wrong_answers": [
            "Medical procedure to remove waste products from the blood.",
            "Medical procedure to examine the kidneys using sound waves.",
            "Surgical removal of the kidneys."
        ]
    },
     {
        "question": "What is Orchid/o or test/o?",
        "correct_answer": "Testes (male gonad).",
        "wrong_answers": [
            "Head of the penis.",
            "Male.",
            "Prostate."
        ]
    },
    {
        "question": "What is Balan/o?",
        "correct_answer": "Head of the penis.",
        "wrong_answers": [
            "Testes (male gonad).",
            "Male.",
            "Prostate."
        ]
    },
    {
        "question": "What is Andr/o?",
        "correct_answer": "Male.",
        "wrong_answers": [
            "Testes (male gonad).",
            "Head of the penis.",
            "Prostate."
        ]
    },
    {
        "question": "What is Prostat/o?",
        "correct_answer": "Prostate.",
        "wrong_answers": [
            "Testes (male gonad).",
            "Head of the penis.",
            "Male."
        ]
    },
    {
        "question": "What is Vas/o?",
        "correct_answer": "Vessel or duct.",
        "wrong_answers": [
            "Testes (male gonad).",
            "Head of the penis.",
            "Prostate."
        ]
    },
    {
        "question": "What is -rrhaphy?",
        "correct_answer": "Suturing.",
        "wrong_answers": [
            "Testes (male gonad).",
            "Head of the penis.",
            "Prostate."
        ]
    },
     {
        "question": "What is Orchiditis?",
        "correct_answer": "Inflammation of the testes.",
        "wrong_answers": [
            "Surgical removal of the testes.",
            "Artery supplying blood to the testes.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Orchidectomy?",
        "correct_answer": "Surgical removal of the testes.",
        "wrong_answers": [
            "Inflammation of the testes.",
            "Artery supplying blood to the testes.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Testicular Artery?",
        "correct_answer": "Artery supplying blood to the testes.",
        "wrong_answers": [
            "Inflammation of the testes.",
            "Surgical removal of the testes.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Testosterone?",
        "correct_answer": "Male sex hormone.",
        "wrong_answers": [
            "Inflammation of the testes.",
            "Surgical removal of the testes.",
            "Artery supplying blood to the testes."
        ]
    },
    {
        "question": "What is Balanitis?",
        "correct_answer": "Inflammation of the head of the penis.",
        "wrong_answers": [
            "Surgical removal of the testes.",
            "Male sex hormone.",
            "Artery supplying blood to the testes."
        ]
    },
    {
        "question": "What is Androgenic?",
        "correct_answer": "Stimulating maleness.",
        "wrong_answers": [
            "Surgical removal of the testes.",
            "Inflammation of the head of the penis.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Androgynous?",
        "correct_answer": "Having characteristics of both male and female appearance.",
        "wrong_answers": [
            "Surgical removal of the testes.",
            "Inflammation of the head of the penis.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Prostatitis?",
        "correct_answer": "Inflammation of the prostate gland.",
        "wrong_answers": [
            "Surgical removal of the testes.",
            "Inflammation of the head of the penis.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Prostatectomy?",
        "correct_answer": "Surgical removal of the prostate gland.",
        "wrong_answers": [
            "Inflammation of the testes.",
            "Inflammation of the head of the penis.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Vas Deferens?",
        "correct_answer": "Duct carrying semen from testes to urethra.",
        "wrong_answers": [
            "Inflammation of the testes.",
            "Inflammation of the head of the penis.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Vasectomy?",
        "correct_answer": "Surgical cutting of the vas deferens.",
        "wrong_answers": [
            "Inflammation of the testes.",
            "Inflammation of the head of the penis.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Herniorrhaphy?",
        "correct_answer": "Surgical correction of inguinal hernia.",
        "wrong_answers": [
            "Inflammation of the testes.",
            "Inflammation of the head of the penis.",
            "Male sex hormone."
        ]
    },
    {
        "question": "What is Hypospadias?",
        "correct_answer": "A congenital condition where the opening of the urethra is on the underside of the penis.",
        "wrong_answers": [
            "A condition where the scrotum fills with fluid.",
            "Enlarged veins within the scrotum.",
            "Undescended testicle(s)."
        ]
    },
    {
        "question": "What is Hydrocele?",
        "correct_answer": "A condition where fluid accumulates in the sac around the testicle(s).",
        "wrong_answers": [
            "A congenital condition where the opening of the urethra is on the underside of the penis.",
            "Enlarged veins within the scrotum.",
            "Undescended testicle(s)."
        ]
    },
    {
        "question": "What is Varicocele?",
        "correct_answer": "Enlarged veins within the scrotum.",
        "wrong_answers": [
            "A congenital condition where the opening of the urethra is on the underside of the penis.",
            "A condition where fluid accumulates in the sac around the testicle(s).",
            "Undescended testicle(s)."
        ]
    },
    {
        "question": "What is Cryptorchidism?",
        "correct_answer": "A condition where one or both testicles fail to descend into the scrotum.",
        "wrong_answers": [
            "A congenital condition where the opening of the urethra is on the underside of the penis.",
            "A condition where fluid accumulates in the sac around the testicle(s).",
            "Enlarged veins within the scrotum."
        ]
    },
    {
        "question": "What is Benign Prostatic Hypertrophy (BPH)?",
        "correct_answer": "Non-cancerous enlargement of the prostate gland.",
        "wrong_answers": [
            "A condition where the opening of the urethra is on the underside of the penis.",
            "A condition where fluid accumulates in the sac around the testicle(s).",
            "Enlarged veins within the scrotum."
        ]
    },
    {
        "question": "What is Transurethral Resection of the Prostate (TURP)?",
        "correct_answer": "Surgical procedure to remove excess prostate tissue that is blocking urine flow.",
        "wrong_answers": [
            "A condition where the opening of the urethra is on the underside of the penis.",
            "A condition where fluid accumulates in the sac around the testicle(s).",
            "Non-cancerous enlargement of the prostate gland."
        ]
    },
    {
        "question": "What is Prostate Specific Antigen (PSA)?",
        "correct_answer": "A protein produced by the prostate gland, elevated levels may indicate prostate cancer.",
        "wrong_answers": [
            "A congenital condition where the opening of the urethra is on the underside of the penis.",
            "A condition where fluid accumulates in the sac around the testicle(s).",
            "Non-cancerous enlargement of the prostate gland."
        ]
    },
    {
        "question": "What is Hyster/o or metr/?",
        "correct_answer": "Uterus.",
        "wrong_answers": [
            "Uterine tube.",
            "Vagina.",
            "Ovary."
        ]
    },
    {
        "question": "What is Salping/o or -salpinx?",
        "correct_answer": "Uterine tube.",
        "wrong_answers": [
            "Uterus.",
            "Vagina.",
            "Ovary."
        ]
    },
    {
        "question": "What is Colp/o?",
        "correct_answer": "Vagina.",
        "wrong_answers": [
            "Uterus.",
            "Uterine tube.",
            "Ovary."
        ]
    },
    {
        "question": "What is Oophor/o?",
        "correct_answer": "Ovary.",
        "wrong_answers": [
            "Uterus.",
            "Uterine tube.",
            "Vagina."
        ]
    },
    {
        "question": "What is Men/o?",
        "correct_answer": "Menstruation.",
        "wrong_answers": [
            "Uterus.",
            "Uterine tube.",
            "Vagina."
        ]
    },
    {
        "question": "What is Mamm/o or mast/o?",
        "correct_answer": "Breast.",
        "wrong_answers": [
            "Uterus.",
            "Uterine tube.",
            "Ovary."
        ]
    },
    {
        "question": "What is -pareunia or coitus?",
        "correct_answer": "Intercourse.",
        "wrong_answers": [
            "Uterus.",
            "Uterine tube.",
            "Ovary."
        ]
    },
    {
        "question": "What is Hysterectomy?",
        "correct_answer": "Surgical removal of the uterus.",
        "wrong_answers": [
            "Inflammation of the lining of the uterus.",
            "Surgical reconstruction of the vagina.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Endometritis?",
        "correct_answer": "Inflammation of the lining of the uterus.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Blood in the uterine tube.",
            "Painful menstruation."
        ]
    },
    {
        "question": "What is Salpingitis?",
        "correct_answer": "Inflammation of the uterine tube.",
        "wrong_answers": [
            "Surgical reconstruction of the vagina.",
            "Painful menstruation.",
            "Blood in the uterine tube."
        ]
    },
    {
        "question": "What is Hematosalpinx?",
        "correct_answer": "Blood in the uterine tube.",
        "wrong_answers": [
            "Inflammation of the lining of the uterus.",
            "Surgical removal of the uterus.",
            "Surgical reconstruction of the vagina."
        ]
    },
    {
        "question": "What is Colporrhaphy?",
        "correct_answer": "Suturing a tear in the vagina.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Colpoplasty?",
        "correct_answer": "Surgical reconstruction of the vagina.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Colposcopy?",
        "correct_answer": "Medical procedure to view the interior of the vagina and cervix.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Oophorectomy?",
        "correct_answer": "Surgical removal of the ovary.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Blood in the uterine tube."
        ]
    },
    {
        "question": "What is Oophoropexy?",
        "correct_answer": "Surgical fixation or reattachment of the ovary.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Blood in the uterine tube."
        ]
    },
    {
        "question": "What is Menarche?",
        "correct_answer": "The first occurrence of menstruation.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Painful menstruation."
        ]
    },
    {
        "question": "What is Dysmenorrhea?",
        "correct_answer": "Painful menstruation.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Blood in the uterine tube."
        ]
    },
    {
        "question": "What is Mammogram?",
        "correct_answer": "X-ray of the breast.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Mastectomy?",
        "correct_answer": "Surgical removal of the breast.",
        "wrong_answers": [
            "Inflammation of the lining of the uterus.",
            "Blood in the uterine tube.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Dyspareunia?",
        "correct_answer": "Painful intercourse.",
        "wrong_answers": [
            "Surgical removal of the uterus.",
            "Inflammation of the lining of the uterus.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Precoital?",
        "correct_answer": "Before intercourse.",
        "wrong_answers": [
            "Painful intercourse.",
            "Surgical removal of the uterus.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Postcoital?",
        "correct_answer": "After intercourse.",
        "wrong_answers": [
            "Painful intercourse.",
            "Surgical removal of the uterus.",
            "Surgical removal of the ovary."
        ]
    },
    {
        "question": "What is Endometriosis?",
        "correct_answer": "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
        "wrong_answers": [
            "Inflammation of the pelvic organs.",
            "Downward displacement of the uterus into the vaginal canal.",
            "A surgical procedure to view the inside of the vagina and cervix."
        ]
    },
    {
        "question": "What is Pelvic Inflammatory Disease (PID)?",
        "correct_answer": "An infection of the female reproductive organs.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "Downward displacement of the uterus into the vaginal canal.",
            "A surgical procedure to view the inside of the vagina and cervix."
        ]
    },
    {
        "question": "What is Prolapsed Uterus?",
        "correct_answer": "Downward displacement of the uterus into the vaginal canal.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "Inflammation of the pelvic organs.",
            "A surgical procedure to view the inside of the vagina and cervix."
        ]
    },
    {
        "question": "What is Obstetrician?",
        "correct_answer": "A medical doctor specializing in pregnancy, childbirth, and postpartum care.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "Downward displacement of the uterus into the vaginal canal."
        ]
    },
    {
        "question": "What is Gynecologist?",
        "correct_answer": "A medical doctor specializing in the female reproductive system.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "A surgical procedure to view the inside of the vagina and cervix."
        ]
    },
    {
        "question": "What is Episiotomy?",
        "correct_answer": "A surgical incision made in the perineum to widen the vaginal opening during childbirth.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "A medical procedure to view the inside of the vagina and cervix."
        ]
    },
    {
        "question": "What is Hysterosalpingogram?",
        "correct_answer": "An X-ray procedure to examine the uterus and fallopian tubes.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "A surgical procedure to widen the vaginal opening during childbirth."
        ]
    },
    {
        "question": "What is Colposcopy?",
        "correct_answer": "A medical procedure to view the cervix and vagina in detail.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "A surgical procedure to widen the vaginal opening during childbirth."
        ]
    },
    {
        "question": "What is Dilation and Curettage (D & C)?",
        "correct_answer": "A surgical procedure to remove tissue from the inside of the uterus.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "A medical procedure to view the cervix and vagina in detail."
        ]
    },
    {
        "question": "What is Mammoplasty?",
        "correct_answer": "Surgical reconstruction or augmentation of the breast.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "A surgical procedure to widen the vaginal opening during childbirth."
        ]
    },
    {
        "question": "What is Pudendal Block?",
        "correct_answer": "A regional anesthetic injection used during childbirth to numb the perineum and surrounding area.",
        "wrong_answers": [
            "A condition where tissue similar to the lining of the uterus grows outside the uterus.",
            "An infection of the female reproductive organs.",
            "A surgical procedure to widen the vaginal opening during childbirth."
        ]
    },
     {
        "question": "What does -gravida mean?",
        "correct_answer": "Pregnancy.",
        "wrong_answers": [
            "Live birth.",
            "Labor/birth/delivery.",
            "A medical condition related to the uterus."
        ]
    },
    {
        "question": "What does -para mean?",
        "correct_answer": "Live birth.",
        "wrong_answers": [
            "Pregnancy.",
            "Labor/birth/delivery.",
            "A medical condition related to the uterus."
        ]
    },
    {
        "question": "What does Part/o or toc/o mean?",
        "correct_answer": "Labor, birth, or delivery.",
        "wrong_answers": [
            "Pregnancy.",
            "Live birth.",
            "A medical condition related to the uterus."
        ]
    },
    {
        "question": "What is Nulligravida?",
        "correct_answer": "Never pregnant.",
        "wrong_answers": [
            "First-time pregnant.",
            "Many pregnancies.",
            "Many live births."
        ]
    },
    {
        "question": "What is Primigravida?",
        "correct_answer": "First-time pregnant.",
        "wrong_answers": [
            "Never pregnant.",
            "Many pregnancies.",
            "Many live births."
        ]
    },
    {
        "question": "What is Multigravida?",
        "correct_answer": "Many pregnancies.",
        "wrong_answers": [
            "Never pregnant.",
            "First-time pregnant.",
            "Many live births."
        ]
    },
    {
        "question": "What is Prepartum?",
        "correct_answer": "Before delivery.",
        "wrong_answers": [
            "After delivery.",
            "Difficult delivery.",
            "Many live births."
        ]
    },
    {
        "question": "What is Postpartum?",
        "correct_answer": "After delivery.",
        "wrong_answers": [
            "Before delivery.",
            "Difficult delivery.",
            "Many live births."
        ]
    },
    {
        "question": "What is Dystocia?",
        "correct_answer": "Difficult delivery.",
        "wrong_answers": [
            "Before delivery.",
            "After delivery.",
            "Many live births."
        ]
    },
    {
        "question": "What is Nullipara?",
        "correct_answer": "No live births.",
        "wrong_answers": [
            "Never pregnant.",
            "First-time pregnant.",
            "Many pregnancies."
        ]
    },
    {
        "question": "What is Multipara?",
        "correct_answer": "Many live births.",
        "wrong_answers": [
            "Never pregnant.",
            "First-time pregnant.",
            "Many pregnancies."
        ]
    },
    {
        "question": "What is Abruptio Placentae?",
        "correct_answer": "Premature separation of the placenta from the uterine wall.",
        "wrong_answers": [
            "Abnormal placement of the placenta over or near the cervix.",
            "Seizures during pregnancy.",
            "A pregnancy that occurs outside the uterus."
        ]
    },
    {
        "question": "What is Placenta Previa?",
        "correct_answer": "Abnormal placement of the placenta over or near the cervix.",
        "wrong_answers": [
            "Premature separation of the placenta from the uterine wall.",
            "Seizures during pregnancy.",
            "A pregnancy that occurs outside the uterus."
        ]
    },
    {
        "question": "What is Eclampsia?",
        "correct_answer": "Seizures during pregnancy.",
        "wrong_answers": [
            "Premature separation of the placenta from the uterine wall.",
            "Abnormal placement of the placenta over or near the cervix.",
            "A pregnancy that occurs outside the uterus."
        ]
    },
    {
        "question": "What is Ectopic Pregnancy?",
        "correct_answer": "A pregnancy that occurs outside the uterus, often in the fallopian tube.",
        "wrong_answers": [
            "Premature separation of the placenta from the uterine wall.",
            "Abnormal placement of the placenta over or near the cervix.",
            "Seizures during pregnancy."
        ]
    },
    {
        "question": "What is Osteomalacia?",
        "correct_answer": "Softening of the bone.",
        "wrong_answers": [
            "Cartilage.",
            "Joint.",
            "Bone marrow."
        ]
    },
    {
        "question": "What is Osteoporosis?",
        "correct_answer": "Porous bone.",
        "wrong_answers": [
            "Softening of the bone.",
            "Cartilage.",
            "Joint."
        ]
    },
    {
        "question": "What is Arthralgia?",
        "correct_answer": "Pain in a joint.",
        "wrong_answers": [
            "Softening of the bone.",
            "Cartilage.",
            "Bone marrow."
        ]
    },
    {
        "question": "What is Myasthenia?",
        "correct_answer": "Weakness or loss of strength in muscles.",
        "wrong_answers": [
            "Bone marrow.",
            "Tendon.",
            "Ligament."
        ]
    },
    {
        "question": "What is Hypertrophy?",
        "correct_answer": "Development or stimulation of tissues.",
        "wrong_answers": [
            "Bone marrow.",
            "Cartilage.",
            "Muscle."
        ]
    },
    {
        "question": "What is Tenosynovitis?",
        "correct_answer": "Inflammation of the tendon and its sheath.",
        "wrong_answers": [
            "Bone marrow.",
            "Cartilage.",
            "Ligament."
        ]
    },
    {
        "question": "What is Myalgia?",
        "correct_answer": "Muscle pain.",
        "wrong_answers": [
            "Bone marrow.",
            "Cartilage.",
            "Tendon."
        ]
    },
    {
        "question": "What is Bursitis?",
        "correct_answer": "Inflammation of the bursa.",
        "wrong_answers": [
            "Softening of the bone.",
            "Pain in a joint.",
            "Weakness or loss of strength in muscles."
        ]
    },
     {
        "question": "What is Osteitis?",
        "correct_answer": "Inflammation of the bone.",
        "wrong_answers": [
            "Abnormal growth of bone tissue.",
            "Mature bone cell.",
            "Inflammation of cartilage."
        ]
    },
    {
        "question": "What is Chondritis?",
        "correct_answer": "Inflammation of cartilage.",
        "wrong_answers": [
            "Abnormal growth of bone tissue.",
            "Mature bone cell.",
            "Inflammation of bone."
        ]
    },
    {
        "question": "What is Arthritis?",
        "correct_answer": "Inflammation of a joint.",
        "wrong_answers": [
            "Surgical repair of a joint.",
            "Abnormal growth of bone tissue.",
            "Inflammation of muscle."
        ]
    },
    {
        "question": "What is Myeloma?",
        "correct_answer": "Cancerous tumor of the bone marrow.",
        "wrong_answers": [
            "Inflammation of the bone.",
            "Abnormal growth of bone tissue.",
            "Mature bone cell."
        ]
    },
    {
        "question": "What is Tendonitis?",
        "correct_answer": "Inflammation of a tendon.",
        "wrong_answers": [
            "Surgical repair of a tendon.",
            "Abnormal growth of bone tissue.",
            "Inflammation of muscle."
        ]
    },
    {
        "question": "What is Ligamentous Injury?",
        "correct_answer": "Injury to a ligament.",
        "wrong_answers": [
            "Inflammation of a ligament.",
            "Abnormal growth of bone tissue.",
            "Inflammation of muscle."
        ]
    },
    {
        "question": "What is Bursitis?",
        "correct_answer": "Inflammation of the bursa.",
        "wrong_answers": [
            "Inflammation of the bone.",
            "Inflammation of cartilage.",
            "Inflammation of muscle."
        ]
    },
    {
        "question": "What is Myositis?",
        "correct_answer": "Inflammation of muscle tissue.",
        "wrong_answers": [
            "Inflammation of bone.",
            "Inflammation of cartilage.",
            "Inflammation of tendon."
        ]
    },
    {
        "question": "What is Osteomalacia?",
        "correct_answer": "Softening of the bone due to vitamin D deficiency.",
        "wrong_answers": [
            "Softening of cartilage.",
            "Weakness of muscle.",
            "Shriveling of muscles."
        ]
    },
    {
        "question": "What is Osteoporosis?",
        "correct_answer": "A condition characterized by porous and weakened bones.",
        "wrong_answers": [
            "Softening of cartilage.",
            "Inflammation of tendon.",
            "Increase in muscle size and strength."
        ]
    },
    {
        "question": "What is Myasthenia Gravis?",
        "correct_answer": "An autoimmune neuromuscular disorder characterized by weakness and fatigue of voluntary muscles.",
        "wrong_answers": [
            "Inflammation of bone marrow.",
            "Inflammation of muscle.",
            "Take away pain."
        ]
    },
    {
        "question": "What is Atrophy?",
        "correct_answer": "Shriveling or wasting away of tissues, such as muscles.",
        "wrong_answers": [
            "Increase in size and strength of muscles.",
            "Inflammation of bone.",
            "Inflammation of cartilage."
        ]
    },
    {
        "question": "What is Analgesia?",
        "correct_answer": "A state of pain relief.",
        "wrong_answers": [
            "Pain in joints.",
            "Inflammation of bone.",
            "Increase in muscle size."
        ]
    },
    {
        "question": "What is Arthritis?",
        "correct_answer": "Inflammation of a joint.",
        "wrong_answers": [
            "A condition characterized by porous and weakened bones.",
            "Softening of the bone due to vitamin D deficiency.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Osteoporosis?",
        "correct_answer": "A condition characterized by porous and weakened bones.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "Softening of the bone due to vitamin D deficiency.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Osteomalacia?",
        "correct_answer": "Softening of the bone due to vitamin D deficiency.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Carpal Tunnel Syndrome?",
        "correct_answer": "Compression of the median nerve in the wrist.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Softening of the bone due to vitamin D deficiency."
        ]
    },
    {
        "question": "What is Tendonitis?",
        "correct_answer": "Inflammation of a tendon.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Rotator Cuff Tear?",
        "correct_answer": "Tear or injury in the rotator cuff of the shoulder.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Bursitis?",
        "correct_answer": "Inflammation of the bursa, a fluid-filled sac near a joint.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Muscular Dystrophy?",
        "correct_answer": "A group of genetic disorders characterized by progressive weakness and loss of muscle mass.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Myasthenia Gravis?",
        "correct_answer": "An autoimmune neuromuscular disorder characterized by weakness and fatigue of voluntary muscles.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Compression of the median nerve in the wrist."
        ]
    },
    {
        "question": "What is Lupus Erythematosus?",
        "correct_answer": "An autoimmune disease that causes inflammation in various parts of the body, including joints, skin, kidneys, and other organs.",
        "wrong_answers": [
            "Inflammation of a joint.",
            "A condition characterized by porous and weakened bones.",
            "Compression of the median nerve in the wrist."
        ]
    },
     {
        "question": "What does an Orthopaedist specialize in?",
        "correct_answer": "Diagnosis and treatment of musculoskeletal conditions, including bones, joints, ligaments, tendons, and muscles.",
        "wrong_answers": [
            "Diagnosis and treatment of autoimmune diseases affecting joints and connective tissues.",
            "Treatment of bone disorders using osteopathic techniques.",
            "Treatment of foot disorders and diseases."
        ]
    },
    {
        "question": "What does a Rheumatologist specialize in?",
        "correct_answer": "Diagnosis and treatment of autoimmune diseases affecting joints and connective tissues.",
        "wrong_answers": [
            "Diagnosis and treatment of musculoskeletal conditions, including bones, joints, ligaments, tendons, and muscles.",
            "Treatment of bone disorders using osteopathic techniques.",
            "Treatment of foot disorders and diseases."
        ]
    },
    {
        "question": "What does an Osteopath/Osteopathic Physician (D.O.) specialize in?",
        "correct_answer": "Treatment of bone disorders using osteopathic techniques.",
        "wrong_answers": [
            "Diagnosis and treatment of musculoskeletal conditions, including bones, joints, ligaments, tendons, and muscles.",
            "Diagnosis and treatment of autoimmune diseases affecting joints and connective tissues.",
            "Treatment of foot disorders and diseases."
        ]
    },
    {
        "question": "What does a Podiatrist specialize in?",
        "correct_answer": "Treatment of foot disorders and diseases.",
        "wrong_answers": [
            "Diagnosis and treatment of musculoskeletal conditions, including bones, joints, ligaments, tendons, and muscles.",
            "Diagnosis and treatment of autoimmune diseases affecting joints and connective tissues.",
            "Treatment of bone disorders using osteopathic techniques."
        ]
    },
    {
        "question": "What does a Physical Therapist do?",
        "correct_answer": "Assists in rehabilitation and improvement of physical function through exercises, manual therapy, and other techniques.",
        "wrong_answers": [
            "Diagnosis and treatment of musculoskeletal conditions, including bones, joints, ligaments, tendons, and muscles.",
            "Diagnosis and treatment of autoimmune diseases affecting joints and connective tissues.",
            "Treatment of foot disorders and diseases."
        ]
    },
    {
        "question": "What is Arthroscopy?",
        "correct_answer": "A minimally invasive surgical procedure used to visualize, diagnose, and treat problems inside a joint.",
        "wrong_answers": [
            "A diagnostic imaging technique used to assess bone density and detect abnormalities.",
            "A procedure used to measure electrical activity in muscles.",
            "A surgical procedure to remove a small piece of muscle tissue for examination."
        ]
    },
    {
        "question": "What is a Bone Scan?",
        "correct_answer": "A nuclear imaging test used to diagnose and monitor bone disorders, such as fractures, infections, and tumors.",
        "wrong_answers": [
            "A minimally invasive surgical procedure used to visualize, diagnose, and treat problems inside a joint.",
            "A procedure used to measure electrical activity in muscles.",
            "A surgical procedure to remove a small piece of muscle tissue for examination."
        ]
    },
    {
        "question": "What is Electromyography?",
        "correct_answer": "A diagnostic procedure used to assess the health of muscles and the nerve cells that control them by measuring electrical activity.",
        "wrong_answers": [
            "A minimally invasive surgical procedure used to visualize, diagnose, and treat problems inside a joint.",
            "A nuclear imaging test used to diagnose and monitor bone disorders.",
            "A surgical procedure to remove a small piece of muscle tissue for examination."
        ]
    },
    {
        "question": "What is a Muscle Biopsy?",
        "correct_answer": "A surgical procedure to remove a small piece of muscle tissue for examination under a microscope.",
        "wrong_answers": [
            "A minimally invasive surgical procedure used to visualize, diagnose, and treat problems inside a joint.",
            "A nuclear imaging test used to diagnose and monitor bone disorders.",
            "A diagnostic procedure used to assess the health of muscles and nerve cells."
        ]
    },
    {
        "question": "Is 'Benign' associated with good or bad news?",
        "correct_answer": "Good news (non-cancerous).",
        "wrong_answers": [
            "Bad news (cancerous).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Low grade' associated with good or bad news?",
        "correct_answer": "Usually good news (indicating slower-growing cancer cells).",
        "wrong_answers": [
            "Usually bad news (indicating aggressive cancer cells).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Radiosensitive' associated with good or bad news?",
        "correct_answer": "Good news (cancer cells are sensitive to radiation treatment).",
        "wrong_answers": [
            "Bad news (cancer cells are resistant to radiation treatment).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'No metastases' associated with good or bad news?",
        "correct_answer": "Good news (cancer has not spread to other parts of the body).",
        "wrong_answers": [
            "Bad news (cancer has spread to other parts of the body).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Well differentiated' associated with good or bad news?",
        "correct_answer": "Usually good news (cells look similar to normal cells and tend to grow and spread more slowly).",
        "wrong_answers": [
            "Usually bad news (cells look very abnormal and tend to grow and spread quickly).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Negative nodes' associated with good or bad news?",
        "correct_answer": "Good news (lymph nodes do not contain cancer cells).",
        "wrong_answers": [
            "Bad news (lymph nodes contain cancer cells).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'In remission' associated with good or bad news?",
        "correct_answer": "Good news (cancer is under control or in a state of improvement).",
        "wrong_answers": [
            "Bad news (cancer is worsening or spreading).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Surgically resectable' associated with good or bad news?",
        "correct_answer": "Usually good news (cancer can be removed with surgery).",
        "wrong_answers": [
            "Usually bad news (cancer cannot be removed with surgery).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Malignant' associated with good or bad news?",
        "correct_answer": "Bad news (cancerous).",
        "wrong_answers": [
            "Good news (non-cancerous).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'High grade' associated with good or bad news?",
        "correct_answer": "Usually bad news (indicating more aggressive cancer cells).",
        "wrong_answers": [
            "Usually good news (indicating slower-growing cancer cells).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Radioresistant' associated with good or bad news?",
        "correct_answer": "Bad news (cancer cells are resistant to radiation treatment).",
        "wrong_answers": [
            "Good news (cancer cells are sensitive to radiation treatment).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Metastases' associated with good or bad news?",
        "correct_answer": "Bad news (cancer has spread to other parts of the body).",
        "wrong_answers": [
            "Good news (cancer has not spread to other parts of the body).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Poorly differentiated' associated with good or bad news?",
        "correct_answer": "Usually bad news (cells look very abnormal and tend to grow and spread quickly).",
        "wrong_answers": [
            "Usually good news (cells look similar to normal cells and tend to grow and spread more slowly).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Positive nodes' associated with good or bad news?",
        "correct_answer": "Bad news (lymph nodes contain cancer cells).",
        "wrong_answers": [
            "Good news (lymph nodes do not contain cancer cells).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Relapse' associated with good or bad news?",
        "correct_answer": "Bad news (cancer has returned after a period of improvement).",
        "wrong_answers": [
            "Good news (cancer is under control or in a state of improvement).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
    {
        "question": "Is 'Inoperable' associated with good or bad news?",
        "correct_answer": "Usually bad news (cancer cannot be removed with surgery).",
        "wrong_answers": [
            "Usually good news (cancer can be removed with surgery).",
            "Neither good nor bad news.",
            "Unknown."
        ]
    },
     {
        "question": "What is Carcinoma?",
        "correct_answer": "A malignant tumor that arises from epithelial cells.",
        "wrong_answers": [
            "A benign tumor composed of glandular tissue.",
            "A type of cancer that starts in connective tissue.",
            "A type of autoimmune disease."
        ]
    },
    {
        "question": "What is Sarcoma?",
        "correct_answer": "A malignant tumor that arises from connective tissue (such as bone, muscle, or cartilage).",
        "wrong_answers": [
            "A benign tumor composed of connective tissue.",
            "A type of cancer that starts in epithelial cells.",
            "A type of viral infection."
        ]
    },
    {
        "question": "What are Tumor Markers?",
        "correct_answer": "Usually used for monitoring cancer activity or response to treatment.",
        "wrong_answers": [
            "Indicative of cancer diagnosis.",
            "Associated with benign tumors only.",
            "Used for vaccination against cancer."
        ]
    },
    {
        "question": "What is Radiation?",
        "correct_answer": "A treatment method for cancer that uses high-energy rays or particles to destroy cancer cells.",
        "wrong_answers": [
            "A diagnostic imaging technique.",
            "A form of chemotherapy.",
            "A surgical procedure to remove tumors."
        ]
    },
    {
        "question": "What is Chemotherapy?",
        "correct_answer": "A treatment method for cancer that uses drugs to kill cancer cells.",
        "wrong_answers": [
            "A form of radiation therapy.",
            "A type of surgery to remove tumors.",
            "A method for monitoring cancer activity."
        ]
    },
    {
        "question": "What is Surgery?",
        "correct_answer": "A treatment method for cancer that involves physically removing the tumor from the body.",
        "wrong_answers": [
            "A form of radiation therapy.",
            "A type of chemotherapy.",
            "A method for monitoring cancer activity."
        ]
    }
    
    
]




#Total questions for premid 1

total_Anatomy = len(Anatomy_questions + Anatomy_practical)
print(f"created a total of {total_Anatomy} questions for Anatomy questions.")

total_Biology = len(Biology_questions)
print(f"created a total of {total_Biology} questions for Biology questions.")

total_chemistry = len(Chemistry_questions + Chemistry_practical)
print(f"created a total of {total_chemistry} questions for Chemistry questions.")

total_NIT = len(NIT_questions)
print(f"created a total of {total_NIT} questions for NIT questions.")

total_PPC = len(PPC_questions)
print(f"created a total of {total_PPC} questions for PPC questions.")


total_questions = (total_Anatomy + total_Biology + total_chemistry + total_NIT + total_PPC )
print(f"{SL}created a total of {total_questions} for premid 1 questions. practical not included{SL}")


#Total questions for premid 2

total_PPCT = len(PPC_terms)
print(f"created a total of {total_PPCT} questions for PPCT questions.")