 #    # This is a sample Python script.
 #
 #    # Press Shift+F10 to execute it or replace it with your code.
 #    # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
 #
 #
 #    def print_hi(name):
 #        # Use a breakpoint in the code line below to debug your script.
 #        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
 #
 #
 #    # Press the green button in the gutter to run the script.
 #    if __name__ == '__main__':
 #        print_hi('PyCharm')
 #
 #    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
 #
 #    # 1. Sabse upar yeh line zaroor honi chahiye (agar pehle se nahi hai toh daal dein)
 #    from flask import Flask, render_template
 #
 #    app = Flask(__name__)
 #
 #
 #    @app.route('/')
 #    def home():
 #        places = [
 #            {"id": 1, "name": "Maldives", "img": "/static/images/maldives.jpg", "cat": "Influencer Famous",
 #             "price": "₹2,50,000"},
 #            {"id": 2, "name": "Meghalaya Root Bridges", "img": "/static/images/meghalaya.jpg", "cat": "Untouched Offbeat",
 #             "price": "₹40,000"},
 #            {"id": 3, "name": "Spiti Valley Expedition", "img": "/static/images/spiti.jpg", "cat": "Untouched Offbeat",
 #             "price": "₹55,000"}
 #        ]
 #
 #        # 👇 2. YAHAN THEEK KIYA HAI 👇
 #        return render_template('index.html', places=places)
 #
 #