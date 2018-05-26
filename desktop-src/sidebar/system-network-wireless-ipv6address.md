---
title: System.Network.Wireless.ipv6Address property
description: Gets the Internet Protocol, version 6 (IPv6) address of the wireless network adapter.
ms.assetid: 8360752e-2ee3-4e06-b2a5-9ca8298f07f7
keywords:
- ipv6Address property Windows Sidebar
- ipv6Address property Windows Sidebar , System.Network.Wireless object
- System.Network.Wireless object Windows Sidebar , ipv6Address property
topic_type:
- apiref
api_name:
- System.Network.Wireless.ipv6Address
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

# System.Network.Wireless.ipv6Address property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Internet Protocol, version 6 (IPv6) address of the wireless network adapter.

This property is read-only.

## Syntax


```JScript
stripv6Address = System.Network.Wireless.ipv6Address
```



## Property value

A **String** that receives the IPv6 address.

## Remarks

If the system has multiple network interfaces, only the active one is detected.

## Examples

The following example demonstrates how to use the **ipv6Address** property.


```JScript
var mytext = "address: " + System.Network.Wireless.ipv6Address;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Naptypes.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





