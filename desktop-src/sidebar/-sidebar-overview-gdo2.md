---
title: Developing a Gadget for Windows Sidebar Part 2 The G BACKGROUND, G IMAGE, G TEXT Presentation Elements and GIMAGE Protocol
description: The second of three overviews that describe how to create a basic gadget for the Windows Sidebar.
ms.assetid: f03fc7d8-8d64-4bc8-aa15-7dd79e3e9303
keywords:
- Windows Sidebar,creating gadgets
- Sidebar,creating gadgets
- gadgets,creating
- creating gadgets
- Windows Sidebar,examples
- Sidebar,examples
- gadgets,examples
- Gadget.xml
- Windows Sidebar,backgrounds
- Sidebar,backgrounds
- gadgets,backgrounds
- Windows Sidebar,elements
- Sidebar,elements
- gadgets,elements
- Windows Sidebar,gimage protocol
- Sidebar,gimage protocol
- gadgets,gimage protocol
- gimage protocol
- Windows Sidebar,image sizing
- Sidebar,image sizing
- gadgets,image sizing
- G IMAGE
- G TEXT
- G BACKGROUND
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Developing a Gadget for Windows Sidebar Part 2: The G:BACKGROUND, G:IMAGE, G:TEXT Presentation Elements and GIMAGE Protocol

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

The second of three overviews that describe how to create a basic gadget for the Windows Sidebar. In this overview, we demonstrate how to declare a background image and add some simple text and graphics to a gadget using the three presentation elements in the Sidebar `g` namespace ([**g:background**](background-element.md), [**g:image**](image-element.md), and [**g:text**](gtext.md)) and the native Sidebar image protocol (gimage).

