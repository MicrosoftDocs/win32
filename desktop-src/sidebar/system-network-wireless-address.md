---
title: System.Network.Wireless.address property
description: Gets the Internet Protocol (IP) address of the active network adapter.
ms.assetid: '9e1550b5-dcff-40a9-8831-0731fcd39743'
keywords: ["address property Windows Sidebar", "address property Windows Sidebar , System.Network.Wireless object", "System.Network.Wireless object Windows Sidebar , address property"]
topic_type:
- apiref
api_name:
- System.Network.Wireless.address
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Network.Wireless.address property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Internet Protocol (IP) address of the active network adapter.

This property is read-only.

## Syntax


```JScript
straddress = System.Network.Wireless.address
```



## Property value

A **String** that receives the IP address.

## Remarks

If the system has multiple network interfaces, only the active interface is detected.

## Examples

The following example demonstrates how to use the **address** property.


```JScript
var mytext = "address: " + System.Network.Wireless.address;
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



 

 





