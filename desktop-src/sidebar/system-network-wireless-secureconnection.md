---
title: System.Network.Wireless.secureConnection property
description: Gets whether the current connection is secure.
ms.assetid: 'a4fec351-808e-4e68-a5ca-0fdb59f3bd4c'
keywords: ["secureConnection property Windows Sidebar", "secureConnection property Windows Sidebar , System.Network.Wireless object", "System.Network.Wireless object Windows Sidebar , secureConnection property"]
topic_type:
- apiref
api_name:
- System.Network.Wireless.secureConnection
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Network.Wireless.secureConnection property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets whether the current connection is secure.

This property is read-only.

## Syntax


```JScript
bsecureConnection = System.Network.Wireless.secureConnection
```



## Property value

A **Boolean** that receives the state of the current connection.

<dt>



 (TRUE)


</dt> <dd>

The connection is secure.

</dd> <dt>



 (FALSE)


</dt> <dd>

The connection is not secure.

</dd> </dl>

## Remarks

If the system has multiple network interfaces, only the active one is detected.

## Examples

The following example demonstrates how to use the **secureConnection** property.


```JScript
var mytext = "Secure: " + System.Network.Wireless.secureConnection;
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



 

 





