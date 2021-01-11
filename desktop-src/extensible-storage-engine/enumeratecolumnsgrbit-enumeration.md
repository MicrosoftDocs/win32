---
description: "Learn more about: EnumerateColumnsGrbit enumeration"
title: EnumerateColumnsGrbit enumeration
TOCTitle: EnumerateColumnsGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.enumeratecolumnsgrbit(v=EXCHG.10)
ms:contentKeyID: 39516754
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateCompressOutput
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateCopy
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateIgnoreDefault
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.None
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateTaggedOnly
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumeratePresenceOnly
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateCompressOutput
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateIgnoreDefault
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.None
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateCopy
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumeratePresenceOnly
- Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit.EnumerateTaggedOnly
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EnumerateColumnsGrbit enumeration

Options for JetEnumerateColumns.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration EnumerateColumnsGrbit
'Usage
Dim instance As EnumerateColumnsGrbit
```

``` csharp
[FlagsAttribute]
public enum EnumerateColumnsGrbit
```

## Members

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Member name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>None</td>
<td>Default options.</td>
</tr>
<tr class="even">
<td></td>
<td>EnumerateCompressOutput</td>
<td>When enumerating column values, all columns for which we are retrieving all values and that have only one non-NULL column value may be returned in a compressed format. The status for such columns will be set to <a href="hh557250(v=exchg.10).md">ColumnSingleValue</a> and the size of the column value and the memory containing the column value will be returned directly in the <a href="dn335081(v=exchg.10).md">JET_ENUMCOLUMN</a> structure. It is not guaranteed that all eligible columns are compressed in this manner. See <a href="dn335081(v=exchg.10).md">JET_ENUMCOLUMN</a> for more information.</td>
</tr>
<tr class="odd">
<td></td>
<td>EnumerateCopy</td>
<td>This option indicates that the modified column values of the record should be enumerated rather than the original column values. If a column value has not been modified, the original column value is enumerated. In this way, a column value that has not yet been inserted or updated may be enumerated when inserting or updating a record.
<p>This option is identical to <a href="hh578120(v=exchg.10).md">RetrieveCopy</a>.</p></td>
</tr>
<tr class="even">
<td></td>
<td>EnumerateIgnoreDefault</td>
<td>If a given column is not present in the record then no column value will be returned. Ordinarily, the default value for the column, if any, would be returned in this case. It is guaranteed that if the column is set to a value different than the default value then that different value will be returned (that is, if a column with a default value is explicitly set to NULL then a NULL will be returned as the value for that column). Even if this option is requested, it is still possible to see a column value that happens to be equal to the default value. No effort is made to remove column values that match their default values. It is important to remember that this option affects the output of <a href="dn292148(v=exchg.10).md">JetEnumerateColumns(JET_SESID, JET_TABLEID, Int32, [], Int32, [], JET_PFNREALLOC, IntPtr, Int32, EnumerateColumnsGrbit)</a> when used with EnumeratePresenceOnly or EnumerateTaggedOnly.</td>
</tr>
<tr class="odd">
<td></td>
<td>EnumeratePresenceOnly</td>
<td>If a non-NULL value exists for the requested column or column value then the associated data is not returned. Instead, the associated status for that column or column value will be set to <a href="hh557250(v=exchg.10).md">ColumnPresent</a>. If the column or column value is NULL then <a href="hh557250(v=exchg.10).md">ColumnNull</a> will be returned as usual.</td>
</tr>
<tr class="even">
<td></td>
<td>EnumerateTaggedOnly</td>
<td>When enumerating all column values in the record (for example,that is when numColumnids is zero), only tagged column values will be returned. This option is not allowed when enumerating a specific array of column IDs.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

[EnumerateIgnoreUserDefinedDefault](./server2003grbits.enumerateignoreuserdefineddefault-field.md)

[EnumerateInRecordOnly](./windows7grbits.enumerateinrecordonly-field.md)
