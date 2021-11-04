---
description: "Learn more about: JET_OBJECTINFO Structure"
title: JET_OBJECTINFO Structure
TOCTitle: JET_OBJECTINFO Structure
ms:assetid: 9d348ab3-d453-4316-9233-681f165e8ef1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269353(v=EXCHG.10)
ms:contentKeyID: 32765640
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_OBJECTINFO Structure


_**Applies to:** Windows | Windows Server_

## JET_OBJECTINFO Structure

The **JET_OBJECTINFO** structure holds information about an object. Tables are the only object types that are currently supported.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_OBJTYP objtyp;
      JET_DATESERIAL dtCreate;
      JET_DATESERIAL dtUpdate;
      JET_GRBIT grbit;
      unsigned long flags;
      unsigned long cRecord;
      unsigned long cPage;
    } JET_OBJECTINFO;
```

### Members

**cbStruct**

The size, in bytes, of the **JET_OBJECTINFO** structure.

**objtyp**

Holds the [JET_OBJTYP](./jet-objtyp.md) of the structure. Currently only tables will be returned (that is, JET_objtypTable).

**dtCreate**

Obsolete. Do not use.

**dtUpdate**

Obsolete. Do not use.

**grbit**

A group of bits that contain the options that are available for this call, which include zero or more of the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitTableInfoBookmark</p> | <p>The table can have bookmarks.</p> | 
| <p>JET_bitTableInfoRollback</p> | <p>The table can be rolled back.</p> | 
| <p>JET_bitTableInfoUpdatable</p> | <p>The table can be updated.</p> | 



**flags**

A bit field that contains zero or more of the following flags.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitObjectSystem</p> | <p>The table is a System Table and is for internal use only.</p> | 
| <p>JET_bitObjectTableDerived</p> | <p>The table inherited DDL from a template table.</p> | 
| <p>JET_bitObjectTableFixedDDL</p> | <p>The DDL for the table cannot be modified.</p> | 
| <p>JET_bitObjectTableNoFixedVarColumnsInDerivedTables</p> | <p>Used in conjunction with JET_bitObjectTableTemplate to disallow fixed or variable columns in derived tables (so that fixed or variable columns can be added to the template in the future).</p><p><strong>Windows XP:  </strong>This value is introduced in Windows XP.</p> | 
| <p>JET_bitObjectTableTemplate</p> | <p>The table is a template table.</p> | 



**cRecord**

The number of records in the table.

This value is retrieved only if **JET_OBJECTINFO** was passed to [JetGetObjectInfo](./jetgetobjectinfo-function.md).

**cPage**

The number of pages that are being used by the table.

This value is retrieved only if **JET_OBJECTINFO** was passed to [JetGetObjectInfo](./jetgetobjectinfo-function.md).

### Remarks

A **JET_OBJECTINFO** structure gets populated by a call to [JetGetObjectInfo](./jetgetobjectinfo-function.md) or [JetGetTableInfo](./jetgettableinfo-function.md). If the API call does not succeed, the contents of the structure are undefined.

If applicable, the table statistics include the number of records and the number of pages that are in the clustered index (that is, the index containing the record data). The index statistics are accessed separately by name, using [JetGetIndexInfo](./jetgetindexinfo-function.md) or [JetGetTableIndexInfo](./jetgettableindexinfo-function.md).

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_OBJTYP](./jet-objtyp.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetIndexInfo](./jetgetindexinfo-function.md)  
[JetGetObjectInfo](./jetgetobjectinfo-function.md)  
[JetGetTableIndexInfo](./jetgettableindexinfo-function.md)  
[JetGetTableInfo](./jetgettableinfo-function.md)
