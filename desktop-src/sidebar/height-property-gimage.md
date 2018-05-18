---
title: image.height property
description: Gets or sets the height of the g image element.
ms.assetid: '6c0e6e39-df13-418c-bf0d-a4c597597c5a'
keywords: ["height property Windows Sidebar", "height property Windows Sidebar , image object", "image object Windows Sidebar , height property"]
topic_type:
- apiref
api_name:
- image.height
api_location:
- Sidebar.Exe
api_type:
- COM
---

# image.height property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the height of the [**g:image**](image-element.md) element.

This property is read/write.

## Syntax


```JScript
iheight = image.height
image.height = iheight
```



## Property value

An **Integer** that specifies or receives the height, in pixels, to scale the target element.

## Remarks

> \[!Caution\]  
> Other than [**g:background**](background-element.md), avoid images that render to the absolute edges of a gadget. In high-DPI, rounding errors can cause a magenta fringe around the border of the gadget.

 

## Examples

The following example demonstrates how to set the height of the [**g:image**](image-element.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgHeight = imgBackground.addImageObject(file, intX, intY);
imgHeight.height = 50;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
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

 

 





