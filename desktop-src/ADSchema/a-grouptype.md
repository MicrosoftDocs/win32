---
title: Group-Type attribute
description: Contains a set of flags that define the type and scope of a group object.
ms.assetid: cd37ed2f-8503-4227-b0d2-c8135605cb84
ms.tgt_platform: multiple
keywords:
- Group-Type attribute AD Schema
- groupType attribute AD Schema
topic_type:
- apiref
api_name:
- Group-Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Group-Type attribute

Contains a set of flags that define the type and scope of a group object. For the possible values for this attribute, see Remarks.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Group-Type                           |
| Ldap-Display-Name | groupType                            |
| Size              | \-                                   |
| Update Privilege  | Domain administrator                 |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.750               |
| System-Id-Guid    | 9a9a021e-4a5b-11d1-a9c3-0000f80367c1 |
| Syntax            | [**Enumeration**](s-enumeration.md) |



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
|------------------------|-------------------------------------|
| Link-Id                | \-                                  |
| MAPI-Id                | \-                                  |
| System-Only            | False                               |
| Is-Single-Valued       | True                                |
| Is Indexed             | True                                |
| In Global Catalog      | True                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                        |
| Range-Lower            | \-                                  |
| Range-Upper            | \-                                  |
| Search-Flags           | 0x00000009                          |
| System-Flags           | 0x00000012                          |
| Classes used in        | [**Group**](c-group.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-------------------------------------|
| Link-Id                | \-                                  |
| MAPI-Id                | \-                                  |
| System-Only            | False                               |
| Is-Single-Valued       | True                                |
| Is Indexed             | True                                |
| In Global Catalog      | True                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                        |
| Range-Lower            | \-                                  |
| Range-Upper            | \-                                  |
| Search-Flags           | 0x00000009                          |
| System-Flags           | 0x00000012                          |
| Classes used in        | [**Group**](c-group.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|-------------------------------------|
| Link-Id                | \-                                  |
| MAPI-Id                | \-                                  |
| System-Only            | False                               |
| Is-Single-Valued       | True                                |
| Is Indexed             | True                                |
| In Global Catalog      | True                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                        |
| Range-Lower            | \-                                  |
| Range-Upper            | \-                                  |
| Search-Flags           | 0x00000009                          |
| System-Flags           | 0x00000012                          |
| Classes used in        | [**Group**](c-group.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-------------------------------------|
| Link-Id                | \-                                  |
| MAPI-Id                | \-                                  |
| System-Only            | False                               |
| Is-Single-Valued       | True                                |
| Is Indexed             | True                                |
| In Global Catalog      | True                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                        |
| Range-Lower            | \-                                  |
| Range-Upper            | \-                                  |
| Search-Flags           | 0x00000009                          |
| System-Flags           | 0x00000012                          |
| Classes used in        | [**Group**](c-group.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-------------------------------------|
| Link-Id                | \-                                  |
| MAPI-Id                | \-                                  |
| System-Only            | False                               |
| Is-Single-Valued       | True                                |
| Is Indexed             | True                                |
| In Global Catalog      | True                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                        |
| Range-Lower            | \-                                  |
| Range-Upper            | \-                                  |
| Search-Flags           | 0x00000009                          |
| System-Flags           | 0x00000012                          |
| Classes used in        | [**Group**](c-group.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-------------------------------------|
| Link-Id                | \-                                  |
| MAPI-Id                | \-                                  |
| System-Only            | False                               |
| Is-Single-Valued       | True                                |
| Is Indexed             | True                                |
| In Global Catalog      | True                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                        |
| Range-Lower            | \-                                  |
| Range-Upper            | \-                                  |
| Search-Flags           | 0x00000009                          |
| System-Flags           | 0x00000012                          |
| Classes used in        | [**Group**](c-group.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-------------------------------------|
| Link-Id                | \-                                  |
| MAPI-Id                | \-                                  |
| System-Only            | False                               |
| Is-Single-Valued       | True                                |
| Is Indexed             | True                                |
| In Global Catalog      | True                                |
| NT-Security-Descriptor | O:BAG:BAD:S:                        |
| Range-Lower            | \-                                  |
| Range-Upper            | \-                                  |
| Search-Flags           | 0x00000009                          |
| System-Flags           | 0x00000012                          |
| Classes used in        | [**Group**](c-group.md)<br/> |



## Remarks

This attribute can be zero or a combination of one or more of the following values.



| Value                   | Description                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------|
| 1 (0x00000001)          | Specifies a group that is created by the system.                                             |
| 2 (0x00000002)          | Specifies a group with global scope.                                                         |
| 4 (0x00000004)          | Specifies a group with domain local scope.                                                   |
| 8 (0x00000008)          | Specifies a group with universal scope.                                                      |
| 16 (0x00000010)         | Specifies an APP\_BASIC group for Windows Server Authorization Manager.                      |
| 32 (0x00000020)         | Specifies an APP\_QUERY group for Windows Server Authorization Manager.                      |
| 2147483648 (0x80000000) | Specifies a security group. If this flag is not set, then the group is a distribution group. |



 

For more information about group type and scope, see the [Group types](/previous-versions/windows/it-pro/windows-server-2003/cc781446(v=ws.10)) and [Group scope](/previous-versions/windows/it-pro/windows-server-2003/cc755692(v=ws.10)) topics on Microsoft TechNet.

 

