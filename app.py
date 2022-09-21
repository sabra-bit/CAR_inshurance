import streamlit as st
from streamlit_option_menu import option_menu
from algo1SVM import SVM
from algo2DecisionTree import DST
from algo2LG import LG
from algo2XGBOOST import XGB
import pickle
from datetime import date

todays_date = date.today()
st.title("Comparing")



selected = option_menu(
    menu_title= "Algorithms",
    options =['logistic regression' , 'decision tree' , 'XGBoost' , 'SVM'],
    orientation= "horizontal"
    )

if selected == 'logistic regression':
    btn = st.button("train logistic regression")
    if btn:
        acc = LG()
        st.warning("accuracy = %.2f"%(acc*100)  +'%')
    
    age = st.number_input('Age', 22,100)
    jop = st.selectbox('Jop',['Employee','PrivateJob'])
    if jop == 'Employee':
        jop = 0
    else:
        jop = 1
    Qualification = st.selectbox('Qualification',['HigherEdu','MiddleEdu','BasicEdu'])
    if Qualification == 'HigherEdu':
        Qualification = 0
    if Qualification == 'MiddleEdu':
        Qualification = 1
    else:
        Qualification = 2

    hstat = st.selectbox('Hstatus',['GoodHealth','Stable','ChronicDiseases'])
    if hstat == 'GoodHealth':
        hstat = 0
    if hstat == 'Stable':
        hstat = 1
    else:
        hstat = 2
    ManufacturingYear = int(st.date_input('ManufacturingYear').strftime('%Y'))
    

    cc = st.number_input('C.C', 300,6000)
    
    if ManufacturingYear == int(todays_date.year):
        vage = 1
    else:
        vage = int(todays_date.year) - ManufacturingYear
        
    

    use = st.selectbox('Use',['Commercial','Private'])
    if use == 'Commercial':
        use = 0
    else:
        use = 1
    vMileg = st.number_input('V Milege', 0,9999990)
    premium = st.number_input('Premium', 0,9999990)
    tclaim = st.selectbox('Tclaim',['High','Medium','Low'])
    if tclaim == 'High':
        tclaim = 0
    if tclaim == 'Medium':
        tclaim = 1
    else:
        tclaim = 2
    Insurance = st.number_input('InsuranceVal', 0,999999990)
    # st.selectbox('Jop',['Employee','PrivateJob'])


    if st.button('Predict'):

        pickle_in = open("CarData_LG.pickle", "rb")
        orical = pickle.load(pickle_in)

        predicted= orical.predict([[int(age),int(jop),int(Qualification),int(hstat),int(ManufacturingYear),int(cc),int(vage),int(use),int(vMileg),int(premium),int(tclaim),int(Insurance)]])
        
        if predicted == 1:
            st.error("rejection")
        else:
            st.success("acception")

if selected == 'decision tree':
    btn = st.button("train decision tree")
    if btn:
        acc = DST()
        st.warning("accuracy = %.2f"%(acc*100)  +'%')
    age = st.number_input('Age', 22,100)
    jop = st.selectbox('Jop',['Employee','PrivateJob'])
    if jop == 'Employee':
        jop = 0
    else:
        jop = 1
    Qualification = st.selectbox('Qualification',['HigherEdu','MiddleEdu','BasicEdu'])
    if Qualification == 'HigherEdu':
        Qualification = 0
    if Qualification == 'MiddleEdu':
        Qualification = 1
    else:
        Qualification = 2

    hstat = st.selectbox('Hstatus',['GoodHealth','Stable','ChronicDiseases'])
    if hstat == 'GoodHealth':
        hstat = 0
    if hstat == 'Stable':
        hstat = 1
    else:
        hstat = 2
    ManufacturingYear = int(st.date_input('ManufacturingYear').strftime('%Y'))
    

    cc = st.number_input('C.C', 300,6000)
    
    if ManufacturingYear == int(todays_date.year):
        vage = 1
    else:
        vage = int(todays_date.year) - ManufacturingYear
        
    

    use = st.selectbox('Use',['Commercial','Private'])
    if use == 'Commercial':
        use = 0
    else:
        use = 1
    vMileg = st.number_input('V Milege', 0,9999990)
    premium = st.number_input('Premium', 0,9999990)
    tclaim = st.selectbox('Tclaim',['High','Medium','Low'])
    if tclaim == 'High':
        tclaim = 0
    if tclaim == 'Medium':
        tclaim = 1
    else:
        tclaim = 2
    Insurance = st.number_input('InsuranceVal', 0,999999990)
    # st.selectbox('Jop',['Employee','PrivateJob'])


    if st.button('Predict'):

        pickle_in = open("CarData_DT.pickle", "rb")
        orical = pickle.load(pickle_in)

        predicted= orical.predict([[int(age),int(jop),int(Qualification),int(hstat),int(ManufacturingYear),int(cc),int(vage),int(use),int(vMileg),int(premium),int(tclaim),int(Insurance)]])
        
        if predicted == 1:
            st.error("rejection")
        else:
            st.success("acception")

    
