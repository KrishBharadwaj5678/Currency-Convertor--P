import streamlit as st
import json
import requests

st.set_page_config(
    page_title="Currency Pulse",
    page_icon="bitcoin.png",
    menu_items={
        "About":"""Discover the power of accurate and timely currency conversions with CurrencyPulse. Experience the pulse of the global financial market with CurrencyPulse – your ultimate currency exchange hub."""
    }
)

st.markdown("## :orange[ Your Real-Time Currency Exchange Hub]")

amount=st.number_input("Amount",format="%d",min_value=1)

curr_from=st.selectbox("From",("AED - United Arab Emirates Dirham","AFN- Afghan Afghani","AMD - Armenia","ANG - Netherlands Antillean Guilder","AOA - Angolan Kwanza","ARS - Argentine Peso","AUD - Australian Dollar","AWG - Aruban Florin","AZN - Azerbaijani Manat","BAM - Bosnian Convertible Mark","BBD - Barbadian Dollar","BDT - Bangladeshi Taka","BGN - Bulgarian Lev","BHD - Bahraini Dinar","BIF - Burundian Franc","BMD - Bermudian Dollar","BND - Brunei Dollar","BOB - Bolivian Boliviano","BRL - Brazilian Real","BSD - Bahamian Dollar","BTC - Bitcoin","BTN - Bhutanese Ngultrum","BWP - Botswana Pula","BYN - Belarusian Ruble","BYR - Belarusian Ruble","BZD - Belize Dollar","CAD - Canadian Dollar","CDF - Congolese Franc","CHF - Swiss Franc","CLF - Unidad de Fomento ","CLP - Chilean Peso","CNY - Chinese Yuan Renminbi","COP - Colombian Peso","CRC - Costa Rican Colón","CUC - Cuban Convertible Peso","CUP - Cuban Peso","CVE - Cape Verdean Escudo","CZK - Czech Koruna","DJF - Djiboutian Franc","DKK - Danish Krone","DOP - Dominican Peso","DZD - Algerian Dinar","EGP - Egyptian Pound","ETB - Ethiopian Birr","EUR - Euro","FJD - Fijian Dollar","GBP - British Pound Sterling","GEL - Georgian Lari","GHS - Ghanaian Cedi","GMD - Gambian Dalasi","GNF - Guinean Franc","GTQ - Guatemalan Quetzal","GYD - Guyanese Dollar","HKD - Hong Kong Dollar","HNL - Honduran Lempira","HRK - Croatian Kuna","HTG - Haitian Gourde","HUF - Hungarian Forint","IDR - Indonesian Rupiah","ILS - Israeli New Shekel","INR - Indian Rupee","IQD - Iraqi Dinar","IRR - Iranian Rial","ISK - Icelandic Króna","JMD - Jamaican Dollar","JOD - Jordanian Dinar","JPY - Japanese Yen","KES - Kenyan Shilling","KGS - Kyrgyzstani Som","KHR - Cambodian Riel","KMF - Comorian Franc","KRW - South Korean Won","KWD - Kuwaiti Dinar","KYD - Cayman Islands Dollar","KZT - Kazakhstani Tenge","LAK - Lao Kip","LBP - Lebanese Pound","LKR - Sri Lankan Rupee","LRD - Liberian Dollar","LSL - Lesotho Loti","LTL - Lithuanian Litas","LVL - Latvian Lats","LYD - Libyan Dinar","MAD - Moroccan Dirham","MDL - Moldovan Leu","MGA - Malagasy Ariary","MKD - Macedonian Denar","MMK - Myanmar Kyat","MOP - Macanese Pataca","MRO - Mauritanian Ouguiya","MUR - Mauritian Rupee","MVR - Maldivian Rufiyaa","MWK - Malawian Kwacha","MXN - Mexican Peso","MYR - Malaysian Ringgit","MZN - Mozambican Metical","NAD - Namibian Dollar","NGN - Nigerian Naira","NIO - Nicaraguan Córdoba","NOK - Norwegian Krone","NPR - Nepalese Rupee","NZD - New Ze aland Dollar","OMR - Omani Rial","PAB - Panamanian Balboa","PEN - Peruvian Sol","PGK - Papua New Guinean Kina","PHP - Philippine Peso","PKR - Pakistani Rupee","PLN - Polish Złoty","PYG - Paraguayan Guarani","QAR - Qatari Riyal","RON - Romanian Leu","RSD - Serbian Dinar","RUB - Russian Ruble","RWF - Rwandan Franc","SAR - Saudi Riyal","SBD - Solomon Islands Dollar","SCR - Seychellois Rupee","SDG - Sudanese Pound","SEK - Swedish Krona","SGD - Singapore Dollar","SHP - Saint Helena Pound","SLL - Sierra Leonean Leone","SOS - Somali Shilling","SRD - Surinamese Dollar","STD - São Tomé and Príncipe Dobra","SVC - Salvadoran Colón","SZL - Swazi Lilangeni","THB - Thai Baht","TJS - Tajikistani Somoni","TMT - Turkmenistan Manat","TND - Tunisian Dinar","TOP - Tongan Pa'anga","TRY - Turkish Lira","TTD - Trinidad and Tobago Dollar","TWD - New Taiwan Dollar","TZS - Tanzanian Shilling","UAH - Ukrainian Hryvnia","UGX - Ugandan Shilling","USD - United States Dollar","UYU - Uruguayan Peso","UZS - Uzbekistan Som","VND - Vietnamese Dong","XAF - Central African CFA Franc","XCD - East Caribbean Dollar","XDR - Special Drawing Rights","XOF - West African CFA Franc","XPF - CFP Franc","YER - Yemeni Rial","ZAR - South African Rand","ZMK - Zambian Kwacha","ZMW - Zambian Kwacha","ZWL -  Zimbabwean Dollar (ZWL)")) 


