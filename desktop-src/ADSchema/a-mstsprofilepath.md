---
title: ms-TS-Profile-Path attribute
description: Terminal Services Profile Path specifies a roaming or mandatory profile path to use when the user logs on to the terminal server. The profile path is in the following network path format \\\\ServerName\\ProfilesFolderName\\UserName.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '9b13f91d-c3ee-4862-800c-fda831dce859'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-schema'
ms.tgt_platform: multiple
keywords: ["ms-TS-Profile-Path attribute AD Schema", "msTSProfilePath attribute AD Schema"]
topic_type:
- apiref
api_name:
- ms-TS-Profile-Path
api_type:
- Schema
---

# ms-TS-Profile-Path attribute

Terminal Services Profile Path specifies a roaming or mandatory profile path to use when the user logs on to the terminal server. The profile path is in the following network path format: **\\\\***ServerName***\\***ProfilesFolderName***\\***UserName*.



|                   |                                             |
|-------------------|---------------------------------------------|
| CN                | ms-TS-Profile-Path                          |
| Ldap-Display-Name | msTSProfilePath                             |
| Size              | \-                                          |
| Update Privilege  | \-                                          |
| Update Frequency  | \-                                          |
| Attribute-Id      | 1.2.840.113556.1.4.1976                     |
| System-Id-Guid    | e65c30db-316c-4060-a3a0-387b083f09cd        |
| Syntax            | [**String(Unicode)**](s-string-unicode.md) |



## Implementations

-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

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
| Range-Upper            | 32767                             |
| Search-Flags           | 0x00000000                        |
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
| Range-Upper            | 32767                             |
| Search-Flags           | 0x00000000                        |
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
| Range-Upper            | 32767                             |
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



 

 





