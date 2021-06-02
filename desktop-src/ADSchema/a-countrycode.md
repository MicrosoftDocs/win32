---
title: Country-Code attribute
description: Specifies the country/region code for the user's language of choice. This value is not used by Windows 2000.
ms.assetid: 7011cb76-aa86-4203-bcc4-0136bb11c403
ms.tgt_platform: multiple
keywords:
- Country-Code attribute AD Schema
- countryCode attribute AD Schema
topic_type:
- apiref
api_name:
- Country-Code
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Country-Code attribute

Specifies the country/region code for the user's language of choice. This value is not used by Windows 2000.



| Entry | Value |
|-------------------|-----------------------------------------|
| CN                | Country-Code                            |
| Ldap-Display-Name | countryCode                             |
| Size              | 2 bytes                                 |
| Update Privilege  | Account owner or domain administrator   |
| Update Frequency  | When the user's country/region changes. |
| Attribute-Id      | 1.2.840.113556.1.4.25                   |
| System-Id-Guid    | 5fd42471-1262-11d0-a060-00aa006c33ed    |
| Syntax            | [**Enumeration**](s-enumeration.md)    |



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
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                |
| MAPI-Id                | \-                                                                                                                                |
| System-Only            | False                                                                                                                             |
| Is-Single-Valued       | True                                                                                                                              |
| Is Indexed             | False                                                                                                                             |
| In Global Catalog      | False                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                      |
| Range-Lower            | \-                                                                                                                                |
| Range-Upper            | \-                                                                                                                                |
| Search-Flags           | 0x00000010                                                                                                                        |
| System-Flags           | 0x00000010                                                                                                                        |
| Classes used in        | [**Organizational-Person**](c-organizationalperson.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                |
| MAPI-Id                | \-                                                                                                                                |
| System-Only            | False                                                                                                                             |
| Is-Single-Valued       | True                                                                                                                              |
| Is Indexed             | False                                                                                                                             |
| In Global Catalog      | False                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                      |
| Range-Lower            | 0                                                                                                                                 |
| Range-Upper            | 65535                                                                                                                             |
| Search-Flags           | 0x00000010                                                                                                                        |
| System-Flags           | 0x00000010                                                                                                                        |
| Classes used in        | [**Organizational-Person**](c-organizationalperson.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|----------------------------------------------------------------|
| Link-Id                | \-                                                             |
| MAPI-Id                | \-                                                             |
| System-Only            | False                                                          |
| Is-Single-Valued       | True                                                           |
| Is Indexed             | False                                                          |
| In Global Catalog      | False                                                          |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                   |
| Range-Lower            | 0                                                              |
| Range-Upper            | 65535                                                          |
| Search-Flags           | 0x00000010                                                     |
| System-Flags           | 0x00000010                                                     |
| Classes used in        | [**Organizational-Unit**](c-organizationalunit.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                |
| MAPI-Id                | \-                                                                                                                                |
| System-Only            | False                                                                                                                             |
| Is-Single-Valued       | True                                                                                                                              |
| Is Indexed             | False                                                                                                                             |
| In Global Catalog      | False                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                      |
| Range-Lower            | 0                                                                                                                                 |
| Range-Upper            | 65535                                                                                                                             |
| Search-Flags           | 0x00000010                                                                                                                        |
| System-Flags           | 0x00000010                                                                                                                        |
| Classes used in        | [**Organizational-Person**](c-organizationalperson.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                |
| MAPI-Id                | \-                                                                                                                                |
| System-Only            | False                                                                                                                             |
| Is-Single-Valued       | True                                                                                                                              |
| Is Indexed             | False                                                                                                                             |
| In Global Catalog      | False                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                      |
| Range-Lower            | 0                                                                                                                                 |
| Range-Upper            | 65535                                                                                                                             |
| Search-Flags           | 0x00000010                                                                                                                        |
| System-Flags           | 0x00000010                                                                                                                        |
| Classes used in        | [**Organizational-Person**](c-organizationalperson.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                |
| MAPI-Id                | \-                                                                                                                                |
| System-Only            | False                                                                                                                             |
| Is-Single-Valued       | True                                                                                                                              |
| Is Indexed             | False                                                                                                                             |
| In Global Catalog      | False                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                      |
| Range-Lower            | 0                                                                                                                                 |
| Range-Upper            | 65535                                                                                                                             |
| Search-Flags           | 0x00000010                                                                                                                        |
| System-Flags           | 0x00000010                                                                                                                        |
| Classes used in        | [**Organizational-Person**](c-organizationalperson.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                |
| MAPI-Id                | \-                                                                                                                                |
| System-Only            | False                                                                                                                             |
| Is-Single-Valued       | True                                                                                                                              |
| Is Indexed             | False                                                                                                                             |
| In Global Catalog      | False                                                                                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                      |
| Range-Lower            | 0                                                                                                                                 |
| Range-Upper            | 65535                                                                                                                             |
| Search-Flags           | 0x00000010                                                                                                                        |
| System-Flags           | 0x00000010                                                                                                                        |
| Classes used in        | [**Organizational-Person**](c-organizationalperson.md)<br/> [**Organizational-Unit**](c-organizationalunit.md)<br/> |



 

 





