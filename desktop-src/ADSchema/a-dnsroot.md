---
title: Dns-Root attribute
description: The uppermost DNS domain name assigned to a domain/directory partition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0b33daad-b5c5-4126-86fa-abd3e0006c5f
ms.prod: windows-server-dev
ms.technology: active-directory-schema
ms.tgt_platform: multiple
keywords:
- Dns-Root attribute AD Schema
- dnsRoot attribute AD Schema
topic_type:
- apiref
api_name:
- Dns-Root
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Dns-Root attribute

The uppermost DNS domain name assigned to a domain/directory partition. This is set on a crossRef object and is used, among other things, for referral generation. When searching through an entire domain tree, the search must be initiated at the Dns-Root object. This attribute can be multi-valued, in which case multiple referrals are generated.



|                   |                                             |
|-------------------|---------------------------------------------|
| CN                | Dns-Root                                    |
| Ldap-Display-Name | dnsRoot                                     |
| Size              | \-                                          |
| Update Privilege  | This value is set by the system.            |
| Update Frequency  | \-                                          |
| Attribute-Id      | 1.2.840.113556.1.4.28                       |
| System-Id-Guid    | bf967959-0de6-11d0-a285-00aa003049e2        |
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



|                        |                                            |
|------------------------|--------------------------------------------|
| Link-Id                | \-                                         |
| MAPI-Id                | \-                                         |
| System-Only            | False                                      |
| Is-Single-Valued       | False                                      |
| Is Indexed             | True                                       |
| In Global Catalog      | False                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                               |
| Range-Lower            | 1                                          |
| Range-Upper            | 255                                        |
| Search-Flags           | 0x00000001                                 |
| System-Flags           | 0x00000010                                 |
| Classes used in        | [**Cross-Ref**](c-crossref.md)<br/> |



## Windows Server 2003



|                        |                                            |
|------------------------|--------------------------------------------|
| Link-Id                | \-                                         |
| MAPI-Id                | \-                                         |
| System-Only            | False                                      |
| Is-Single-Valued       | False                                      |
| Is Indexed             | True                                       |
| In Global Catalog      | False                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                               |
| Range-Lower            | 1                                          |
| Range-Upper            | 255                                        |
| Search-Flags           | 0x00000001                                 |
| System-Flags           | 0x00000010                                 |
| Classes used in        | [**Cross-Ref**](c-crossref.md)<br/> |



## ADAM



|                        |                                            |
|------------------------|--------------------------------------------|
| Link-Id                | \-                                         |
| MAPI-Id                | \-                                         |
| System-Only            | False                                      |
| Is-Single-Valued       | False                                      |
| Is Indexed             | True                                       |
| In Global Catalog      | False                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                               |
| Range-Lower            | 1                                          |
| Range-Upper            | 255                                        |
| Search-Flags           | 0x00000001                                 |
| System-Flags           | 0x00000010                                 |
| Classes used in        | [**Cross-Ref**](c-crossref.md)<br/> |



## Windows Server 2003 R2



|                        |                                            |
|------------------------|--------------------------------------------|
| Link-Id                | \-                                         |
| MAPI-Id                | \-                                         |
| System-Only            | False                                      |
| Is-Single-Valued       | False                                      |
| Is Indexed             | True                                       |
| In Global Catalog      | False                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                               |
| Range-Lower            | 1                                          |
| Range-Upper            | 255                                        |
| Search-Flags           | 0x00000001                                 |
| System-Flags           | 0x00000010                                 |
| Classes used in        | [**Cross-Ref**](c-crossref.md)<br/> |



## Windows Server 2008



|                        |                                            |
|------------------------|--------------------------------------------|
| Link-Id                | \-                                         |
| MAPI-Id                | \-                                         |
| System-Only            | False                                      |
| Is-Single-Valued       | False                                      |
| Is Indexed             | True                                       |
| In Global Catalog      | False                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                               |
| Range-Lower            | 1                                          |
| Range-Upper            | 255                                        |
| Search-Flags           | 0x00000001                                 |
| System-Flags           | 0x00000010                                 |
| Classes used in        | [**Cross-Ref**](c-crossref.md)<br/> |



## Windows Server 2008 R2



|                        |                                            |
|------------------------|--------------------------------------------|
| Link-Id                | \-                                         |
| MAPI-Id                | \-                                         |
| System-Only            | False                                      |
| Is-Single-Valued       | False                                      |
| Is Indexed             | True                                       |
| In Global Catalog      | False                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                               |
| Range-Lower            | 1                                          |
| Range-Upper            | 255                                        |
| Search-Flags           | 0x00000001                                 |
| System-Flags           | 0x00000010                                 |
| Classes used in        | [**Cross-Ref**](c-crossref.md)<br/> |



## Windows Server 2012



|                        |                                            |
|------------------------|--------------------------------------------|
| Link-Id                | \-                                         |
| MAPI-Id                | \-                                         |
| System-Only            | False                                      |
| Is-Single-Valued       | False                                      |
| Is Indexed             | True                                       |
| In Global Catalog      | False                                      |
| NT-Security-Descriptor | O:BAG:BAD:S:                               |
| Range-Lower            | 1                                          |
| Range-Upper            | 255                                        |
| Search-Flags           | 0x00000001                                 |
| System-Flags           | 0x00000010                                 |
| Classes used in        | [**Cross-Ref**](c-crossref.md)<br/> |



 

 





