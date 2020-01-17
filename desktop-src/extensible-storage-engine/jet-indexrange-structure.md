---
title: JET_INDEXRANGE Structure
TOCTitle: JET_INDEXRANGE Structure
ms:assetid: 8e437f7d-1e21-4a0b-a5a5-1c78235a4f80
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269335(v=EXCHG.10)
ms:contentKeyID: 32765624
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

# JET_INDEXRANGE Structure


_**Applies to:** Windows | Windows Server_

## JET_INDEXRANGE Structure

The **JET_INDEXRANGE** structure identifies an index range when it is used with the [JetIntersectIndexes](gg269289\(v=exchg.10\).md) function.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_TABLEID tableid;
      JET_GRBIT grbit;
    } JET_INDEXRANGE;
```

### Members

**cbStruct**

The size, in bytes, of the **JET_INDEXRANGE**.

**tableid**

A cursor that has previously had an index range set with [JetSetIndexRange](gg294112\(v=exchg.10\).md).

**grbit**

A bitmask composed of exactly one of the following.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_bitRecordInIndex</p></td>
<td><p>Specifies that the index range should be treated normally.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitRecordNotInIndex</p></td>
<td><p>Reserved for future use. Do not use.</p></td>
</tr>
</tbody>
</table>


### Remarks

Each **JET_INDEXRANGE** structure that is passed to [JetIntersectIndexes](gg269289\(v=exchg.10\).md) represents an index range, which will be intersected by the API call. The cursor that is given in **JET_INDEXRANGE** must have a valid index range set on it already, with a successful call to [JetSetIndexRange](gg294112\(v=exchg.10\).md).

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
[JetSetIndexRange](gg294112\(v=exchg.10\).md)

