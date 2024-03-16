import streamlit as st
import subprocess

# Main Streamlit app



def tab1():
    st.title("Welcome to our SDTM World!")
    st.subheader('DataCartographers')
    # st.image('https://www.prospection.com/wp-content/uploads/2021/06/Data-Mapping.jpg')
    # st.markdown('<h1 class="orange-line">DataCartographers</h1>',unsafe_allow_html=True)
    st.write("1. Mahesh Wankhede")
    st.write("2. Prathmesh Shewale")
    st.write("3. Rahul Bunage")
    st.write("4. Poonam Phalke")

def tab2():
    st.title('RAW TO SDTM FORMAT CONVERSION')
    st.write("Please select the domain you want to convert from raw to SDTM:")

    domain = ['DM', 'AE', 'MH', 'CM', 'SV']
    domain = st.radio("Select Domain", domain)
    # Define the Python script file for each domain
    domain_scripts = {'DM': 'DM.py', 'AE': 'AE.py','MH': 'MH.py','CM': 'CM.py','SV': 'SV.py'    }

    # Execute the selected domain script
    if st.button('Process'):
        if domain in domain_scripts:
            script_path = domain_scripts[domain]
            try:
                result = subprocess.check_output(["python", script_path], stderr=subprocess.STDOUT)
                print("Subprocess output:", result.decode("utf-8"))
                st.write(f"Executed {script_path}")
                st.write(result)
                return result
            except subprocess.CalledProcessError as e:
                print("Subprocess error:", e.output.decode("utf-8"))
            
        else:
            st.error("No script found for selected domain.")

def tab3():
    if st.button("Submit"):
        st.write("Submit button clicked!")

def main():
    st.sidebar.title("Navigation")
    tabs = ["Welcome", "DOMAINS", "SDTM"]
    current_tab = st.sidebar.radio("Go to", tabs)

    if current_tab == "Welcome":
        tab1()
    elif current_tab == "DOMAINS":
        tab2()
    elif current_tab == "SDTM":
        tab3()
    # Select domain
    # domain = st.selectbox('Select Domain:', ['DM', 'AE', 'MH', 'CM', 'SV'])
    # st.subheader("Domain Specific Files")
    # st.write("Please select the domain you want to convert from raw to SDTM:")

    # domain = ['DM', 'AE', 'MH', 'CM', 'SV']
    # domain = st.radio("Select Domain", domain)
    # # Define the Python script file for each domain
    # domain_scripts = {'DM': 'DM.py', 'AE': 'AE.py','MH': 'MH.py','CM': 'CM.py','SV': 'SV.py'    }

    # # Execute the selected domain script
    # if st.button('Process'):
    #     if domain in domain_scripts:
    #         script_path = domain_scripts[domain]
    #         try:
    #             result = subprocess.check_output(["python", script_path], stderr=subprocess.STDOUT)
    #             print("Subprocess output:", result.decode("utf-8"))
    #             st.write(f"Executed {script_path}")
    #             st.write(result)
    #             return result
    #         except subprocess.CalledProcessError as e:
    #             print("Subprocess error:", e.output.decode("utf-8"))
            
    #     else:
    #         st.error("No script found for selected domain.")

if __name__ == '__main__':
    main()
