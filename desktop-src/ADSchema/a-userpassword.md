---
title: User-Password attribute
description: The user's password in UTF-8 format. This is a write-only attribute.
ms.assetid: fcbd5e46-93fc-461e-aa6e-26d08114e73a
ms.tgt_platform: multiple
keywords:
- User-Password attribute AD Schema
- userPassword attribute AD Schema
topic_type:
- apiref
api_name:
- User-Password
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# User-Password attribute

The user's password in UTF-8 format. This is a write-only attribute.



| Entry | Value |
|-------------------|-------------------------------------------------------|
| CN                | User-Password                                         |
| Ldap-Display-Name | userPassword                                          |
| Size              | \-                                                    |
| Update Privilege  | Domain administrator or account owner.                |
| Update Frequency  | \-                                                    |
| Attribute-Id      | 2.5.4.35                                              |
| System-Id-Guid    | bf967a6e-0de6-11d0-a285-00aa003049e2                  |
| Syntax            | [**Object(Replica-Link)**](s-object-replica-link.md) |



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
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                     |
| MAPI-Id                | 0x8153                                                                                                                                                 |
| System-Only            | False                                                                                                                                                  |
| Is-Single-Valued       | False                                                                                                                                                  |
| Is Indexed             | False                                                                                                                                                  |
| In Global Catalog      | False                                                                                                                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                           |
| Range-Lower            | 1                                                                                                                                                      |
| Range-Upper            | 128                                                                                                                                                    |
| Search-Flags           | 0x00000000                                                                                                                                             |
| System-Flags           | 0x00000010                                                                                                                                             |
| Classes used in        | [**Organization**](c-organization.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> [**Person**](c-person.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                       |
| MAPI-Id                | 0x8153                                                                                                                                                                                                                   |
| System-Only            | False                                                                                                                                                                                                                    |
| Is-Single-Valued       | False                                                                                                                                                                                                                    |
| Is Indexed             | False                                                                                                                                                                                                                    |
| In Global Catalog      | False                                                                                                                                                                                                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                             |
| Range-Lower            | 1                                                                                                                                                                                                                        |
| Range-Upper            | 128                                                                                                                                                                                                                      |
| Search-Flags           | 0x00000000                                                                                                                                                                                                               |
| System-Flags           | 0x00000010                                                                                                                                                                                                               |
| Classes used in        | [**Organization**](c-organization.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> [**Person**](c-person.md)<br/> [**simpleSecurityObject**](c-simplesecurityobject.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                               |
| MAPI-Id                | 0x8153                                                                                                           |
| System-Only            | False                                                                                                            |
| Is-Single-Valued       | False                                                                                                            |
| Is Indexed             | False                                                                                                            |
| In Global Catalog      | False                                                                                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                     |
| Range-Lower            | 1                                                                                                                |
| Range-Upper            | 128                                                                                                              |
| Search-Flags           | 0x00000000                                                                                                       |
| System-Flags           | 0x00000010                                                                                                       |
| Classes used in        | [**Organization**](c-organization.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                           |
| MAPI-Id                | 0x8153                                                                                                                                                                                                                                                                                                                                                                       |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                        |
| In Global Catalog      | False                                                                                                                                                                                                                                                                                                                                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                 |
| Range-Lower            | 1                                                                                                                                                                                                                                                                                                                                                                            |
| Range-Upper            | 128                                                                                                                                                                                                                                                                                                                                                                          |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                   |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                   |
| Classes used in        | [**Organization**](c-organization.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> [**Person**](c-person.md)<br/> [**simpleSecurityObject**](c-simplesecurityobject.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                           |
| MAPI-Id                | 0x8153                                                                                                                                                                                                                                                                                                                                                                       |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                        |
| In Global Catalog      | False                                                                                                                                                                                                                                                                                                                                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                 |
| Range-Lower            | 1                                                                                                                                                                                                                                                                                                                                                                            |
| Range-Upper            | 128                                                                                                                                                                                                                                                                                                                                                                          |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                   |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                   |
| Classes used in        | [**Organization**](c-organization.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> [**Person**](c-person.md)<br/> [**simpleSecurityObject**](c-simplesecurityobject.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                           |
| MAPI-Id                | 0x8153                                                                                                                                                                                                                                                                                                                                                                       |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                        |
| In Global Catalog      | False                                                                                                                                                                                                                                                                                                                                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                 |
| Range-Lower            | 1                                                                                                                                                                                                                                                                                                                                                                            |
| Range-Upper            | 128                                                                                                                                                                                                                                                                                                                                                                          |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                   |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                   |
| Classes used in        | [**Organization**](c-organization.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> [**Person**](c-person.md)<br/> [**simpleSecurityObject**](c-simplesecurityobject.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                                                                                                                                                                                                                                                           |
| MAPI-Id                | 0x8153                                                                                                                                                                                                                                                                                                                                                                       |
| System-Only            | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is-Single-Valued       | False                                                                                                                                                                                                                                                                                                                                                                        |
| Is Indexed             | False                                                                                                                                                                                                                                                                                                                                                                        |
| In Global Catalog      | False                                                                                                                                                                                                                                                                                                                                                                        |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                                                                                 |
| Range-Lower            | 1                                                                                                                                                                                                                                                                                                                                                                            |
| Range-Upper            | 128                                                                                                                                                                                                                                                                                                                                                                          |
| Search-Flags           | 0x00000000                                                                                                                                                                                                                                                                                                                                                                   |
| System-Flags           | 0x00000010                                                                                                                                                                                                                                                                                                                                                                   |
| Classes used in        | [**Organization**](c-organization.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> [**Person**](c-person.md)<br/> [**simpleSecurityObject**](c-simplesecurityobject.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> [**shadowAccount**](c-shadowaccount.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> |



 

 





