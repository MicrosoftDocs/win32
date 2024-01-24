---
title: ms-FRS-Topology-Pref attribute
description: The ms-FRS-Topology-Pref attribute is used to record the preferred NTFRS topology settings.
ms.assetid: 2804ad8a-bec8-491b-84ea-bdff1c8635d0
ms.tgt_platform: multiple
keywords:
- ms-FRS-Topology-Pref attribute AD Schema
- msFRS-Topology-Pref attribute AD Schema
topic_type:
- apiref
api_name:
- ms-FRS-Topology-Pref
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-FRS-Topology-Pref attribute

The **ms-FRS-Topology-Pref** attribute is used to record the preferred NTFRS topology settings. When an FRS member gets added or deleted to the replica set, these attributes are referred, and adjustments made to the connections between the rest of the FRS members in the replica set.

Valid values for this attribute are as follows.

| Value | Description                              |
|-------|------------------------------------------|
| 1     | FRS\_RSTOPOLOGYPREF\_RING<br/>     |
| 2     | FRS\_RSTOPOLOGYPREF\_HUBSPOKE<br/> |
| 3     | FRS\_RSTOPOLOGYPREF\_FULLMESH<br/> |
| 4     | FRS\_RSTOPOLOGYPREF\_CUSTOM<br/>   |



 



| Entry | Value |
|-------------------|--------------------------------------------------------------------|
| CN                | ms-FRS-Topology-Pref                                               |
| Ldap-Display-Name | msFRS-Topology-Pref                                                |
| Size              | \-                                                                 |
| Update Privilege  | Domain administrator                                               |
| Update Frequency  | When the replica set is created or the preferred topology changes. |
| Attribute-Id      | 1.2.840.113556.1.4.1692                                            |
| System-Id-Guid    | 92aa27e0-5c50-402d-9ec1-ee847def9788                               |
| Syntax            | [**String(Unicode)**](s-string-unicode.md)                        |



## Implementations

-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2003



| Entry | Value |
|------------------------|-----------------------------------------------------------|
| Link-Id                | \-                                                        |
| MAPI-Id                | \-                                                        |
| System-Only            | False                                                     |
| Is-Single-Valued       | True                                                      |
| Is Indexed             | False                                                     |
| In Global Catalog      | False                                                     |
| NT-Security-Descriptor | O:BAG:BAD:S:                                              |
| Range-Lower            | \-                                                        |
| Range-Upper            | \-                                                        |
| Search-Flags           | 0x00000000                                                |
| System-Flags           | 0x00000000                                                |
| Classes used in        | [**NTFRS-Replica-Set**](c-ntfrsreplicaset.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-----------------------------------------------------------|
| Link-Id                | \-                                                        |
| MAPI-Id                | \-                                                        |
| System-Only            | False                                                     |
| Is-Single-Valued       | True                                                      |
| Is Indexed             | False                                                     |
| In Global Catalog      | False                                                     |
| NT-Security-Descriptor | O:BAG:BAD:S:                                              |
| Range-Lower            | \-                                                        |
| Range-Upper            | \-                                                        |
| Search-Flags           | 0x00000000                                                |
| System-Flags           | 0x00000000                                                |
| Classes used in        | [**NTFRS-Replica-Set**](c-ntfrsreplicaset.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-----------------------------------------------------------|
| Link-Id                | \-                                                        |
| MAPI-Id                | \-                                                        |
| System-Only            | False                                                     |
| Is-Single-Valued       | True                                                      |
| Is Indexed             | False                                                     |
| In Global Catalog      | False                                                     |
| NT-Security-Descriptor | O:BAG:BAD:S:                                              |
| Range-Lower            | \-                                                        |
| Range-Upper            | \-                                                        |
| Search-Flags           | 0x00000000                                                |
| System-Flags           | 0x00000000                                                |
| Classes used in        | [**NTFRS-Replica-Set**](c-ntfrsreplicaset.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-----------------------------------------------------------|
| Link-Id                | \-                                                        |
| MAPI-Id                | \-                                                        |
| System-Only            | False                                                     |
| Is-Single-Valued       | True                                                      |
| Is Indexed             | False                                                     |
| In Global Catalog      | False                                                     |
| NT-Security-Descriptor | O:BAG:BAD:S:                                              |
| Range-Lower            | \-                                                        |
| Range-Upper            | \-                                                        |
| Search-Flags           | 0x00000000                                                |
| System-Flags           | 0x00000000                                                |
| Classes used in        | [**NTFRS-Replica-Set**](c-ntfrsreplicaset.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-----------------------------------------------------------|
| Link-Id                | \-                                                        |
| MAPI-Id                | \-                                                        |
| System-Only            | False                                                     |
| Is-Single-Valued       | True                                                      |
| Is Indexed             | False                                                     |
| In Global Catalog      | False                                                     |
| NT-Security-Descriptor | O:BAG:BAD:S:                                              |
| Range-Lower            | \-                                                        |
| Range-Upper            | \-                                                        |
| Search-Flags           | 0x00000000                                                |
| System-Flags           | 0x00000000                                                |
| Classes used in        | [**NTFRS-Replica-Set**](c-ntfrsreplicaset.md)<br/> |



 

 





