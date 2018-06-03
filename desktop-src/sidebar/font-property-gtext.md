---
title: text.font property
description: Gets or sets the font name.
ms.assetid: 87cd4777-78ec-46bf-b8d8-269be2038a92
keywords:
- font property Windows Sidebar
- font property Windows Sidebar , text object
- text object Windows Sidebar , font property
topic_type:
- apiref
api_name:
- text.font
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

# text.font property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the font name.

This property is read/write.

## Syntax


```JScript
strfont = text.font
text.font = strfont
```



## Property value

A **String** that specifies or receives the name of the font applied to the target element.

<dt>



 (Times New Roman)


</dt> <dd>

Default. If the font is not installed on the system or no font is specified.

</dd> </dl>

## Examples

The following example demonstrates how to assign a font name to the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtFont = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtFont.font = "Times New Roman";
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

[**image**](image-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