-   [Introduction](#introduction)
-   [Background Images and the G:BACKGROUND Element](#background-images-and-the-gbackground-element)
-   [The G:TEXT and G:IMAGE Elements](#the-gtext-and-gimage-elements)
-   [The GIMAGE Protocol](#the-gimage-protocol)
    -   [Sizing](#sizing)
-   [For Further Reference](#for-further-reference)

## Introduction

The Sidebar presentation elements expose their functionality through qualified HTML elements in the Sidebar `g` namespace and the gadget presentation APIs. These elements, along with all standard HTML elements, are exposed through the gadget Document Object Model (DOM) and are accessible from gadget script.

The Sidebar supports JPEG, bitmap (BMP), Graphics Interchange Format (GIF), and Portable Network Graphics (PNG) image types. Only PNG supports alpha channel transparency.

> [!Note]  
> The Sidebar presentation elements are not available in standard HTML documents and do not render in external browsers such as Windows Internet Explorer.

 

## Background Images and the G:BACKGROUND Element

There are a number of methods that can be used to declare a gadget background element and specify its image source. Generally, the background object and its image source are declared in the gadget HTML file using the [**g:background**](background-element.md) element:


```
<body>
    <g:background id="imgBackground" src="images/background.png">
        <span id="gadgetContent">Hello World!</span>
    </g:background>
</body>
```



An alternative is to declare the [**g:background**](background-element.md) as previously described, but specify the image source in Microsoft JScript:


```
<html>
    <head>
        <title>Hello World</title>
        <script type="text/jscript" language="jscript">
            function init()
            {
                var oBackground = document.getElementById("imgBackground");
                oBackground.src = "url(images/background.png)";
            }
        </script>
    </head>
    
    <body onload="init()">
        <g:background id="imgBackground">
            <span id="gadgetContent">Hello World!</span>
        </g:background>
    </body>
</html>
```



> \[!Caution\]  
> When using background images with alpha channel transparency the following two methods can result in unpredictable rendering, such as transparent pixels replaced with magenta, and limitations in functionality. As such, they are presented here for information purposes only and are not recommended.

 

> \[!Important\]  
> For Windows 7, when the new `<autoscaleDPI>` element of the gadget manifest is set to true (for high-DPI support) and the following methods are used, rendering issues can increase significantly.

 

The following example uses the [**background**](system-gadget-background.md) property to declare the gadget background image:


```
<html>
    <head>
        <title>Hello World</title>
        <script type="text/jscript" language="jscript">
        function init()
        {
            System.Gadget.background = "images\\background.png";
        }
        </script>
    </head>
    
    <body onload="init()">
        <g:background id="imgBackground">
            <span id="gadgetContent">Hello World!</span>
        </g:background>
    </body>
</html>
```



A similar method uses Cascading Style Sheets (CSS) to update the [backgroundImage Property](http://go.microsoft.com/fwlink/p/?linkid=144190) as shown in the following example:


```
<html>
    <head>
        <title>Hello World</title>
        <script type="text/jscript" language="jscript">
        function init()
        {
            with(document.body.style)
                backgroundImage = "images\\background.png"; 
        }
        </script>
    </head>
    
    <body onload="init()">
        <g:background id="imgBackground">
            <span id="gadgetContent">Hello World!</span>
        </g:background>
    </body>
</html>
```



Finally, just like a standard webpage, the gadget background can simply be declared as an attribute of the `<body>` tag and modified with CSS. However, this does not expose the background as a [**g:background**](background-element.md) scripting element.


```
<html>
    <head>
        <style>
            body{width:120;height:160;font:8 pt Arial;color:white;
            filter:progid:DXImageTransform.Microsoft.Gradient(GradientType=1, StartColorStr="#000000",
            EndColorStr="#0000FF")}
        </style>
    </head>
    <body bgcolor="red" background="background.jpg">
    ...
    </body>
</html>
```



When one background image needs to be swapped for another of different size, such as when a gadget is docked or undocked, it is recommended that the width of the background element be set to 0. This forces the platform to recalculate the size of the image and refresh appropriately.

See the [**onUndock**](system-gadget-onundock.md) or [**onDock**](system-gadget-ondock.md) topics for an example.

## The G:TEXT and G:IMAGE Elements

The [**g:text**](gtext.md) and [**g:image**](image-element.md) elements expose gadget text and image functionality respectively.

> [!Note]  
> The [**g:text**](gtext.md) and [**g:image**](image-element.md) elements can be declared in the gadget HTML file but it is highly recommended that you use the [**addImageObject**](addimageobject-method-gbackground.md) and [**addTextObject**](addtextobject-method-gbackground.md) methods from JScript instead. This will ensure the element is exposed through the gadget DOM.

 

The following example demonstrates how to add images and text to the background layer of a gadget. These objects will appear at the top of the z-order for the background layer, but below any UI controls.

> \[!Caution\]  
> Other than [**g:background**](background-element.md), avoid images that render to the absolute edges of a gadget. In high-DPI, rounding errors can cause a magenta fringe around the border of the gadget.

 


```C++
// Initialize the gImage object
// DEFAULT_IMG_PATH: the default image path.
function initImage()
{
    // Check if the user has already selected an image file to use. If not use default.
    if (System.Gadget.Settings.read("imageFile") == "")
    {
        System.Gadget.Settings.write("imageFile", DEFAULT_IMG_PATH);
    }
    imageFile = System.Gadget.Settings.read("imageFile");
    
    // Create the image object
    oImage = document.getElementById("background").addImageObject("", 0, 0);
}

// Initialize the gText object
function initText()
{
    oText = document.getElementById("background").addTextObject("", "Verdana", 10, "blue", 0, 0);
}

function showImage()
{
    oImage.src = System.Gadget.Settings.read("imageFile");
}

function showText(newValue)
{
    oText.value = newValue;
}
```



**g:image** and **g:text** objects can also be added to the gadget DOM by declaring them in the gadget HTML file:


```
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=Unicode" />
    <link href="css/Graphic.css" rel="stylesheet" type="text/css" />
    <script language="javascript" src="js/graphic.js" type="text/javascript"></script>
</head>
<body>
<g:background 
id="imgBackground" 
src="images\background.png">
<g:text id="txtTest" blur="20">test</g:text>
<g:image id="imgTest" src="images/aerologo.png"/>
</g:background>
</body>
</html>
```



> [!Note]  
> This method does not expose the objects as [**g:image**](image-element.md) or [**g:text**](gtext.md) elements. You can locate and assign the objects using the `document.getElementById("...")` method, but the **g:image** or **g:text** methods and properties are not available.

 

## The GIMAGE Protocol

This protocol is useful for adding images to the gadget DOM more efficiently than the standard HTML `<img>` tag. This efficiency results from improved thumbnail handling and image caching (it will attempt to use thumbnails from the Windows cache if the requested size is smaller than 256 pixels by 256 pixels) when compared with requesting an image using the `file://` or `http://` protocols. An added benefit of the `gimage` protocol is that any file other than a standard image file can be specified as a source, and the icon associated with that file's type is displayed.

> [!Note]  
> When the `gimage` protocol is specified, the requested file **must** be on the local machine and must not contain a server reference.

 

Despite its name, the `gimage` protocol is unrelated to the [**g:image**](image-element.md) element. The image, or associated icon, is returned as a bytestream and, as such, is not exposed to gadget script as a **g:image** element. However, the `<img>` object is still a member of the gadget DOM and is exposed through standard JScript members.


```
function findGIMAGE()
{
    var oGIMAGE = document.getElementById("imgGIMAGE");
    
    // Get a standard JScript <img> object property.
    var srcValue = oGIMAGE.src;
    
    // Undefined G:IMAGE property.
    var opacityValue = oGIMAGE.opacity;
}

...

<img id="imgGIMAGE" 
src="gimage:///C:\Users\user\AppData\Local\Microsoft\Windows Sidebar\Gadgets\SDK_Graphic.gadget\js\graphic.js" />
```



### Sizing

As stated previously, one of the benefits of the `gimage` protocol is enhanced thumbnail handling and image sizing. Typically, you would supply the image height and width as a querystring appended to the `src` attribute value or as an inline style.


```
// --------------------------------------------------------------------
// Add an image to the gadget DOM using the gimage protocol.
// --------------------------------------------------------------------
function addGIMAGE()
{
    var heightWidthLoad = "?width=25&amp;height=25";
    var oImage = document.createElement("img");
    oImage.src = "gimage:///" + System.Gadget.path + "\\images\\aerologo.png" + heightWidthLoad;
    oImage.id = "imgGIMAGEx";
    document.body.appendChild(oImage);
}

// --------------------------------------------------------------------
// Switch an image using the gimage protocol.
// --------------------------------------------------------------------
function switchGIMAGE(file)
{
    // Specify the height, width, and interpolation method.
    imgGIMAGE.style.height = 25;
    imgGIMAGE.style.width = 25;
    imgGIMAGE.style.msInterpolationMode = "bicubic";
    imgGIMAGE.src = "gimage:///" + System.Gadget.path + "\\images\\aerologo.png";
}

<!--
Specify gimage details from script.
-->
<img id="imgGIMAGE" src="images/blank.png" height="0" width="0" />
```



If only one of the height and width is specified, the image is scaled proportionally; if neither the height or width is specified, the image is scaled proportionally to 120 pixels by 120 pixels. In either case, any unfilled areas are rendered as transparent.

## For Further Reference

[Developing a Gadget for Windows Sidebar Part 1: The Basics](-sidebar-overview-gdo.md)

[Developing a Gadget for Windows Sidebar Part 3: Settings and Flyouts](-sidebar-overview-gdo3.md)

For Windows Vista User Experience Guidelines, see [Windows Vista User Experience Guidelines for the Sidebar](http://msdn.microsoft.com/library/aa974179.aspx)

To read posts from the Sidebar team, including gadget authoring tips, links to gadget information, and news about the platform, see the [Gadget Corner blog](http://blogs.msdn.com/sidebar/default.aspx).

To participate in developer community discussions on writing gadgets for the Sidebar, see the [Sidebar Gadget Development forum](http://go.microsoft.com/fwlink/p/?linkid=142587).

 

 




