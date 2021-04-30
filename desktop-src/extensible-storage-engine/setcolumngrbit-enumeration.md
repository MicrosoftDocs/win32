---
description: "Learn more about: SetColumnGrbit enumeration"
title: SetColumnGrbit enumeration
TOCTitle: SetColumnGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.SetColumnGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.setcolumngrbit(v=EXCHG.10)
ms:contentKeyID: 39509934
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.AppendLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.RevertToDefaultValue
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.ZeroLength
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.UniqueMultiValues
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.OverwriteLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.SeparateLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.SizeLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.IntrinsicLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.None
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.UniqueNormalizedMultiValues
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.RevertToDefaultValue
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.None
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.OverwriteLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.SeparateLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.UniqueNormalizedMultiValues
- Microsoft.Isam.Esent.Interop.SetColumnGrbit
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.UniqueMultiValues
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.SizeLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.IntrinsicLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.AppendLV
- Microsoft.Isam.Esent.Interop.SetColumnGrbit.ZeroLength
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SetColumnGrbit enumeration

Options for JetSetColumn.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration SetColumnGrbit
'Usage
Dim instance As SetColumnGrbit
```

``` csharp
[FlagsAttribute]
public enum SetColumnGrbit
```

## Members

<table>
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
<td>AppendLV</td>
<td>This option is used to append data to a column of type JET_coltypLongText or JET_coltypLongBinary. The same behavior can be achieved by determining the size of the existing long value and specifying ibLongValue in psetinfo. However, its simpler to use this grbit since knowing the size of the existing column value is not necessary.</td>
</tr>
<tr class="odd">
<td></td>
<td>OverwriteLV</td>
<td>This option is used replace the existing long value with the newly provided data. When this option is used, it is as though the existing long value has been set to 0 (zero) length prior to setting the new data.</td>
</tr>
<tr class="even">
<td></td>
<td>RevertToDefaultValue</td>
<td>This option is only applicable for tagged, sparse or multi-valued columns. It causes the column to return the default column value on subsequent retrieve column operations. All existing column values are removed.</td>
</tr>
<tr class="odd">
<td></td>
<td>SeparateLV</td>
<td>This option is used to force a long value, columns of type JET_coltyp.LongText or JET_coltyp.LongBinary, to be stored separately from the remainder of record data. This occurs normally when the size of the long value prevents it from being stored with remaining record data. However, this option can be used to force the long value to be stored separately. Note that long values four bytes in size of smaller cannot be forced to be separate. In such cases, the option is ignored.</td>
</tr>
<tr class="even">
<td></td>
<td>SizeLV</td>
<td>This option is used to interpret the input buffer as a integer number of bytes to set as the length of the long value described by the given columnid and if provided, the sequence number in psetinfo-&gt;itagSequence. If the size given is larger than the existing column value, the column will be extended with 0s. If the size is smaller than the existing column value then the value will be truncated.</td>
</tr>
<tr class="odd">
<td></td>
<td>UniqueMultiValues</td>
<td>This option is used to enforce that all values in a multi-valued column are distinct. This option compares the source column data, without any transformations, to other existing column values and an error is returned if a duplicate is found. If this option is given, then AppendLV, OverwriteLV and SizeLV cannot also be given.</td>
</tr>
<tr class="even">
<td></td>
<td>UniqueNormalizedMultiValues</td>
<td>This option is used to enforce that all values in a multi-valued column are distinct. This option compares the key normalized transformation of column data, to other similarly transformed existing column values and an error is returned if a duplicate is found. If this option is given, then AppendLV, OverwriteLV and SizeLV cannot also be given.</td>
</tr>
<tr class="odd">
<td></td>
<td>ZeroLength</td>
<td>This option is used to set a value to zero length. Normally, a column value is set to NULL by passing a cbMax of 0 (zero). However, for some types, like JET_coltyp.Text, a column value can be 0 (zero) length instead of NULL, and this option is used to differentiate between NULL and 0 (zero) length.</td>
</tr>
<tr class="even">
<td></td>
<td>IntrinsicLV</td>
<td>Try to store long-value columns in the record, even if they exceed the default separation size.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

[Compressed](./windows7grbits.compressed-field.md)

[Uncompressed](./windows7grbits.uncompressed-field.md)
