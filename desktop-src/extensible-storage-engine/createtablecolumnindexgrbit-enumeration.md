---
description: "Learn more about: CreateTableColumnIndexGrbit enumeration"
title: CreateTableColumnIndexGrbit enumeration
TOCTitle: CreateTableColumnIndexGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.createtablecolumnindexgrbit(v=EXCHG.10)
ms:contentKeyID: 39516657
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.FixedDDL
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.NoFixedVarColumnsInDerivedTables
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.None
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.TemplateTable
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.TemplateTable
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.NoFixedVarColumnsInDerivedTables
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.FixedDDL
- Microsoft.Isam.Esent.Interop.CreateTableColumnIndexGrbit.None
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# CreateTableColumnIndexGrbit enumeration

Options for JetCreateTableColumnIndex.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration CreateTableColumnIndexGrbit
'Usage
Dim instance As CreateTableColumnIndexGrbit
```

``` csharp
[FlagsAttribute]
public enum CreateTableColumnIndexGrbit
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
<td>FixedDDL</td>
<td>The DDL is fixed.</td>
</tr>
<tr class="odd">
<td></td>
<td>TemplateTable</td>
<td>The DDL is inheritable. Implies FixedDDL.</td>
</tr>
<tr class="even">
<td></td>
<td>NoFixedVarColumnsInDerivedTables</td>
<td>Used in conjunction with TemplateTable.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
