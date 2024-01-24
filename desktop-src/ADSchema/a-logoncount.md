---
title: Logon-Count attribute
description: The number of times the account has successfully logged on. A value of 0 indicates that the value is unknown.
ms.assetid: 8b12bea7-dfc3-46e3-a4a2-92b5f1239b98
ms.tgt_platform: multiple
keywords:
- Logon-Count attribute AD Schema
- logonCount attribute AD Schema
topic_type:
- apiref
api_name:
- Logon-Count
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Logon-Count attribute

The number of times the account has successfully logged on. A value of 0 indicates that the value is unknown.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Logon-Count                          |
| Ldap-Display-Name | logonCount                           |
| Size              | 4 bytes                              |
| Update Privilege  | Domain administrator                 |
| Update Frequency  | Each time the user logs on.          |
| Attribute-Id      | 1.2.840.113556.1.4.169               |
| System-Id-Guid    | bf9679aa-0de6-11d0-a285-00aa003049e2 |
| Syntax            | [**Enumeration**](s-enumeration.md) |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000011                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000011                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000011                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000011                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000011                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000011                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Remarks

This attribute is not replicated and is maintained on each domain controller in the domain. To get an accurate value for the user's total number of successful logon attempts in the domain, each domain controller in the domain must be queried and the sum of the values should be used. Keep in mind that the attribute is not replicated, therefore domain controllers that are retired may have counted logons for the user as well, and these will be missing from the count.

> [!IMPORTANT]
> Due to compatibility with 16-bit versions of LAN Manager, the attribute has an upper limit of 65535. After this limit has been reached, you cannot use it as an indicator of user activity on this domain controller.

 

 

 





