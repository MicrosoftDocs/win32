---
title: text object
description: Specifies a text element to display in a gadget.
ms.assetid: 84b22483-88bc-4d5c-a86b-b3c5a2a5e6d3
keywords:
- text object Windows Sidebar
- text object Windows Sidebar , described
topic_type:
- apiref
api_name:
- text
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# text object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Specifies a text element to display in a gadget.

## Members

The **text** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **text** object has these methods.



| Method                                      | Description                                               |
|:--------------------------------------------|:----------------------------------------------------------|
| [**addGlow**](addglow-method-gtext.md)     | Adds a glow effect to a **g:text** element. <br/>   |
| [**addShadow**](addshadow-method-gtext.md) | Adds a shadow effect to a **g:text** element. <br/> |



 

### Properties

The **text** object has these properties.



| Property                                                   | Access type           | Description                                                                                                        |
|:-----------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**align**](align-property-gtext.md)<br/>           | Read/write<br/> | Gets or sets the text alignment. <br/>                                                                       |
| [**blur**](blur-property-gtext.md)<br/>             | Read/write<br/> | Gets or sets the level of blur applied to the **g:text** element. <br/>                                      |
| [**brightness**](brightness-property-gtext.md)<br/> | Read/write<br/> | Gets or sets the brightness of the **g:text** element. <br/>                                                 |
| [**color**](color-property-gtext.md)<br/>           | Read/write<br/> | Gets or sets the text color. <br/>                                                                           |
| [**font**](font-property-gtext.md)<br/>             | Read/write<br/> | Gets or sets the font name. <br/>                                                                            |
| [**fontsize**](fontsize-property-gtext.md)<br/>     | Read/write<br/> | Gets or sets the font size. <br/>                                                                            |
| [**height**](height-property-gtext.md)<br/>         | Read/write<br/> | Gets or sets the height of the **g:text** element. <br/>                                                     |
| [**left**](left-property-gtext.md)<br/>             | Read/write<br/> | Gets or sets the number of pixels from the left edge of the gadget to position the **g:text** element. <br/> |
| [**opacity**](opacity-property-gtext.md)<br/>       | Read/write<br/> | Gets or sets the opacity of the **g:text** element. <br/>                                                    |
| [**rotation**](rotation-property-gtext.md)<br/>     | Read/write<br/> | Gets or sets the degree of rotation applied to the **g:text** element. <br/>                                 |
| [**top**](top-property-gtext.md)<br/>               | Read/write<br/> | Gets or sets the number of pixels from the top edge of the gadget to position the **g:text** element. <br/>  |
| [**value**](value-property-gtext.md)<br/>           | Read/write<br/> | Gets or sets the value of the **g:text** element. <br/>                                                      |
| [**width**](width-property-gtext.md)<br/>           | Read/write<br/> | Gets or sets the width of the **g:text** element. <br/>                                                      |



 

## Remarks

This element can be declared in the gadget HTML file or created with the [**addTextObject**](addtextobject-method-gbackground.md) method from a script file. However, if the element is declared in the HTML file, it will not be accessible from script and will affect the gadget element layout rather than being part of the background.

> \[!Important\]  
> For Windows 7, when the new `<autoscaleDPI>` element of the gadget manifest is set to true (for high-DPI support) gadgets should explicitly specify a text size.

 

This element is not rendered.

This element requires a closing tag.

## Examples

This example shows how to declare a **g:text** element in the gadget HTML file.


```JScript
<g:text id="txtTest">test</g:text>
```



This example shows how to create a **g:text** element in a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtShadow = imgBackground.addTextObject("test", "Verdana", 25, "Red", 50, 50);
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



 

 





