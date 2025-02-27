# import streamlit as st

# # Set up the page
# st.set_page_config(page_title="Unit Converter", layout="centered")
# st.title("Unit Converter")

# # Define conversion functions

# def convert_length(value, from_unit, to_unit):
#     # Conversion factors relative to 1 meter
#     factors = {
#         "Meter": 1,
#         "Kilometer": 1000,
#         "Centimeter": 0.01,
#         "Millimeter": 0.001,
#         "Mile": 1609.34,
#         "Yard": 0.9144,
#         "Foot": 0.3048,
#         "Inch": 0.0254,
#     }
#     # Convert the input value to meters, then to the target unit
#     meters = value * factors[from_unit]
#     result = meters / factors[to_unit]
#     return result

# def convert_weight(value, from_unit, to_unit):
#     # Conversion factors relative to 1 kilogram
#     factors = {
#         "Kilogram": 1,
#         "Gram": 0.001,
#         "Milligram": 1e-6,
#         "Pound": 0.453592,
#         "Ounce": 0.0283495,
#     }
#     kilograms = value * factors[from_unit]
#     result = kilograms / factors[to_unit]
#     return result

# def convert_temperature(value, from_unit, to_unit):
#     if from_unit == to_unit:
#         return value
#     if from_unit == "Celsius" and to_unit == "Fahrenheit":
#         return (value * 9/5) + 32
#     elif from_unit == "Fahrenheit" and to_unit == "Celsius":
#         return (value - 32) * 5/9
#     elif from_unit == "Celsius" and to_unit == "Kelvin":
#         return value + 273.15
#     elif from_unit == "Kelvin" and to_unit == "Celsius":
#         return value - 273.15
#     elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
#         return (value - 32) * 5/9 + 273.15
#     elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
#         return (value - 273.15) * 9/5 + 32

# # Sidebar to choose conversion type
# conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# if conversion_type == "Length":
#     units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
#     value = st.number_input("Enter value to convert", value=1.0)
#     from_unit = st.selectbox("From", units, key="length_from")
#     to_unit = st.selectbox("To", units, key="length_to")
#     if st.button("Convert"):
#         result = convert_length(value, from_unit, to_unit)
#         st.success(f"{value} {from_unit} = {result} {to_unit}")

# elif conversion_type == "Weight":
#     units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
#     value = st.number_input("Enter value to convert", value=1.0)
#     from_unit = st.selectbox("From", units, key="weight_from")
#     to_unit = st.selectbox("To", units, key="weight_to")
#     if st.button("Convert"):
#         result = convert_weight(value, from_unit, to_unit)
#         st.success(f"{value} {from_unit} = {result} {to_unit}")

# elif conversion_type == "Temperature":
#     units = ["Celsius", "Fahrenheit", "Kelvin"]
#     value = st.number_input("Enter temperature", value=0.0)
#     from_unit = st.selectbox("From", units, key="temp_from")
#     to_unit = st.selectbox("To", units, key="temp_to")
#     if st.button("Convert"):
#         result = convert_temperature(value, from_unit, to_unit)
#         st.success(f"{value} {from_unit} = {result} {to_unit}")
                                 




