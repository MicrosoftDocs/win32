---
description: "Learn more about: JET_RECPOS Structure"
title: JET_RECPOS Structure
TOCTitle: JET_RECPOS Structure
ms:assetid: 7c335120-4b84-4095-8f13-e5315d4996b1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269308(v=EXCHG.10)
ms:contentKeyID: 32765598
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

# JET_RECPOS Structure


_**Applies to:** Windows | Windows Server_

## JET_RECPOS Structure

The **JET_RECPOS** structure contains a collection of integers that represent a fractional position within an index. **centriesLT** is the number of index entries less than the current index key. **centriesInRange** is the number of index entries equal to the current key. **centriesInRange** is not supported and is always returned as 1. **centriesTotal** is the number of index entries in the index. All values are approximations with no guarantee of accuracy.

```cpp
    typedef struct {
      unsigned long cbStruct;
      unsigned long centriesLT;
      unsigned long centriesInRange;
      unsigned long centriesTotal;
    } JET_RECPOS;
```

### Members

**cbStruct**

The size of the [JET_RETINFO](./jet-retinfo-structure.md) structure, in bytes. This value confirms the presence of the following fields.

**centriesLT**

The approximate number of index entries less than the current key.

**centriesInRange**

The approximate number of index entries equal to the current key. This field is always set to 1, regardless of the number of index entries that are actually equal to the current key.

**centriesTotal**

The approximate number of entries in the index.

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

[JET_RETINFO](./jet-retinfo-structure.md)  
[JetGetRecordPosition](./jetgetrecordposition-function.md)
