from flask import Flask, request, render_template_string
 
app = Flask(__name__)
 
@app.route('/')
def profile():
    return '''
<!DOCTYPE html>
<html>
<head>
<title>My Profile</title>
<style>
    body {
        background-color: lightblue;
        font-family: Arial, sans-serif;
        margin: 40px;
        padding: 20px;
    }
    h1 {
        color: darkblue;
        text-align: center;
    }
    .profile-photo {
        display: block;
        margin: 0 auto;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        border: 3px solid #333;
    }
    .intro {
        text-align: center;
        font-size: 18px;
        margin: 20px 0;
    }
    .highlight {
        font-weight: bold;
        color: darkgreen;
    }
    form {
        background: #fff;
        padding: 20px;
        border-radius: 10px;
        max-width: 400px;
        margin: 0 auto;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    input, textarea {
        width: 100%;
        padding: 10px;
        margin-top: 10px;
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    button {
        background-color: darkblue;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    button:hover {
        background-color: navy;
    }
</style>
<script>
    function sayHello() {
        const name = document.getElementById("helloName").value;
        if (name) {
            alert("Hello, " + name + "!");
        } else {
            alert("Please enter your name.");
        }
    }
</script>
</head>
<body>
 
<h1>Welcome to My Profile Page</h1>
 
<img src="static/Rajeshwari.jpg" class="profile-photo" alt="Profile photo of Rajeshwari">
 
<div class="intro">
    Hi, I'm <span class="highlight">Rajeshwari</span>. <br>
    I have completed my Graduation and I love <span class="highlight">singing, reading, and cooking</span>.
</div>
 
<form>
<label for="name">Name:</label>
<input type="text" id="name" name="name" required>
 
    <label for="email">Email:</label>
<input type="email" id="email" name="email" required>
 
    <label for="message">Message:</label>
<textarea id="message" name="message" rows="4" required></textarea>
 
    <button type="submit">Submit</button>
</form>
 
<br><br>
 
<div style="text-align: center;">
<input type="text" id="helloName" placeholder="Enter your name" />
<button onclick="sayHello()">Say Hello</button>
</div>
 
</body>
</html>
    '''
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)