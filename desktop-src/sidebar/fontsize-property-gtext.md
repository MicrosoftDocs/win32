---
title: text.fontsize property
description: Gets or sets the font size.
ms.assetid: 930f3bcc-71d9-4d33-b7bd-9dfd830c6d8c
keywords:
- fontsize property Windows Sidebar
- fontsize property Windows Sidebar , text object
- text object Windows Sidebar , fontsize property
topic_type:
- apiref
api_name:
- text.fontsize
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# text.fontsize property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the font size.

This property is read/write.

## Syntax


```JScript
strfontsize = text.fontsize
text.fontsize = strfontsize
```



## Property value

A **String** that specifies or receives the size of the font applied to the target element.

<dt>



 (12)


</dt> <dd>

Default. If the font size is not available for the font specified.

</dd> </dl>

## Remarks

> \[!Important\]  
> For Windows 7, when the new `<autoscaleDPI>` element of the gadget manifest is set to true (for high-DPI support) gadgets should explicitly specify a text size.

 

## Examples

The following example demonstrates how to assign a font size to the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtSize = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtSize.fontsize = 12;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Olectl.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**background**](background-element.md)
</dt> <dt>

[**image**](image-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





