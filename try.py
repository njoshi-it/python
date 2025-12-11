
import json

'''
import openai

# Set your API key
openai.api_key = "YOUR_API_KEY_HERE"

# Call the GPT model
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain virtual environments in Python."}
    ]
)

# Print the AI's response
print(response.choices[0].message.content)
'''
'''
class Person:
    def __init__(self, name, age):  #object constructor
        self.name = name
        self.age = age

    def __str__(self):
            return f"{self.name} is {self.age} years old."

    def __repr__(self):
            return f"(name={self.name})"


p = [Person("John", 36)]
print(p)

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)  # append method for list
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)  # remove method for list
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
my_playlist.remove_song("Bohemian Rhapsody")
my_playlist.show_songs()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):  #inheritance
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
  def printname(self):
  	super().printname()  #method overriding
  	print("hello override")  #additional functionality

x = Student("Mike", "Olsen")
x.printname()
y= Student("ram", "tam")
y.printname()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # Private property
  def fnc(self):  # Public method to access private property
  	return self.__age

p1 = Person("Emil", 25)
print(p1.name)  
print(p1.fnc())  # Accessing private property via public method
print(p1._Person__age)  # Accessing private property using name mangling

class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()  # Creating instance of inner class
inner.display()


class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):  # Access outer class instance
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()
'''

with open("fast.py", "r") as f:  #reading file using with to close file automatically
    for line in f:
        print(line.strip())

with open("fast.py") as inp, open("output.py", "w") as out:  #opening two files
    for line in inp:
        out.write(line.upper()) #reading from inp and writing to out in uppercase

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)

