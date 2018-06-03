---
title: dhcp-Type attribute
description: The type of DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 46ab7db7-a752-45aa-a10b-1195b5cf6f80
ms.prod: windows-server-dev
ms.technology: active-directory-schema
ms.tgt_platform: multiple
keywords:
- dhcp-Type attribute AD Schema
- dhcpType attribute AD Schema
topic_type:
- apiref
api_name:
- dhcp-Type
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# dhcp-Type attribute

The type of DHCP server. This attribute is set on all objects of objectClass [**dHCPClass**](c-dhcpclass.md). Its value defines the type of object:

``` syntax
  0 - DHCP Root Object
  1 - DHCP Server
```



|                   |                                                        |
|-------------------|--------------------------------------------------------|
| CN                | dhcp-Type                                              |
| Ldap-Display-Name | dhcpType                                               |
| Size              | 4 bytes                                                |
| Update Privilege  | Domain administrator.                                  |
| Update Frequency  | When a new server is added or removed from the forest. |
| Attribute-Id      | 1.2.840.113556.1.4.699                                 |
| System-Id-Guid    | 963d273b-48be-11d1-a9c3-0000f80367c1                   |
| Syntax            | [**Enumeration**](s-enumeration.md)                   |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



|                        |                                              |
|------------------------|----------------------------------------------|
| Link-Id                | \-                                           |
| MAPI-Id                | \-                                           |
| System-Only            | False                                        |
| Is-Single-Valued       | True                                         |
| Is Indexed             | True                                         |
| In Global Catalog      | False                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                 |
| Range-Lower            | \-                                           |
| Range-Upper            | \-                                           |
| Search-Flags           | 0x00000001                                   |
| System-Flags           | 0x00000010                                   |
| Classes used in        | [**DHCP-Class**](c-dhcpclass.md)<br/> |



## Windows Server 2003



|                        |                                              |
|------------------------|----------------------------------------------|
| Link-Id                | \-                                           |
| MAPI-Id                | \-                                           |
| System-Only            | False                                        |
| Is-Single-Valued       | True                                         |
| Is Indexed             | True                                         |
| In Global Catalog      | False                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                 |
| Range-Lower            | \-                                           |
| Range-Upper            | \-                                           |
| Search-Flags           | 0x00000001                                   |
| System-Flags           | 0x00000010                                   |
| Classes used in        | [**DHCP-Class**](c-dhcpclass.md)<br/> |



## Windows Server 2003 R2



|                        |                                              |
|------------------------|----------------------------------------------|
| Link-Id                | \-                                           |
| MAPI-Id                | \-                                           |
| System-Only            | False                                        |
| Is-Single-Valued       | True                                         |
| Is Indexed             | True                                         |
| In Global Catalog      | False                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                 |
| Range-Lower            | \-                                           |
| Range-Upper            | \-                                           |
| Search-Flags           | 0x00000001                                   |
| System-Flags           | 0x00000010                                   |
| Classes used in        | [**DHCP-Class**](c-dhcpclass.md)<br/> |



## Windows Server 2008



|                        |                                              |
|------------------------|----------------------------------------------|
| Link-Id                | \-                                           |
| MAPI-Id                | \-                                           |
| System-Only            | False                                        |
| Is-Single-Valued       | True                                         |
| Is Indexed             | True                                         |
| In Global Catalog      | False                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                 |
| Range-Lower            | \-                                           |
| Range-Upper            | \-                                           |
| Search-Flags           | 0x00000001                                   |
| System-Flags           | 0x00000010                                   |
| Classes used in        | [**DHCP-Class**](c-dhcpclass.md)<br/> |



## Windows Server 2008 R2



|                        |                                              |
|------------------------|----------------------------------------------|
| Link-Id                | \-                                           |
| MAPI-Id                | \-                                           |
| System-Only            | False                                        |
| Is-Single-Valued       | True                                         |
| Is Indexed             | True                                         |
| In Global Catalog      | False                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                 |
| Range-Lower            | \-                                           |
| Range-Upper            | \-                                           |
| Search-Flags           | 0x00000001                                   |
| System-Flags           | 0x00000010                                   |
| Classes used in        | [**DHCP-Class**](c-dhcpclass.md)<br/> |



## Windows Server 2012



|                        |                                              |
|------------------------|----------------------------------------------|
| Link-Id                | \-                                           |
| MAPI-Id                | \-                                           |
| System-Only            | False                                        |
| Is-Single-Valued       | True                                         |
| Is Indexed             | True                                         |
| In Global Catalog      | False                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                 |
| Range-Lower            | \-                                           |
| Range-Upper            | \-                                           |
| Search-Flags           | 0x00000001                                   |
| System-Flags           | 0x00000010                                   |
| Classes used in        | [**DHCP-Class**](c-dhcpclass.md)<br/> |



 

 





