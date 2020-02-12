---
title: JET_PFNSTATUS Callback Function
TOCTitle: JET_PFNSTATUS Callback Function
ms:assetid: 8b0cf5bf-a4ee-4d8f-8dd7-556c35cd269d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269326(v=EXCHG.10)
ms:contentKeyID: 32765616
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

# JET_PFNSTATUS Callback Function


_**Applies to:** Windows | Windows Server_

## JET_PFNSTATUS Callback Function

The **JET_PFNSTATUS** callback function receives information about the progress of long-running operations, such as defragmentation, backup, or restore operations. During such operations, the database engine calls this callback function to give an update on the progress of the operation.

```cpp
    JET_ERR JET_API JET_PFNSTATUS(
                           JET_SESID  sesid,
                           JET_SNP snp,
                           JET_SNT snt,
                           void* pv
    );
```

### Parameters

*sesid*

The session of type [JET_SESID](gg269253\(v=exchg.10\).md) with which the long-running function was called.

*snp*

The type of operation as specified in [JET_SNP](gg269311\(v=exchg.10\).md). Types of operations include repair, compact, restore, backup, update, scrub, and update the record format.

*snt*

The status of an operation. Status types include beginning, in progress, completion, or failure. The status will be specified with the third parameter of type [JET_SNT](gg269294\(v=exchg.10\).md).

*pv*

An optional pointer to a structure of type [JET_SNPROG](gg269328\(v=exchg.10\).md).

### Return Value

This function returns the [JET_ERR](gg294092\(v=exchg.10\).md) datatype with one of the [Extensible Storage Engine error codes](gg269297\(v=exchg.10\).md). For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

On success, the operation that issued the callback can proceed normally. In some cases, the callback might return a warning that influences that operation.

On failure, the operation that issued the callback might proceed normally or might fail.

### Remarks

This callback function will be used in a progress notification in which the structure will indicate the current state of the progress. Note that the callback function might be called multiple times for the progress of the operation.

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

[Extensible Storage Engine error codes](gg269297\(v=exchg.10\).md)  
[Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md)  
[JET_SESID](gg269253\(v=exchg.10\).md)  
[JET_SNP](gg269311\(v=exchg.10\).md)  
[JET_SNPROG](gg269328\(v=exchg.10\).md)  
[JET_SNT](gg269294\(v=exchg.10\).md)

