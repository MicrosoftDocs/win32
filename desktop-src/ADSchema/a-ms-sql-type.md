---
title: MS-SQL-Type attribute
description: The replication type used by this SQL server.
ms.assetid: 8e7fa9ab-9a25-4ee3-9134-68af698a5fb8
ms.tgt_platform: multiple
keywords:
- MS-SQL-Type attribute AD Schema
- mS-SQL-Type attribute AD Schema
topic_type:
- apiref
api_name:
- MS-SQL-Type
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MS-SQL-Type attribute

The replication type used by this SQL server. The following values are the possible values for this attribute.



| Value        | Description                           |
|--------------|---------------------------------------|
| 0<br/> | Transactional replication.<br/> |
| 1<br/> | Snapshot replication.<br/>      |
| 2<br/> | Merge replication.<br/>         |



 



| Entry | Value |
|-------------------|---------------------------------------------|
| CN                | MS-SQL-Type                                 |
| Ldap-Display-Name | mS-SQL-Type                                 |
| Size              | \-                                          |
| Update Privilege  | Domain administrator                        |
| Update Frequency  | When replication is set up.                 |
| Attribute-Id      | 1.2.840.113556.1.4.1391                     |
| System-Id-Guid    | ca48eba8-ccee-11d2-9993-0000f87a57d4        |
| Syntax            | [**String(Unicode)**](s-string-unicode.md) |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                  |
| MAPI-Id                | \-                                                                                                                                  |
| System-Only            | False                                                                                                                               |
| Is-Single-Valued       | True                                                                                                                                |
| Is Indexed             | False                                                                                                                               |
| In Global Catalog      | False                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                        |
| Range-Lower            | \-                                                                                                                                  |
| Range-Upper            | \-                                                                                                                                  |
| Search-Flags           | 0x00000000                                                                                                                          |
| System-Flags           | 0x00000010                                                                                                                          |
| Classes used in        | [**MS-SQL-SQLPublication**](c-ms-sql-sqlpublication.md)<br/> [**MS-SQL-OLAPDatabase**](c-ms-sql-olapdatabase.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                  |
| MAPI-Id                | \-                                                                                                                                  |
| System-Only            | False                                                                                                                               |
| Is-Single-Valued       | True                                                                                                                                |
| Is Indexed             | False                                                                                                                               |
| In Global Catalog      | False                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                        |
| Range-Lower            | \-                                                                                                                                  |
| Range-Upper            | \-                                                                                                                                  |
| Search-Flags           | 0x00000000                                                                                                                          |
| System-Flags           | 0x00000010                                                                                                                          |
| Classes used in        | [**MS-SQL-SQLPublication**](c-ms-sql-sqlpublication.md)<br/> [**MS-SQL-OLAPDatabase**](c-ms-sql-olapdatabase.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                  |
| MAPI-Id                | \-                                                                                                                                  |
| System-Only            | False                                                                                                                               |
| Is-Single-Valued       | True                                                                                                                                |
| Is Indexed             | False                                                                                                                               |
| In Global Catalog      | False                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                        |
| Range-Lower            | \-                                                                                                                                  |
| Range-Upper            | \-                                                                                                                                  |
| Search-Flags           | 0x00000000                                                                                                                          |
| System-Flags           | 0x00000010                                                                                                                          |
| Classes used in        | [**MS-SQL-SQLPublication**](c-ms-sql-sqlpublication.md)<br/> [**MS-SQL-OLAPDatabase**](c-ms-sql-olapdatabase.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                  |
| MAPI-Id                | \-                                                                                                                                  |
| System-Only            | False                                                                                                                               |
| Is-Single-Valued       | True                                                                                                                                |
| Is Indexed             | False                                                                                                                               |
| In Global Catalog      | False                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                        |
| Range-Lower            | \-                                                                                                                                  |
| Range-Upper            | \-                                                                                                                                  |
| Search-Flags           | 0x00000000                                                                                                                          |
| System-Flags           | 0x00000010                                                                                                                          |
| Classes used in        | [**MS-SQL-SQLPublication**](c-ms-sql-sqlpublication.md)<br/> [**MS-SQL-OLAPDatabase**](c-ms-sql-olapdatabase.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                  |
| MAPI-Id                | \-                                                                                                                                  |
| System-Only            | False                                                                                                                               |
| Is-Single-Valued       | True                                                                                                                                |
| Is Indexed             | False                                                                                                                               |
| In Global Catalog      | False                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                        |
| Range-Lower            | \-                                                                                                                                  |
| Range-Upper            | \-                                                                                                                                  |
| Search-Flags           | 0x00000000                                                                                                                          |
| System-Flags           | 0x00000010                                                                                                                          |
| Classes used in        | [**MS-SQL-SQLPublication**](c-ms-sql-sqlpublication.md)<br/> [**MS-SQL-OLAPDatabase**](c-ms-sql-olapdatabase.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Link-Id                | \-                                                                                                                                  |
| MAPI-Id                | \-                                                                                                                                  |
| System-Only            | False                                                                                                                               |
| Is-Single-Valued       | True                                                                                                                                |
| Is Indexed             | False                                                                                                                               |
| In Global Catalog      | False                                                                                                                               |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                                                                                        |
| Range-Lower            | \-                                                                                                                                  |
| Range-Upper            | \-                                                                                                                                  |
| Search-Flags           | 0x00000000                                                                                                                          |
| System-Flags           | 0x00000010                                                                                                                          |
| Classes used in        | [**MS-SQL-SQLPublication**](c-ms-sql-sqlpublication.md)<br/> [**MS-SQL-OLAPDatabase**](c-ms-sql-olapdatabase.md)<br/> |



 

 





