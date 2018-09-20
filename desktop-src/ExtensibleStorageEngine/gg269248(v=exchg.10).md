---
title: JET_DBID
TOCTitle: JET_DBID
ms:assetid: 516acb79-aa75-4609-81b6-3b2e4e0c95af
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269248(v=EXCHG.10)
ms:contentKeyID: 32765550
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET\_DBID


_**Applies to:** Windows | Windows Server_

## JET\_DBID

The **JET\_DBID** data type contains the handle to the database. A database handle is used to manage the schema of a database. It can also be used to manage the tables inside of that database.

    typedef unsigned long JET_DBID;

### Data Types

JET\_DBID

Handle to the database.

A value of JET\_dbidNil indicates that the handle is invalid.

### Remarks

A database handle is created by means of a call to [JetCreateDatabase](gg269212\(v=exchg.10\).md) or [JetOpenDatabase](gg269299\(v=exchg.10\).md).

A database handle can be explicitly closed by [JetCloseDatabase](gg294123\(v=exchg.10\).md) or implicitly closed by [JetEndSession](gg294054\(v=exchg.10\).md) or [JetTerm](gg269298\(v=exchg.10\).md).

A database handle can be used only within the session in which it was created. The existence of a database handle corresponds to the logical open of a database. A logical open is different from the physical open of a database, which happens when a database is attached to the system.

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

[JetCreateDatabase](gg269212\(v=exchg.10\).md)  
[JetOpenDatabase](gg269299\(v=exchg.10\).md)  
[JetCloseDatabase](gg294123\(v=exchg.10\).md)  
[JetEndSession](gg294054\(v=exchg.10\).md)

