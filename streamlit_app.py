import streamlit as st
import streamlit.components.v1 as components

# p5.jsスケッチをHTMLで埋め込む
p5_code = """
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
    <script>
      function setup() {
        createCanvas(400, 400);
        background(220);
      }
    
      function draw() {
        if(key === 'Enter'){
            fill(100, 150, 255);
            ellipse(mouseX, mouseY, 50, 50);
        }
      }
    </script>
  </head>
  <body>
  </body>
</html>
"""

st.title("Streamlit + p5.js デモ")
components.html(p5_code, height=450)
