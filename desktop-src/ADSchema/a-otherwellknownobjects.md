---
title: Other-Well-Known-Objects attribute
description: Contains a list of containers by GUID and Distinguished Name. This permits retrieving an object after it has been moved by using just the GUID and the domain name. Whenever the object is moved, the system automatically updates the Distinguished Name.
ms.assetid: 2f33c4ac-235c-47a1-9340-5b90f7edb73b
ms.tgt_platform: multiple
keywords:
- Other-Well-Known-Objects attribute AD Schema
- otherWellKnownObjects attribute AD Schema
topic_type:
- apiref
api_name:
- Other-Well-Known-Objects
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Other-Well-Known-Objects attribute

Contains a list of containers by GUID and Distinguished Name. This permits retrieving an object after it has been moved by using just the GUID and the domain name. Whenever the object is moved, the system automatically updates the Distinguished Name.



| Entry | Value |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CN                | Other-Well-Known-Objects                                                                                                                                                                                      |
| Ldap-Display-Name | otherWellKnownObjects                                                                                                                                                                                         |
| Size              | Sample for retrieving the Users container in the microsoft domain: LDAP://(WKGUID=a9d1ca15768811d1aded00c04fd8d5cd,dc=microsoft,dc=com). NOTE: Angle brackets replaced by parentheses to avoid XML conflicts. |
| Update Privilege  | Schema administrator                                                                                                                                                                                          |
| Update Frequency  | Whenever the object is moved.                                                                                                                                                                                 |
| Attribute-Id      | 1.2.840.113556.1.4.1359                                                                                                                                                                                       |
| System-Id-Guid    | 1ea64e5d-ac0f-11d2-90df-00c04fd91ab1                                                                                                                                                                          |
| Syntax            | [**Object(DN-Binary)**](s-object-dn-binary.md)                                                                                                                                                               |



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
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | False                           |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | False                           |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000010                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



 

 





