---
description: Represent the types for main and custom shim databases.
ms.assetid: e893963a-6130-4f65-b925-6f3d292fc86d
title: Shim Database Types
ms.topic: reference
ms.date: 05/31/2018
---

# Shim Database Types

Represent the types for main and custom shim databases.



| Constant/value                                                                                                                                                                                                                                                | Description                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| <span id="SDB_DATABASE_MAIN"></span><span id="sdb_database_main"></span><dl> <dt>**SDB\_DATABASE\_MAIN**</dt> <dt>0x80000000</dt> </dl>                    | The main database. If this flag is not present, the database is a custom database.<br/> |
| <span id="SDB_DATABASE_SHIM"></span><span id="sdb_database_shim"></span><dl> <dt>**SDB\_DATABASE\_SHIM**</dt> <dt>0x00010000</dt> </dl>                    | The database contains application entries to be shimmed.<br/>                           |
| <span id="SDB_DATABASE_MSI"></span><span id="sdb_database_msi"></span><dl> <dt>**SDB\_DATABASE\_MSI**</dt> <dt>0x00020000</dt> </dl>                       | The database contains MSI entries.<br/>                                                 |
| <span id="SDB_DATABASE_DRIVERS"></span><span id="sdb_database_drivers"></span><dl> <dt>**SDB\_DATABASE\_DRIVERS**</dt> <dt>0x00040000</dt> </dl>           | The database contains driver block entries.<br/>                                        |
| <span id="SDB_DATABASE_DETAILS"></span><span id="sdb_database_details"></span><dl> <dt>**SDB\_DATABASE\_DETAILS**</dt> <dt>0x00080000</dt> </dl>           | The database contains Apphelp details.<br/>                                             |
| <span id="SDB_DATABASE_SP_DETAILS"></span><span id="sdb_database_sp_details"></span><dl> <dt>**SDB\_DATABASE\_SP\_DETAILS**</dt> <dt>0x00100000</dt> </dl> | The database contains SP Apphelp details.<br/>                                          |
| <span id="SDB_DATABASE_RESOURCE"></span><span id="sdb_database_resource"></span><dl> <dt>**SDB\_DATABASE\_RESOURCE**</dt> <dt>0x00200000</dt> </dl>        | The resource DLL contains Apphelp details.<br/>                                         |
| <span id="SDB_DATABASE_TYPE_MASK"></span><span id="sdb_database_type_mask"></span><dl> <dt>**SDB\_DATABASE\_TYPE\_MASK**</dt> <dt>0xF02F0000</dt> </dl>    | A mask used to extract main database information.<br/>                                  |
| <span id="SDB_DATABASE_MAIN_SHIM"></span><span id="sdb_database_main_shim"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_SHIM**</dt> </dl>                                                                    | SDB\_DATABASE\_SHIM \| SDB\_DATABASE\_MSI \| SDB\_DATABASE\_MAIN<br/>                   |
| <span id="SDB_DATABASE_MAIN_MSI"></span><span id="sdb_database_main_msi"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_MSI**</dt> </dl>                                                                       | SDB\_DATABASE\_MSI \| SDB\_DATABASE\_MAIN<br/>                                          |
| <span id="SDB_DATABASE_MAIN_DRIVERS"></span><span id="sdb_database_main_drivers"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_DRIVERS**</dt> </dl>                                                           | SDB\_DATABASE\_DRIVERS \| SDB\_DATABASE\_MAIN<br/>                                      |
| <span id="SDB_DATABASE_MAIN_DETAILS"></span><span id="sdb_database_main_details"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_DETAILS**</dt> </dl>                                                           | SDB\_DATABASE\_DETAILS \| SDB\_DATABASE\_MAIN<br/>                                      |
| <span id="SDB_DATABASE_MAIN_SP_DETAILS"></span><span id="sdb_database_main_sp_details"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_SP\_DETAILS**</dt> </dl>                                                 | SDB\_DATABASE\_SP\_DETAILS \| SDB\_DATABASE\_MAIN<br/>                                  |
| <span id="SDB_DATABASE_MAIN_RESOURCE"></span><span id="sdb_database_main_resource"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_RESOURCE**</dt> </dl>                                                        | SDB\_DATABASE\_RESOURCE \| SDB\_DATABASE\_MAIN<br/>                                     |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbOpenDatabase**](sdbopendatabase.md)
</dt> </dl>

 

 




