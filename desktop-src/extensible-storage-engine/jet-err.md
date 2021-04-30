---
description: "Learn more about: JET_ERR"
title: JET_ERR
TOCTitle: JET_ERR
ms:assetid: cd9cb876-251c-458d-a015-8e9045e77fc9
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294092(v=EXCHG.10)
ms:contentKeyID: 32765707
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

# JET_ERR


_**Applies to:** Windows | Windows Server_

## JET_ERR

The **JET_ERR** data type contains an [Extensible Storage Engine error code](./extensible-storage-engine-error-codes.md).

```cpp
typedef long JET_ERR;
```

### Data Types

JET_ERR

A zero value (corresponding to JET_errSuccess) indicates that the call succeeded. A positive value warns of a non-fatal condition that occurred during an otherwise successful call. A negative value indicates that the call failed.

### Remarks

For information about returning errors as HRESULTs, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md). For information about flags for configuring the database to handle errors, see [Error Handling Parameters](./error-handling-parameters.md).

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

[Extensible Storage Engine Errors](./extensible-storage-engine-errors.md)  
[Extensible Storage Engine Error Codes](./extensible-storage-engine-error-codes.md)  
[Error Handling Parameters](./error-handling-parameters.md)
