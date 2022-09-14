---
title: User-Principal-Name attribute
description: This attribute contains the UPN that is an Internet-style login name for a user based on the Internet standard RFC 822.
ms.assetid: 588e76fa-45b6-4853-821a-9e5730255b9f
ms.tgt_platform: multiple
keywords:
- User-Principal-Name attribute AD Schema
- userPrincipalName attribute AD Schema
topic_type:
- apiref
api_name:
- User-Principal-Name
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# User-Principal-Name attribute

This attribute contains the UPN that is an Internet-style login name for a user based on the Internet standard [RFC 822](https://www.ietf.org/rfc/rfc0822.txt). The UPN is shorter than the distinguished name and easier to remember. By convention, this should map to the user email name. The value set for this attribute is equal to the length of the user's ID and the domain name. For more information about this attribute, see [User Naming Attributes](/windows/desktop/AD/naming-properties).



| Entry | Value |
|-------------------|---------------------------------------------|
| CN                | User-Principal-Name                         |
| Ldap-Display-Name | userPrincipalName                           |
| Size              | \-                                          |
| Update Privilege  | Domain administrator or account owner.      |
| Update Frequency  | In theory this should never change.         |
| Attribute-Id      | 1.2.840.113556.1.4.656                      |
| System-Id-Guid    | 28630ebb-41d5-11d1-a9c1-0000f80367c1        |
| Syntax            | [**String(Unicode)**](s-string-unicode.md) |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**ADAM**](#adam)
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
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000001                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000001                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|--------------|
| Link-Id                | \-           |
| MAPI-Id                | \-           |
| System-Only            | False        |
| Is-Single-Valued       | True         |
| Is Indexed             | True         |
| In Global Catalog      | True         |
| NT-Security-Descriptor | O:BAG:BAD:S: |
| Range-Lower            | \-           |
| Range-Upper            | \-           |
| Search-Flags           | 0x00000001   |
| System-Flags           | 0x00000012   |
| Classes used in        | \-           |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000001                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000001                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000001                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | True                              |
| In Global Catalog      | True                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000001                        |
| System-Flags           | 0x00000012                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Remarks

In ADAM, this attribute is not required to be in the Internet standard RFC 822 format; it can be a simple name.

 

