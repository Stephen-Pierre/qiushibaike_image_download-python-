import urllib.request
import re
import os

"""
编写爬虫爬取糗图百科的搞笑图片

"""

# url = 'src="//pic.qiushibaike.com/system/pictures/12179/121791757/medium/9K2OWJ66PB4O0X5T.jpg"'


def handle_request(url, page):
	'''创建请求对象并返回'''
	url = url + str(page) + '/'
	headers = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

	}
	request = urllib.request.Request(url, headers=headers)
	return request


def download_image(content):
	'''下载方法，解析出下载链接并下载所有图片'''
	# 创建保存目标文件夹
	dirname = 'qiutu'
	if not os.path.exists(dirname):
		os.mkdir(dirname)
	# 根据内容解析出图片链接地址
	pattren = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', re.S)
	lt = pattren.findall(content)
	# 遍历地址下载图片
	for url in lt:
		url = "https:" + url
		# 为图片命名
		filename = url.split('/')[-1]
		filepath = dirname + '/' + filename
		# 打印提示信息
		print('%s图片正在下载.....'%filename)
		# 发送请求下载图片
		urllib.request.urlretrieve(url, filepath)
		print('%s图片下载完成！！！'%filename)


def main():
	url = 'https://www.qiushibaike.com/pic/page/'
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	for page in range(start_page, end_page + 1):
		# 生成请求对象
		request = handle_request(url, page)
		# 发送请求获取响应内容
		content = urllib.request.urlopen(request).read().decode()
		# 打印提示信息
		print('第%s页正在下载......'%page)
		# 解析响应内容，获取下载链接，并下载所有图片
		download_image(content)
		print('第%s页下载完成！！！'%page)



if __name__ == '__main__':
	main()