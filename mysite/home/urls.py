# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import home
urlpatterns = [ 
    url(r'^test/', home.test, name="test"), 
        
    url(r'^$', home.index, name="index"),
    url(r'^tostr/', home.tostr, name="tostr"),     
    url(r'^recog_img/', home.recog_img, name="recog_img"),    
  
    url(r'^apidict/', home.apidict, name="apidict"),  
    url(r'^apidata/', home.apidata, name="apidata"),     
    url(r'^distinguish_img/', home.distinguish_img, name="distinguish_img"),     
    url(r'^wx_uploadFile/', home.wx_uploadFile, name="wx_uploadFile"),     

    url(r'^bar_code/', home.bar_code, name="bar_code"),
    url(r'^batch_code/', home.batch_code, name="batch_code"),
    url(r'^downLoadFile/', home.downLoadFile, name="downLoadFile"),    
    url(r'^QR_code/', home.QR_code, name="QR_code"), 
    
]