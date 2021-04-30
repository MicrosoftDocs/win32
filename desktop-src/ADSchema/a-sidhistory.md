---
title: SID-History attribute
description: Contains previous SIDs used for the object if the object was moved from another domain.
ms.assetid: d738002b-fc05-4c60-aaf9-b83be61ed5a9
ms.tgt_platform: multiple
keywords:
- SID-History attribute AD Schema
- sIDHistory attribute AD Schema
topic_type:
- apiref
api_name:
- SID-History
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# SID-History attribute

Contains previous SIDs used for the object if the object was moved from another domain. Whenever an object is moved from one domain to another, a new SID is created and that new SID becomes the objectSID. The previous SID is added to the sIDHistory property.



| Entry | Value |
|-------------------|------------------------------------------------|
| CN                | SID-History                                    |
| Ldap-Display-Name | sIDHistory                                     |
| Size              | \-                                             |
| Update Privilege  | This value is set by the system.               |
| Update Frequency  | Each time the object is moved to a new domain. |
| Attribute-Id      | 1.2.840.113556.1.4.609                         |
| System-Id-Guid    | 17eb4278-d167-11d0-b002-0000f80367c1           |
| Syntax            | [**String(Sid)**](s-string-sid.md)            |



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
| System-Only            | True                                                         |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | True                                                         |
| In Global Catalog      | True                                                         |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000001                                                   |
| System-Flags           | 0x00000012                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



 

 





