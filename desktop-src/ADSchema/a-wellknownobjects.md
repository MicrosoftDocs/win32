---
title: Well-Known-Objects attribute
description: This attribute contains a list of well-known object containers by GUID and distinguished name.
ms.assetid: e3c2d243-6734-4c2f-9ead-bc4ec071d1f1
ms.tgt_platform: multiple
keywords:
- Well-Known-Objects attribute AD Schema
- wellKnownObjects attribute AD Schema
topic_type:
- apiref
api_name:
- Well-Known-Objects
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Well-Known-Objects attribute

This attribute contains a list of well-known object containers by GUID and distinguished name. The well-known objects are system containers. This information is used to retrieve an object after it has been moved by using just the GUID and the domain name. Whenever the object is moved, the system automatically updates the Distinguished Name portion of the Well-Known-Objects values that referred to the object. The file Ntdsapi.h contains the following definitions, which can be used to retrieve an object (the GUIDs that are associated to these objects are contained in Ntdsapi.h):

-   GUID\_USERS\_CONTAINER\_W
-   GUID\_COMPUTRS\_CONTAINER\_W
-   GUID\_SYSTEMS\_CONTAINER\_W
-   GUID\_DOMAIN\_CONTROLLERS\_CONTAINER\_W
-   GUID\_INFRASTRUCTURE\_CONTAINER\_W
-   GUID\_DELETED\_OBJECTS\_CONTAINER\_W
-   GUID\_LOSTANDFOUND\_CONTAINER\_W
-   GUID\_FOREIGNSECURITYPRINCIPALS\_CONTAINER\_W
-   GUID\_PROGRAM\_DATA\_CONTAINER\_W
-   GUID\_MICROSOFT\_PROGRAM\_DATA\_CONTAINER\_W
-   GUID\_NTDS\_QUOTAS\_CONTAINER\_W



| Entry | Value |
|-------------------|-------------------------------------------------|
| CN                | Well-Known-Objects                              |
| Ldap-Display-Name | wellKnownObjects                                |
| Size              | \-                                              |
| Update Privilege  | This value is set by the system.                |
| Update Frequency  | Whenever one of the system containers is moved. |
| Attribute-Id      | 1.2.840.113556.1.4.618                          |
| System-Id-Guid    | 05308983-7688-11d1-aded-00c04fd8d5cd            |
| Syntax            | [**Object(DN-Binary)**](s-object-dn-binary.md) |



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
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | \-                              |
| Range-Upper            | \-                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|---------------------------------|
| Link-Id                | \-                              |
| MAPI-Id                | \-                              |
| System-Only            | True                            |
| Is-Single-Valued       | False                           |
| Is Indexed             | False                           |
| In Global Catalog      | True                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                    |
| Range-Lower            | 16                              |
| Range-Upper            | 16                              |
| Search-Flags           | 0x00000000                      |
| System-Flags           | 0x00000012                      |
| Classes used in        | [**Top**](c-top.md)<br/> |



 

 





