---
title: image.rotation property
description: Gets or sets the degree of rotation applied to the g image element.
ms.assetid: '16628f01-1c09-4f56-ae59-050c589a3c65'
keywords: ["rotation property Windows Sidebar", "rotation property Windows Sidebar , image object", "image object Windows Sidebar , rotation property"]
topic_type:
- apiref
api_name:
- image.rotation
api_location:
- Sidebar.Exe
api_type:
- COM
---

# image.rotation property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the degree of rotation applied to the [**g:image**](image-element.md) element.

This property is read/write.

## Syntax


```JScript
rotation = image.rotation
image.rotation = rotation
```



## Property value

A **Floating-point** that specifies or receives the degree of rotation. Positive values indicate clockwise rotation and negative values indicate counter-clockwise rotation.

<dt>



 (0)


</dt> <dd>

Default. No rotation applied. The target element is not modified.

</dd> </dl>

## Remarks

The rotation amount can be specified in the gadget HTML and script files.

## Examples

The following example demonstrates how to rotate the [**g:image**](image-element.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgRotation = imgBackground.addImageObject(file, intX, intY);
imgRotation.rotation = 90.0;
```



The following example demonstrates how to rotate the [**g:background**](background-element.md) element in the gadget HTML file.


```JScript
<g:image src="..\aerologo.png" rotation="90.0"/>
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
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

 

 





