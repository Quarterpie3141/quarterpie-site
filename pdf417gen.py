from pdf417 import encode, render_svg

def text_to_pdf417_svg(text, filename="barcode.svg", scale=3):
    # Encode the text
    codes = encode(text, security_level=2)
    
    # Render the barcode
    svg_tree = render_svg(codes, scale=scale, ratio=3, color="black")
    
    # Get the root <svg> element and apply crispEdges
    root = svg_tree.getroot()
    root.set("shape-rendering", "crispEdges")
    
    # Save the file
    svg_tree.write(filename)
    print(f"Barcode successfully saved to {filename}")

# Usage
text_data = "Everyone has the right to freedom of thought, conscience and religion"
text_to_pdf417_svg(text_data)