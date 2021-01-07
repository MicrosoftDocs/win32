---
description: "Learn more about: Invalid Handle Constants"
title: Invalid Handle Constants
TOCTitle: Invalid Handle Constants
ms:assetid: 594d7804-725f-4f72-b5f0-56f099c1c17b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269256(v=EXCHG.10)
ms:contentKeyID: 32765558
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

# Invalid Handle Constants


_**Applies to:** Windows | Windows Server_

## Invalid Handle Constants

The following constants indicate invalid handles for different aspects of ESE.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Constant/value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_instanceNil<br />
(~(JET_INSTANCE)0)</p></td>
<td><p>An invalid handle for a database instance.<br />
<strong>Windows XP:</strong> Introduced in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>JET_sesidNil<br />
(~(JET_SESID)0)</p></td>
<td><p>An invalid handle for a session ID.</p></td>
</tr>
<tr class="odd">
<td><p>JET_tableidNil<br />
(~(JET_TABLEID)0)</p></td>
<td><p>An invalid handle for a table ID.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitNil<br />
((JET_GRBIT)0)</p></td>
<td><p>An invalid handle for a group of bits.</p></td>
</tr>
<tr class="odd">
<td><p>JET_LSNil<br />
(~(JET_LS)0)</p></td>
<td><p>An invalid handle for the Local Storage.</p></td>
</tr>
<tr class="even">
<td><p>JET_dbidNil<br />
((JET_DBID) 0xFFFFFFFF)</p></td>
<td><p>An invalid handle for the database ID.</p></td>
</tr>
</tbody>
</table>


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

