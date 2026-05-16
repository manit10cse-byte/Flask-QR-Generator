from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_image = None
    
    if request.method == 'POST':
        # This grabs the link from your HTML search bar!
        link = request.form.get('link') 
        
        if link:
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            qr_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
            
    # THIS is the exact line that links Python to your index.html
    return render_template('index.html', qr_image=qr_image)

if __name__ == '__main__':
    app.run(debug=True)