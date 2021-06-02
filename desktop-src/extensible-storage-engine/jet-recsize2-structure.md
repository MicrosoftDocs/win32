---
description: "Learn more about: JET_RECSIZE2 Structure"
title: JET_RECSIZE2 Structure
TOCTitle: JET_RECSIZE2 Structure
ms:assetid: 02a13b5b-d904-49b2-baaa-c60328d70290
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269174(v=EXCHG.10)
ms:contentKeyID: 32765477
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

# JET_RECSIZE2 Structure


_**Applies to:** Windows | Windows Server_

## JET_RECSIZE2 Structure

The **JET_RECSIZE2** structure is used by [JetGetRecordSize2](./jetgetrecordsize2-function.md) to return information about a record's usage requirements in user data space, number of set columns, number of values, and ESE record structure overhead space.

**Windows 7:** The **JET_RECSIZE2** structure is introduced in the Windows 7 operating system.

```cpp
    typedef struct {
      unsigned __int64 cbData;
      unsigned __int64 cbLongValueData;
      unsigned __int64 cbOverhead;
      unsigned __int64 cbLongValueOverhead;
      unsigned __int64 cNonTaggedColumns;
      unsigned __int64 cTaggedColumns;
      unsigned __int64 cLongValues;
      unsigned __int64 cMultiValues;
      unsigned __int64 cCompressedColumns;
      unsigned __int64 cbDataCompressed;
      unsigned __int64 cbLongValueDataCompressed;
    } JET_RECSIZE2;
```

### Members

**cbData**

User data set in the record.

**Note**  The key size is not included in this.

**cbLongValueData**

User data associated with the record but stored in the long-value tree.

**Note**  This does not count intrinsic long-values.

**cbOverhead**

The overhead of the ESE record structure for this record. This includes the record's key size.

**cbLongValueOverhead**

The overhead of the long-value data.

**Note**  This does not count intrinsic long-values.

**cNonTaggedColumns**

Total number of fixed and variable columns set in this record.

**cTaggedColumns**

Total number of tagged columns set in this record.

**cLongValues**

Total number of long values stored in the long-value tree for this record.

**Note**  This does not count intrinsic long-values.

**cMultiValues**

The accumulation of the total number of values beyond the first for all columns in the record.

**cCompressedColumns**

The total number of compressed columns.

**cbDataCompressed**

The compressed size of user data in this record. This is the same as cbData if no intrinsic long-values are compressed.

**cbLongValueDataCompressed**

The compressed size of user data in the long-value tree. This is the same as cbLongValue data if no separated long values are compressed.

### Remarks

The total number of values in the record would be **cMultiValues** + **cNonTaggedColumns** + **cTaggedColumns**.

The logical data in the record is (cbData+cbLongValueData) and the physical size of the data is (cbDataCompressed+cbLongValueDataCompressed). This can be used to calculate the compression ratio of stored data.

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista operating system.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008 operating system.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JetGetRecordSize](./jetgetrecordsize-function.md)  
[JetGetRecordSize2](./jetgetrecordsize2-function.md)
