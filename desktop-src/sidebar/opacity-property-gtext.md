---
title: text.opacity property
description: Gets or sets the opacity of the g text element.
ms.assetid: 338cf6a7-ed64-4427-bd39-1b6a641ad97e
keywords:
- opacity property Windows Sidebar
- opacity property Windows Sidebar , text object
- text object Windows Sidebar , opacity property
topic_type:
- apiref
api_name:
- text.opacity
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

# text.opacity property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the opacity of the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
iopacity = text.opacity
text.opacity = iopacity
```



## Property value

An **Integer** that specifies or receives the opacity the target element. The value ranges from `0` to `100`.

<dt>



 (0)


</dt> <dd>

The target element is completely transparent.

</dd> <dt>



 (100)


</dt> <dd>

Default. The target element is completely opaque.

</dd> </dl>

## Remarks

## Examples

The following example demonstrates how to set the opacity of the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtOpacity = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtOpacity.opacity = 0;
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

 

 





