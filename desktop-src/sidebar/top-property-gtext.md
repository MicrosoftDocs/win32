---
title: text.top property
description: Gets or sets the number of pixels from the top edge of the gadget to position the g text element.
ms.assetid: eb1c2093-e5c6-4788-9d4a-d3a2b8229221
keywords:
- top property Windows Sidebar
- top property Windows Sidebar , text object
- text object Windows Sidebar , top property
topic_type:
- apiref
api_name:
- text.top
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

# text.top property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the number of pixels from the top edge of the gadget to position the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
itop = text.top
text.top = itop
```



## Property value

An **Integer** that specifies or receives the position, in pixels, of the target element from the top edge of the gadget.

## Remarks

This value overrides any positioning declared previously.

## Examples

The following example demonstrates how to set the top-position of the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtTop = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtTop.top = 0;
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

 

 





