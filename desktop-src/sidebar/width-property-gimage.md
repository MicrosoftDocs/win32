---
title: image.width property
description: Gets or sets the width of the g image element.
ms.assetid: 1fef45b9-edee-4dfa-a161-8e1e813c6538
keywords:
- width property Windows Sidebar
- width property Windows Sidebar , image object
- image object Windows Sidebar , width property
topic_type:
- apiref
api_name:
- image.width
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

# image.width property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the width of the [**g:image**](image-element.md) element.

This property is read/write.

## Syntax


```JScript
iwidth = image.width
image.width = iwidth
```



## Property value

An **Integer** that specifies or receives the width, in pixels, to scale the target element.

## Remarks

> \[!Caution\]  
> Other than [**g:background**](background-element.md), avoid images that render to the absolute edges of a gadget. In high-DPI, rounding errors can cause a magenta fringe around the border of the gadget.

 

## Examples

The following example demonstrates how to set the width of the [**g:image**](image-element.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgWidth = imgBackground.addImageObject(file, intX, intY);
imgWidth.width = 50;
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

 

 





