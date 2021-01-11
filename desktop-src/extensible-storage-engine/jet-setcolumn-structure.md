---
description: "Learn more about: JET_SETCOLUMN Structure"
title: JET_SETCOLUMN Structure
TOCTitle: JET_SETCOLUMN Structure
ms:assetid: 3fdb8ec0-3c40-44f3-9859-72e22a504b90
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269233(v=EXCHG.10)
ms:contentKeyID: 32765535
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

# JET_SETCOLUMN Structure


_**Applies to:** Windows | Windows Server_

## JET_SETCOLUMN Structure

The **JET_SETCOLUMN** structure contains input and output parameters for [JetSetColumns](./jetsetcolumns-function.md). Fields in the structure describe what column value to set, how to set it, and where to get the column set data.

```cpp
    typedef struct {
      JET_COLUMNID columnid;
      const void* pvData;
      unsigned long cbData;
      JET_GRBIT grbit;
      unsigned long ibLongValue;
      unsigned long itagSequence;
      JET_ERR err;
    } JET_SETCOLUMN;
```

### Members

**columnid**

The column identifier for a column to set.

**pvData**

A pointer to data to set into a column.

**cbData**

The size of allocation, in bytes, starting at **pvData** in bytes.

**grbit**

A group of bits that contain the options to be used for this call, which include zero or more of the following.

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
<td><p>JET_bitSetAppendLV</p></td>
<td><p>Appends data to a column of type <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a> or <a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a>. The same behavior can be achieved by determining the size of the existing long value and specifying <strong>ibLongValue</strong> in <strong>psetinfo</strong>. However, it's simpler to use this <em>grbit</em>, since knowing the size of the existing column value is not necessary.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitSetOverwriteLV</p></td>
<td><p>Replaces the existing long value with the new data. When this option is used, it is as though the existing long value has been set to 0 (zero) length prior to setting the new data.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitSetSizeLV</p></td>
<td><p>Interprets the input buffer as an integer number of bytes to set as the length of the long value described by the given columnid and if provided, the sequence number in psetinfo-&gt;itagSequence. If the size given is larger than the existing column value, the column will be extended with 0s. If the size is smaller than the existing column value then the value will be truncated.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitSetZeroLength</p></td>
<td><p>Sets a value to zero length. Normally, a column value is set to NULL by passing a cbMax of 0. However, for some types, like <a href="gg269213(v=exchg.10).md">JET_coltypText</a>, a column value can be 0 length instead of NULL, and this option is used to differentiate between NULL and 0 length.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitSetSeparateLV</p></td>
<td><p>Forces a long value, columns of type <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a> or <a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a>, to be stored separately from the remainder of record data. This occurs normally when the size of the long value prevents it from being stored with remaining record data. However, this option can be used to force the long value to be stored separately. Note that long values four bytes in size or smaller cannot be forced to be separate. In such cases, the option is ignored.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitSetUniqueMultiValues</p></td>
<td><p>Enforces distinct values in a multi-valued column. This option compares the source column data, without any transformations, to other existing column values and an error is returned if a duplicate is found. If this option is given, then JET_bitSetAppendLv, JET_bitSetOverwriteLV, and JET_bitSetSizeLV cannot also be given.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitSetUniqueNormalizedMultiValues</p></td>
<td><p>Enforces distinct values in a multi-valued column. This option compares the key normalized transformation of column data to other similarly transformed existing column values and an error is returned if a duplicate is found. If this option is given, then JET_bitSetAppendLv, JET_bitSetOverwriteLV, and JET_bitSetSizeLV cannot also be given.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitSetRevertToDefaultValue</p></td>
<td><p>Causes the column to return the default column value on subsequent retrieve column operations. All existing column values are removed. This option is only applicable for tagged, sparse, or multi-valued columns.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitSetIntrinsicLV</p></td>
<td><p>Keeps the long value, columns of type <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a> or JET_coltypeLongBinary, stored with the remaining record data if possible. Normally, long columns are stored separately when their length exceeds 1024 bytes or would otherwise cause the record length to exceed its page size related size limitation. However, if this option is set, the set column operation will fail with error JET_errColumnTooBig rather than store this column value separate from the remaining record data.</p></td>
</tr>
</tbody>
</table>


**ibLongValue**

The offset to the first byte to be retrieved from a column of type [JET_coltypLongBinary](./jet-coltyp.md), or [JET_coltypLongText](./jet-coltyp.md).

**itagSequence**

Describes the sequence number of value in a multi-valued column. An **itagSequence** of 0 indicates that the column value set should be added as a new instance of a multi-valued column.

**err**

Error codes and warnings returned from the set column operation.

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

[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JetSetColumns](./jetsetcolumns-function.md)
