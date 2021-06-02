---
title: UAS-Compat attribute
description: Indicates if the security account manager will enforce data sizes to make Active Directory compatible with the LanManager User Account System (UAS).
ms.assetid: 745e271e-28f4-4012-83a8-606d88de0221
ms.tgt_platform: multiple
keywords:
- UAS-Compat attribute AD Schema
- uASCompat attribute AD Schema
topic_type:
- apiref
api_name:
- UAS-Compat
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# UAS-Compat attribute

Indicates if the security account manager will enforce data sizes to make Active Directory compatible with the LanManager User Account System (UAS). If this value is 0, no limits are enforced. If this value is 1, the following limits are enforced.



| Value                          | Length                         |
|--------------------------------|--------------------------------|
| Password<br/>            | 0 to 14 characters<br/>  |
| Account Name<br/>        | 0 to 20 characters<br/>  |
| Domain Name<br/>         | 0 to 15 characters<br/>  |
| Computer Name<br/>       | 0 to 15 characters<br/>  |
| Comments<br/>            | 0 to 48 characters<br/>  |
| Home Directory<br/>      | 0 to 256 characters<br/> |
| Script Path<br/>         | 0 to 256 characters<br/> |
| Time Units Per Week<br/> | 168 bits (21 bytes)<br/> |



 



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | UAS-Compat                           |
| Ldap-Display-Name | uASCompat                            |
| Size              | \-                                   |
| Update Privilege  | Performed by an administrator.       |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.155               |
| System-Id-Guid    | bf967a61-0de6-11d0-a285-00aa003049e2 |
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
|------------------------|-------------------------------------------------------|
| Link-Id                | \-                                                    |
| MAPI-Id                | \-                                                    |
| System-Only            | False                                                 |
| Is-Single-Valued       | True                                                  |
| Is Indexed             | False                                                 |
| In Global Catalog      | False                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                          |
| Range-Lower            | \-                                                    |
| Range-Upper            | \-                                                    |
| Search-Flags           | 0x00000000                                            |
| System-Flags           | 0x00000010                                            |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-------------------------------------------------------|
| Link-Id                | \-                                                    |
| MAPI-Id                | \-                                                    |
| System-Only            | False                                                 |
| Is-Single-Valued       | True                                                  |
| Is Indexed             | False                                                 |
| In Global Catalog      | False                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                          |
| Range-Lower            | \-                                                    |
| Range-Upper            | \-                                                    |
| Search-Flags           | 0x00000000                                            |
| System-Flags           | 0x00000010                                            |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-------------------------------------------------------|
| Link-Id                | \-                                                    |
| MAPI-Id                | \-                                                    |
| System-Only            | False                                                 |
| Is-Single-Valued       | True                                                  |
| Is Indexed             | False                                                 |
| In Global Catalog      | False                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                          |
| Range-Lower            | \-                                                    |
| Range-Upper            | \-                                                    |
| Search-Flags           | 0x00000000                                            |
| System-Flags           | 0x00000010                                            |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-------------------------------------------------------|
| Link-Id                | \-                                                    |
| MAPI-Id                | \-                                                    |
| System-Only            | False                                                 |
| Is-Single-Valued       | True                                                  |
| Is Indexed             | False                                                 |
| In Global Catalog      | False                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                          |
| Range-Lower            | \-                                                    |
| Range-Upper            | \-                                                    |
| Search-Flags           | 0x00000000                                            |
| System-Flags           | 0x00000010                                            |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-------------------------------------------------------|
| Link-Id                | \-                                                    |
| MAPI-Id                | \-                                                    |
| System-Only            | False                                                 |
| Is-Single-Valued       | True                                                  |
| Is Indexed             | False                                                 |
| In Global Catalog      | False                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                          |
| Range-Lower            | \-                                                    |
| Range-Upper            | \-                                                    |
| Search-Flags           | 0x00000000                                            |
| System-Flags           | 0x00000010                                            |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-------------------------------------------------------|
| Link-Id                | \-                                                    |
| MAPI-Id                | \-                                                    |
| System-Only            | False                                                 |
| Is-Single-Valued       | True                                                  |
| Is Indexed             | False                                                 |
| In Global Catalog      | False                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                          |
| Range-Lower            | \-                                                    |
| Range-Upper            | \-                                                    |
| Search-Flags           | 0x00000000                                            |
| System-Flags           | 0x00000010                                            |
| Classes used in        | [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



 

 





