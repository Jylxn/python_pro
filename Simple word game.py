letterhome = [
    "A Letter Home", """

Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm
moving to COUNTRY. The truth is, I've always been passionate about
PLURAL_NOUN, and COUNTRY is the best place in the world to build a
career around them. I'll need to start small-- At first, all I'll be 
allowed to do is to VERB near them, but when people see how ADJECTIVE 
I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my 
PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME""",
    [
        ["An occupation-", "OCCUPATION"],
        ["A country-", "COUNTRY"],
        ["A plural noun-", "PLURAL_NOUN"],
        ["A verb, like 'run,' 'eat,' ot 'think'-", "VERB"],
        ["An adjective, like 'beautiful,' 'smart,' or 'funny'-", "ADJECTIVE"],
        ["A personal item- ", "PERSONAL_ITEM"],
        ["A holiday, like Christmans or Labour day-", "HOLIDAY"],
        ["Your name-", "NAME"],
    ]
]

sale = [
    "A great sale", """ 
  
  SALE SALE SALE

  Today only: Buy NUMBER PLURAL_NOUN and get a free NOUN!

  Sign up for our exclusive METAL card and receive 50% off your
  first purchase !

  """,
    [["A number-", "NUMBER"], ["A plural noun-", "PLURAL_NOUN"],
     ["A noun-", "NOUN"], ["A metal-", "METAL"]]
]

showandtell = [
    "Show and Tell", """
  Have you seen my pet ANIMAL? It's the best -- No pet can VERB1 as 
  ADVERB as it can. It's NUMBER years old, and its name is NAME.You can 
  VERB2 it if you want, but be careful, because it might VERB3.
  """,
    [["An animal-", "ANIMAL"], ["A verb, like run, jump or cry-", "VERB1"],
     ["An adverb, like quickly or elegantly-", "ADVERB"],
     ["A number-", "NUMBER"], ["A name-", "NAME"],
     ["A transitive verb, like speak to,notice or touch -", "VERB2"],
     ["A verb, like run, jump or cry-", "VERB3"]]
]

stories = [letterhome, sale, showandtell]

print("Select a story:")
for index,story in enumerate(stories):
  title = story[0]
  print(str(index) + " - " + title)

selection = int(input("Choose a story: "))
story = stories[selection]
prosestring = story[1]
replacements = story[2]

for prompt, placeholder in replacements:
  userinput = input(prompt)
  prosestring = prosestring.replace(placeholder, userinput)
print(prosestring)