import streamlit as st
import streamlit.components.v1 as components

p5_code = """
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
    <script>
      let circles = [];

      function setup() {
        createCanvas(400, 400);
      }
    
      function draw() {
        background(220);
        for (let c of circles) {
          fill(c.color);
          ellipse(c.x, c.y, 40, 40);
        }
      }

      // キーが押されたとき
      function keyPressed() {
        if (keyCode === ENTER) {   // Enterキー判定
          circles.push({
            x: mouseX,
            y: mouseY,
            color: color(random(255), random(255), random(255))
          });
        }
      }
    </script>
  </head>
  <body>
  </body>
</html>
"""

st.title("Streamlit + p5.js デモ（Enterキーでマウス位置に円追加）")
components.html(p5_code, height=450)
