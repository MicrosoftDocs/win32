---
title: text.blur property
description: Gets or sets the level of blur applied to the g text element.
ms.assetid: 'c9b204f6-16e9-4d88-a72e-3507d5984a33'
keywords: ["blur property Windows Sidebar", "blur property Windows Sidebar , text object", "text object Windows Sidebar , blur property"]
topic_type:
- apiref
api_name:
- text.blur
api_location:
- Sidebar.Exe
api_type:
- COM
---

# text.blur property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the level of blur applied to the [**g:text**](gtext.md) element.

This property is read/write.

## Syntax


```JScript
iblur = text.blur
text.blur = iblur
```



## Property value

An **Integer** that specifies or receives the blur radius (or boundary). The value ranges from `0` to `100`.

<dt>



 (0)


</dt> <dd>

Default. No blur effect applied. The target element is not modified.

</dd> <dt>



 (100)


</dt> <dd>

Full blur effect applied.

</dd> </dl>

## Remarks

The opacity of the [**g:text**](gtext.md) element must be set to a value of at least 1 for the blur effect to be visible.

## Examples

The following example demonstrates how to add a blur effect to the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtBlur = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtBlur.blur = 10;
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

 

 





