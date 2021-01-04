---
title: Home-Directory attribute
description: The home directory for the account.
ms.assetid: 7fd431f2-f2e0-476f-82ed-04f776c234eb
ms.tgt_platform: multiple
keywords:
- Home-Directory attribute AD Schema
- homeDirectory attribute AD Schema
topic_type:
- apiref
api_name:
- Home-Directory
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Home-Directory attribute

The home directory for the account. If [**homeDrive**](a-homedrive.md) is set and specifies a drive letter, **homeDirectory** must be a UNC path. Otherwise, **homeDirectory** is a fully qualified local path including the drive letter (for example, *DriveLetter***:\\***Directory***\\***Folder*). This value can be a null string.



| Entry | Value |
|-------------------|------------------------------------------------------------------------------------|
| CN                | Home-Directory                                                                     |
| Ldap-Display-Name | homeDirectory                                                                      |
| Size              | \-                                                                                 |
| Update Privilege  | Domain administrator                                                               |
| Update Frequency  | When the user's record is created and whenever the home directory needs to change. |
| Attribute-Id      | 1.2.840.113556.1.4.44                                                              |
| System-Id-Guid    | bf967985-0de6-11d0-a285-00aa003049e2                                               |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)                                        |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-----------------------------------|
| Link-Id                | \-                                |
| MAPI-Id                | \-                                |
| System-Only            | False                             |
| Is-Single-Valued       | True                              |
| Is Indexed             | False                             |
| In Global Catalog      | False                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                      |
| Range-Lower            | \-                                |
| Range-Upper            | \-                                |
| Search-Flags           | 0x00000010                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                  |
| MAPI-Id                | \-                                                                                  |
| System-Only            | False                                                                               |
| Is-Single-Valued       | True                                                                                |
| Is Indexed             | False                                                                               |
| In Global Catalog      | False                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                        |
| Range-Lower            | \-                                                                                  |
| Range-Upper            | \-                                                                                  |
| Search-Flags           | 0x00000010                                                                          |
| System-Flags           | 0x00000010                                                                          |
| Classes used in        | [**User**](c-user.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                  |
| MAPI-Id                | \-                                                                                  |
| System-Only            | False                                                                               |
| Is-Single-Valued       | True                                                                                |
| Is Indexed             | False                                                                               |
| In Global Catalog      | False                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                        |
| Range-Lower            | \-                                                                                  |
| Range-Upper            | \-                                                                                  |
| Search-Flags           | 0x00000010                                                                          |
| System-Flags           | 0x00000010                                                                          |
| Classes used in        | [**User**](c-user.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                  |
| MAPI-Id                | \-                                                                                  |
| System-Only            | False                                                                               |
| Is-Single-Valued       | True                                                                                |
| Is Indexed             | False                                                                               |
| In Global Catalog      | False                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                        |
| Range-Lower            | \-                                                                                  |
| Range-Upper            | \-                                                                                  |
| Search-Flags           | 0x00000010                                                                          |
| System-Flags           | 0x00000010                                                                          |
| Classes used in        | [**User**](c-user.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                  |
| MAPI-Id                | \-                                                                                  |
| System-Only            | False                                                                               |
| Is-Single-Valued       | True                                                                                |
| Is Indexed             | False                                                                               |
| In Global Catalog      | False                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                        |
| Range-Lower            | \-                                                                                  |
| Range-Upper            | \-                                                                                  |
| Search-Flags           | 0x00000010                                                                          |
| System-Flags           | 0x00000010                                                                          |
| Classes used in        | [**User**](c-user.md)<br/> [**posixAccount**](c-posixaccount.md)<br/> |



## See also

<dl> <dt>

[**homeDrive**](a-homedrive.md)
</dt> </dl>

 

 