import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Unit Converter Pro",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .header {
        color: #2E86C1;
        text-align: center;
        padding: 1rem;
        font-size: 2.5rem;
        border-bottom: 2px solid #2E86C1;
        margin-bottom: 2rem;
    }
    .result-box {
        padding: 1.5rem;
        background: #EBF5FB;
        border-radius: 10px;
        margin-top: 1rem;
        border-left: 5px solid #2E86C1;
    }
    .unit-section {
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown('<h1 class="header">🔮 Unit Converter Pro</h1>', unsafe_allow_html=True)

# Conversion functions (optimized)
def convert_length(value, from_unit, to_unit):
    factors = {
        "📏 Meter": 1, "🚀 Kilometer": 1000, "📎 Centimeter": 0.01,
        "📌 Millimeter": 0.001, "🏁 Mile": 1609.34, "🏈 Yard": 0.9144,
        "👞 Foot": 0.3048, "📐 Inch": 0.0254
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    factors = {
        "⚖️ Kilogram": 1, "🥛 Gram": 0.001, "💊 Milligram": 1e-6,
        "🏋️ Pound": 0.453592, "🍗 Ounce": 0.0283495
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    converters = {
        ('🌡️ Celsius', '🌡️ Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('🌡️ Fahrenheit', '🌡️ Celsius'): lambda x: (x - 32) * 5/9,
        ('🌡️ Celsius', '🔥 Kelvin'): lambda x: x + 273.15,
        ('🔥 Kelvin', '🌡️ Celsius'): lambda x: x - 273.15,
        ('🌡️ Fahrenheit', '🔥 Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
        ('🔥 Kelvin', '🌡️ Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32
    }
    return converters.get((from_unit, to_unit), lambda x: x)(value)

# Sidebar with enhanced features
with st.sidebar:
    st.subheader("🔧 Conversion Settings")
    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["📏 Length", "⚖️ Weight", "🌡️ Temperature"],
        index=0
    )
    
    st.markdown("---")
    st.subheader("📚 Quick Reference")
    st.markdown("""
    - 1 Meter = 100cm
    - 1 Kilogram = 2.20462lbs
    - 0°C = 32°F
    """)

# Main conversion interface
with st.container():
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        value = st.number_input(
            "Enter value to convert",
            min_value=0.0,
            value=1.0,
            step=0.1,
            format="%.4f"
        )

    with col3:
        if st.button("🔄 Swap Units", use_container_width=True):
            st.session_state.from_unit, st.session_state.to_unit = (
                st.session_state.to_unit, st.session_state.from_unit
            )

# Conversion type handling
if "📏 Length" in conversion_type:
    units = ["📏 Meter", "🚀 Kilometer", "📎 Centimeter", "📌 Millimeter",
             "🏁 Mile", "🏈 Yard", "👞 Foot", "📐 Inch"]
elif "⚖️ Weight" in conversion_type:
    units = ["⚖️ Kilogram", "🥛 Gram", "💊 Milligram", "🏋️ Pound", "🍗 Ounce"]
else:
    units = ["🌡️ Celsius", "🌡️ Fahrenheit", "🔥 Kelvin"]

# Unit selection columns
col_from, col_to = st.columns(2)
with col_from:
    from_unit = st.selectbox(
        "From",
        units,
        key="from_unit",
        index=0
    )

with col_to:
    to_unit = st.selectbox(
        "To",
        units,
        key="to_unit",
        index=1
    )

# Conversion and result display
if st.button("✨ Convert Now!", type="primary", use_container_width=True):
    try:
        if "temperature" in conversion_type.lower():
            result = convert_temperature(value, from_unit, to_unit)
            # Validate temperature ranges
            if "kelvin" in from_unit.lower() and value < 0:
                st.error("❌ Temperature cannot be below absolute zero (0K)!")
                result = "N/A"
        else:
            result = convert_length(value, from_unit, to_unit) if "length" in conversion_type.lower() else convert_weight(value, from_unit, to_unit)
        
        if result != "N/A":
            st.markdown(f"""
            <div class="result-box">
                <h3 style="margin:0; color: #2E86C1">🎉 Conversion Result:</h3>
                <p style="font-size: 1.5rem; margin: 0.5rem 0">
                    {value:.4f} {from_unit.split()[-1]} = 
                    <strong>{result:.4f}</strong> {to_unit.split()[-1]}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"⚠️ Conversion error: {str(e)}")

# Additional features
st.markdown("---")
with st.expander("📖 Conversion Guides"):
    st.markdown("""
    **Length Conversion Tips:**
    - 1 inch = 2.54 centimeters
    - 1 mile = 1.609 kilometers
    
    **Weight Conversion Tips:**
    - 1 pound ≈ 0.4536 kilograms
    - 1 ounce ≈ 28.3495 grams
    
    **Temperature Formulas:**
    - °F = (°C × 9/5) + 32
    - K = °C + 273.15
    """)

