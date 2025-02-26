import streamlit as st

# Set up the page
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter")

# Define conversion functions

def convert_length(value, from_unit, to_unit):
    # Conversion factors relative to 1 meter
    factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
    }
    # Convert the input value to meters, then to the target unit
    meters = value * factors[from_unit]
    result = meters / factors[to_unit]
    return result

def convert_weight(value, from_unit, to_unit):
    # Conversion factors relative to 1 kilogram
    factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    }
    kilograms = value * factors[from_unit]
    result = kilograms / factors[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# Sidebar to choose conversion type
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    value = st.number_input("Enter value to convert", value=1.0)
    from_unit = st.selectbox("From", units, key="length_from")
    to_unit = st.selectbox("To", units, key="length_to")
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    value = st.number_input("Enter value to convert", value=1.0)
    from_unit = st.selectbox("From", units, key="weight_from")
    to_unit = st.selectbox("To", units, key="weight_to")
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter temperature", value=0.0)
    from_unit = st.selectbox("From", units, key="temp_from")
    to_unit = st.selectbox("To", units, key="temp_to")
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
