---
title: JetCloseTable Function
TOCTitle: JetCloseTable Function
ms:assetid: c8975145-e48a-4029-9522-1509263019ae
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294087(v=EXCHG.10)
ms:contentKeyID: 32765702
ms.date: 04/11/2016
ms.topic: article
api_name: 
- JetCloseTable
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetCloseTable Function


_**Applies to:** Windows | Windows Server_

## JetCloseTable Function

The **JetCloseTable** function closes an open table in a database. The table may be a temporary table or a normal table.

    JET_ERR JET_API JetCloseTable(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid
    );

### Parameters

*sesid*

Identifies the database session context that will be used for the API call.

*tableid*

Identifies the table to be closed.

Set *tableid* to JET_tableidNil to release memory.

### Return Value

This function returns the [JET_ERR](gg294092\(v=exchg.10\).md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errSuccess</p></td>
<td><p>The operation completed successfully.</p></td>
</tr>
</tbody>
</table>


#### Remarks

This function must be called on all tables opened with [JetOpenTable](gg294118\(v=exchg.10\).md).

The exception to this rule happens when [JetOpenTable](gg294118\(v=exchg.10\).md) is called in a transaction and the transaction is rolled back (with [JetRollback](gg269273\(v=exchg.10\).md)). When rolling back a transaction, the table is automatically closed. In this case, it is an error to close the table with **JetCloseTable**.

#### Requirements

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
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](gg294092\(v=exchg.10\).md)  
[JET_GRBIT](gg294066\(v=exchg.10\).md)  
[JET_SESID](gg269253\(v=exchg.10\).md)  
[JET_TABLEID](gg269182\(v=exchg.10\).md)  
[JetOpenTable](gg294118\(v=exchg.10\).md)  
[JetRollback](gg269273\(v=exchg.10\).md)

