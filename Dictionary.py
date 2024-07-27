monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions)
print(monthConversions["Nov"])
print(monthConversions["Feb"])
print(monthConversions.get("Riz", "Not a valid key"))
print(monthConversions.get("Riz"))
