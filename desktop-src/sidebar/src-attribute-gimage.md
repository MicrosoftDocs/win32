---
title: image.src property
description: Gets or sets the image file used by the g image element.
ms.assetid: f1481f85-3a07-4f71-90ae-a3d395d8eec6
keywords:
- src property Windows Sidebar
- src property Windows Sidebar , image object
- image object Windows Sidebar , src property
topic_type:
- apiref
api_name:
- image.src
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

# image.src property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the image file used by the [**g:image**](image-element.md) element.

This property is read/write.

## Syntax


```JScript
strsrc = image.src
image.src(strUNC) = strsrc
```



## Property value

a UNC path or a URI.

## Remarks

Valid image filetypes are .JPG, .BMP, .GIF, or .PNG.

Special characters in UNC paths should be escaped with a '\\'.

## Examples

The following example demonstrates how to specify a new image for the [**g:image**](image-element.md) element from a gadget script file.


```JScript
// imgBackground is the value of the 'id' attribute for the g:background element.
var imgSrc = imgBackground.addImageObject(file, intX, intY);
imgSrc.src = "..\\aero\%logo.png";
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

 

 





