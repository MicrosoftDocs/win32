---
title: text.align property
description: Gets or sets the text alignment.
ms.assetid: 2aef9d9d-64f8-45a9-8372-74a2331347b6
keywords:
- align property Windows Sidebar
- align property Windows Sidebar , text object
- text object Windows Sidebar , align property
topic_type:
- apiref
api_name:
- text.align
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

# text.align property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the text alignment.

This property is read/write.

## Syntax


```JScript
ialign = text.align
text.align = ialign
```



## Property value

An **Integer** that specifies or receives the text alignment.

<dt>



 (0)


</dt> <dd>

Default. Based on Sidebar alignment. Text is aligned right when the Sidebar is anchored to the right and aligned left when the Sidebar is anchored to the left.

</dd> <dt>



 (1)


</dt> <dd>

Center.

</dd> <dt>



 (2)


</dt> <dd>

Left.

</dd> <dt>



 (4)


</dt> <dd>

Right.

</dd> </dl>

## Examples

The following example demonstrates how to align a [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtAlign = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtAlign.align = 1;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Safeint.h</dt> </dl>                           |
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

 

 





