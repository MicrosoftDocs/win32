---
title: Token-Groups attribute
description: A computed attribute that contains the list of SIDs due to a transitive group membership expansion operation on a given user or computer. Token Groups cannot be retrieved if no Global Catalog is present to retrieve the transitive reverse memberships.
ms.assetid: bb430c9f-20b7-4f21-804d-fbd4864b6505
ms.tgt_platform: multiple
keywords:
- Token-Groups attribute AD Schema
- tokenGroups attribute AD Schema
topic_type:
- apiref
api_name:
- Token-Groups
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Token-Groups attribute

A computed attribute that contains the list of SIDs due to a transitive group membership expansion operation on a given user or computer. Token Groups cannot be retrieved if no Global Catalog is present to retrieve the transitive reverse memberships.

> [!NOTE]
> Retrieving Token Groups is an expensive operation on the domain controllers, requiring a BASE scope LDAP query to return the attribute values for a given security principal object. Care should be taken when scaling the use of this attribute in larger environments. It can impact overall domain controller performance up to the point that it prevents the domain controller from processing other requests. 



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Token-Groups                         |
| Ldap-Display-Name | tokenGroups                          |
| Size              | \-                                   |
| Update Privilege  | This value is set by the system.     |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.1301              |
| System-Id-Guid    | b7c69e6d-2cc7-11d2-854e-00a0c983f608 |
| Syntax            | [**String(Sid)**](s-string-sid.md)  |



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
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | False                                                        |
| In Global Catalog      | False                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000000                                                   |
| System-Flags           | 0x08000014                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | False                                                        |
| In Global Catalog      | False                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000000                                                   |
| System-Flags           | 0x08000014                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | False                                                        |
| In Global Catalog      | False                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000000                                                   |
| System-Flags           | 0x08000014                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | False                                                        |
| In Global Catalog      | False                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000000                                                   |
| System-Flags           | 0x08000014                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | False                                                        |
| In Global Catalog      | False                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000000                                                   |
| System-Flags           | 0x08000014                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | False                                                        |
| In Global Catalog      | False                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000000                                                   |
| System-Flags           | 0x08000014                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|--------------------------------------------------------------|
| Link-Id                | \-                                                           |
| MAPI-Id                | \-                                                           |
| System-Only            | False                                                        |
| Is-Single-Valued       | False                                                        |
| Is Indexed             | False                                                        |
| In Global Catalog      | False                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                 |
| Range-Lower            | \-                                                           |
| Range-Upper            | \-                                                           |
| Search-Flags           | 0x00000000                                                   |
| System-Flags           | 0x08000014                                                   |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> |



 

 





