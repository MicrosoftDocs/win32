---
title: JET_RECSIZE Structure
TOCTitle: JET_RECSIZE Structure
ms:assetid: bb2a63bb-7956-46c2-9791-0d0678a6c366
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294072(v=EXCHG.10)
ms:contentKeyID: 32765687
ms.date: 04/11/2016
ms.topic: article
api_name: 
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET\_RECSIZE Structure


_**Applies to:** Windows | Windows Server_

## JET\_RECSIZE Structure

The **JET\_RECSIZE** structure is used by [JetGetRecordSize](gg294045\(v=exchg.10\).md) to return information about a record's usage requirements in user data space, number of set columns, number of values, and ESE record structure overhead space.

**Windows Vista:** The **JET\_RECSIZE** structure is introduced in Windows Vista.

    typedef struct {
      unsigned __int64 cbData;
      unsigned __int64 cbLongValueData;
      unsigned __int64 cbOverhead;
      unsigned __int64 cbLongValueOverhead;
      unsigned __int64 cNonTaggedColumns;
      unsigned __int64 cTaggedColumns;
      unsigned __int64 cLongValues;
      unsigned __int64 cMultiValues;
    } JET_RECSIZE;

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

### Remarks

The total number of values in the record would be **cMultiValues** + **cNonTaggedColumns** + **cTaggedColumns**.

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JetGetRecordSize](gg294045\(v=exchg.10\).md)

