---
description: "Learn more about: CreateIndexGrbit enumeration"
title: CreateIndexGrbit enumeration
TOCTitle: CreateIndexGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.CreateIndexGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.createindexgrbit(v=EXCHG.10)
ms:contentKeyID: 39511957
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexUnversioned
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexIgnoreFirstNull
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexUnique
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexDisallowNull
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexPrimary
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.None
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexSortNullsHigh
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexIgnoreAnyNull
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexLazyFlush
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexEmpty
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexIgnoreNull
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexEmpty
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.None
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexIgnoreFirstNull
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexIgnoreAnyNull
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexLazyFlush
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexUnversioned
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexSortNullsHigh
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexDisallowNull
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexIgnoreNull
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexPrimary
- Microsoft.Isam.Esent.Interop.CreateIndexGrbit.IndexUnique
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# CreateIndexGrbit enumeration

Options for JetCreateIndex.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration CreateIndexGrbit
'Usage
Dim instance As CreateIndexGrbit
```

``` csharp
[FlagsAttribute]
public enum CreateIndexGrbit
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
<td>IndexUnique</td>
<td>Duplicate index entries (keys) are disallowed. This is enforced when JetUpdate is called, not when JetSetColumn is called.</td>
</tr>
<tr class="odd">
<td></td>
<td>IndexPrimary</td>
<td>The index is a primary (clustered) index. Every table must have exactly one primary index. If no primary index is explicitly defined over a table, then the database engine will create its own primary index.</td>
</tr>
<tr class="even">
<td></td>
<td>IndexDisallowNull</td>
<td>None of the columns over which the index is created may contain a NULL value.</td>
</tr>
<tr class="odd">
<td></td>
<td>IndexIgnoreNull</td>
<td>Do not add an index entry for a row if all of the columns being indexed are NULL.</td>
</tr>
<tr class="even">
<td></td>
<td>IndexIgnoreAnyNull</td>
<td>Do not add an index entry for a row if any of the columns being indexed are NULL.</td>
</tr>
<tr class="odd">
<td></td>
<td>IndexIgnoreFirstNull</td>
<td>Do not add an index entry for a row if the first column being indexed is NULL.</td>
</tr>
<tr class="even">
<td></td>
<td>IndexLazyFlush</td>
<td>Specifies that the index operations will be logged lazily. JET_bitIndexLazyFlush does not affect the laziness of data updates. If the indexing operations is interrupted by process termination, Soft Recovery will still be able to able to get the database to a consistent state, but the index may not be present.</td>
</tr>
<tr class="odd">
<td></td>
<td>IndexEmpty</td>
<td>Do not attempt to build the index, because all entries would evaluate to NULL. grbit MUST also specify JET_bitIgnoreAnyNull when JET_bitIndexEmpty is passed. This is a performance enhancement. For example if a new column is added to a table, then an index is created over this newly added column, all of the records in the table would be scanned even though they would never get added to the index anyway. Specifying JET_bitIndexEmpty skips the scanning of the table, which could potentially take a long time.</td>
</tr>
<tr class="even">
<td></td>
<td>IndexUnversioned</td>
<td>Causes index creation to be visible to other transactions. Normally a session in a transaction will not be able to see an index creation operation in another session. This flag can be useful if another transaction is likely to create the same index, so that the second index-create will simply fail instead of potentially causing many unnecessary database operations. The second transaction may not be able to use the index immediately. The index creation operation needs to complete before it is usable. The session must not currently be in a transaction to create an index without version information.</td>
</tr>
<tr class="odd">
<td></td>
<td>IndexSortNullsHigh</td>
<td>Specifying this flag causes NULL values to be sorted after data for all columns in the index.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
