---
description: "Learn more about: TempTableGrbit enumeration"
title: TempTableGrbit enumeration
TOCTitle: TempTableGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.TempTableGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.temptablegrbit(v=EXCHG.10)
ms:contentKeyID: 39515065
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.TempTableGrbit
- Microsoft.Isam.Esent.Interop.TempTableGrbit.ErrorOnDuplicateInsertion
- Microsoft.Isam.Esent.Interop.TempTableGrbit.None
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Unique
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Updatable
- Microsoft.Isam.Esent.Interop.TempTableGrbit.SortNullsHigh
- Microsoft.Isam.Esent.Interop.TempTableGrbit.ForceMaterialization
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Indexed
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Scrollable
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.TempTableGrbit.ErrorOnDuplicateInsertion
- Microsoft.Isam.Esent.Interop.TempTableGrbit.None
- Microsoft.Isam.Esent.Interop.TempTableGrbit
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Indexed
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Updatable
- Microsoft.Isam.Esent.Interop.TempTableGrbit.ForceMaterialization
- Microsoft.Isam.Esent.Interop.TempTableGrbit.SortNullsHigh
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Scrollable
- Microsoft.Isam.Esent.Interop.TempTableGrbit.Unique
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# TempTableGrbit enumeration

Options for temporary table creation.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration TempTableGrbit
'Usage
Dim instance As TempTableGrbit
```

``` csharp
[FlagsAttribute]
public enum TempTableGrbit
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
<td>Indexed</td>
<td>This option requests that the temporary table be flexible enough to permit the use of JetSeek to lookup records by index key. If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</td>
</tr>
<tr class="odd">
<td></td>
<td>Unique</td>
<td>This option requests that records with duplicate index keys be removed from the final set of records in the temporary table. Prior to Windows Server 2003, the database engine always assumed this option to be in effect due to the fact that all clustered indexes must also be a primary key and thus must be unique. As of Windows Server 2003, it is now possible to create a temporary table that does NOT remove duplicates when the <a href="dn351284(v=exchg.10).md">ForwardOnly</a> option is also specified. It is not possible to know which duplicate will win and which duplicates will be discarded in general. However, when the ErrorOnDuplicateInsertion option is requested then the first record with a given index key to be inserted into the temporary table will always win.</td>
</tr>
<tr class="even">
<td></td>
<td>Updatable</td>
<td>This option requests that the temporary table be flexible enough to allow records that have previously been inserted to be subsequently changed. If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</td>
</tr>
<tr class="odd">
<td></td>
<td>Scrollable</td>
<td>This option requests that the temporary table be flexible enough to allow records to be scanned in arbitrary order and direction using <a href="dn292217(v=exchg.10).md">JetMove(JET_SESID, JET_TABLEID, Int32, MoveGrbit)</a>. If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</td>
</tr>
<tr class="even">
<td></td>
<td>SortNullsHigh</td>
<td>This option requests that NULL key column values sort closer to the end of the index than non-NULL key column values.</td>
</tr>
<tr class="odd">
<td></td>
<td>ForceMaterialization</td>
<td>This option forces the temporary table manager to abandon any attempt to choose a clever strategy for managing the temporary table that will result in enhanced performance.</td>
</tr>
<tr class="even">
<td></td>
<td>ErrorOnDuplicateInsertion</td>
<td>This option requests that any attempt to insert a record with the same index key as a previously inserted record will immediately fail with <a href="hh564840(v=exchg.10).md">KeyDuplicate</a>. If this option is not requested then a duplicate may be detected immediately and fail or may be silently removed later depending on the strategy chosen by the database engine to implement the temporary table based on the requested functionality. If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

[ForwardOnly](./server2003grbits.forwardonly-field.md)

[IntrinsicLVsOnly](./windows7grbits.intrinsiclvsonly-field.md)
