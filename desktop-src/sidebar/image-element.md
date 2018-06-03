---
title: image object
description: Specifies an image element to display in a gadget.
ms.assetid: bcc3db81-45e8-46ae-af49-8f81829c0303
keywords:
- image object Windows Sidebar
- image object Windows Sidebar , described
topic_type:
- apiref
api_name:
- image
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# image object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Specifies an image element to display in a gadget.

## Members

The **image** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **image** object has these methods.



| Method                                       | Description                                                |
|:---------------------------------------------|:-----------------------------------------------------------|
| [**addGlow**](addglow-method-gimage.md)     | Adds a glow effect to a **g:image** element. <br/>   |
| [**addShadow**](addshadow-method-gimage.md) | Adds a shadow effect to a **g:image** element. <br/> |



 

### Properties

The **image** object has these properties.



| Property                                                    | Access type           | Description                                                                                                         |
|:------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**blur**](blur-property-gimage.md)<br/>             | Read/write<br/> | Gets or sets the level of blur applied to the **g:image** element. <br/>                                      |
| [**brightness**](brightness-property-gimage.md)<br/> | Read/write<br/> | Gets or sets the brightness of the **g:image** element. <br/>                                                 |
| [**height**](height-property-gimage.md)<br/>         | Read/write<br/> | Gets or sets the height of the **g:image** element. <br/>                                                     |
| [**left**](left-property-gimage.md)<br/>             | Read/write<br/> | Gets or sets the number of pixels from the left edge of the gadget to position the **g:image** element. <br/> |
| [**opacity**](opacity-attribute-gimage.md)<br/>      | Read/write<br/> | Gets or sets the opacity of the **g:image** element. <br/>                                                    |
| [**rotation**](rotation-attribute-gimage.md)<br/>    | Read/write<br/> | Gets or sets the degree of rotation applied to the **g:image** element. <br/>                                 |
| [**softEdge**](softedge-property-gimage.md)<br/>     | Read/write<br/> | Gets or sets the amount of edge softening that is applied to the **g:image** element. <br/>                   |
| [**src**](src-attribute-gimage.md)<br/>              | Read/write<br/> | Gets or sets the image file used by the **g:image** element. <br/>                                            |
| [**top**](top-property-gimage.md)<br/>               | Read/write<br/> | Gets or sets the number of pixels from the top edge of the gadget to position the **g:image** element. <br/>  |
| [**width**](width-property-gimage.md)<br/>           | Read/write<br/> | Gets or sets the width of the **g:image** element. <br/>                                                      |



 

## Remarks

The Windows Sidebar supports JPEG, bitmap (BMP), Graphics Interchange Format (GIF), and Portable Network Graphics (PNG) image types. Only PNG supports alpha channel transparency.

This element can be declared in the gadget HTML file or created with the [**addImageObject**](addimageobject-method-gbackground.md) method from a script file. However, if the element is declared in the HTML file, it will affect the gadget element layout rather than being part of the background.

> \[!Caution\]  
> Other than [**g:background**](background-element.md), avoid images that render to the absolute edges of a gadget. In high-DPI, rounding errors can cause a magenta fringe around the border of the gadget.

 

This element is a $disp element.

This element requires a closing tag.

## Examples

This example shows how to create a **g:image** element in a gadget script file that exposes all **g:image** members.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgGlow = imgBackground.addImageObject("file://img.png", 0, 0);
```



This example shows how to declare a **g:image** element in the gadget HTML file that exposes a subset of **g:image** members (similar funtionality to [**g:background**](background-element.md)).


```JScript
<g:image src="..\aerologo.png" id="imgTest" onclick="changeText()" />
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





