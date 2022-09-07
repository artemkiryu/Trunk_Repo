message = input(">")
words = message.split(" ")  # space to separate your text in output
emojis = {
    ":)": "😊",
    ":(": "☹",
    ":|": "😐"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
