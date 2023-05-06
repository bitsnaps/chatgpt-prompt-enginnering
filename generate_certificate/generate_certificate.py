import drawsvg as draw

# Create the drawing with the desired dimensions
d = draw.Drawing(600, 400, origin='center')

# Add the DeepLearning.AI logo (assuming you have the SVG path data)
#logo_path = "M0,0 L10,0 10,10 0,10z"  # Replace this with the actual path data of the logo
logo_path = "m18.85992,36.81782c-9.86376,0 -17.85992,-7.65992 -17.85992,-17.10891c0,-9.44899 7.99616,-17.10891 17.85992,-17.10891c9.86376,0 17.85992,7.65992 17.85992,17.10891c0,9.44899 -7.99616,17.10891 -17.85992,17.10891zm-0.03415,-6.93976c7.43083,0 13.45471,-5.81415 13.45471,-12.98628c0,-7.17212 -6.02388,-12.98628 -13.45471,-12.98628c-7.43082,0 -13.4547,5.81416 -13.4547,12.98628c0,7.17213 6.02388,12.98628 13.4547,12.98628zm-0.06829,-2.67971c-6.67643,0 -12.08875,-5.07585 -12.08875,-11.33723c0,-6.26138 5.41232,-11.33723 12.08875,-11.33723c6.67642,0 12.08874,5.07585 12.08874,11.33723c0,6.26138 -5.41232,11.33723 -12.08874,11.33723zm-0.03415,-4.6036c5.03561,0 9.11778,-3.84534 9.11778,-8.58881c0,-4.74347 -4.08217,-8.58881 -9.11778,-8.58881c-5.03561,0 -9.11778,3.84534 -9.11778,8.58881c0,4.74347 4.08217,8.58881 9.11778,8.58881zm0.06829,-2.13002c-3.97945,0 -7.20543,-3.24547 -7.20543,-7.24896c0,-4.00349 3.22598,-7.24896 7.20543,-7.24896c3.97946,0 7.20544,3.24547 7.20544,7.24896c0,4.00349 -3.22598,7.24896 -7.20544,7.24896zm-0.23904,-6.25266c1.96144,0 3.5515,-1.66119 3.5515,-3.71036c0,-2.04918 -1.59006,-3.71037 -3.5515,-3.71037c-1.96144,0 -3.55149,1.66119 -3.55149,3.71037c0,2.04917 1.59005,3.71036 3.55149,3.71036z"
logo = draw.Path(logo_path, fill='#FF3A3E', transform='translate(-250, 150) scale(0.5)')
d.append(logo)

# Add the certificate title
d.append(draw.Text("Certificate of Completion", 30, 0, 100, center=0.5))

# Add the course title
d.append(draw.Text("Prompt Engineering", 25, 0, 50, center=0.5))

# Add the recipient's name
d.append(draw.Text("John Doe", 20, 0, 0, center=0.5))

# Add the issuer name
d.append(draw.Text("Delivered by DeepLearning.AI", 15, 0, -50, center=0.5))

# Save the certificate as an SVG file
d.save_svg("certificate.svg")


