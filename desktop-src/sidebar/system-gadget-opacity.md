---
title: System.Gadget.opacity property
description: Gets the gadget opacity.
ms.assetid: '476d1f79-fb6f-45e5-b6ab-89fb74bd517a'
keywords: ["opacity property Windows Sidebar", "opacity property Windows Sidebar , System.Gadget object", "System.Gadget object Windows Sidebar , opacity property"]
topic_type:
- apiref
api_name:
- System.Gadget.opacity
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Gadget.opacity property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the gadget opacity.

This property is read-only.

## Syntax


```JScript
iopacity = System.Gadget.opacity
```



## Property value

An **Integer** that receives the opacity of the gadget. The value ranges from `0` to `100`.

<dt>



 (0)


</dt> <dd>

The gadget is completely transparent.

</dd> <dt>



 (100)


</dt> <dd>

The gadget is completely opaque.

</dd> </dl>

## Remarks

The opacity can be specified in the gadget HTML and script files.

## Examples

The following example demonstrates how to get the opacity of a gadget.


```JScript
var mytext = "opacity: " + System.Gadget.opacity;
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

[**System.Gadget**](system-gadget.md)
</dt> </dl>

 

 





