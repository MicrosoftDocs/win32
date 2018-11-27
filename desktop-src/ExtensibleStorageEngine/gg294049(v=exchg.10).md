---
title: JET_RETINFO Structure
TOCTitle: JET_RETINFO Structure
ms:assetid: a47a7902-3ecd-4d42-941f-89d25d78eb4c
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294049(v=EXCHG.10)
ms:contentKeyID: 32765648
ms.date: 04/11/2016
ms.topic: article
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET\_RETINFO Structure


_**Applies to:** Windows | Windows Server_

## JET\_RETINFO Structure

The **JET\_RETINFO** structure contains optional input and output parameters for [JetRetrieveColumn](gg269198\(v=exchg.10\).md). A null pointer can be passed where a pointer to this structure would otherwise be passed. Passing a null pointer is the same as passing **JET\_RETINFO** with **cbStruct** set to sizeof(JET\_RETINFO), **ibLongValue** set to 0 (zero) and **itagSequence** set to 1.

    typedef struct {
      unsigned long cbStruct;
      unsigned long ibLongValue;
      unsigned long itagSequence;
      JET_COLUMNID columnidNextTagged;
    } JET_RETINFO;

### Members

**cbStruct**

Must be set to the size of the **JET\_RETINFO** structure, in bytes, and serves to confirm the presence of the following fields.

**ibLongValue**

The offset to the first byte to be retrieved from a column of type [JET\_coltypLongBinary](gg269213\(v=exchg.10\).md), or [JET\_coltypLongText](gg269213\(v=exchg.10\).md). Note that the amount of data retrieved from this offset is the lower of the size of the output buffer and the size of data in the actual value after this offset.

**itagSequence**

Describes the sequence number of value in a multi-valued column. Note that the array of values is one-based. The first value is sequence 1, not 0. If the record column has only one value then 1 should be passed as the **itagSequence**

With a column that can contain multiple values, it is only possible to use a sequence number larger than 1 in [JetSetColumn](gg294137\(v=exchg.10\).md) and [JetRetrieveColumn](gg269198\(v=exchg.10\).md) or 0 in [JetSetColumn](gg294137\(v=exchg.10\).md). In the current implementation of the engine, any column that was created with JET\_bitColumnTagged can contain multiple values. Columns created with JET\_bitColumnMultiValued differ from multi-valued tagged columns only in the way that they are indexed. See [JET\_INDEXCREATE](gg269186\(v=exchg.10\).md) for more information.

**columnidNextTagged**

Returns the columnid of the retrieved tagged, multi-valued or sparse, column when all tagged columns are retrieved by passing 0 as the columnid to [JetRetrieveColumn](gg269198\(v=exchg.10\).md).

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

[JET\_COLTYP](gg269213\(v=exchg.10\).md)  
[JET\_COLUMNID](gg294104\(v=exchg.10\).md)  
[JET\_RETINFO](gg294049\(v=exchg.10\).md)  
[JetRetrieveColumn](gg269198\(v=exchg.10\).md)

