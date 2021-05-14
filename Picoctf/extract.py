# PYTHON3 SCRIPT 

import os

filename = "dolls.png"
extract_dir = "ext"
flag = 0
while flag == 0:
	print("\n== Extracting ==\n")
	os.system("unzip {} -d {}".format(filename,extract_dir))
	if os.path.exists(extract_dir+"/base_images"):
		os.chdir(extract_dir+"/base_images")
	else:
		os.chdir(extract_dir)
	for file in os.listdir():
		if file.endswith(".txt"):
			print("\n== FLAG: ")
			print(os.system("cat {}".format(file)))
			flag = 1
		else:
			filename = file
# Remove the folders
# os.system("rm -r /path/to/ext")
