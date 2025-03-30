import streamlit as st

# Distance converter function
def distance_convertor(from_unit, to_unit, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Temperature converter function
def temperature_convertor(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result

# Weight converter function
def weight_convertor(from_unit, to_unit, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Pressure converter function
def pressure_convertor(from_unit, to_unit, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] / units[to_unit]
    return result

# Streamlit UI elements to select conversion type and input values
st.title("Unit Converter")

# Choose conversion type
conversion_type = st.selectbox("Choose Conversion Type:", ["Distance", "Temperature", "Weight", "Pressure"])

# Input value
value = st.number_input("Enter value to convert:", value=0.0)

if conversion_type == "Distance":
    from_unit = st.selectbox("From Unit (Distance)", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To Unit (Distance)", ["Meters", "Kilometers", "Feet", "Miles"])
    if value:
        result = distance_convertor(from_unit, to_unit, value)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit (Temperature)", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To Unit (Temperature)", ["Celsius", "Fahrenheit"])
    if value:
        result = temperature_convertor(from_unit, to_unit, value)
        st.write(f"{value}° {from_unit} = {result:.3f}° {to_unit}")

elif conversion_type == "Weight":
    from_unit = st.selectbox("From Unit (Weight)", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To Unit (Weight)", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if value:
        result = weight_convertor(from_unit, to_unit, value)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Pressure":
    from_unit = st.selectbox("From Unit (Pressure)", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("To Unit (Pressure)", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    if value:
        result = pressure_convertor(from_unit, to_unit, value)
        st.write(f"{value} {from_unit} = {result:.2f} {to_unit}")

# ✅ Footer
st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px; color: #555;'>🚀 This application is created by <b>Muhammad Yameen Saleem</b></p>", unsafe_allow_html=True)

