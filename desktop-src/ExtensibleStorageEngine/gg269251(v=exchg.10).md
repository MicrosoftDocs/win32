---
title: JET_ENUMCOLUMNID Structure
TOCTitle: JET_ENUMCOLUMNID Structure
ms:assetid: 5480ebf1-4fc9-49b5-bbb3-12542b86c8f1
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269251(v=EXCHG.10)
ms:contentKeyID: 32765553
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

# JET\_ENUMCOLUMNID Structure


_**Applies to:** Windows | Windows Server_

## JET\_ENUMCOLUMNID Structure

The **JET\_ENUMCOLUMNID** structure enumerates a specific set of columns and, optionally, a specific set of multiple values for those columns when the [JetEnumerateColumns](gg269321\(v=exchg.10\).md) function is used. [JetEnumerateColumns](gg269321\(v=exchg.10\).md) returns an array of **JET\_ENUMCOLUMNID** structures.

    typedef struct {
      JET_COLUMNID columnid;
      unsigned long ctagSequence;
      unsigned long* rgtagSequence;
    } JET_ENUMCOLUMNID;

### Members

**columnid**

The column ID to enumerate.

If the column ID is 0 (zero) then the enumeration of this column is skipped and a corresponding slot in the output array of [JET\_ENUMCOLUMN](gg294138\(v=exchg.10\).md) structures will be generated with a column state of JET\_wrnColumnSkipped.

**ctagSequence**

Optionally identifies an array of column values (by one-based index) to enumerate for the specified column ID.

If **ctagSequence** is 0 (zero) then **rgtagSequence** is ignored and all column values for the specified column ID will be enumerated.

If an element of **rgtagSequence** is 0 (zero), then the enumeration of that column value (by one-based index) will be skipped. A corresponding slot in the output array of the **JET\_ENUMCOLUMNID** structure will be generated with a column status value of JET\_wrnColumnSkipped.

**rgtagSequence**

An array of one-based indices into the array of column values for a given column. A single element is an **itagSequence** which is defined in [JET\_RETRIEVECOLUMN](gg269334\(v=exchg.10\).md). An **itagSequence** of 0 (zero) means "skip". An **itagSequence** of 1 means return the first column value of the column, 2 means the second, and so on.

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

[JET\_COLUMNID](gg294104\(v=exchg.10\).md)  
[JET\_ENUMCOLUMN](gg294138\(v=exchg.10\).md)  
[JET\_ENUMCOLUMNID](gg269251\(v=exchg.10\).md)  
[JET\_RETRIEVECOLUMN](gg269334\(v=exchg.10\).md)  
[JetEnumerateColumns](gg269321\(v=exchg.10\).md)

