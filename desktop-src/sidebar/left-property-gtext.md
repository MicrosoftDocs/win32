---
title: text.left property
description: Gets or sets the number of pixels from the left edge of the gadget to position the g text element.
ms.assetid: 280dd9de-cce5-4b9c-84f0-f22f1d6d497a
keywords:
- left property Windows Sidebar
- left property Windows Sidebar , text object
- text object Windows Sidebar , left property
topic_type:
- apiref
api_name:
- text.left
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

# text.left property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the number of pixels from the left edge of the gadget to position the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
ileft = text.left
text.left = ileft
```



## Property value

An **Integer** that specifies or receives the position, in pixels, of the target element from the left edge of the gadget.

## Remarks

This value overrides any positioning declared previously.

## Examples

The following example demonstrates how to set the left-position of the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtLeft = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtLeft.left = 0;
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

 

 





