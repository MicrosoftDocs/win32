---
title: background.src property
description: Gets or sets the image file used by the g background element.
ms.assetid: '8133ec91-a2a0-49ba-b3cd-8425a6264d55'
keywords: ["src property Windows Sidebar", "src property Windows Sidebar , background object", "background object Windows Sidebar , src property"]
topic_type:
- apiref
api_name:
- background.src
api_location:
- Sidebar.Exe
api_type:
- COM
---

# background.src property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the image file used by the [**g:background**](background-element.md) element.

This property is read/write.

## Syntax


```JScript
strsrc = background.src
background.src = strsrc
```



## Property value

A **String** that specifies or receives a UNC path or a URI.

## Remarks

Valid image filetypes are .JPG, .BMP, .GIF, or .PNG.

Special characters in UNC paths should be escaped with a '\\'.

## Examples

The following example demonstrates how to specify a new image for the [**g:background**](background-element.md) element from a gadget script file.


```JScript
// imgBackground is the value of the 'id' attribute for the g:background element.
imgBackground.src = "http://www.microsoft.com/logo.gif";
// or
imgBackground.src = "..\\aero\&amp;logo.png";
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

 

 





