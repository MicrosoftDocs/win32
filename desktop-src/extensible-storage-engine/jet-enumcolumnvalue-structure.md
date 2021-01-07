---
description: "Learn more about: JET_ENUMCOLUMNVALUE Structure"
title: JET_ENUMCOLUMNVALUE Structure
TOCTitle: JET_ENUMCOLUMNVALUE Structure
ms:assetid: a9882d7b-0c53-4a5d-bc98-0979e6e68c88
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294052(v=EXCHG.10)
ms:contentKeyID: 32765652
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

# JET_ENUMCOLUMNVALUE Structure


_**Applies to:** Windows | Windows Server_

## JET_ENUMCOLUMNVALUE Structure

The **JET_ENUMCOLUMNVALUE** structure enumerates the column values of a record using the [JetEnumerateColumns](./jetenumeratecolumns-function.md) function. [JetEnumerateColumns](./jetenumeratecolumns-function.md) returns an array of **JET_ENUMCOLUMNVALUE** structures. The array is returned in memory that was allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to that function.

```cpp
    typedef struct {
      unsigned long itagSequence;
      JET_ERR err;
      unsigned long cbData;
      void* pvData;
    } JET_ENUMCOLUMNVALUE;
```

### Members

**itagSequence**

The column value (by one-based index) that was enumerated.

**err**

The column status code resulting from the enumeration of the column value.

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
<td><p>JET_wrnColumnNull</p></td>
<td><p>The requested column value is NULL.</p></td>
</tr>
<tr class="even">
<td><p>JET_wrnColumnSkipped</p></td>
<td><p>The <em>itagSequence</em> that is specified in the element of the <em>rgtagSequence</em> array in the <a href="gg294138(v=exchg.10).md">JET_ENUMCOLUMN</a> struct corresponding to this <strong>JET_ENUMCOLUMNVALUE</strong> struct was zero.</p></td>
</tr>
<tr class="odd">
<td><p>JET_wrnColumnTruncated</p></td>
<td><p>The requested column value was truncated to the specified size before being returned.</p>
<p>This truncation occurs only for long text and long binary columns that contain large amounts of data.</p></td>
</tr>
</tbody>
</table>


**cbData**

The column value that was enumerated for the column.

The output buffer is returned in memory that was allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to [JetEnumerateColumns](./jetenumeratecolumns-function.md).

**pvData**

The column value that was enumerated for the column.

The output buffer is returned in memory that was allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to [JetEnumerateColumns](./jetenumeratecolumns-function.md).

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

[JET_ENUMCOLUMN](./jet-enumcolumn-structure.md)  
[JET_ENUMCOLUMNVALUE]()  
[JET_ERR](./jet-err.md)  
[JetEnumerateColumns](./jetenumeratecolumns-function.md)  
[realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019)
