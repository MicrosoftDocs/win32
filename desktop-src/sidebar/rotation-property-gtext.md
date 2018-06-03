---
title: text.rotation property
description: Gets or sets the degree of rotation applied to the g text element.
ms.assetid: abefaca7-321f-40cd-b182-49978285cb43
keywords:
- rotation property Windows Sidebar
- rotation property Windows Sidebar , text object
- text object Windows Sidebar , rotation property
topic_type:
- apiref
api_name:
- text.rotation
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

# text.rotation property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the degree of rotation applied to the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
rotation = text.rotation
text.rotation = rotation
```



## Property value

A **Floating-point** that specifies or receives the degree of rotation. Positive values indicate clockwise rotation and negative values indicate counter-clockwise rotation.

<dt>



 (0)


</dt> <dd>

Default. No rotation applied. The target element is not modified.

</dd> </dl>

## Examples

The following example demonstrates how to rotate the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtRotation = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtRotation.rotation = 90.0;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>D2d1helper.h</dt> </dl>                        |
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

 

 





