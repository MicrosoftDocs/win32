---
title: background.addTextObject method
description: Adds a g text element to the g background element.
ms.assetid: 861e0fee-261f-4fa1-bc3b-891f4d7bed90
keywords:
- addTextObject method Windows Sidebar
- addTextObject method Windows Sidebar , background object
- background object Windows Sidebar , addTextObject method
topic_type:
- apiref
api_name:
- background.addTextObject
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# background.addTextObject method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Adds a [**g:text**](gtext.md) element to the [**g:background**](background-element.md) element.

## Syntax


```JScript
iRetVal = background.addTextObject(
  strText,
  strFont,
  intFontSize,
  strColor,
  intXOffset,
  intYOffset
)
```



## Parameters

<dl> <dt>

*strText* \[in\]
</dt> <dd>

A string that specifies the text to be added.

</dd> <dt>

*strFont* \[in\]
</dt> <dd>

A string that specifies the font name in which to render the text.

</dd> <dt>

*intFontSize* \[in\]
</dt> <dd>

An integer that specifies the absolute value for the point-size in which to render the text. This value is limited to an integer; there are no overload methods that allow the use of alternate HTML-standard values such as absolute sizes (`xx-small | x-small | small | medium | large | x-large | xx-large`), relative sizes (`larger | smaller`), percentages, or other length specifications (`cm, mm, in, pc, px, em, or ex`).

</dd> <dt>

*strColor* \[in\]
</dt> <dd>

A string that specifies the color of the text.

</dd> <dt>

*intXOffset* \[in\]
</dt> <dd>

An integer specifying the horizontal position of the text relative to the top-left corner of the background.

</dd> <dt>

*intYOffset* \[in\]
</dt> <dd>

An integer specifying the vertical position of the image relative to the top-left corner of the background.

</dd> </dl>

## Remarks

The default font and size is 12-point Times New Roman if the specified font and size are not available on the system.

## Examples

The following example demonstrates how to add text to a gadget background.


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



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**background**](background-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





