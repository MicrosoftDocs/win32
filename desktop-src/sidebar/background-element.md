---
title: background object
description: Declares a gadget background with content and properties.
ms.assetid: '9d0467d9-a02c-4629-be60-6effb551721d'
keywords: ["background object Windows Sidebar", "background object Windows Sidebar , described"]
topic_type:
- apiref
api_name:
- background
api_location:
- Sidebar.Exe
api_type:
- COM
---

# background object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Declares a gadget background with content and properties.

## Members

The **background** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **background** object has these methods.



| Method                                                      | Description                                                                                                                                                                                                                                                               |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**addGlow**](addglow-method-gbackground.md)               | Adds a glow effect to the **g:background** element. <br/>                                                                                                                                                                                                           |
| [**addImageObject**](addimageobject-method-gbackground.md) | Adds a [**g:image**](image-element.md) element to the **g:background** element. <br/>                                                                                                                                                                              |
| [**addShadow**](addshadow-method-gbackground.md)           | Adds a shadow effect to the **g:background** image. <br/>                                                                                                                                                                                                           |
| [**addTextObject**](addtextobject-method-gbackground.md)   | Adds a [**g:text**](gtext.md) element to the **g:background** element. <br/>                                                                                                                                                                                       |
| [**removeObjects**](removeobjects-method-gbackground.md)   | Removes all [**g:text**](gtext.md) and [**g:image**](image-element.md) elements added to the gadget background using the [**addTextObject**](addtextobject-method-gbackground.md) and [**addImageObject**](addimageobject-method-gbackground.md) methods. <br/> |



 

### Properties

The **background** object has these properties.



| Property                                                         | Access type           | Description                                                                                            |
|:-----------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------|
| [**blur**](blur-property-gbackground.md)<br/>             | Read/write<br/> | Gets or sets the level of blur applied to the **g:background** element. <br/>                    |
| [**brightness**](brightness-property-gbackground.md)<br/> | Read/write<br/> | Gets or sets the brightness of the **g:background** element. <br/>                               |
| [**opacity**](opacity-attribute-gbackground.md)<br/>      | Read/write<br/> | Gets or sets the opacity of the **g:background** element. <br/>                                  |
| [**rotation**](rotation-attribute-gbackground.md)<br/>    | Read/write<br/> | Gets or sets the degree of rotation applied to the **g:background** element. <br/>               |
| [**softEdge**](softedge-property-gbackground.md)<br/>     | Read/write<br/> | Gets or sets the amount of edge softening that is applied to the **g:background** element. <br/> |
| [**src**](src-attribute-gbackground.md)<br/>              | Read/write<br/> | Gets or sets the image file used by the **g:background** element. <br/>                          |



 

## Remarks

The Windows Sidebar supports JPEG, bitmap (BMP), Graphics Interchange Format (GIF), and Portable Network Graphics (PNG) image types. Only PNG supports alpha channel transparency.

This element is declared in the gadget HTML file through a non-standard tag.

An image can be assigned to the **g:background** element from a gadget script file by using the [**background**](system-gadget-background.md) property or [**src**](src-attribute-gbackground.md) property.

> [!Note]  
> The Cascading Style Sheets (CSS) `backgroundImage` property can also be used to assign an image to the background.

 

Attributes of the **g:background** element can be accessed from the gadget script files if the element has an `id` tag.

This element is a $disp element.

This element requires a closing tag.

## Examples

The following example shows how to declare a **g:background** element in HTML.


```JScript
<g:background id="imgBackground" src="images/background.png" />
```



The following example shows how to use the [**src**](src-attribute-gbackground.md) property to assign an image to the **g:background** element.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
imgBackground.src = "../images/bg_undocked.jpg";
```



The following example shows how to access attributes of the **g:background** element.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
imgBackground.opacity = 50;
```



The following example shows how to use the [**background**](system-gadget-background.md) property to assign an image to the **g:background** element.

> \[!Caution\]  
> When using background images with alpha channel transparency the following two methods can result in unpredictable rendering, such as transparent pixels replaced with magenta, and limitations in functionality. As such, they are presented here for information purposes only and are not recommended.

 

> \[!Important\]  
> For Windows 7, when the new `<autoscaleDPI>` element of the gadget manifest is set to true (for high-DPI support) and the following methods are used, rendering issues can increase significantly.

 


```JScript
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



The following example shows how to use CSS to assign an image to the **g:background** element.

> \[!Important\]  
> When using background images with alpha channel transparency the following method can result in unpredictable rendering (typically with magenta replacing transparent pixels) and limitations in functionality. As such, it is presented here for information purposes only and is not recommended.

 

> \[!Warning\]  
> For Windows 7, when the `<autoscaleDPI>` element is set to true and the following method is used, rendering issues increase significantly.

 


```JScript
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



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