if selected == 'XGBoost':
    btn = st.button("train XGBoost")
    if btn:
        acc = XGB()
        st.warning("accuracy = %.2f"%(acc*100)  +'%')
    
    age = st.number_input('Age', 22,100)
    jop = st.selectbox('Jop',['Employee','PrivateJob'])
    if jop == 'Employee':
        jop = 0
    else:
        jop = 1
    Qualification = st.selectbox('Qualification',['HigherEdu','MiddleEdu','BasicEdu'])
    if Qualification == 'HigherEdu':
        Qualification = 0
    if Qualification == 'MiddleEdu':
        Qualification = 1
    else:
        Qualification = 2

    hstat = st.selectbox('Hstatus',['GoodHealth','Stable','ChronicDiseases'])
    if hstat == 'GoodHealth':
        hstat = 0
    if hstat == 'Stable':
        hstat = 1
    else:
        hstat = 2
    ManufacturingYear = int(st.date_input('ManufacturingYear').strftime('%Y'))
    

    cc = st.number_input('C.C', 300,6000)
    
    if ManufacturingYear == int(todays_date.year):
        vage = 1
    else:
        vage = int(todays_date.year) - ManufacturingYear
        
    

    use = st.selectbox('Use',['Commercial','Private'])
    if use == 'Commercial':
        use = 0
    else:
        use = 1
    vMileg = st.number_input('V Milege', 0,9999990)
    premium = st.number_input('Premium', 0,9999990)
    tclaim = st.selectbox('Tclaim',['High','Medium','Low'])
    if tclaim == 'High':
        tclaim = 0
    if tclaim == 'Medium':
        tclaim = 1
    else:
        tclaim = 2
    Insurance = st.number_input('InsuranceVal', 0,999999990)
    # st.selectbox('Jop',['Employee','PrivateJob'])


    if st.button('Predict'):

        pickle_in = open("CarData_XGBOOST.pickle", "rb")
        orical = pickle.load(pickle_in)

        predicted= orical.predict([[int(age),int(jop),int(Qualification),int(hstat),int(ManufacturingYear),int(cc),int(vage),int(use),int(vMileg),int(premium),int(tclaim),int(Insurance)]])
        
        if predicted == 1:
            st.error("rejection")
        else:
            st.success("acception")

    
if selected == 'SVM':
    btn = st.button("train SVM")
    if btn:
        acc = SVM()
        st.warning("accuracy = %.2f"%(acc*100)  +'%')
    
    age = st.number_input('Age', 22,100)
    jop = st.selectbox('Jop',['Employee','PrivateJob'])
    if jop == 'Employee':
        jop = 0
    else:
        jop = 1
    Qualification = st.selectbox('Qualification',['HigherEdu','MiddleEdu','BasicEdu'])
    if Qualification == 'HigherEdu':
        Qualification = 0
    if Qualification == 'MiddleEdu':
        Qualification = 1
    else:
        Qualification = 2

    hstat = st.selectbox('Hstatus',['GoodHealth','Stable','ChronicDiseases'])
    if hstat == 'GoodHealth':
        hstat = 0
    if hstat == 'Stable':
        hstat = 1
    else:
        hstat = 2
    ManufacturingYear = int(st.date_input('ManufacturingYear').strftime('%Y'))
    

    cc = st.number_input('C.C', 300,6000)
   
    if ManufacturingYear == int(todays_date.year):
        vage = 1
    else:
        vage = int(todays_date.year) - ManufacturingYear
        
    

    use = st.selectbox('Use',['Commercial','Private'])
    if use == 'Commercial':
        use = 0
    else:
        use = 1
    vMileg = st.number_input('V Milege', 0,9999990)
    premium = st.number_input('Premium', 0,9999990)
    tclaim = st.selectbox('Tclaim',['High','Medium','Low'])
    if tclaim == 'High':
        tclaim = 0
    if tclaim == 'Medium':
        tclaim = 1
    else:
        tclaim = 2
    Insurance = st.number_input('InsuranceVal', 0,999999990)
    # st.selectbox('Jop',['Employee','PrivateJob'])


    if st.button('Predict'):

        pickle_in = open("CarData_DT.pickle", "rb")
        orical = pickle.load(pickle_in)

        predicted= orical.predict([[int(age),int(jop),int(Qualification),int(hstat),int(ManufacturingYear),int(cc),int(vage),int(use),int(vMileg),int(premium),int(tclaim),int(Insurance)]])
        
        if predicted == 1:
            st.error("rejection")
        else:
            st.success("acception")
