---
title: System.Network.Wireless.primaryDNSAddress property
description: Gets the Internet Protocol (IP) address of the first available Domain Name System (DNS) server on the wireless network.
ms.assetid: d6254e43-88e1-4986-b378-92da056e469b
keywords:
- primaryDNSAddress property Windows Sidebar
- primaryDNSAddress property Windows Sidebar , System.Network.Wireless object
- System.Network.Wireless object Windows Sidebar , primaryDNSAddress property
topic_type:
- apiref
api_name:
- System.Network.Wireless.primaryDNSAddress
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

# System.Network.Wireless.primaryDNSAddress property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets the Internet Protocol (IP) address of the first available Domain Name System (DNS) server on the wireless network.

This property is read-only.

## Syntax


```JScript
strprimaryDNSAddress = System.Network.Wireless.primaryDNSAddress
```



## Property value

A **String** that receives the IP address.

## Remarks

If the system has multiple network interfaces, only the active one is detected.

DNS servers are used by Windows systems to cross-reference computer or domain names with IP addresses.

## Examples

The following example demonstrates how to use the **primaryDNSAddress** property.


```JScript
var mytext = "address: " + System.Network.Wireless.primaryDNSAddress;
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



 

 





