---
title: Lockout-Time attribute
description: The date and time (UTC) that this account was locked out.
ms.assetid: 4a0a66a3-9f7f-48ec-9b96-a9c3e72b2b6b
ms.tgt_platform: multiple
keywords:
- Lockout-Time attribute AD Schema
- lockoutTime attribute AD Schema
topic_type:
- apiref
api_name:
- Lockout-Time
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Lockout-Time attribute

The date and time (UTC) that this account was locked out. This value is stored as a large integer that represents the number of 100-nanosecond intervals since January 1, 1601 (UTC). A value of zero means that the account is not currently locked out.



| Entry | Value |
|-------------------|----------------------------------------------------------------------------------|
| CN                | Lockout-Time                                                                     |
| Ldap-Display-Name | lockoutTime                                                                      |
| Size              | 8 bytes                                                                          |
| Update Privilege  | Domain administrator                                                             |
| Update Frequency  | When the user's record is created and whenever the lockout time needs to change. |
| Attribute-Id      | 1.2.840.113556.1.4.662                                                           |
| System-Id-Guid    | 28630ebf-41d5-11d1-a9c1-0000f80367c1                                             |
| Syntax            | [**Interval**](s-interval.md)                                                   |



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
| Search-Flags           | 0x00000000                        |
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
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|-------------------------------------------------------------------|
| Link-Id                | \-                                                                |
| MAPI-Id                | \-                                                                |
| System-Only            | False                                                             |
| Is-Single-Valued       | True                                                              |
| Is Indexed             | False                                                             |
| In Global Catalog      | False                                                             |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                      |
| Range-Lower            | \-                                                                |
| Range-Upper            | \-                                                                |
| Search-Flags           | 0x00000000                                                        |
| System-Flags           | 0x00000010                                                        |
| Classes used in        | [**ms-DS-Bindable-Object**](c-msds-bindableobject.md)<br/> |



## Windows Server 2003 R2



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
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008



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
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2008 R2



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
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Windows Server 2012



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
| Search-Flags           | 0x00000000                        |
| System-Flags           | 0x00000010                        |
| Classes used in        | [**User**](c-user.md)<br/> |



## Remarks

The high part of this large integer corresponds to the **dwHighDateTime** member of the [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) structure and the low part corresponds to the **dwLowDateTime** member of the **FILETIME** structure.

This attribute value is only reset when the account is logged onto successfully. This means that this value may be non zero, yet the account is not locked out. To accurately determine if the account is locked out, you must add the [**Lockout-Duration**](a-lockoutduration.md) to this time and compare the result to the current time, accounting for local time zones and daylight savings time.

## See also

<dl> <dt>

[**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime)
</dt> <dt>

[**Lockout-Duration**](a-lockoutduration.md)
</dt> </dl>

 

