import streamlit as st
import re

st.set_page_config(page_title="Word & Vowel Counter", page_icon="📝")

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextArea > div > div > textarea {
        background-color: #ffffff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 15px 30px;
        font-size: 18px;
    }
    @keyframes slideIn {
        0% {
            transform: translateX(-100%);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }
    h1 {
        animation: slideIn 1s ease-out;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .metric-value {
        color: #4CAF50 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📝 Word & Vowel Counter")
st.write("Enter your text below to count words, sentences and vowels!")

# Text input area
text = st.text_area("Enter your text here:", height=200)

if st.button("Count!", use_container_width=True):
    if text:
        # Word count
        words = len(text.split())
        
        # Sentence count
        sentences = len(re.split(r'[.!?]+', text.strip()))
        
        # Vowel count
        vowels = len(re.findall(r'[aeiouAEIOU]', text))
        
        # Display counts in columns with custom styling
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
                <div style='text-align: center'>
                    <p>Words</p>
                    <p class='metric-value' style='font-size: 24px'>{words}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
                <div style='text-align: center'>
                    <p>Sentences</p>
                    <p class='metric-value' style='font-size: 24px'>{sentences}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
                <div style='text-align: center'>
                    <p>Vowels</p>
                    <p class='metric-value' style='font-size: 24px'>{vowels}</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Additional statistics
        st.write("### Text Statistics:")
        
        # Character count (excluding spaces)
        chars_no_space = len(text.replace(" ", ""))
        st.write(f"- Characters (excluding spaces): {chars_no_space}")
        
        # Character count (including spaces)
        chars_with_space = len(text)
        st.write(f"- Characters (including spaces): {chars_with_space}")
        
        # Average word length
        if words > 0:
            avg_word_length = chars_no_space / words
            st.write(f"- Average word length: {avg_word_length:.1f} characters")
        
        # Most common vowels
        vowel_counts = {}
        for vowel in 'aeiouAEIOU':
            count = text.count(vowel)
            if count > 0:
                vowel_counts[vowel] = count
        
        if vowel_counts:
            st.write("### Vowel Distribution:")
            for vowel, count in sorted(vowel_counts.items()):
                st.write(f"- '{vowel}': {count} times")
    else:
        st.info("Enter some text above to see the analysis! ✨")
