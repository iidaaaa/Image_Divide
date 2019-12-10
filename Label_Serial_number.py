import glob
import os
import shutil

input_path=r'\*.jpg'
output_path=r''


def main():
	i=1
	j=0
	#フォルダの中の.jpgが存在するまでjpgをfilesに代入
	files=glob.glob(input_path)
	for f in files:
		i1="{0:08d}".format(i)

		path_out=output_path+"\\"+str(i1) + ".jpg"
		#print(path_out)
		files1=str(f)
		#ファイル名変更　切り取り&ドロップも可能
		os.rename(files1,path_out)
		#ファイルコピー
		#shutil.copy(files1,output_path)
		#print(f)

		i+=1
		print(i)

	#renban()
if __name__=="__main__":
	main()