curr_to=st.selectbox("To",("AED - United Arab Emirates Dirham","AFN- Afghan Afghani","AMD - Armenia","ANG - Netherlands Antillean Guilder","AOA - Angolan Kwanza","ARS - Argentine Peso","AUD - Australian Dollar","AWG - Aruban Florin","AZN - Azerbaijani Manat","BAM - Bosnian Convertible Mark","BBD - Barbadian Dollar","BDT - Bangladeshi Taka","BGN - Bulgarian Lev","BHD - Bahraini Dinar","BIF - Burundian Franc","BMD - Bermudian Dollar","BND - Brunei Dollar","BOB - Bolivian Boliviano","BRL - Brazilian Real","BSD - Bahamian Dollar","BTC - Bitcoin","BTN - Bhutanese Ngultrum","BWP - Botswana Pula","BYN - Belarusian Ruble","BYR - Belarusian Ruble","BZD - Belize Dollar","CAD - Canadian Dollar","CDF - Congolese Franc","CHF - Swiss Franc","CLF - Unidad de Fomento ","CLP - Chilean Peso","CNY - Chinese Yuan Renminbi","COP - Colombian Peso","CRC - Costa Rican Colón","CUC - Cuban Convertible Peso","CUP - Cuban Peso","CVE - Cape Verdean Escudo","CZK - Czech Koruna","DJF - Djiboutian Franc","DKK - Danish Krone","DOP - Dominican Peso","DZD - Algerian Dinar","EGP - Egyptian Pound","ETB - Ethiopian Birr","EUR - Euro","FJD - Fijian Dollar","GBP - British Pound Sterling","GEL - Georgian Lari","GHS - Ghanaian Cedi","GMD - Gambian Dalasi","GNF - Guinean Franc","GTQ - Guatemalan Quetzal","GYD - Guyanese Dollar","HKD - Hong Kong Dollar","HNL - Honduran Lempira","HRK - Croatian Kuna","HTG - Haitian Gourde","HUF - Hungarian Forint","IDR - Indonesian Rupiah","ILS - Israeli New Shekel","INR - Indian Rupee","IQD - Iraqi Dinar","IRR - Iranian Rial","ISK - Icelandic Króna","JMD - Jamaican Dollar","JOD - Jordanian Dinar","JPY - Japanese Yen","KES - Kenyan Shilling","KGS - Kyrgyzstani Som","KHR - Cambodian Riel","KMF - Comorian Franc","KRW - South Korean Won","KWD - Kuwaiti Dinar","KYD - Cayman Islands Dollar","KZT - Kazakhstani Tenge","LAK - Lao Kip","LBP - Lebanese Pound","LKR - Sri Lankan Rupee","LRD - Liberian Dollar","LSL - Lesotho Loti","LTL - Lithuanian Litas","LVL - Latvian Lats","LYD - Libyan Dinar","MAD - Moroccan Dirham","MDL - Moldovan Leu","MGA - Malagasy Ariary","MKD - Macedonian Denar","MMK - Myanmar Kyat","MOP - Macanese Pataca","MRO - Mauritanian Ouguiya","MUR - Mauritian Rupee","MVR - Maldivian Rufiyaa","MWK - Malawian Kwacha","MXN - Mexican Peso","MYR - Malaysian Ringgit","MZN - Mozambican Metical","NAD - Namibian Dollar","NGN - Nigerian Naira","NIO - Nicaraguan Córdoba","NOK - Norwegian Krone","NPR - Nepalese Rupee","NZD - New Ze aland Dollar","OMR - Omani Rial","PAB - Panamanian Balboa","PEN - Peruvian Sol","PGK - Papua New Guinean Kina","PHP - Philippine Peso","PKR - Pakistani Rupee","PLN - Polish Złoty","PYG - Paraguayan Guarani","QAR - Qatari Riyal","RON - Romanian Leu","RSD - Serbian Dinar","RUB - Russian Ruble","RWF - Rwandan Franc","SAR - Saudi Riyal","SBD - Solomon Islands Dollar","SCR - Seychellois Rupee","SDG - Sudanese Pound","SEK - Swedish Krona","SGD - Singapore Dollar","SHP - Saint Helena Pound","SLL - Sierra Leonean Leone","SOS - Somali Shilling","SRD - Surinamese Dollar","STD - São Tomé and Príncipe Dobra","SVC - Salvadoran Colón","SZL - Swazi Lilangeni","THB - Thai Baht","TJS - Tajikistani Somoni","TMT - Turkmenistan Manat","TND - Tunisian Dinar","TOP - Tongan Pa'anga","TRY - Turkish Lira","TTD - Trinidad and Tobago Dollar","TWD - New Taiwan Dollar","TZS - Tanzanian Shilling","UAH - Ukrainian Hryvnia","UGX - Ugandan Shilling","USD - United States Dollar","UYU - Uruguayan Peso","UZS - Uzbekistan Som","VND - Vietnamese Dong","XAF - Central African CFA Franc","XCD - East Caribbean Dollar","XDR - Special Drawing Rights","XOF - West African CFA Franc","XPF - CFP Franc","YER - Yemeni Rial","ZAR - South African Rand","ZMK - Zambian Kwacha","ZMW - Zambian Kwacha","ZWL -  Zimbabwean Dollar (ZWL)"))

btn=st.button("Convert")
if btn:
    froms=curr_from[0:3]
    to=curr_to[0:3]
    url="https://api.currencyapi.com/v3/latest?apikey=cur_live_aEYnv5Txd5gyTGdnNeCfH2ISM901x7BdUURwIKc3&currencies="+to+"&base_currency="+froms
    data=requests.get(url)
    raw=data.text
    main=json.loads(raw)
    currency=main["data"][to]["value"]
    st.write("<h4>" + str(amount) + " " + curr_from[6::1] + " = </h4>", unsafe_allow_html=True)
    st.write("<h3 style='color:#005EB5;'>" + "{:.5f}".format(currency*amount) + " " + curr_to[6::1] + "</h3>", unsafe_allow_html=True)