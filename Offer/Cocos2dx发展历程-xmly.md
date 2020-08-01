# Cocos2dx发展历程

标签（空格分隔）： Cocos2dx

---




## Cocos2dx发展历程

[原文参考](https://retro.moe/2017/04/16/cocos2d-in-a-glimpse/)

### Python版本

- 2005-2007
Ricardo和朋友使用Python语言设计并开发多种游戏，在设计新游戏的过程中，每次都要重新开发引擎；
- 2008.02
在阿根廷Los Cocos组建游戏开发团队并开始创建游戏开发引擎；
- 2008.03
在PyCon 2008芝加哥宣布了alpha版本(v0.1)，命名Los cocos，之后改名为Cocos2d；
- 2008.07
EuroPython 2008上展示了Cocos2d(v0.3)；

### Cocos2d-iPhone

- 2008.06
公布用Objective-C编写的Cocos2d for iPhone v0.1；
- 2008.07
使用该开发引擎开发了第一个游戏Sapus Tongue；
- 2008.12
使用该引擎开发的游戏在App Store中已超过40个；
- 2009年初
使用该引擎开发的Stick Wars获得了应用商店排名第一；
- 2011.07
在社区帮助下，发布了cocos2d-iphonev1.0；

![001.png-36kB][1]

### 其他版本的移植

- Java
cocos2d-android, cocos2d-android-1
- C++
Cocos2d-x
- JavaScript
Cocos2d-HTML5, Cocos2d-JavaScript
- C#
CocosNet, Cocos2d-XNA, CocosSharp
- Go
Gocos2d
- Python
基于cocos2d-iphone新端口（非原始cocos2d）
- Ruby
ShinyCocos, RubyMotion支持

![002.png-61.9kB][2]

### Cocos2d-x

- 2010.07
由Zhe Wang创建，使用C++，使用Objective-C命名方式，开启了Cocos2d-x元年；
- 2011.07
开始使用Lua脚本语言开发游戏逻辑；
- 2011.07之后
**Cocos2d-x v2.0**版本诞生，将OpenGLES1.0版本提升到2.0，支持**Cocos Builder**编辑器，支持JavaScript。
随后抛弃了OC编程风格的**Cocos2d-x v3.0**支持C++11特性；
- 2012年
quick团队（非cocos2dx团队）开发quick-cocos2d-x用以提升lua脚本的易用性，后被cocos官方收购将引擎命名为**cocos2d-lua**；

![000.png-58.3kB][3]


## 从v2.0到v3.0

1. 接口中的CC去掉:

    ```
    CCSprite -> Sprite , CCCallFunc -> CallFunc
    ```
2. 结构体变化

    ```
    ccp(x, y) -> Point(x, y)
    ccpAdd(p1,p2) -> p1+p2;
    ccpSub -> p1-p2
    ccpMult -> p1*p2
    ccpLength(p) -> p.getLength()
    ccpDot(p1,p2); -> p1.dot(p2)
    ccc3() -> Color3B()
    ccc4() -> Color4B()
    ccWHITE -> Color3B::WHITE
    CCPointZero -> Point::ZERO
    CCSizeZero -> Size:ZERO
    ```
3. 单例的应用接口

    ```
    ::sharedSome() -> ::getInstance()
    ```
4. 点、大小、区域

    ```
    CCPoint  -> Vec2
    CCSize -> Size
    CCRect -> Rect
    ```
5. CC to Some

    ```
    CCLog -> CCLOG
    CCArray -> __Array or cocos2d::Vector<T>
    CCSet -> __Set
    ccTouchBegan -> onTouchBegan
    CCObject -> Ref
    CCPointZero -> Vec2::Zero
    ```
6. 回调函数

    ```
    // new callbacks based on C++11
    #define CC_CALLBACK_0(__selector__,__target__, ) std::bind(&__selector__,__target__, ##__VA_ARGS__)
    #define CC_CALLBACK_1(__selector__,__target__, ) std::bind(&__selector__,__target__, std::placeholders::_1, ##__VA_ARGS__)
    #define CC_CALLBACK_2(__selector__,__target__, ) std::bind(&__selector__,__target__, std::placeholders::_1, std::placeholders::_2, ##__VA_ARGS__)
    #define CC_CALLBACK_3(__selector__,__target__, ) std::bind(&__selector__,__target__, std::placeholders::_1, std::placeholders::_2, std::placeholders::_3 ##__VA_ARGS__)
    ```
7. Function对象使用

    ```
    CallFunc::create([&](){
        Sprite *sprite = Sprite::create("s");
        this->addChild(sprite);
    });
    ```
8. clone replace copy

    ```
    //v2.0
    copy()->autorelease()
    //same as v3.0
    clone()
    ```

## Cocos产品

### Cocos

- [Cocos v2.2](https://www.cocos.com/%e7%8e%8b%e5%93%b2%e5%bc%a0%e6%99%93%e9%be%99%e4%ba%8e%e5%90%9b%ef%bc%9acocos-v2-2%e5%8f%91%e5%b8%83-%e5%bb%b6%e7%bb%ad%e3%80%81%e6%95%b4%e5%90%88%e4%b8%8e%e5%bc%80%e6%94%be#45)
提供了3D编辑器，编辑器向前兼容以及向后兼容；
插件扩展方面，支持了基于LUA的自定义控件，支持控件面板和属性面板的扩展，增加了一种导出格式—LUA代码导出格式，开放了数据导出接口，用户可以自定义自己的数据格式，满足自己的特殊需求；
完整工具链，可以完整地完成新建、开发调试、到发布的全过程；
开放的Cocos Store接入各家服务。

- [Cocos v2.2.5](https://www.cocos.com/%e6%b8%b8%e6%88%8f%e5%bc%80%e5%8f%91%ef%bc%9acocos-v2-2-5%e5%8f%91%e5%b8%83-%e6%89%8b%e6%9c%ba%e4%b8%80%e9%94%ae%e5%8f%91%e5%b8%83%ef%bc%8c%e6%94%af%e6%8c%813d%e6%8e%a7%e4%bb%b6#51)
Cocos v2.2.5可以将Cocos Studio编辑的场景UI直接发布到手机上，查看运行效果；
自定义简单的3D扩展控件，亦可通过编写C#代码来自定义一个高级的3D控件；
新建项目流程，创建项目更加方便快捷；

- [Cocos v2.3](https://www.cocos.com/%e8%a7%a6%e6%8e%a7%e7%a7%91%e6%8a%80cocos-v2-3-0%e5%8f%91%e5%b8%83-%e4%b8%ba%e5%bc%80%e5%8f%91%e8%80%85%e8%80%8c%e5%ae%8c%e5%96%84%ef%bc%8c%e7%bb%86%e8%8a%82%e6%9b%b4%e8%b6%8b#64)
为开发者而完善，新增标尺与参考线等功能；
cocos v2.3.0版本的导出json功能得到了优化，场景资源列表能够存储到当前的json里；
为便于开发者快速掌握最新最全的API，cocos v2.3.0版本贴心推出了更新版的cocos文档；
3D场景：支持参考坐标轴与原点快速切换；

这条线最终貌似废弃了，或者说重新整合到Cocos Creator，如下；

### Cocos2d-x

- [API Reference](https://docs.cocos2d-x.org/api-ref/index.html)

- [Cocos2d-x v3.9](https://www.cocos.com/cocos-2d-x-v3-9%e6%96%b0%e7%89%88%e5%8f%91%e5%b8%83-hold%e4%bd%8f%e7%9c%8b%e8%84%b8%e6%97%b6%e4%bb%a3#91)
3D模块功能 3D MotionStreak，支持拖尾效果，优化优化 Sprite3D支持材质系统；
2D模块增加帧回调函数和动画回调函数,新增脚本组件系统,使用Component重构2D物理组件, EditBox:优化iOS和Win32平台的实现，统一与Android平台的表现, 移除AssetsManager, AssetsManagerEx和Downloader对curl的依赖,优化粒子性能;

- [Cocos v3.10(包含Cocos2d-x框架)](https://www.cocos.com/cocos-v3-10%e5%a4%a7%e6%95%b4%e5%90%88%e7%89%88%e6%9c%ac%e5%8f%91%e5%b8%83-%e5%9b%be%e5%bd%a2%e5%8c%96%e8%ae%be%e8%ae%a1%e8%ae%a9%e6%93%8d%e4%bd%9c%e6%9b%b4%e7%9b%b4%e8%a7%82#97)
整合了引擎，不知道团队想干嘛，可能是觉得开发的时候太乱了，搞一套开发流程，编辑器Cocos Studio现已重构了吧恐怕；
![004.png-21.2kB][4]

- [Cocos2d-x v3.15](https://www.cocos.com/cocos-creator-v1-5%e5%8f%91%e5%b8%83%ef%bc%9a%e7%89%a9%e7%90%86%e9%9b%86%e6%88%90%e3%80%812d%e6%91%84%e5%83%8f%e6%9c%ba%e3%80%81typescript#995)
    全面支持 Android Studio，包括编译、代码编辑和调试C++代码：使用文档
    音频模块在Android平台使用tremolo和 MP3 Decoder Library 解码音频文件，使得音频模块效率更高，兼容更多的Android设备
    WebSockets 和 SocketIO 支持 SSL
    AssetsManagerEx更加稳定
    更新 Spine runtime 到v3.5.35
    更新 flatbuffer 到v1.5
    升级 OpenSSL 到v1.1.0
    去除 Windows 8.1 的支持
    去除32位linux的支持

- [Cocos2d-x v3.16](https://www.cocos.com/cocos2d-x-v3-16%e6%ad%a3%e5%bc%8f%e7%89%88%e5%8f%91%e5%b8%83%e5%95%a6%ef%bc%81#1126)
    更好地支持 creator_to_cocos2dx 这个Cocos Creator的插件
    新增 LayerRadiaGradientLayer
    支持__Android Studio 2.3.3__
    修复lua工程在Xcode 8.0+模拟器崩溃问题
    回退CocosStudio的reader和flatbuffer
    修复iOS 11编译错误
    使用bullet的预编译库以加快编译速度
    去除Windows 10 metor模式、Windows Phone和Tizen的支持
    Web引擎更新Spine runtime到v3.5.35


- [Cocos2d-x v3.17](https://www.cocos.com/cocos2d-x-v3-17-%e6%ad%a3%e5%bc%8f%e7%89%88%e6%9c%ac%e5%8f%91%e5%b8%83#1462)
    支持 iPhone X
    支持 Android Studio 3.0+
    CMake 支持全平台，支持预编译引擎库
    升级 Spine runtime 至 v3.6.39
    升级 GLFW 至 3.2.1，并提供预编译库
    更新 Box2D，并提供预编译库
    去除 Android 的 ant 工程
    去除 Visual Studio 2013 的支持


- [Cocos2d-x v4.0]()
    iOS/macOS 支持 metal
    使用 CMake，删除各平台的工程文件
    升级 GLFW 到 3.3
    升级 minizip 到 1.2
    删除废弃函数
    删除 h5 引擎和 Javascript 绑定
    删除 tiff
    删除 SimpleAudioEngine
    删除 experimental 名字空间
    修复 macOS 15 系统字体绘制问题
    适配 iOS13, UIWebView 使用 WKWebView 实现,VideoPlayer 使用 AVPlayerController 实现
    修复 lua 工程在 64 位设备的崩溃问题


### Cocos Creator

- [关于 Cocos Creator](https://docs.cocos.com/creator/manual/zh/getting-started/introduction.html)
Cocos Creator是一个完整的游戏开发解决方案，包含了轻量高效的跨平台游戏引擎，以及能更快速开发游戏所需要的各种图形界面工具，其完全为引擎定制打造，包含从设计、开发、预览、调试到发布的整个工作流所需的全功能一体化编辑器；
提供面向设计和开发的两种工作流，提供简单顺畅的分工合作方式；
目前支持发布游戏到 Web、iOS、Android、各类"小游戏"、PC客户端等平台，真正实现一次开发，全平台运行。
![003.jpg-279.3kB][5]
v1.0主要内容发布：
新 UI 控件：文本框和网格式布局；
骨骼动画和瓦片地图支持；

- [Cocos Creator v1.1](https://www.cocos.com/cocos-creator-1-1%e5%8f%91%e5%b8%83-%e6%b8%b8%e6%88%8f%e5%bc%80%e5%8f%91%e5%8e%9f%e6%9d%a5%e5%8f%af%e4%bb%a5%e6%9b%b4%e7%ae%80%e5%8d%95#99)
导入 Cocos Studio / Cocos Builder 的工程资源；
加入碰撞体组件系统；
开放定制 JavaScript 和 C++ 引擎的工作流程；
完善资源动态加载的接口；

- [Cocos Creator v1.2](https://www.cocos.com/cocos-creator-1-2%e5%8f%91%e5%b8%83%ef%bc%9ah5%e5%bf%ab5%e5%80%8d%e3%80%81%e5%8c%85%e4%bd%93%e5%b0%8f30%e3%80%81lua%e6%94%af%e6%8c%81%e9%a2%84%e8%a7%88%e7%89%88#399)
如标题，Cocos Creator 1.2发布：H5快5倍、包体小30%、Lua支持预览版，提升了引擎性能；

- [Cocos Creator v1.3](https://www.cocos.com/cocos-creator-v1-3%e5%8f%91%e5%b8%83%ef%bc%8c%e6%80%bb%e6%9c%89%e4%b8%80%e9%a1%b9%e6%96%b0%e5%8a%9f%e8%83%bd%e6%98%af%e4%bd%a0%e6%9c%9f%e5%be%85%e5%b7%b2%e4%b9%85%e7%9a%84#651)
添加了新功能，富文本支持，Dragon Bones，骨骼动画支持，Prefab 自动同步与打包时自动合图大大降低美术人员管理项目资源的成本，新增 UI 控件（PageView，Toggle ， Toggle Group，Slider），Creator for Lua 1.1 新升级，插件形式全自动工作流程，全新 AudioEngine；

- [Cocos Creator v1.4](https://www.cocos.com/%e6%96%b0%e5%b9%b4%e6%96%b0%e7%89%88%ef%bc%8c%e6%96%b0%e9%94%8b%e6%b7%ac%e7%a0%ba%ef%bc%9acocos-creator-v1-4%e5%8f%91%e5%b8%83#815)
性能大幅提升，原生平台提升80%以上、H5平台提升超过50%
支持Spine和DragonBones最新版本，支持网格动画，让动画栩栩如生
UI 文字显示增强，支持批量渲染
插件商店上线，新插件开发工作流程公布
热更新问题修复，接口增强
增加原生音频软解码方案，提高兼容性
支持VS Code 调试网页版游戏

- [Cocos Creator v1.5](https://www.cocos.com/%e5%8a%9f%e8%83%bd%e9%a2%84%e5%91%8a%ef%bc%9acreator-1-5%e7%89%a9%e7%90%86%e5%bc%95%e6%93%8e%e9%9b%86%e6%88%90#886)
1.2版开始提供的Collider碰撞组件做碰撞检测，版本1.5集成的物理引擎可以做复杂的物理效果；
在Creator 1.5里面，Box2D集成到编辑器里，用户可以方便快捷的拖拽、进行各种物理属性编辑；
Cocos2d-x + Box2D开发中，经常需要关注从物理世界到Cocos2d世界的坐标转换，而Cocos Creator的物理集成则能够实现自动转换，用户只需关注熟悉的像素坐标即可。

- [Cocos Creator v1.7](https://www.cocos.com/cocos-creator-v1-7%e5%8f%91%e5%b8%83%ef%bc%9ajsb%e5%8d%87%e7%ba%a72-0%e3%80%81%e4%b8%80%e9%94%ae%e5%af%bc%e5%87%bacocos2d-x%e3%80%81%e5%8c%85%e4%bd%93%e5%87%8f%e5%b0%8f%e5%92%8c%e9%9b%86%e6%88%90#1242)
    JSB 2.0，原生平台性能提升;
    ![005.png-44.9kB][6]
    Cocos2d-x 导出，支持 C++ & Lua 原生游戏工作流;
    Cocos Analytics – 数据统计;
    原生平台模块裁剪，便捷高效减小原生游戏包体;

- [Cocos Creator v2.0](https://www.cocos.com/cocos-creator-v2-0-%e6%ad%a3%e5%bc%8f%e5%8f%91%e5%b8%83#1683)
重写了底层渲染器，从结构上保障了性能的提升和渲染能力的升级。同时，为了保障用户项目可以更平滑得升级，几乎没有改动组件层的API。当然，这些改动并不是对用户完全透明的，比如引擎加载流程、事件系统、引擎整体 API 的精简和重组;
加入基于 Cocos3D 的 3D 渲染器，具备了正式引入 3D 支持的基础;

- [Cocos Creator v2.1.0](https://www.cocos.com/cocos-creator-2-1-%e6%ad%a3%e5%bc%8f%e5%8f%91%e5%b8%83%ef%bc%8c%e6%96%b0%e5%a2%9e3d%e6%94%af%e6%8c%81#1867)
支持了 3D 模型渲染、3D Camera、3D 骨骼动画、3D 点选等 3D 特性，同时编辑器原生支持解析 FBX 格式的 3D 模型文件，不需要额外的导入流程。

- Cocos Creator v2.0.7
增加华为快游戏正式发布支持；
Cocos 引擎服务面板正式集成 Matchvs,除了与实时音视频服务提供商声网 Agora之外构建合作，帮助开发者快速获取“开黑”能力之外，还同国内优质的联网服务提供商 Matchvs 开展了深入合作，今日 Matchvs SDK 已正式接入服务面板，各位开发者可以通过接入 [Matchvs SDK](https://www.cocos.com/cocos-%e5%bc%95%e6%93%8e%e6%9c%8d%e5%8a%a1%e9%9d%a2%e6%9d%bf%e6%ad%a3%e5%bc%8f%e9%9b%86%e6%88%90-matchvs#2176)，快捷地实现多人即时联网。

- Cocos Creator v2.0.8
完善对安卓新版微信（7.0.3）的支持；

- Cocos Creator v2.0.9
新增了百度小游戏平台的支持;

- [Cocos Creator v2.2](https://www.cocos.com/cocos-creator-v2-2-%e6%ad%a3%e5%bc%8f%e5%8f%91%e5%b8%83#5707)
-对渲染引擎进行了大幅度升级，在原生平台上实现了巨大的性能提升，不仅完胜了所有 Cocos Creator 过往版本，更超越了 Cocos2d-JS 和性能一贯优异的 Cocos2d-lua。因此 2.2 版本的 Cocos Creator，已经能够在原生平台上满足所有 Cocos 新老开发者的性能需求。
在 Android 原生上，Cocos Creator 2.2.0 的性能是 Cocos2d-lua 和 1.9.3 版本的 1.5 – 1.7 倍。
在 iOS 原生上，Cocos Creator 2.2.0 的性能和 Cocos2d-lua 齐平，是 1.9.3 版本的 3 – 4 倍

- Cocos Creator v2.1.4 
正式支持支付宝小游戏平台;

- [Cocos Creator 2.3.0](https://www.cocos.com/cocos-creator-2-3-0-%e6%ad%a3%e5%bc%8f%e4%b8%8a%e7%ba%bf#6601)
移植了 Cocos Creator 3D 中的物理、碰撞和 3D 粒子系统，还升级到了和 3D 引擎一致的正式版本材质系统，能够胜任更多品类的游戏开发;
支持 3D 物理系统;
支持 3D 碰撞系统;
支持 3D 粒子系统;
升级材质系统到正式版;
支持 Spine 与 DragonBones 挂载节点;
支持 Spine 二进制资源格式;


- Cocos Creator v2.4.1
支持 HUAWEI AppGallery Connect;

- Cocos Creator v2.4.2
字节小游戏基于字节跳动全产品矩阵开发，包含 今日头条、抖音 及 今日头条极速版，是不需用户进行下载，点开即玩的全新游戏类型，与图文、视频等场景有着天然的搭配性。

### Others

![Cocos Creator 3D][7]

- [Cocos Creator 3D v1.0](https://www.cocos.com/cocos-creator-3d-v1-0-%e6%ad%a3%e5%bc%8f%e5%8f%91%e5%b8%83#5626)
将持续把 3D 方面的新技术应用到 Cocos Creator 3D 工具链以及增强 Cocos Creator 2D 产品的表现力和性能。立足于为开发者提供一个轻量、易用的 3D 创作工具，潜心探索三年多，经历了三个多月的大范围公测，Cocos Creator 3D 已准备就绪，于今日发布正式版本，真正为 Cocos 开发者加持 3D 游戏的开发能力。

- [Cocos Analytics](https://www.cocos.com/analytics)
![007.png-33kB][8]

  [1]: http://static.zybuluo.com/usiege/n8ib3xn6s4fjj3pi9bx6lhwq/001.png
  [2]: http://static.zybuluo.com/usiege/hhcq9b9wsuhab11jf1du2r9a/002.png
  [3]: http://static.zybuluo.com/usiege/70dz5na7asyrc8rxkqwpqiwx/000.png
  [4]: http://static.zybuluo.com/usiege/rn4kct89rw9us1dpeuhhqgig/004.png
  [5]: http://static.zybuluo.com/usiege/vle1nm8r3fdudq3bagim4olt/003.jpg
  [6]: http://static.zybuluo.com/usiege/iie9uapzldfhn09oj1x6h58s/005.png
  [7]: http://static.zybuluo.com/usiege/1aqmyuh7olhtbrjjbb3ia4eb/006.png
  [8]: http://static.zybuluo.com/usiege/vvimcgr92gc6ansc2ca9fmda/007.png