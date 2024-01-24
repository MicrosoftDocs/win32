---
description: "Learn more about: JetDeleteColumn2 Function"
title: JetDeleteColumn2 Function
TOCTitle: JetDeleteColumn2 Function
ms:assetid: 840b5acd-8bbf-4524-9741-5d74e3427329
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269320(v=EXCHG.10)
ms:contentKeyID: 32765610
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetDeleteColumn2
- JetDeleteColumn2A
- JetDeleteColumn2W
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetDeleteColumn2 Function


_**Applies to:** Windows | Windows Server_

## JetDeleteColumn2 Function

The **JetDeleteColumn2** function deletes a column from an ESE database table and enables a *grbit* option to be set.

**Windows XP:  JetDeleteColumn2** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetDeleteColumn2(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          const tchar* szColumnName,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*tableid*

The table that contains the column to be deleted.

*szColumnName*

The name of the column to be deleted.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitDeleteColumnIgnoreTemplateColumns</p> | <p>Setting JET_bitDeleteColumIgnoreTemplateColumns will cause the API to only attempt to delete columns in the derived table. If a column of that name exists in the base table it will be ignored.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errColumnInUse</p> | <p>The column is currently in use. It may be currently used by an index.</p> | 
| <p>JET_errFixedDDL</p> | <p>An attempt was made to modify the fixed DDL.</p> | 
| <p>JET_errFixedInheritedDDL</p> | <p>The column named in <em>szColumnName</em> exists in the template table, and the DDL of a template table cannot be modified.</p> | 
| <p>JET_errInvalidName</p> | <p>This may be returned if a bad name for <em>szColumnName</em> was given.</p> | 
| <p>JET_errPermissionDenied</p> | <p>The table is not writable. This may get returned if the database was opened in read-only mode.</p> | 
| <p>JET_errTransReadOnly</p> | <p>The transaction is a read-only transaction.</p> | 



#### Remarks

Calling [JetDeleteColumn](./jetdeletecolumn-function.md) is identical to calling **JetDeleteColumn2** with *grbit* set to zero (0).

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetDeleteColumn2W</strong> (Unicode) and <strong>JetDeleteColumn2A</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetDeleteColumn](./jetdeletecolumn-function.md)
