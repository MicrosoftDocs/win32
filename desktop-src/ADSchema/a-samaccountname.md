---
title: SAM-Account-Name attribute
description: The logon name used to support clients and servers running earlier versions of the operating system, such as Windows NT 4.0, Windows 95, Windows 98, and LAN Manager.
ms.assetid: dc661e59-9a36-4d2b-93f0-f88edf7efd66
ms.tgt_platform: multiple
keywords:
- SAM-Account-Name attribute AD Schema
- sAMAccountName attribute AD Schema
topic_type:
- apiref
api_name:
- SAM-Account-Name
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# SAM-Account-Name attribute

The logon name used to support clients and servers running earlier versions of the operating system, such as Windows NT 4.0, Windows 95, Windows 98, and LAN Manager.

This attribute must be 20 characters or less to support earlier clients, and cannot contain any of these characters:

-   "/ \\ \[ \] : ; \| = , + \* ? < >



| Entry | Value |
|-------------------|------------------------------------------------------------------------------------------|
| CN                | SAM-Account-Name                                                                         |
| Ldap-Display-Name | sAMAccountName                                                                           |
| Size              | 20 characters or less.                                                                   |
| Update Privilege  | Domain administrator                                                                     |
| Update Frequency  | This value should be assigned when the account record is created, and should not change. |
| Attribute-Id      | 1.2.840.113556.1.4.221                                                                   |
| System-Id-Guid    | 3e0abfd0-126a-11d0-a060-00aa006c33ed                                                     |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)                                              |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | 0                                                            |
| Range-Upper            | 256                                                          |
| Search-Flags           | 0x0000000D                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | 0                                                            |
| Range-Upper            | 256                                                          |
| Search-Flags           | 0x0000000D                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | 0                                                            |
| Range-Upper            | 256                                                          |
| Search-Flags           | 0x0000000D                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | 0                                                            |
| Range-Upper            | 256                                                          |
| Search-Flags           | 0x0000000D                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | 0                                                            |
| Range-Upper            | 256                                                          |
| Search-Flags           | 0x0000000D                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | True                                                         |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | 0                                                            |
| Range-Upper            | 256                                                          |
| Search-Flags           | 0x0000000D                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



 

 





