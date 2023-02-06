# AirBnB clone - The console

This project is a school exercice in Python. This is the first step towards building our first full web application: the AirBnB clone.

<ul>
<li>Stephen Nderitu</li>

</ul>

We have to do 11 mandatory tasks (0 to 10) and 7 advanced tasks (11 to 17).
</br>
</br>

## Requirements
</br>

### Python Scripts

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
</br>

### Python Unit Tests

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/QX7d4D__xhOJIGIWZBp39g" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project</li>
<li>e.g., For <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>e.g., For <code>models/user.py</code>, unit tests must be in: <code>tests/test_models/test_user.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>
</br>

### Execution

<p>Your shell should work like this in interactive mode:</p>

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>

<p>But also in non-interactive mode: (like the Shell project in C)</p>

<pre><code>$ echo &quot;help&quot; | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>
</br>

## Tasks
</br>

0. README, AUTHORS

Write a README.md and Authors file
</br>
</br>

1. Be Pycodestyle compliant!

beautiful code that passes the pycodestyle checks :)
</br>
</br>

2. Unittests

All your files, classes, functions must be tested with unit tests
</br>
</br>

3. BaseModel

Write a class BaseModel that defines all common attributes/methods for other classes :

Public instance attributes:

<ul>
<li>id</li>
<li>created_at</li>
<li>updated_at</li>
</ul>
</br>

<ul>
<li>__str__</li>
</ul>
</br>

Public instance methods
<ul>
<li>save(self)</li>
<li>to_dict(self)</li>
</ul>
</br>
</br>

4. Create BaseModel from dictionary

Update models/base_model.py

<ul>
<li>__init__(self, *args, **kwargs)</li>
</ul>
</br>
</br>

5. Store first object

Manage the serialization/deserialization of an instance into/from a json file (file.json)

