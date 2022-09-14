---
title: Pwd-Properties attribute
description: Password Properties. Part of Domain Policy. A bitfield to indicate complexity and storage restrictions.
ms.assetid: 9d73595f-508f-4562-a928-4833df977ab3
ms.tgt_platform: multiple
keywords:
- Pwd-Properties attribute AD Schema
- pwdProperties attribute AD Schema
topic_type:
- apiref
api_name:
- Pwd-Properties
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Pwd-Properties attribute

Password Properties. Part of Domain Policy. A bitfield to indicate complexity and storage restrictions.



| Entry | Value |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CN                | Pwd-Properties                                                                                                                                                                                                           |
| Ldap-Display-Name | pwdProperties                                                                                                                                                                                                            |
| Size              | Integer. DOMAIN\_PASSWORD\_COMPLEX 1, DOMAIN\_PASSWORD\_NO\_ANON\_CHANGE 2, DOMAIN\_PASSWORD\_NO\_CLEAR\_CHANGE 4, DOMAIN\_LOCKOUT\_ADMINS 8, DOMAIN\_PASSWORD\_STORE\_CLEARTEXT 16, DOMAIN\_REFUSE\_PASSWORD\_CHANGE 32 |
| Update Privilege  | Domain administrator                                                                                                                                                                                                     |
| Update Frequency  | When the policy for a user changes.                                                                                                                                                                                      |
| Attribute-Id      | 1.2.840.113556.1.4.93                                                                                                                                                                                                    |
| System-Id-Guid    | bf967a0b-0de6-11d0-a285-00aa003049e2                                                                                                                                                                                     |
| Syntax            | [**Enumeration**](s-enumeration.md)                                                                                                                                                                                     |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                    |
| MAPI-Id                | \-                                                                                                                                                    |
| System-Only            | False                                                                                                                                                 |
| Is-Single-Valued       | True                                                                                                                                                  |
| Is Indexed             | False                                                                                                                                                 |
| In Global Catalog      | False                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                          |
| Range-Lower            | \-                                                                                                                                                    |
| Range-Upper            | \-                                                                                                                                                    |
| Search-Flags           | 0x00000000                                                                                                                                            |
| System-Flags           | 0x00000010                                                                                                                                            |
| Classes used in        | [**Domain-Policy**](c-domainpolicy.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                    |
| MAPI-Id                | \-                                                                                                                                                    |
| System-Only            | False                                                                                                                                                 |
| Is-Single-Valued       | True                                                                                                                                                  |
| Is Indexed             | False                                                                                                                                                 |
| In Global Catalog      | False                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                          |
| Range-Lower            | \-                                                                                                                                                    |
| Range-Upper            | \-                                                                                                                                                    |
| Search-Flags           | 0x00000000                                                                                                                                            |
| System-Flags           | 0x00000010                                                                                                                                            |
| Classes used in        | [**Domain-Policy**](c-domainpolicy.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                    |
| MAPI-Id                | \-                                                                                                                                                    |
| System-Only            | False                                                                                                                                                 |
| Is-Single-Valued       | True                                                                                                                                                  |
| Is Indexed             | False                                                                                                                                                 |
| In Global Catalog      | False                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                          |
| Range-Lower            | \-                                                                                                                                                    |
| Range-Upper            | \-                                                                                                                                                    |
| Search-Flags           | 0x00000000                                                                                                                                            |
| System-Flags           | 0x00000010                                                                                                                                            |
| Classes used in        | [**Domain-Policy**](c-domainpolicy.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                    |
| MAPI-Id                | \-                                                                                                                                                    |
| System-Only            | False                                                                                                                                                 |
| Is-Single-Valued       | True                                                                                                                                                  |
| Is Indexed             | False                                                                                                                                                 |
| In Global Catalog      | False                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                          |
| Range-Lower            | \-                                                                                                                                                    |
| Range-Upper            | \-                                                                                                                                                    |
| Search-Flags           | 0x00000000                                                                                                                                            |
| System-Flags           | 0x00000010                                                                                                                                            |
| Classes used in        | [**Domain-Policy**](c-domainpolicy.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                    |
| MAPI-Id                | \-                                                                                                                                                    |
| System-Only            | False                                                                                                                                                 |
| Is-Single-Valued       | True                                                                                                                                                  |
| Is Indexed             | False                                                                                                                                                 |
| In Global Catalog      | False                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                          |
| Range-Lower            | \-                                                                                                                                                    |
| Range-Upper            | \-                                                                                                                                                    |
| Search-Flags           | 0x00000000                                                                                                                                            |
| System-Flags           | 0x00000010                                                                                                                                            |
| Classes used in        | [**Domain-Policy**](c-domainpolicy.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                    |
| MAPI-Id                | \-                                                                                                                                                    |
| System-Only            | False                                                                                                                                                 |
| Is-Single-Valued       | True                                                                                                                                                  |
| Is Indexed             | False                                                                                                                                                 |
| In Global Catalog      | False                                                                                                                                                 |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                          |
| Range-Lower            | \-                                                                                                                                                    |
| Range-Upper            | \-                                                                                                                                                    |
| Search-Flags           | 0x00000000                                                                                                                                            |
| System-Flags           | 0x00000010                                                                                                                                            |
| Classes used in        | [**Domain-Policy**](c-domainpolicy.md)<br/> [**Sam-Domain**](c-samdomain.md)<br/> [**Sam-Domain-Base**](c-samdomainbase.md)<br/> |



 

 





