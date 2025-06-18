import easyocr
import warnings
import ssl

warnings.filterwarnings("ignore", message=".*CUDA.*|.*pin_memory.*")  # 隐藏CUDA、pin_memory警告（电脑没有GPU时会报错）
ssl._create_default_https_context = ssl._create_unverified_context    # 解决HTTPS证书验证问题 (下载模型时会报错)
reader = easyocr.Reader(['ch_sim','en'])                              # 您可以一次传递多种语言，但并非所有语言都可以一起使用。英语与每种语言都兼容，共享共同字符的语言通常彼此兼容
result = reader.readtext('Captcha.jpg', detail = 0, paragraph=True)   # detail=0：获取简单输出 ； paragraph=True：将原始结果合并成易于阅读的段落
print(result)
