---
title: text.value property
description: Gets or sets the value of the g text element.
ms.assetid: 'f16c288a-f36d-4789-b4ba-41a17a9cb01b'
keywords: ["value property Windows Sidebar", "value property Windows Sidebar , text object", "text object Windows Sidebar , value property"]
topic_type:
- apiref
api_name:
- text.value
api_location:
- Sidebar.Exe
api_type:
- COM
---

# text.value property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the value of the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
strvalue = text.value
text.value = strvalue
```



## Property value

A **String** that specifies or receives the value to assign to the target element.

## Examples

The following example demonstrates how to set the value of the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtValue = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtValue.value = "success";
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

 

 





