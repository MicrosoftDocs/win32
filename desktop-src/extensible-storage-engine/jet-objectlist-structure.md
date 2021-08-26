---
description: "Learn more about: JET_OBJECTLIST Structure"
title: JET_OBJECTLIST Structure
TOCTitle: JET_OBJECTLIST Structure
ms:assetid: 95f12f2a-13da-48d4-a254-fc0cb718b17d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269348(v=EXCHG.10)
ms:contentKeyID: 32765635
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_OBJECTLIST Structure


_**Applies to:** Windows | Windows Server_

## JET_OBJECTLIST Structure

The **JET_OBJECTLIST** structure traverses a temporary table that was created with [JetGetObjectInfo](./jetgetobjectinfo-function.md). Each row in the temporary table describes an object in the database.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_TABLEID tableid;
      unsigned long cRecord;
      JET_COLUMNID columnidcontainername;
      JET_COLUMNID columnidobjectname;
      JET_COLUMNID columnidobjtyp;
      JET_COLUMNID columniddtCreate;
      JET_COLUMNID columniddtUpdate;
      JET_COLUMNID columnidgrbit;
      JET_COLUMNID columnidflags;
      JET_COLUMNID columnidcRecord;
      JET_COLUMNID columnidcPage;
    } JET_OBJECTLIST;
```

### Members

**cbStruct**

The size of the structure, in bytes. The API call will update this field, so the caller should ensure that this value matches sizeof( JET_INDEXLIST ).

**tableid**

The table identifier of the temporary table that was created. The caller must contain code that will close the table.

**cRecord**

The number of records in the temporary table that was created.

**columnidcontainername**

The column identifier of the name of the type of container.

The only containers that are currently supported are tables. This column is a [JET_coltypText](./jet-coltyp.md).

**columnidobjectname**

The column identifier of the name of the object.

This column is a [JET_coltypText](./jet-coltyp.md).

**columnidobjtyp**

The column identifier of the type of the object. The only containers that are currently supported are tables, so this field will be JET_objtypTable.

This column is a [JET_coltypLong](./jet-coltyp.md).

**columniddtCreate**

Obsolete. Do not use.

**columniddtUpdate**

Obsolete. Do not use.

**columnidgrbit**

The column identifier of the **grbits** that are applicable to the object. For a list of applicable **grbits**, see [JET_TABLECREATE](./jet-tablecreate-structure.md).

This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidflags**

The column identifier of the flags that are applicable to the object. For a list of applicable flags, see [JET_OBJECTINFO](./jet-objectinfo-structure.md).

This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidcRecord**

The column identifier of the number of records that are present in the table that is named in **columnidobjectname**.

This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidcPage**

The column identifier of the number of pages the object uses.

This column is a [JET_coltypLong](./jet-coltyp.md).

### Remarks

Each row in the temporary table corresponds to an object in the database.

When the temporary table is created with the *InfoLevel* parameter in the [JetGetObjectInfo](./jetgetobjectinfo-function.md) function set to JET_ObjInfoListNoStats, the columns identified by **columnidcRecord** and **columnidcPage** will not contain meaningful information.

Currently, only information about tables will be in the temporary table.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_OBJECTINFO](./jet-objectinfo-structure.md)  
[JET_TABLECREATE](./jet-tablecreate-structure.md)  
[JetGetObjectInfo](./jetgetobjectinfo-function.md)
