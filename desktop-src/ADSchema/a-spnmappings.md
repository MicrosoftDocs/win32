---
title: SPN-Mappings attribute
description: This multiple-valued attribute contains a list of service principal names (SPN) to show the equivalence of SPN types.
ms.assetid: 6d37618d-426d-4e7b-8475-c912adb595ee
ms.tgt_platform: multiple
keywords:
- SPN-Mappings attribute AD Schema
- sPNMappings attribute AD Schema
topic_type:
- apiref
api_name:
- SPN-Mappings
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# SPN-Mappings attribute

This multiple-valued attribute contains a list of service principal names (SPN) to show the equivalence of SPN types. The SPN is the name a client uses to uniquely identify an instance of a service. If you install multiple instances of a service on computers throughout a forest, each instance must have its own SPN. A given service instance can have multiple SPNs if there are multiple names that clients might use for authentication. For example, "ldap/..." SPNs could be mapped so that they are equivalent to "host/..." SPNs.



| Entry | Value |
|-------------------|--------------------------------------------------------------------------------------------------------------------|
| CN                | SPN-Mappings                                                                                                       |
| Ldap-Display-Name | sPNMappings                                                                                                        |
| Size              | \-                                                                                                                 |
| Update Privilege  | This value is set during the product installation. It can be modified by the system administrator at a later time. |
| Update Frequency  | \-                                                                                                                 |
| Attribute-Id      | 1.2.840.113556.1.4.1347                                                                                            |
| System-Id-Guid    | 2ab0e76c-7041-11d2-9905-0000f87a57d4                                                                               |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)                                                                        |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | False                                            |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | False                                            |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | False                                            |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | False                                            |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | False                                            |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|--------------------------------------------------|
| Link-Id                | \-                                               |
| MAPI-Id                | \-                                               |
| System-Only            | False                                            |
| Is-Single-Valued       | False                                            |
| Is Indexed             | False                                            |
| In Global Catalog      | False                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                     |
| Range-Lower            | \-                                               |
| Range-Upper            | \-                                               |
| Search-Flags           | 0x00000000                                       |
| System-Flags           | 0x00000010                                       |
| Classes used in        | [**NTDS-Service**](c-ntdsservice.md)<br/> |



 

 





