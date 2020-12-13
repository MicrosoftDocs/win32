---
title: Manager attribute
description: Contains the distinguished name of the user who is the user's manager. The manager's user object contains a directReports property that contains references to all user objects that have their manager properties set to this distinguished name.
ms.assetid: 40743784-a99c-4ec0-9140-9f865c073244
ms.tgt_platform: multiple
keywords:
- Manager attribute AD Schema
- manager attribute AD Schema
topic_type:
- apiref
api_name:
- Manager
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Manager attribute

Contains the distinguished name of the user who is the user's manager. The manager's user object contains a directReports property that contains references to all user objects that have their manager properties set to this distinguished name.



| Entry | Value |
|-------------------|-----------------------------------------------------------------------------|
| CN                | Manager                                                                     |
| Ldap-Display-Name | manager                                                                     |
| Size              | \-                                                                          |
| Update Privilege  | Domain administrator or account owner.                                      |
| Update Frequency  | When the user's record is created and whenever the manager needs to change. |
| Attribute-Id      | 0.9.2342.19200300.100.1.10                                                  |
| System-Id-Guid    | bf9679b5-0de6-11d0-a285-00aa003049e2                                        |
| Syntax            | [**Object(DS-DN)**](s-object-ds-dn.md)                                     |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|--------------------------------------------------------------------|
| Link-Id                | 42                                                                 |
| MAPI-Id                | 0x8005                                                             |
| System-Only            | False                                                              |
| Is-Single-Valued       | True                                                               |
| Is Indexed             | False                                                              |
| In Global Catalog      | True                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                       |
| Range-Lower            | \-                                                                 |
| Range-Upper            | \-                                                                 |
| Search-Flags           | 0x00000010                                                         |
| System-Flags           | 0x00000010                                                         |
| Classes used in        | [**Organizational-Person**](c-organizationalperson.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | 42                                                                                                                     |
| MAPI-Id                | 0x8005                                                                                                                 |
| System-Only            | False                                                                                                                  |
| Is-Single-Valued       | True                                                                                                                   |
| Is Indexed             | False                                                                                                                  |
| In Global Catalog      | True                                                                                                                   |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                           |
| Range-Lower            | \-                                                                                                                     |
| Range-Upper            | \-                                                                                                                     |
| Search-Flags           | 0x00000010                                                                                                             |
| System-Flags           | 0x00000010                                                                                                             |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Organizational-Person**](c-organizationalperson.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | 42                                                                                                                     |
| MAPI-Id                | 0x8005                                                                                                                 |
| System-Only            | False                                                                                                                  |
| Is-Single-Valued       | True                                                                                                                   |
| Is Indexed             | False                                                                                                                  |
| In Global Catalog      | True                                                                                                                   |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                           |
| Range-Lower            | \-                                                                                                                     |
| Range-Upper            | \-                                                                                                                     |
| Search-Flags           | 0x00000010                                                                                                             |
| System-Flags           | 0x00000010                                                                                                             |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Organizational-Person**](c-organizationalperson.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | 42                                                                                                                     |
| MAPI-Id                | 0x8005                                                                                                                 |
| System-Only            | False                                                                                                                  |
| Is-Single-Valued       | True                                                                                                                   |
| Is Indexed             | False                                                                                                                  |
| In Global Catalog      | True                                                                                                                   |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                           |
| Range-Lower            | \-                                                                                                                     |
| Range-Upper            | \-                                                                                                                     |
| Search-Flags           | 0x00000010                                                                                                             |
| System-Flags           | 0x00000010                                                                                                             |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Organizational-Person**](c-organizationalperson.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | 42                                                                                                                     |
| MAPI-Id                | 0x8005                                                                                                                 |
| System-Only            | False                                                                                                                  |
| Is-Single-Valued       | True                                                                                                                   |
| Is Indexed             | False                                                                                                                  |
| In Global Catalog      | True                                                                                                                   |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                           |
| Range-Lower            | \-                                                                                                                     |
| Range-Upper            | \-                                                                                                                     |
| Search-Flags           | 0x00000010                                                                                                             |
| System-Flags           | 0x00000010                                                                                                             |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Organizational-Person**](c-organizationalperson.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | 42                                                                                                                     |
| MAPI-Id                | 0x8005                                                                                                                 |
| System-Only            | False                                                                                                                  |
| Is-Single-Valued       | True                                                                                                                   |
| Is Indexed             | False                                                                                                                  |
| In Global Catalog      | True                                                                                                                   |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                           |
| Range-Lower            | \-                                                                                                                     |
| Range-Upper            | \-                                                                                                                     |
| Search-Flags           | 0x00000010                                                                                                             |
| System-Flags           | 0x00000010                                                                                                             |
| Classes used in        | [**inetOrgPerson**](c-inetorgperson.md)<br/> [**Organizational-Person**](c-organizationalperson.md)<br/> |



 

 





