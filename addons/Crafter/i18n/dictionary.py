from common.i18n.dictionary import preprocess_dictionary

dictionary = {
    "zh_CN": {
        "Crafter": "Crafter",
        "Plans":"方案",
        #==========面板==========
            #==========导入世界==========
        "Import World":"导入世界",
        "Import Editable Area":"导入可编辑区域",
        "World path":"存档地址",
        "XYZ-1":"坐标1",
        "XYZ-2":"坐标2",
            #==========导入资源==========
        "Import Resources":"导入资源",
        "Resources":"资源包预设",
        "original":"原版",
        "Open Resources Plans":"打开资源包预设列表文件夹",
        "Reload Resources Plans":"刷新资源预设列表",
        "Resource":"资源包",
        "Up resource's priority":"提高资源包优先级",
        "Down resource's priority":"降低资源包优先级",
        "Texture Interpolation":"纹理插值",
        "Texture interpolation method":"纹理插值类型",
        "Set Texture Interpolation":"设置纹理插值",
            #==========加载材质==========
        "Load Materials":"加载材质",
        "Rain":"雨",
        "Materials index":"材质索引",
        "Open Materials":"打开材质文件夹",
        "Reload Materials":"刷新材质列表",
        "Load Material":"加载材质",
        "Classification Basis":"材质分类依据",
        "default":"默认",
        "Open Classification Basis":"打开材质分类依据文件夹",
        "Reload Classification Basis":"刷新材质分类依据列表",
        #==========操作介绍==========
            #==========导入世界==========
        "Import world":"导入世界",
        "Import the surface world":"导入表面世界",
        "Import the solid area":"导入实心区域",
        "Starting coordinates":"起始坐标",
        "Ending coordinates":"结束坐标",
            #==========导入资源==========
        "Set texture interpolation":"设置纹理插值",
            #==========加载材质==========
        "rain":"雨",
        "Load material":"加载材质",
        "Classification basis":"材质分类依据",
        
    }
}

dictionary = preprocess_dictionary(dictionary)

dictionary["zh_HANS"] = dictionary["zh_CN"]
