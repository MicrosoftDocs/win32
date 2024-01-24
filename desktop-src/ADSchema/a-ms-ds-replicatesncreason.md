---
title: MS-DS-Replicates-NC-Reason attribute
description: Attribute of ntdsConnection object that indicates why (or whether) the KCC shows the connection is useful in the replication topology. Is multiple-valued and has DistName+Binary syntax, where the binary part is an int-size bitfield.
ms.assetid: ba66e346-d288-4c0b-b41e-599c3f8e8405
ms.tgt_platform: multiple
keywords:
- MS-DS-Replicates-NC-Reason attribute AD Schema
- mS-DS-ReplicatesNCReason attribute AD Schema
topic_type:
- apiref
api_name:
- MS-DS-Replicates-NC-Reason
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MS-DS-Replicates-NC-Reason attribute

Attribute of ntdsConnection object that indicates why (or whether) the KCC shows the connection is useful in the replication topology. Is multiple-valued and has DistName+Binary syntax, where the binary part is an int-size bitfield.



| Entry | Value |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| CN                | MS-DS-Replicates-NC-Reason                                                                                                                 |
| Ldap-Display-Name | mS-DS-ReplicatesNCReason                                                                                                                   |
| Size              | Value for binary portion: 0 = NO\_REASON,1 = GC\_TOPOLOGY, 2 = RING\_TOPOLOGY, 4 = MINIMIZE\_HOPS\_TOPOLOGY, 8 = STALE\_SERVERS\_TOPOLOGY. |
| Update Privilege  | This value is set by the system.                                                                                                           |
| Update Frequency  | Can change in response to changes in the network topology.                                                                                 |
| Attribute-Id      | 1.2.840.113556.1.4.1408                                                                                                                    |
| System-Id-Guid    | 0ea12b84-08b3-11d3-91bc-0000f87a57d4                                                                                                       |
| Syntax            | [**Object(DN-Binary)**](s-object-dn-binary.md)                                                                                            |



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
|------------------------|--------------------------------------------------------|
| Link-Id                | \-                                                     |
| MAPI-Id                | \-                                                     |
| System-Only            | False                                                  |
| Is-Single-Valued       | False                                                  |
| Is Indexed             | False                                                  |
| In Global Catalog      | False                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                           |
| Range-Lower            | \-                                                     |
| Range-Upper            | \-                                                     |
| Search-Flags           | 0x00000000                                             |
| System-Flags           | 0x00000010                                             |
| Classes used in        | [**NTDS-Connection**](c-ntdsconnection.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|--------------------------------------------------------|
| Link-Id                | \-                                                     |
| MAPI-Id                | \-                                                     |
| System-Only            | False                                                  |
| Is-Single-Valued       | False                                                  |
| Is Indexed             | False                                                  |
| In Global Catalog      | False                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                           |
| Range-Lower            | \-                                                     |
| Range-Upper            | \-                                                     |
| Search-Flags           | 0x00000000                                             |
| System-Flags           | 0x00000010                                             |
| Classes used in        | [**NTDS-Connection**](c-ntdsconnection.md)<br/> |



## ADAM



| Entry | Value |
|------------------------|--------------------------------------------------------|
| Link-Id                | \-                                                     |
| MAPI-Id                | \-                                                     |
| System-Only            | False                                                  |
| Is-Single-Valued       | False                                                  |
| Is Indexed             | False                                                  |
| In Global Catalog      | False                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                           |
| Range-Lower            | \-                                                     |
| Range-Upper            | \-                                                     |
| Search-Flags           | 0x00000000                                             |
| System-Flags           | 0x00000010                                             |
| Classes used in        | [**NTDS-Connection**](c-ntdsconnection.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|--------------------------------------------------------|
| Link-Id                | \-                                                     |
| MAPI-Id                | \-                                                     |
| System-Only            | False                                                  |
| Is-Single-Valued       | False                                                  |
| Is Indexed             | False                                                  |
| In Global Catalog      | False                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                           |
| Range-Lower            | \-                                                     |
| Range-Upper            | \-                                                     |
| Search-Flags           | 0x00000000                                             |
| System-Flags           | 0x00000010                                             |
| Classes used in        | [**NTDS-Connection**](c-ntdsconnection.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|--------------------------------------------------------|
| Link-Id                | \-                                                     |
| MAPI-Id                | \-                                                     |
| System-Only            | False                                                  |
| Is-Single-Valued       | False                                                  |
| Is Indexed             | False                                                  |
| In Global Catalog      | False                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                           |
| Range-Lower            | \-                                                     |
| Range-Upper            | \-                                                     |
| Search-Flags           | 0x00000000                                             |
| System-Flags           | 0x00000010                                             |
| Classes used in        | [**NTDS-Connection**](c-ntdsconnection.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|--------------------------------------------------------|
| Link-Id                | \-                                                     |
| MAPI-Id                | \-                                                     |
| System-Only            | False                                                  |
| Is-Single-Valued       | False                                                  |
| Is Indexed             | False                                                  |
| In Global Catalog      | False                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                           |
| Range-Lower            | \-                                                     |
| Range-Upper            | \-                                                     |
| Search-Flags           | 0x00000000                                             |
| System-Flags           | 0x00000010                                             |
| Classes used in        | [**NTDS-Connection**](c-ntdsconnection.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|--------------------------------------------------------|
| Link-Id                | \-                                                     |
| MAPI-Id                | \-                                                     |
| System-Only            | False                                                  |
| Is-Single-Valued       | False                                                  |
| Is Indexed             | False                                                  |
| In Global Catalog      | False                                                  |
| NT-Security-Descriptor | O:BAG:BAD:S:                                           |
| Range-Lower            | \-                                                     |
| Range-Upper            | \-                                                     |
| Search-Flags           | 0x00000000                                             |
| System-Flags           | 0x00000010                                             |
| Classes used in        | [**NTDS-Connection**](c-ntdsconnection.md)<br/> |



 

 





