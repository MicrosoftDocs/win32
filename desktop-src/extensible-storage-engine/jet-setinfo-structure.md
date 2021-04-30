---
description: "Learn more about: JET_SETINFO Structure"
title: JET_SETINFO Structure
TOCTitle: JET_SETINFO Structure
ms:assetid: cbc41175-e48f-46b0-aeb1-1120fa2cd981
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294090(v=EXCHG.10)
ms:contentKeyID: 32765705
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

# JET_SETINFO Structure


_**Applies to:** Windows | Windows Server_

## JET_SETINFO Structure

The **JET_SETINFO** structure contains optional input parameters for [JetSetColumn](./jetsetcolumn-function.md). A **NULL** pointer can be passed where a pointer to this structure would otherwise be passed. The meaning of passing a **NULL** is the same as passing **JET_SETINFO** with **cbStruct** set to sizeof(JET_SETINFO), **ibLongValue** set to 0 (zero) and **itagSequence** set to 1.

```cpp
typedef struct {
  unsigned long cbStruct;
  unsigned long ibLongValue;
  unsigned long itagSequence;
} JET_SETINFO;
```

### Members

**cbStruct**

The size, in bytes, of the **JET_SETINFO**. This value confirms the presence of the following fields.

**ibLongValue**

The offset to the first byte to be set in a column of type [JET_coltypLongBinary](./jet-coltyp.md) or [JET_coltypLongText](./jet-coltyp.md).

**itagSequence**

Describes the sequence number of value in a multi-valued column to be set. The array of values is one-based. The first value is sequence 1, not 0 (zero). If the record column has only one value then 1 should be passed as the **itagSequence** if that value is being replaced. A value of 0 (zero) means to add a new column value instance to the end of the sequence of column values.

With a column that can contain multiple values, it is only possible to use a sequence number larger than 1 in [JetSetColumn](./jetsetcolumn-function.md) and [JetRetrieveColumn](./jetretrievecolumn-function.md) or 0 in [JetSetColumn](./jetsetcolumn-function.md). In the current implementation of the engine, any column that was created with JET_bitColumnTagged can contain multiple values. Columns created with JET_bitColumnMultiValued differ from multi-valued tagged columns only in the way that they are indexed. See [JET_INDEXCREATE](./jet-indexcreate-structure.md) for more information.

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

[JetSetColumn](./jetsetcolumn-function.md)
