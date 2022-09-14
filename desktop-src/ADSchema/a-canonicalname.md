---
title: Canonical-Name attribute
description: The name of the object in canonical format.
ms.assetid: f217e5fa-f70b-4f4d-afa6-53e4f7e8a0e1
ms.tgt_platform: multiple
keywords:
- Canonical-Name attribute AD Schema
- canonicalName attribute AD Schema
topic_type:
- apiref
api_name:
- Canonical-Name
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Canonical-Name attribute

The name of the object in canonical format. myserver2.fabrikam.com/users/jeffsmith is an example of a distinguished name in canonical format. This is a constructed attribute. The results returned are identical to those returned by the following Active Directory function: DsCrackNames(NULL, DS\_NAME\_FLAG\_SYNTACTICAL\_ONLY, DS\_FQDN\_1779\_NAME, DS\_CANONICAL\_NAME, ...).

For more information about name formats, see [**DsCrackNames**](/windows/desktop/api/ntdsapi/nf-ntdsapi-dscracknamesa).



| Entry | Value |
|-------------------|---------------------------------------------|
| CN                | Canonical-Name                              |
| Ldap-Display-Name | canonicalName                               |
| Size              | \-                                          |
| Update Privilege  | \-                                          |
| Update Frequency  | \-                                          |
| Attribute-Id      | 1.2.840.113556.1.4.916                      |
| System-Id-Guid    | 9a7ad945-ca53-11d1-bbd0-0080c76670c0        |
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
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x08000014                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x08000014                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x08000014                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x08000014                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x08000014                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x08000014                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x08000014                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



 

