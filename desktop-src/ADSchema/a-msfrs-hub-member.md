---
title: ms-FRS-Hub-Member attribute
description: The ms-FRS-Hub-Member attribute is used to record the preferred NTFRS topology settings.
ms.assetid: df8623e0-745a-46f8-a696-8f6e7014fd2b
ms.tgt_platform: multiple
keywords:
- ms-FRS-Hub-Member attribute AD Schema
- msFRS-Hub-Member attribute AD Schema
topic_type:
- apiref
api_name:
- ms-FRS-Hub-Member
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-FRS-Hub-Member attribute

The **ms-FRS-Hub-Member** attribute is used to record the preferred NTFRS topology settings. When an FRS member gets added or deleted to a replica set, these attributes are referred and appropriate adjustments are made to the connections between the rest of the FRS members in the replica set.



| Entry | Value |
|-------------------|--------------------------------------------------------------------|
| CN                | ms-FRS-Hub-Member                                                  |
| Ldap-Display-Name | msFRS-Hub-Member                                                   |
| Size              | \-                                                                 |
| Update Privilege  | Domain administrator                                               |
| Update Frequency  | When the replica set is created or the preferred topology changes. |
| Attribute-Id      | 1.2.840.113556.1.4.1693                                            |
| System-Id-Guid    | 5643ff81-35b6-4ca9-9512-baf0bd0a2772                               |
| Syntax            | [**Object(DS-DN)**](s-object-ds-dn.md)                            |



## Implementations

-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows Server 2003



| Entry | Value |
|------------------------|-----------------------------------------------------------|
| Link-Id                | 1046                                                      |
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
| Link-Id                | 1046                                                      |
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
| Link-Id                | 1046                                                      |
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
| Link-Id                | 1046                                                      |
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
| Link-Id                | 1046                                                      |
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



## Remarks

This is the fully qualified distinguished name of an [**NTFRS-Member**](c-ntfrsmember.md) object. The distinguished name is in the format of "CN=*&lt;computerGuid&gt;*, CN=*\<Dfs Link Name\>*, CN=*\<Dfs Root name\>*, CN=DFS Volumes, CN=File Replication Service,CN=System, DC=..."

 

 





