---
title: JET_RECORDLIST Structure
TOCTitle: JET_RECORDLIST Structure
ms:assetid: 6b4d97a0-4b42-4f7c-bb18-b6db3c92668a
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269287(v=EXCHG.10)
ms:contentKeyID: 32765579
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

# JET_RECORDLIST Structure


_**Applies to:** Windows | Windows Server_

## JET_RECORDLIST Structure

The **JET_RECORDLIST** structure finds records that are in the intersection of specified index ranges when they are used with the [JetIntersectIndexes](gg269289\(v=exchg.10\).md) function.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_TABLEID tableid;
      unsigned long cRecord;
      JET_COLUMNID columnidBookmark;
    } JET_RECORDLIST;
```

### Members

**cbStruct**

The size of the **JET_RECORDLIST** structure, in bytes.

**tableid**

The table identifier of a temporary table that contains the bookmarks for the results of the query. The table will automatically be closed if the current transaction is rolled back with [JetRollback](gg269273\(v=exchg.10\).md); otherwise, it must be closed with [JetCloseTable](gg294087\(v=exchg.10\).md).

**cRecord**

The number of rows in the temporary table.

**columnidBookmark**

The column identifier of the bookmark column in the temporary table.

### Remarks

The temporary table that is identified by **tableid** has a single column. That single column holds bookmarks, and each record should fit in a buffer of size JET_cbBookmarkMost bytes.

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

[JET_COLUMNID](gg294104\(v=exchg.10\).md)  
[JET_GRBIT](gg294066\(v=exchg.10\).md)  
[JET_TABLEID](gg269182\(v=exchg.10\).md)  
[JetCloseTable](gg294087\(v=exchg.10\).md)  
[JetIntersectIndexes](gg269289\(v=exchg.10\).md)  
[JetRollback](gg269273\(v=exchg.10\).md)

