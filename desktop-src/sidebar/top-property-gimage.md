---
title: image.top property
description: Gets or sets the number of pixels from the top edge of the gadget to position the g image element.
ms.assetid: 1126a31c-9b93-4b66-b35b-bd696460f10c
keywords:
- top property Windows Sidebar
- top property Windows Sidebar , image object
- image object Windows Sidebar , top property
topic_type:
- apiref
api_name:
- image.top
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

# image.top property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the number of pixels from the top edge of the gadget to position the [**g:image**](image-element.md) element.

This property is read/write.

## Syntax


```JScript
itop = image.top
image.top = itop
```



## Property value

An **Integer** that specifies or receives the position, in pixels, of the target element from the top edge of the gadget.

## Remarks

> \[!Caution\]  
> Other than [**g:background**](background-element.md), avoid images that render to the absolute edges of a gadget. In high-DPI, rounding errors can cause a magenta fringe around the border of the gadget.

 

This value overrides any positioning declared previously.

## Examples

The following example demonstrates how to set the top-position of the [**g:image**](image-element.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgTop = imgBackground.addImageObject(file, intX, intY);
imgTop.top = 50;
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

 

 





