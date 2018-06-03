---
title: text.height property
description: Gets or sets the height of the g text element.
ms.assetid: 357dc79c-bd7d-420e-aba4-1ba999a6a316
keywords:
- height property Windows Sidebar
- height property Windows Sidebar , text object
- text object Windows Sidebar , height property
topic_type:
- apiref
api_name:
- text.height
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

# text.height property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the height of the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
iheight = text.height
text.height = iheight
```



## Property value

An **Integer** that specifies or receives the height, in pixels, to scale the target element.

## Examples

The following example demonstrates how to set the height of the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtHeight = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtHeight.height = 50;
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

 

 





