---
description: "Learn more about: Error Handling Constants"
title: Error Handling Constants
TOCTitle: Error Handling Constants
ms:assetid: 5a1f9438-2d36-483e-9820-d0de30ee5e01
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269258(v=EXCHG.10)
ms:contentKeyID: 32765560
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

# Error Handling Constants


_**Applies to:** Windows | Windows Server_

## Error Handling Constants

The following constants are used to set the range for the [JET_paramExceptionAction](./error-handling-parameters.md) system parameters.

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
<td><p>JET_ExceptionMsgBox<br />
0x0001</p></td>
<td><p>Displays a message box when an exception occurs.</p></td>
</tr>
<tr class="even">
<td><p>JET_ExceptionNone<br />
0x0002</p></td>
<td><p>Does nothing when an exception occurs.</p></td>
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


### See Also

[Error Handling Parameters](./error-handling-parameters.md)
