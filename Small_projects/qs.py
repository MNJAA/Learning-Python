from ANSI import CR,C,SL
print(C,CR)

Anatomy_questions = [
    
]

total_questions = len(Anatomy_questions)
print(f"{SL}created a total of {total_questions} questions for Anatomy questions.{SL}")

Anatomy_ph = ["Join the Body Party: Where Bones and Friends Hang Out!", "Anatomy Antics: Fun with Organs and Friends!",
              "Anatomy Quest: Where Cells and Smiles Collide!", "Anatomy Aces: Where Learning Meets Limb-rary!",
              "Anatomy Excellence: Charting the Course to Success!", "Body Brilliance Begins with Anatomy Excellence!",
              ]

Biology_questions = [
      {
        "question": "What is the difference between meiosis I and mitosis?",
        "correct_answer": "Sister chromatids remain joined at their centromeres throughout meiosis I but are apart completely in anaphase in mitosis",
        "wrong_answers": [
            "During meiosis I, sister chromatids separate in anaphase similar to mitosis, and they remain joined at their centromeres throughout mitosis.",
            "In both meiosis I and mitosis, sister chromatids separate during anaphase, and they are always apart completely from prophase through telophase."
        ],
        "score": 0
    },
    {
        "question": "IVF uses?",
        "correct_answer": "Phase contrast",
        "wrong_answers": ["SEM", "TEM", "LM"],
        "score": 0
    },
    {
        "question": "What structure from the GI tract is shown? (Image)?",
        "correct_answer": "Stomach",
        "wrong_answers": ["Small intestine", "Colon", "Esophagus"],
        "score": 0
    },
    {
        "question": "Mucus secretion of vagina happens or is produced from?",
        "correct_answer": "Mucous from the cervix",
        "wrong_answers": ["Uterus lining", "Fallopian tubes", "Ovaries"],
        "score": 0
    },
    {
        "question": "Which is a part of internal female genitalia?",
        "correct_answer": "Vagina",
        "wrong_answers": ["Uterus", "Ovaries", "Cervix"],
        "score": 0
    },
    {
        "question": "Maturation of tissue and stuff occurs at which stage of embryological development?",
        "correct_answer": "Fetal",
        "wrong_answers": ["Embryonic", "Neonatal", "Adolescent"],
        "score": 0
    },
    {
        "question": "What is responsible for dilated pupils?",
        "correct_answer": "Oculomotor",
        "wrong_answers": ["Optic nerve", "Trochlear nerve", "Abducens nerve"],
        "score": 0
    },
    {
        "question": "What is one correct statement about kidneys?",
        "correct_answer": "Ureter is the most posterior structure in the root",
        "wrong_answers": ["Renal artery is anterior to the renal vein", "The renal pelvis is located in the cortex", "The nephron is the smallest functional unit"],
        "score": 0
    },
    {
        "question": "Nephron consist of?",
        "correct_answer": "Renal corpuscle and renal tubules",
        "wrong_answers": ["Collecting ducts only", "Glomerulus only", "Renal pelvis and ureter"],
        "score": 0
    },
    {
        "question": "Integral membrane proteins? - span all over phospholipid membrane",
        "correct_answer": "Span all over phospholipid membrane",
        "wrong_answers": ["Are only found in the cytoplasm", "Are soluble in water", "Are located outside the cell"],
        "score": 0
    },
    {
        "question": "What factors affect Passive transport?",
        "correct_answer": "Concentration gradient",
        "wrong_answers": ["Energy input", "Carrier proteins", "ATP hydrolysis"],
        "score": 0
    },
    {
        "question": "The main principle of fluid mosaic of plasma membrane?",
        "correct_answer": "Phospholipid bilayer",
        "wrong_answers": ["Protein monolayer", "Cholesterol layer", "Glycoprotein mesh"],
        "score": 0
    },
    {
        "question": "What is a membrane protein that uses active transport?",
        "correct_answer": "Na+K+ pump",
        "wrong_answers": ["Facilitated diffusion protein", "Ion channel protein", "Aquaporin"],
        "score": 0
    },
    {
        "question": "Air in pleural cavity is:",
        "correct_answer": "Pneumothorax",
        "wrong_answers": ["Hemothorax", "Hydrothorax", "Atelectasis"],
        "score": 0
    },
    {
        "question": "Gonadotroph affected, what gland is impacted?",
        "correct_answer": "Ovary",
        "wrong_answers": ["Testis", "Pituitary gland", "Thyroid gland"],
        "score": 0
    },
    {
        "question": "Hormones that stimulate the posterior pituitary gland to secrete hormones are?",
        "correct_answer": "Stimulating hormones",
        "wrong_answers": ["Inhibiting hormones", "Tropic hormones", "Releasing hormones"],
        "score": 0
    },
    {
        "question": "Which of the following is true about the nervous system?",
        "correct_answer": "31 spinal nerve segments",
        "wrong_answers": ["12 cranial nerves", "42 spinal nerve segments", "24 thoracic nerve segments"],
        "score": 0
    },
    {
        "question": "A CT scan for abdomino pelvic... how is the scan taken?",
        "correct_answer": "Coronal plane",
        "wrong_answers": ["Sagittal plane", "Axial plane", "Transverse plane"],
        "score": 0
    },
    {
        "question": "CT scan of a patient of the vertebral column... how is the picture taken?",
        "correct_answer": "Transverse",
        "wrong_answers": ["Sagittal", "Coronal", "Oblique"],
        "score": 0
    },
    {
        "question": "Which lymphoid organ is responsible for filtering antigens circulating in the blood?",
        "correct_answer": "Spleen",
        "wrong_answers": ["Thymus", "Lymph nodes", "Tonsils"],
        "score": 0
    },
    {
        "question": "What of the following is responsible for bone resorption?",
        "correct_answer": "Osteoclasts",
        "wrong_answers": ["Osteoblasts", "Chondrocytes", "Fibroblasts"],
        "score": 0
    },
    {
        "question": "What is inductive reasoning?",
        "correct_answer": "Drawing a general conclusion from specific observations",
        "wrong_answers": ["Drawing specific conclusions from general observations", "Making predictions based on assumptions", "Deducing specific facts from unrelated observations"],
        "score": 0
    },
    {
        "question": "Which of the following describes astrocytes?",
        "correct_answer": "Prevents harmful substances from passing into the brain",
        "wrong_answers": ["Promotes the passage of harmful substances", "Has no role in substance regulation", "Is not present in the brain"],
        "score": 0
    },
    {
        "question": "Collection of neural bodies inside the CNS:",
        "correct_answer": "Nucleus",
        "wrong_answers": ["Ganglion", "Cortex", "Tract"],
        "score": 0
    },
    {
        "question": "What is the best description of the sensory system?",
        "correct_answer": "From skin to spinal nerves through dorsal root",
        "wrong_answers": ["From muscles to spinal nerves through ventral root", "From brain to peripheral nerves", "From eyes to optic nerve"],
        "score": 0
    },
    {
        "question": "A patient suffers from motor weakness in facial nerves? Part C, Lower part anterior sulcus",
        "correct_answer": "False",
        "wrong_answers": ["True", "Depends on the specific condition", "Motor weakness is not associated with facial nerves"],
        "score": 0
    },
    {
        "question": "DNA wrapped around a core of 8 histones:",
        "correct_answer": "Nucleosome",
        "wrong_answers": ["Chromatin", "Centromere", "Nuclear envelope"],
        "score": 0
    },
    {
        "question": "Patient suffers from touch, position, as well as pain and temperature on the left side. Which area is affected?",
        "correct_answer": "Right side of the brain",
        "wrong_answers": ["Left side of the brain", "Spinal cord", "Peripheral nerves in the left side"],
        "score": 0
    },
    {
        "question": "Patient suffers from touch and position in the left side. Which area of the spinal cord is affected? (Ignore the circle)",
        "correct_answer": "Right side of the spinal cord",
        "wrong_answers": ["Left side of the spinal cord", "Cervical region", "Lumbar region"],
        "score": 0
    },
    {
        "question": "What is the function of the cell?",
        "correct_answer": "Receives/transmits impulses",
        "wrong_answers": ["Produces energy", "Stores genetic information", "Synthesizes proteins"],
        "score": 0
    },
    {
        "question": "Development of tissue and stuff occurs at which stage of embryological development?",
        "correct_answer": "Fetal",
        "wrong_answers": ["Embryonic", "Neonatal", "Adulthood"],
        "score": 0
    },
    {
        "question": "True about cell theory?",
        "correct_answer": "All made of 1 or more cells",
        "wrong_answers": ["Each cell is independent", "Cells do not have genetic material", "Cells do not have specific functions"],
        "score": 0
    },
    {
        "question": "A cross-section of the spinal cord, which part is affected that causes dysfunction of the heart?",
        "correct_answer": "Lateral horn",
        "wrong_answers": ["Dorsal horn", "Ventral horn", "Central canal"],
        "score": 0
    },
    {
        "question": "Which part of the spinal cord has somatic neurons controlling muscle?",
        "correct_answer": "Ventral horn (anterior)",
        "wrong_answers": ["Dorsal horn", "Lateral horn", "Central canal"],
        "score": 0
    },
    {
        "question": "Where does ovulation occur?",
        "correct_answer": "Uterine tube",
        "wrong_answers": ["Ovary", "Uterus", "Cervix"],
        "score": 0
    },
    {
        "question": "What kind of structure is found in the electron microscope but not the light microscope?",
        "correct_answer": "Vacuole",
        "wrong_answers": ["Mitochondrion", "Nucleus", "Endoplasmic reticulum"],
        "score": 0
    },
    
    
      
]

Biology_ph = [
    "Dive into the magical world of cells and discover the secret dance of life!","Explore the jungle of DNA, where each gene is like a colorful treasure waiting to be found!",
    "Biology is like a playful puzzle – let's piece together the wonders of living organisms!","Embark on a thrilling adventure through the ecosystems, where every creature has its own story!",
    "Unleash your inner scientist and watch as the mysteries of Biology unfold like a cheerful storybook!","Get ready for a Bio-party where cells mingle, genes groove, and nature throws the happiest surprises!"
]

total_questions = len(Biology_questions)
print(f"{SL}created a total of {total_questions} questions for Biology questions.{SL}")



total_questions = len(Biology_questions + Anatomy_questions)
print(f"{SL}created a total of {total_questions} questions in this test for all of the objects.{SL}")