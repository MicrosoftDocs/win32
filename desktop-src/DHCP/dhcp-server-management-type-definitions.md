---
title: DHCP Server Management API Type Definitions
description: The following datatypes are used by the DHCP Server Management API.
ms.assetid: 8e29f488-2978-43dd-b7ba-edad2e3e4b29
keywords:
- DHCP_IP_ADDRESS
- DHCP_OPTION_ID
- DHCP_IP_MASK
- DHCP_RESUME_HANDLE
- DHCP_ATTRIB_ID
- DHCP_RESUME_IPV6_HANDLE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DHCP Server Management API Type Definitions

The following datatypes are used by the DHCP Server Management API.


```C++
typedef DWORD DHCP_IP_ADDRESS, *PDHCP_IP_ADDRESS, *LPDHCP_IP_ADDRESS;
typedef DWORD DHCP_OPTION_ID;
typedef DWORD DHCP_IP_MASK;
typedef DWORD DHCP_RESUME_HANDLE;
typedef ULONG DHCP_ATTRIB_ID, *PDHCP_ATTRIB_ID, *LPDHCP_ATTRIB_ID;
typedef DHCP_IPV6_ADDRESS DHCP_RESUME_IPV6_HANDLE;
```



<dl> <dt>

**DHCP\_IP\_ADDRESS**
</dt> <dd>

Specifies an IP address, with the first byte containing the first number in the address, the second byte containing the second number, the third byte containing the third number, and the last byte containing the last number in the address. For example, the address 192.1.1.10 is represented as 11000000 00000001 00000001 00001010 (binary), or 3221291274 (decimal).

</dd> <dt>

**DHCP\_OPTION\_ID**
</dt> <dd>

Specifies a unique DHCP option ID number (code). For example, the IETF documentation on DHCP options (also known as BOOTP vendor extensions), [RFC 2132](Http://go.microsoft.com/fwlink/p/?linkid=84033), defines the option code for a router IP address as 4.

</dd> <dt>

**DHCP\_IP\_MASK**
</dt> <dd>

Specifies an IP subnet mask. A subnet mask is represented in the same fashion as an IP address, with each sequential numeric component of the address placed in the corresponding byte field.

</dd> <dt>

**DHCP\_RESUME\_HANDLE**
</dt> <dd>

Specifies a unique handle to specific server data (such as options or classes) during an enumeration operation. This handle allows an enumeration to handle the data in chunks; for example, the initial call to an enumeration operation passes the handle as 0. Upon execution, a handle to the data is assigned, and this returned handle can be used for subsequent operations to resume the procurement of the remaining data.

</dd> <dt>

**DHCP\_ATTRIB\_ID**
</dt> <dd>

Specifies a value uniquely identifying a DHCP server attribute. An attribute describes some aspect of the DHCP server, such as whether or not it can serve BOOTP clients, or if it is part of a directory service domain controller.

</dd> <dt>

**DHCP\_RESUME\_IPV6\_HANDLE**
</dt> <dd>

DHCP\_IPV6\_ADDRESS structure passed as a resume handle to enumeration operations on DHCPv6 servers.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Dhcpsapi.h</dt> </dl> |



 

 





