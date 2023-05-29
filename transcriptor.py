from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return {
        "txt":"Quantum computing is a multidisciplinary field comprising aspects of computer science, physics, and mathematics that utilizes quantum mechanics to solve complex problems faster than on classical computers. The field of quantum computing includes hardware research and application development. Quantum computers are able to solve certain types of problems faster than classical computers by taking advantage of quantum mechanical effects, such as superposition and quantum interference. Some applications where quantum computers can provide such a speed boost include machine learning (ML), optimization, and simulation of physical systems. Eventual use cases could be portfolio optimization in finance or the simulation of chemical systems, solving problems that are currently impossible for even the most powerful supercomputers on the market."
    }
if __name__ == '__main__':
    app.run(debug=True)
