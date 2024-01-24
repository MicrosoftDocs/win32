---
title: ms-DS-Has-Instantiated-NCs attribute
description: DS replication state information, analogous to (and a superset of) the existing attributes hasMasterNCs and hasPartialReplicaNCs. To be used by the KCC when setting up replication partners.
ms.assetid: 00dda441-e382-4fb2-b735-ae547901c11f
ms.tgt_platform: multiple
keywords:
- ms-DS-Has-Instantiated-NCs attribute AD Schema
- msDS-HasInstantiatedNCs attribute AD Schema
topic_type:
- apiref
api_name:
- ms-DS-Has-Instantiated-NCs
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-Has-Instantiated-NCs attribute

DS replication state information, analogous to (and a superset of) the existing attributes hasMasterNCs and hasPartialReplicaNCs. To be used by the KCC when setting up replication partners.



| Entry | Value |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CN                | ms-DS-Has-Instantiated-NCs                                                                                                                                                                                  |
| Ldap-Display-Name | msDS-HasInstantiatedNCs                                                                                                                                                                                     |
| Size              | 4 bytes                                                                                                                                                                                                     |
| Update Privilege  | This value is set by the system.                                                                                                                                                                            |
| Update Frequency  | Roughly twice as often as hasMasterNCs / hasPartialReplicaNCs. These existing attributes are updated only when the DC adds or removes a partition (For example, when changing from DC to GC or vice versa). |
| Attribute-Id      | 1.2.840.113556.1.4.1709                                                                                                                                                                                     |
| System-Id-Guid    | 11e9a5bc-4517-4049-af9c-51554fb0fc09                                                                                                                                                                        |
| Syntax            | [**Object(DN-Binary)**](s-object-dn-binary.md)                                                                                                                                                             |



## Implementations

-   [**Windows Server 2003**](#windows-server-2003)
-   [**ADAM**](#adam)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------|
| Link-Id                | 2002                                     |
| MAPI-Id                | \-                                       |
| System-Only            | True                                     |
| Is-Single-Valued       | False                                    |
| Is Indexed             | False                                    |
| In Global Catalog      | False                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                             |
| Range-Lower            | 4                                        |
| Range-Upper            | 4                                        |
| Search-Flags           | 0x00000000                               |
| System-Flags           | 0x00000010                               |
| Classes used in        | [**NTDS-DSA**](c-ntdsdsa.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|------------------------------------------|
| Link-Id                | 2002                                     |
| MAPI-Id                | \-                                       |
| System-Only            | True                                     |
| Is-Single-Valued       | False                                    |
| Is Indexed             | False                                    |
| In Global Catalog      | False                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                             |
| Range-Lower            | 4                                        |
| Range-Upper            | 4                                        |
| Search-Flags           | 0x00000000                               |
| System-Flags           | 0x00000010                               |
| Classes used in        | [**NTDS-DSA**](c-ntdsdsa.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------|
| Link-Id                | 2002                                     |
| MAPI-Id                | \-                                       |
| System-Only            | True                                     |
| Is-Single-Valued       | False                                    |
| Is Indexed             | False                                    |
| In Global Catalog      | False                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                             |
| Range-Lower            | 4                                        |
| Range-Upper            | 4                                        |
| Search-Flags           | 0x00000000                               |
| System-Flags           | 0x00000010                               |
| Classes used in        | [**NTDS-DSA**](c-ntdsdsa.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------|
| Link-Id                | 2002                                     |
| MAPI-Id                | \-                                       |
| System-Only            | True                                     |
| Is-Single-Valued       | False                                    |
| Is Indexed             | False                                    |
| In Global Catalog      | False                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                             |
| Range-Lower            | 4                                        |
| Range-Upper            | 4                                        |
| Search-Flags           | 0x00000000                               |
| System-Flags           | 0x00000010                               |
| Classes used in        | [**NTDS-DSA**](c-ntdsdsa.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------|
| Link-Id                | 2002                                     |
| MAPI-Id                | \-                                       |
| System-Only            | True                                     |
| Is-Single-Valued       | False                                    |
| Is Indexed             | False                                    |
| In Global Catalog      | False                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                             |
| Range-Lower            | 4                                        |
| Range-Upper            | 4                                        |
| Search-Flags           | 0x00000000                               |
| System-Flags           | 0x00000010                               |
| Classes used in        | [**NTDS-DSA**](c-ntdsdsa.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------|
| Link-Id                | 2002                                     |
| MAPI-Id                | \-                                       |
| System-Only            | True                                     |
| Is-Single-Valued       | False                                    |
| Is Indexed             | False                                    |
| In Global Catalog      | False                                    |
| NT-Security-Descriptor | O:BAG:BAD:S:                             |
| Range-Lower            | 4                                        |
| Range-Upper            | 4                                        |
| Search-Flags           | 0x00000000                               |
| System-Flags           | 0x00000010                               |
| Classes used in        | [**NTDS-DSA**](c-ntdsdsa.md)<br/> |



 

 





