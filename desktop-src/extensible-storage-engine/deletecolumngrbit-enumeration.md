---
title: DeleteColumnGrbit enumeration (Microsoft.Isam.Esent.Interop)
TOCTitle: DeleteColumnGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.DeleteColumnGrbit
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.deletecolumngrbit(v=EXCHG.10)
ms:contentKeyID: 39512792
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.DeleteColumnGrbit
- Microsoft.Isam.Esent.Interop.DeleteColumnGrbit.IgnoreTemplateColumns
- Microsoft.Isam.Esent.Interop.DeleteColumnGrbit.None
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.DeleteColumnGrbit
- Microsoft.Isam.Esent.Interop.DeleteColumnGrbit.None
- Microsoft.Isam.Esent.Interop.DeleteColumnGrbit.IgnoreTemplateColumns
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# DeleteColumnGrbit enumeration

Options for [JetDeleteColumn2(JET_SESID, JET_TABLEID, String, DeleteColumnGrbit)](dn292132\(v=exchg.10\).md).

This enumeration has a [FlagsAttribute](https://msdn.microsoft.com/en-us/library/dk06fkbc) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration DeleteColumnGrbit
'Usage
Dim instance As DeleteColumnGrbit
```

``` csharp
[FlagsAttribute]
public enum DeleteColumnGrbit
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
<td>IgnoreTemplateColumns</td>
<td>The API should only attempt to delete columns in the derived table. If a column of that name exists in the base table it will be ignored.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

