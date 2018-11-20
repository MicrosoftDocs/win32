---
title: JET_OBJECTLIST Structure
TOCTitle: JET_OBJECTLIST Structure
ms:assetid: 95f12f2a-13da-48d4-a254-fc0cb718b17d
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269348(v=EXCHG.10)
ms:contentKeyID: 32765635
ms.date: 04/11/2016
ms.topic: article
api_name: 
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET\_OBJECTLIST Structure


_**Applies to:** Windows | Windows Server_

## JET\_OBJECTLIST Structure

The **JET\_OBJECTLIST** structure traverses a temporary table that was created with [JetGetObjectInfo](gg269232\(v=exchg.10\).md). Each row in the temporary table describes an object in the database.

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

### Members

**cbStruct**

The size of the structure, in bytes. The API call will update this field, so the caller should ensure that this value matches sizeof( JET\_INDEXLIST ).

**tableid**

The table identifier of the temporary table that was created. The caller must contain code that will close the table.

**cRecord**

The number of records in the temporary table that was created.

**columnidcontainername**

The column identifier of the name of the type of container.

The only containers that are currently supported are tables. This column is a [JET\_coltypText](gg269213\(v=exchg.10\).md).

**columnidobjectname**

The column identifier of the name of the object.

This column is a [JET\_coltypText](gg269213\(v=exchg.10\).md).

**columnidobjtyp**

The column identifier of the type of the object. The only containers that are currently supported are tables, so this field will be JET\_objtypTable.

This column is a [JET\_coltypLong](gg269213\(v=exchg.10\).md).

**columniddtCreate**

Obsolete. Do not use.

**columniddtUpdate**

Obsolete. Do not use.

**columnidgrbit**

The column identifier of the **grbits** that are applicable to the object. For a list of applicable **grbits**, see [JET\_TABLECREATE](gg294146\(v=exchg.10\).md).

This column is a [JET\_coltypLong](gg269213\(v=exchg.10\).md).

**columnidflags**

The column identifier of the flags that are applicable to the object. For a list of applicable flags, see [JET\_OBJECTINFO](gg269353\(v=exchg.10\).md).

This column is a [JET\_coltypLong](gg269213\(v=exchg.10\).md).

**columnidcRecord**

The column identifier of the number of records that are present in the table that is named in **columnidobjectname**.

This column is a [JET\_coltypLong](gg269213\(v=exchg.10\).md).

**columnidcPage**

The column identifier of the number of pages the object uses.

This column is a [JET\_coltypLong](gg269213\(v=exchg.10\).md).

### Remarks

Each row in the temporary table corresponds to an object in the database.

When the temporary table is created with the *InfoLevel* parameter in the [JetGetObjectInfo](gg269232\(v=exchg.10\).md) function set to JET\_ObjInfoListNoStats, the columns identified by **columnidcRecord** and **columnidcPage** will not contain meaningful information.

Currently, only information about tables will be in the temporary table.

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JET\_COLTYP](gg269213\(v=exchg.10\).md)  
[JET\_COLUMNID](gg294104\(v=exchg.10\).md)  
[JET\_ERR](gg294092\(v=exchg.10\).md)  
[JET\_GRBIT](gg294066\(v=exchg.10\).md)  
[JET\_SESID](gg269253\(v=exchg.10\).md)  
[JET\_TABLEID](gg269182\(v=exchg.10\).md)  
[JET\_OBJECTINFO](gg269353\(v=exchg.10\).md)  
[JET\_TABLECREATE](gg294146\(v=exchg.10\).md)  
[JetGetObjectInfo](gg269232\(v=exchg.10\).md)