Private class attributes
<ul>
<li><code>__file_path</code> : path to the JSON file</li>
<li><code>__objects</code> : dictionary store all objects by <class name>.id</li>
</ul>
</br>
Public instance methods
<ul>
<li><code>all(self)</code> : returns the dictionary __objects</li>
<li><code>new(self, obj)</code> : sets in __objects the obj with key <obj class name>.id</li>
<li><code>save(self)</code> : serializes __objects to the JSON file</li>
<li><code>reload(self)</code> : deserializes the JSON file to __objects (only if the JSON file</li>
</ul>
</br>
</br>

6. Console 0.0.1

program called console.py that contains the entry point of the command interpreter

The command interpreter implement:
<ul>
<li><code>quit</code> : exit the program</li>
<li><code>EOF</code> : exit the program</li>
<li><code>help</code> : print all documentation of commands</li>
</ul>
</br>
</br>

7. Console 0.1

Update the command interpreter (console.py) to have these commands:

<ul>
<li><code>create</code> : Create command to create an instance of a class</li>
<li><code>show</code> : Show command to print the string representation of an instance \
based on the class name and id</li>
<li><code>destroy</code> : Destroy command to delete an instance \
based on the class name and id</li>
<li><code>update</code> : Update command to update an instance based on the class name \
and id by adding or updating attribute</li>
</ul>

#### Example
<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn&#39;t exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
[&quot;[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&#39;created_at&#39;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &#39;id&#39;: &#39;49faff9a-6318-451f-87b6-910505c55907&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}&quot;]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&#39;created_at&#39;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &#39;id&#39;: &#39;49faff9a-6318-451f-87b6-910505c55907&#39;, &#39;updated_at&#39;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name &quot;Betty&quot;
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&#39;first_name&#39;: &#39;Betty&#39;, &#39;id&#39;: &#39;49faff9a-6318-451f-87b6-910505c55907&#39;, &#39;created_at&#39;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &#39;updated_at&#39;: datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
[&quot;[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {&#39;id&#39;: &#39;2dd6ef5c-467c-4f82-9521-a772ea7d84e9&#39;, &#39;created_at&#39;: datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), &#39;updated_at&#39;: datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}&quot;, &quot;[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {&#39;first_name&#39;: &#39;Betty&#39;, &#39;id&#39;: &#39;49faff9a-6318-451f-87b6-910505c55907&#39;, &#39;created_at&#39;: datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), &#39;updated_at&#39;: datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}&quot;]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) 
</code></pre>
</br>
</br>

8. First User

class User that inherits from BaseModel:
<ul>
<li><code>email</code></li>
<li><code>password</code></li>
<li><code>first_name</code></li>
<li><code>last_name</code></li>
</ul>
</br>
</br>

9. More classes!

class State that inherits from BaseModel:
<ul>
<li><code>name</code></li>
</ul>
</br>

class City that inherits from BaseModel:
<ul>
<li><code>state_id</code></li>
<li><code>name</code></li>
</ul>
</br>

class Amenity that inherits from BaseModel:
<ul>
<li><code>name</code></li>
</ul>
</br>

class Place that inherits from BaseModel:
<ul>
<li><code>city_id</code></li>
<li><code>user_id</code></li>
<li><code>name</code></li>
<li><code>description</code></li>
<li><code>number_rooms</code></li>
<li><code>number_bathrooms</code></li>
<li><code>max_guest</code></li>
<li><code>price_by_night</code></li>
<li><code>latitude</code></li>
<li><code>longitude</code></li>
<li><code>amenity_ids</code></li>
</ul>
</br>

class Review that inherits from BaseModel:
<ul>
<li><code>place_id</code></li>
<li><code>user_id</code></li>
<li><code>text</code></li>
</ul>
</br>

class State that inherits from BaseModel:
<ul>
<li><code>name</code></li>
</ul>
</br>

class State that inherits from BaseModel:
<ul>
<li><code>name</code></li>
</ul>
</br>

class State that inherits from BaseModel:
<ul>
<li><code>name</code></li>
</ul>
</br>
</br>

10. Console 1.0

Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
</br>
</br>

11. All instances by class name

Update your command interpreter (console.py) to retrieve all instances of a class by using: \<class name>.all()

#### Example
<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {&#39;first_name&#39;: &#39;Betty&#39;, &#39;last_name&#39;: &#39;Bar&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), &#39;password&#39;: &#39;63a9f0ea7bb98050796b649e85481845&#39;, &#39;email&#39;: &#39;airbnb@mail.com&#39;, &#39;id&#39;: &#39;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&#39;}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&#39;first_name&#39;: &#39;Betty&#39;, &#39;last_name&#39;: &#39;Bar&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &#39;password&#39;: &#39;b9be11166d72e9e3ae7fd407165e4bd2&#39;, &#39;email&#39;: &#39;airbnb@mail.com&#39;, &#39;id&#39;: &#39;38f22813-2753-4d42-b37c-57a17f1e4f88&#39;}]
(hbnb) 
</code></pre>
</br>
</br>

12. Count instances

Update your command interpreter (console.py) to retrieve the number of instances of a class: \<class name>.count()

#### Example
<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) 
</code></pre>
</br>
</br>

13. Show

Update your command interpreter (console.py) to retrieve an instance based on its ID: \<class name>.show(\<id>)

#### Example
<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show(&quot;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;)
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {&#39;first_name&#39;: &#39;Betty&#39;, &#39;last_name&#39;: &#39;Bar&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), &#39;password&#39;: &#39;63a9f0ea7bb98050796b649e85481845&#39;, &#39;email&#39;: &#39;airbnb@mail.com&#39;, &#39;id&#39;: &#39;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&#39;}
(hbnb) User.show(&quot;Bar&quot;)
** no instance found **
(hbnb) 
</code></pre>
</br>
</br>

14. Destroy

Update your command interpreter (console.py) to destroy an instance based on his ID: \<class name>.destroy(\<id>)

#### Example
<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy(&quot;246c227a-d5c1-403d-9bc7-6a47bb9f0f68&quot;)
(hbnb) User.count()
1
(hbnb) User.destroy(&quot;Bar&quot;)
** no instance found **
(hbnb) 
</code></pre>
</br>
</br>

15. Update

Update your command interpreter (console.py) to update an instance based on his ID: \<class name>.update(\<id>, \<attribute name>, \<attribute value>)

#### Example
<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&#39;first_name&#39;: &#39;Betty&#39;, &#39;last_name&#39;: &#39;Bar&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), &#39;password&#39;: &#39;b9be11166d72e9e3ae7fd407165e4bd2&#39;, &#39;email&#39;: &#39;airbnb@mail.com&#39;, &#39;id&#39;: &#39;38f22813-2753-4d42-b37c-57a17f1e4f88&#39;}
(hbnb)
(hbnb) User.update(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;first_name&quot;, &quot;John&quot;)
(hbnb) User.update(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, &quot;age&quot;, 89)
(hbnb)
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&#39;age&#39;: 89, &#39;first_name&#39;: &#39;John&#39;, &#39;last_name&#39;: &#39;Bar&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), &#39;password&#39;: &#39;b9be11166d72e9e3ae7fd407165e4bd2&#39;, &#39;email&#39;: &#39;airbnb@mail.com&#39;, &#39;id&#39;: &#39;38f22813-2753-4d42-b37c-57a17f1e4f88&#39;}
(hbnb) 
</code></pre>
</br>
</br>

16. Update from dictionary

Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: \<class name>.update(\<id>, \<dictionary representation>)

#### Example
<pre><code>guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&#39;age&#39;: 23, &#39;first_name&#39;: &#39;Bob&#39;, &#39;last_name&#39;: &#39;Bar&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 15, 32, 299055), &#39;password&#39;: &#39;b9be11166d72e9e3ae7fd407165e4bd2&#39;, &#39;email&#39;: &#39;airbnb@mail.com&#39;, &#39;id&#39;: &#39;38f22813-2753-4d42-b37c-57a17f1e4f88&#39;}
(hbnb) 
(hbnb) User.update(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;, {&#39;first_name&#39;: &quot;John&quot;, &quot;age&quot;: 89})
(hbnb) 
(hbnb) User.show(&quot;38f22813-2753-4d42-b37c-57a17f1e4f88&quot;)
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {&#39;age&#39;: 89, &#39;first_name&#39;: &#39;John&#39;, &#39;last_name&#39;: &#39;Bar&#39;, &#39;created_at&#39;: datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), &#39;updated_at&#39;: datetime.datetime(2017, 9, 28, 21, 17, 10, 788143), &#39;password&#39;: &#39;b9be11166d72e9e3ae7fd407165e4bd2&#39;, &#39;email&#39;: &#39;airbnb@mail.com&#39;, &#39;id&#39;: &#39;38f22813-2753-4d42-b37c-57a17f1e4f88&#39;}
(hbnb) 
</code></pre>
</br>
</br>

17. Unittests for the Console!

Write all unittests for console.py, all features!
</br>
</br>
