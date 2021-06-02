---
title: Object-Sid attribute
description: A binary value that specifies the security identifier (SID) of the user. The SID is a unique value used to identify the user as a security principal.
ms.assetid: 78ef0158-f59e-43df-b3fc-fb0f709936f6
ms.tgt_platform: multiple
keywords:
- Object-Sid attribute AD Schema
- objectSid attribute AD Schema
topic_type:
- apiref
api_name:
- Object-Sid
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Object-Sid attribute

A binary value that specifies the security identifier (SID) of the user. The SID is a unique value used to identify the user as a security principal.



| Entry | Value |
|-------------------|--------------------------------------------------------------|
| CN                | Object-Sid                                                   |
| Ldap-Display-Name | objectSid                                                    |
| Size              | \-                                                           |
| Update Privilege  | This value is set by the system.                             |
| Update Frequency  | This value is set by the system when the account is created. |
| Attribute-Id      | 1.2.840.113556.1.4.146                                       |
| System-Id-Guid    | bf9679e8-0de6-11d0-a285-00aa003049e2                         |
| Syntax            | [**String(Sid)**](s-string-sid.md)                          |



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
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                         |
| MAPI-Id                | 0x8027                                                                                                                                                                                                                                                     |
| System-Only            | False                                                                                                                                                                                                                                                      |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                       |
| Is Indexed             | True                                                                                                                                                                                                                                                       |
| In Global Catalog      | True                                                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                                                          |
| Range-Upper            | 28                                                                                                                                                                                                                                                         |
| Search-Flags           | 0x00000009                                                                                                                                                                                                                                                 |
| System-Flags           | 0x00000012                                                                                                                                                                                                                                                 |
| Classes used in        | [**Foreign-Security-Principal**](c-foreignsecurityprincipal.md)<br/> [**MSMQ-Migrated-User**](c-msmqmigrateduser.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                         |
| MAPI-Id                | 0x8027                                                                                                                                                                                                                                                     |
| System-Only            | True                                                                                                                                                                                                                                                       |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                       |
| Is Indexed             | True                                                                                                                                                                                                                                                       |
| In Global Catalog      | True                                                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                                                          |
| Range-Upper            | 28                                                                                                                                                                                                                                                         |
| Search-Flags           | 0x00000009                                                                                                                                                                                                                                                 |
| System-Flags           | 0x00000012                                                                                                                                                                                                                                                 |
| Classes used in        | [**Foreign-Security-Principal**](c-foreignsecurityprincipal.md)<br/> [**MSMQ-Migrated-User**](c-msmqmigrateduser.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                               |
| MAPI-Id                | 0x8027                                                                                                                                                                                           |
| System-Only            | True                                                                                                                                                                                             |
| Is-Single-Valued       | True                                                                                                                                                                                             |
| Is Indexed             | True                                                                                                                                                                                             |
| In Global Catalog      | True                                                                                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                     |
| Range-Lower            | 0                                                                                                                                                                                                |
| Range-Upper            | 28                                                                                                                                                                                               |
| Search-Flags           | 0x00000009                                                                                                                                                                                       |
| System-Flags           | 0x00000012                                                                                                                                                                                       |
| Classes used in        | [**Foreign-Security-Principal**](c-foreignsecurityprincipal.md)<br/> [**ms-DS-Bind-Proxy**](c-msds-bindproxy.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                         |
| MAPI-Id                | 0x8027                                                                                                                                                                                                                                                     |
| System-Only            | True                                                                                                                                                                                                                                                       |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                       |
| Is Indexed             | True                                                                                                                                                                                                                                                       |
| In Global Catalog      | True                                                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                                                          |
| Range-Upper            | 28                                                                                                                                                                                                                                                         |
| Search-Flags           | 0x00000009                                                                                                                                                                                                                                                 |
| System-Flags           | 0x00000012                                                                                                                                                                                                                                                 |
| Classes used in        | [**Foreign-Security-Principal**](c-foreignsecurityprincipal.md)<br/> [**MSMQ-Migrated-User**](c-msmqmigrateduser.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                         |
| MAPI-Id                | 0x8027                                                                                                                                                                                                                                                     |
| System-Only            | True                                                                                                                                                                                                                                                       |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                       |
| Is Indexed             | True                                                                                                                                                                                                                                                       |
| In Global Catalog      | True                                                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                                                          |
| Range-Upper            | 28                                                                                                                                                                                                                                                         |
| Search-Flags           | 0x00000009                                                                                                                                                                                                                                                 |
| System-Flags           | 0x00000012                                                                                                                                                                                                                                                 |
| Classes used in        | [**Foreign-Security-Principal**](c-foreignsecurityprincipal.md)<br/> [**MSMQ-Migrated-User**](c-msmqmigrateduser.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                         |
| MAPI-Id                | 0x8027                                                                                                                                                                                                                                                     |
| System-Only            | True                                                                                                                                                                                                                                                       |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                       |
| Is Indexed             | True                                                                                                                                                                                                                                                       |
| In Global Catalog      | True                                                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                                                          |
| Range-Upper            | 28                                                                                                                                                                                                                                                         |
| Search-Flags           | 0x00000009                                                                                                                                                                                                                                                 |
| System-Flags           | 0x00000012                                                                                                                                                                                                                                                 |
| Classes used in        | [**Foreign-Security-Principal**](c-foreignsecurityprincipal.md)<br/> [**MSMQ-Migrated-User**](c-msmqmigrateduser.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                         |
| MAPI-Id                | 0x8027                                                                                                                                                                                                                                                     |
| System-Only            | True                                                                                                                                                                                                                                                       |
| Is-Single-Valued       | True                                                                                                                                                                                                                                                       |
| Is Indexed             | True                                                                                                                                                                                                                                                       |
| In Global Catalog      | True                                                                                                                                                                                                                                                       |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                               |
| Range-Lower            | 0                                                                                                                                                                                                                                                          |
| Range-Upper            | 28                                                                                                                                                                                                                                                         |
| Search-Flags           | 0x00000009                                                                                                                                                                                                                                                 |
| System-Flags           | 0x00000012                                                                                                                                                                                                                                                 |
| Classes used in        | [**Foreign-Security-Principal**](c-foreignsecurityprincipal.md)<br/> [**MSMQ-Migrated-User**](c-msmqmigrateduser.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |



 

 





