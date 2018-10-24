---
title: User-Workstations attribute
description: Contains the NetBIOS or DNS names of the computers running Windows NT Workstation or Windows 2000 Professional from which the user can log on.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 92af070b-dadd-404d-8305-d85974639958
ms.tgt_platform: multiple
keywords:
- User-Workstations attribute AD Schema
- userWorkstations attribute AD Schema
topic_type:
- apiref
api_name:
- User-Workstations
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# User-Workstations attribute

Contains the NetBIOS or DNS names of the computers running Windows NT Workstation or Windows 2000 Professional from which the user can log on. Each NetBIOS name is separated by a comma. Multiple names should be separated by commas.



|                   |                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------|
| CN                | User-Workstations                                                                          |
| Ldap-Display-Name | userWorkstations                                                                           |
| Size              | \-                                                                                         |
| Update Privilege  | Domain administrator or account owner.                                                     |
| Update Frequency  | When the user's record is created and whenever the user's login privilege needs to change. |
| Attribute-Id      | 1.2.840.113556.1.4.86                                                                      |
| System-Id-Guid    | bf9679d7-0de6-11d0-a285-00aa003049e2                                                       |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)                                                |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



|                        |                                   |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | 0                                 |
| Range-Upper            | 1024                              |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003



|                        |                                   |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | 0                                 |
| Range-Upper            | 1024                              |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003 R2



|                        |                                   |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | 0                                 |
| Range-Upper            | 1024                              |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008



|                        |                                   |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | 0                                 |
| Range-Upper            | 1024                              |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008 R2



|                        |                                   |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | 0                                 |
| Range-Upper            | 1024                              |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2012



|                        |                                   |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | 0                                 |
| Range-Upper            | 1024                              |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



 

 





