---
title: image.softedge property
description: Gets or sets the amount of edge softening that is applied to the g image element.
ms.assetid: 32216e74-bdb9-4569-bc44-f050e0d01062
keywords:
- softedge property Windows Sidebar
- softedge property Windows Sidebar , image object
- image object Windows Sidebar , softedge property
topic_type:
- apiref
api_name:
- image.softedge
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

# image.softedge property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the amount of edge softening that is applied to the [**g:image**](image-element.md) element.

This property is read/write.

## Syntax


```JScript
isoftedge = image.softedge
image.softedge = isoftedge
```



## Property value

An **Integer** that specifies or receives the radius, in pixels, of the **softEdge** effect. The value ranges from `0` to `30`.

<dt>



 (0)


</dt> <dd>

Default. No edge softening applied. The target element is not modified.

</dd> <dt>



 (30)


</dt> <dd>

Maximum edge softening applied.

</dd> </dl>

## Remarks

**softEdge** blurs the outside edge of the element by the specified radius. This is in contrast to the [**blur**](blur-property-gimage.md) effect, which blurs the entire element.

The **softEdge** effect can be specified in the gadget HTML and script files.

The opacity of the [**g:image**](image-element.md) element must be set to a value of at least 1 for the **softEdge** effect to be visible.

## Examples

The following example demonstrates how to add a **softEdge** effect to the [**g:image**](image-element.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgSoftedge = imgBackground.addImageObject(file, intX, intY);
imgSoftedge.softedge = 5;
```



The following example demonstrates how to add a **softEdge** effect to the [**g:image**](image-element.md) element in the gadget HTML file.


```JScript
<g:image src="..\aerologo.png" softedge="5"/>
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

 

 





