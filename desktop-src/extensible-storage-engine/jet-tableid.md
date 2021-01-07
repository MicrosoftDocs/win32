---
description: "Learn more about: JET_TABLEID"
title: JET_TABLEID
TOCTitle: JET_TABLEID
ms:assetid: 09705c32-97d8-460c-8b58-921497e29c13
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269182(v=EXCHG.10)
ms:contentKeyID: 32765485
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

# JET_TABLEID


_**Applies to:** Windows | Windows Server_

## JET_TABLEID

The JET_TABLEID data type contains a handle to the database cursor to use for a call to the JET API. A cursor can only be used with the session that was used to open that cursor.

```cpp
    typedef JET_API_PTR JET_TABLEID;
```

### Data Types

JET_TABLEID

Either **NULL** or [JET_tableidNil](./invalid-handle-constants.md) can be used to indicate an invalid cursor handle.

### Remarks

A cursor manages the use of a table for the database engine. A cursor can do the following tasks:

  - Scan records

  - Search for records

  - Choose the effective sort order and visibility of those records

  - Create, update, or delete records

  - Modify the schema of the table

The supported functionality of the cursor might change as the status or type of the underlying table changes. For example, a temporary table might disallow searching for data when it is opened with certain options. The cursor is always fully connected to the underlying table and interacts with that data directly without any caching. Almost all of the core ISAM functionality that is exposed by this database engine is works through the cursor.

A cursor can be created using [JetOpenTable](./jetopentable-function.md) or [JetOpenTempTable](./jetopentemptable-function.md). A cursor can be duplicated using [JetDupCursor](./jetdupcursor-function.md). A cursor can be explicitly closed using [JetCloseTable](./jetclosetable-function.md) or implicitly closed using [JetEndSession](./jetendsession-function.md) or [JetTerm](./jetterm-function.md). A cursor can also be implicitly closed by [JetRollback](./jetrollback-function.md) if it was opened in the transaction that was aborted. The maximum number of cursors that can be created at any one time is controlled by [JET_paramMaxCursors](./resource-parameters.md), which can be configured using [JetSetSystemParameter](./jetsetsystemparameter-function.md).

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

[JET_paramMaxSessions](./resource-parameters.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetDupCursor](./jetdupcursor-function.md)  
[JetEndSession](./jetendsession-function.md)  
[JetOpenTable](./jetopentable-function.md)  
[JetOpenTempTable](./jetopentemptable-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetTerm](./jetterm-function.md)
