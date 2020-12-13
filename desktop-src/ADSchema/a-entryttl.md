---
title: Entry-TTL attribute
description: This operational attribute is maintained by the server and appears to be present in every dynamic entry.
ms.assetid: cac0e52e-243d-4822-9419-2af8b9352cee
ms.tgt_platform: multiple
keywords:
- Entry-TTL attribute AD Schema
- entryTTL attribute AD Schema
topic_type:
- apiref
api_name:
- Entry-TTL
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Entry-TTL attribute

This operational attribute is maintained by the server and appears to be present in every dynamic entry. The attribute is not present when the entry does not contain the dynamicObject object class. The value of this attribute is the time, in seconds, that the entry will continue to exist before disappearing from the directory. In the absence of intervening "refresh" operations, the values returned by reading the attribute in two successive searches are guaranteed to be nonincreasing. The smallest permissible value is 0, indicating that the entry may disappear without warning. The attribute is marked NO-USER-MODIFICATION because it may only be changed by using the refresh operation.



| Entry | Value |
|-------------------|---------------------------------------------|
| CN                | Entry-TTL                                   |
| Ldap-Display-Name | entryTTL                                    |
| Size              | 4 bytes. Maximum = 1 year, default = 1 day. |
| Update Privilege  | \-                                          |
| Update Frequency  | \-                                          |
| Attribute-Id      | 1.3.6.1.4.1.1466.101.119.3                  |
| System-Id-Guid    | d213decc-d81a-4384-aac2-dcfcfd631cf8        |
| Syntax            | [**Enumeration**](s-enumeration.md)        |



## Implementations

-   [**Windows Server 2003**](#windows-server-2003)
-   [**ADAM**](#adam)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | 0                                                    |
| Range-Upper            | 31557600                                             |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000014                                           |
| Classes used in        | [**Dynamic-Object**](c-dynamicobject.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | 0                                                    |
| Range-Upper            | 31557600                                             |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000014                                           |
| Classes used in        | [**Dynamic-Object**](c-dynamicobject.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | 0                                                    |
| Range-Upper            | 31557600                                             |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000014                                           |
| Classes used in        | [**Dynamic-Object**](c-dynamicobject.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | 0                                                    |
| Range-Upper            | 31557600                                             |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000014                                           |
| Classes used in        | [**Dynamic-Object**](c-dynamicobject.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | 0                                                    |
| Range-Upper            | 31557600                                             |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000014                                           |
| Classes used in        | [**Dynamic-Object**](c-dynamicobject.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------|
| Link-Id                | \-                                                   |
| MAPI-Id                | \-                                                   |
| System-Only            | False                                                |
| Is-Single-Valued       | True                                                 |
| Is Indexed             | False                                                |
| In Global Catalog      | False                                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                                         |
| Range-Lower            | 0                                                    |
| Range-Upper            | 31557600                                             |
| Search-Flags           | 0x00000000                                           |
| System-Flags           | 0x00000014                                           |
| Classes used in        | [**Dynamic-Object**](c-dynamicobject.md)<br/> |



 

 





