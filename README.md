一键部署正常！<br>
ImgRecognitions_EnCode    图像识别_产生条形码/二维码<br>
一、python3.5 - django1.11.5  2019.01.31<br>
二、功能：图片识别文字、在线生成条形码、二维码。<br>
三、应用：django微信小程序后台。<br>
四、主要技术：<br>
1、识别图像中的字符串，使用baidu-aip模块，优点是：快、准、简洁。<br>
2、图像文件上传，选择文件后直接自动提交。<br>
3、django程序运行，前台有动画的图标。<br>
4、前台实现文件内容的拷贝、粘贴。<br>
5、后台实现上传文件大小设定：支持识别的文件大小,不得大于8MB。<br>
6、在线生成条形码、二维码。删除过期(设定10分钟)文件。<br>
7、db.txt。定时执行任务(设定每分钟执行一次)，数据库数据若有变化，就自动备份到db.txt文件。<br>
五、部署<br>
1、上传git。 在../Mytest 工程目录下执行  $ fab fab push <br>
2、部署到远程主机。在 ../fab_u1604 目录下执行 $ fab -c fabricrc init_deploy_u1604<br>
六、存在问题<br>
1、批量生成条形码，输入框第二行内容也预览了。正确：应该只预览第一行内容。<br>
2、QR_code.html中，qrcode16.js文件，在线使用和下载到本地使用，
script src="https://static.gaitubao.net/js/qrcode16.js">/script> 不支持浏览器：Firefox script src="/static/prettify/js/qrcode16.js">/script>   不知为什么？<br>


提供的API函数：
http://localhost:8000/apidata/ 
http://localhost:8000/apidict/