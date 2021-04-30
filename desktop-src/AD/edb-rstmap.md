---
title: EDB_RSTMAP structure (Ntdsbcli.h)
description: Used with the DsRestoreRegister function to map a backed up database to a new database.
ms.assetid: b2c5d30a-3617-4807-82e8-57f7179b817c
ms.tgt_platform: multiple
keywords:
- EDB_RSTMAP structure Active Directory
- PEDB_RSTMAP structure pointer Active Directory
topic_type:
- apiref
api_name:
- EDB_RSTMAP
- EDB_RSTMAPA
- EDB_RSTMAPW
api_location:
- Ntdsbcli.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EDB\_RSTMAP structure

The **EDB\_RSTMAP** structure is used with the [**DsRestoreRegister**](dsrestoreregister.md) function to map a backed up database to a new database.

## Syntax


```C++
typedef struct {
  LPTSTR szDatabaseName;
  LPTSTR szNewDatabaseName;
} EDB_RSTMAP, *PEDB_RSTMAP;
```



## Members

<dl> <dt>

**szDatabaseName**
</dt> <dd>

Pointer to a null-terminated string that contains the name of the database when it was backed up.

</dd> <dt>

**szNewDatabaseName**
</dt> <dd>

Pointer to a null-terminated string that contains the new name of the database, including its new location, when applicable.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **EDB\_RSTMAPW** (Unicode) and **EDB\_RSTMAPA** (ANSI)<br/>                     |



## See also

<dl> <dt>

[**DsRestoreRegister**](dsrestoreregister.md)
</dt> <dt>

[Directory Backup Structures](directory-backup-structures.md)
</dt> </dl>

 

 





