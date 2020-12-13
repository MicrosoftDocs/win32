---
title: Security-Identifier attribute
description: A unique value of variable length used to identify a user account, group account, or logon session to which an ACE applies.
ms.assetid: bb6a16f6-d2c1-48f1-af9a-40fe2a59f281
ms.tgt_platform: multiple
keywords:
- Security-Identifier attribute AD Schema
- securityIdentifier attribute AD Schema
topic_type:
- apiref
api_name:
- Security-Identifier
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Security-Identifier attribute

A unique value of variable length used to identify a user account, group account, or logon session to which an ACE applies.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Security-Identifier                  |
| Ldap-Display-Name | securityIdentifier                   |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.121               |
| System-Id-Guid    | bf967a2f-0de6-11d0-a285-00aa003049e2 |
| Syntax            | [**String(Sid)**](s-string-sid.md)  |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                |
| MAPI-Id                | \-                                                                                                                |
| System-Only            | False                                                                                                             |
| Is-Single-Valued       | True                                                                                                              |
| Is Indexed             | False                                                                                                             |
| In Global Catalog      | False                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                      |
| Range-Lower            | \-                                                                                                                |
| Range-Upper            | \-                                                                                                                |
| Search-Flags           | 0x00000000                                                                                                        |
| System-Flags           | 0x00000010                                                                                                        |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                |
| MAPI-Id                | \-                                                                                                                |
| System-Only            | False                                                                                                             |
| Is-Single-Valued       | True                                                                                                              |
| Is Indexed             | False                                                                                                             |
| In Global Catalog      | True                                                                                                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                      |
| Range-Lower            | \-                                                                                                                |
| Range-Upper            | \-                                                                                                                |
| Search-Flags           | 0x00000000                                                                                                        |
| System-Flags           | 0x00000010                                                                                                        |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                |
| MAPI-Id                | \-                                                                                                                |
| System-Only            | False                                                                                                             |
| Is-Single-Valued       | True                                                                                                              |
| Is Indexed             | False                                                                                                             |
| In Global Catalog      | True                                                                                                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                      |
| Range-Lower            | \-                                                                                                                |
| Range-Upper            | \-                                                                                                                |
| Search-Flags           | 0x00000000                                                                                                        |
| System-Flags           | 0x00000010                                                                                                        |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                |
| MAPI-Id                | \-                                                                                                                |
| System-Only            | False                                                                                                             |
| Is-Single-Valued       | True                                                                                                              |
| Is Indexed             | False                                                                                                             |
| In Global Catalog      | True                                                                                                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                      |
| Range-Lower            | \-                                                                                                                |
| Range-Upper            | \-                                                                                                                |
| Search-Flags           | 0x00000000                                                                                                        |
| System-Flags           | 0x00000010                                                                                                        |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                |
| MAPI-Id                | \-                                                                                                                |
| System-Only            | False                                                                                                             |
| Is-Single-Valued       | True                                                                                                              |
| Is Indexed             | False                                                                                                             |
| In Global Catalog      | True                                                                                                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                      |
| Range-Lower            | \-                                                                                                                |
| Range-Upper            | \-                                                                                                                |
| Search-Flags           | 0x00000000                                                                                                        |
| System-Flags           | 0x00000010                                                                                                        |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> [**Trusted-Domain**](c-trusteddomain.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                |
| MAPI-Id                | \-                                                                                                                |
| System-Only            | False                                                                                                             |
| Is-Single-Valued       | True                                                                                                              |
| Is Indexed             | False                                                                                                             |
| In Global Catalog      | True                                                                                                              |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                      |
| Range-Lower            | \-                                                                                                                |
| Range-Upper            | \-                                                                                                                |
| Search-Flags           | 0x00000000                                                                                                        |
| System-Flags           | 0x00000010                                                                                                        |
| Classes used in        | [**Security-Principal**](c-securityprincipal.md)<br/> [**Trusted-Domain**](c-trusteddomain.md)<br/> |



 

 





