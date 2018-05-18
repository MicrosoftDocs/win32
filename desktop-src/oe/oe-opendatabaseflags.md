---
title: OPENDATABASEFLAGS
description: Do not use. DWORD that specifies various flags that are used when opening a database.
ms.assetid: '8eadd761-d52b-4552-8d79-b61f3feb3daf'
topic_type:
- apiref
api_name:
- OPEN_DATABASE_NORESET
- OPEN_DATABASE_EXCLUSIVE
- OPEN_DATABASE_NOCREATE
- OPEN_DATABASE_READONLY
- OPEN_DATABASE_ALLOWMISSINGCOLUMNS
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# OPENDATABASEFLAGS

Do not use. DWORD that specifies various flags that are used when opening a database.



| Constant/value                                                                                                                                                                                                                                                                             | Description                                                                                                                                              |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="OPEN_DATABASE_NORESET"></span><span id="open_database_noreset"></span><dl> <dt>**OPEN\_DATABASE\_NORESET**</dt> <dt>0x00000001</dt> </dl>                                     | If this flag is set and there is corruption detected, allows the database to completely clear its contents and create a new, empty, database.<br/> |
| <span id="OPEN_DATABASE_EXCLUSIVE"></span><span id="open_database_exclusive"></span><dl> <dt>**OPEN\_DATABASE\_EXCLUSIVE**</dt> <dt>0x00000020</dt> </dl>                               | If this flag is not set, the database file can be opened by multiple instances of the database software at once.<br/>                              |
| <span id="OPEN_DATABASE_NOCREATE"></span><span id="open_database_nocreate"></span><dl> <dt>**OPEN\_DATABASE\_NOCREATE**</dt> <dt>0x00000040</dt> </dl>                                  | When this flag is set, if the database doesn't already exist, the function won't create a new one.<br/>                                            |
| <span id="OPEN_DATABASE_READONLY"></span><span id="open_database_readonly"></span><dl> <dt>**OPEN\_DATABASE\_READONLY**</dt> <dt>0x00000080</dt> </dl>                                  | When this flag is set, the database file is opened for read only.<br/>                                                                             |
| <span id="OPEN_DATABASE_ALLOWMISSINGCOLUMNS"></span><span id="open_database_allowmissingcolumns"></span><dl> <dt>**OPEN\_DATABASE\_ALLOWMISSINGCOLUMNS**</dt> <dt>0x00000400</dt> </dl> | When this flag is set, the database file is opened even when some columns defined in schema are missing.<br/>                                      |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





