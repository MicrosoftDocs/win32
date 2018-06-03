---
title: background.addImageObject method
description: Adds a g image element to the g background element.
ms.assetid: d6a55394-6b9e-4dde-88dc-2bee16137ac3
keywords:
- addImageObject method Windows Sidebar
- addImageObject method Windows Sidebar , background object
- background object Windows Sidebar , addImageObject method
topic_type:
- apiref
api_name:
- background.addImageObject
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

# background.addImageObject method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Adds a [**g:image**](image-element.md) element to the [**g:background**](background-element.md) element.

## Syntax


```JScript
objRetVal = background.addImageObject(
  strUNC,
  intXOffset,
  intYOffset
)
```



## Parameters

<dl> <dt>

*strUNC* \[in\]
</dt> <dd>

A UNC string that specifies the new image to be added.

</dd> <dt>

*intXOffset* \[in\]
</dt> <dd>

An integer that specifies the horizontal position of the image relative to the top-left corner of the background.

</dd> <dt>

*intYOffset* \[in\]
</dt> <dd>

An integer that specifies the vertical position of the image relative to the top-left corner of the background.

</dd> </dl>

## Return value

Returns a [**g:image**](image-element.md) object.

## Remarks

The initial background image remains at the bottom of the z-order and is overlayed with the new image, which effectively becomes part of the background.

Valid image types are .JPG, .BMP, .GIF, and .PNG.

## Examples

The following example demonstrates how to add an image to a gadget background.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgGlow = imgBackground.addImageObject("file://img.png", 0, 0);
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

 

 





