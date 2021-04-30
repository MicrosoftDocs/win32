---
description: "Learn more about: IndexKeyGrbit enumeration"
title: IndexKeyGrbit enumeration
TOCTitle: IndexKeyGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.IndexKeyGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.indexkeygrbit(v=EXCHG.10)
ms:contentKeyID: 39514044
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.IndexKeyGrbit
- Microsoft.Isam.Esent.Interop.IndexKeyGrbit.Ascending
- Microsoft.Isam.Esent.Interop.IndexKeyGrbit.Descending
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IndexKeyGrbit
- Microsoft.Isam.Esent.Interop.IndexKeyGrbit.Descending
- Microsoft.Isam.Esent.Interop.IndexKeyGrbit.Ascending
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IndexKeyGrbit enumeration

Key definition grbits. Used when retrieving information about an index.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration IndexKeyGrbit
'Usage
Dim instance As IndexKeyGrbit
```

``` csharp
[FlagsAttribute]
public enum IndexKeyGrbit
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
<td>Ascending</td>
<td>Key segment is ascending.</td>
</tr>
<tr class="even">
<td></td>
<td>Descending</td>
<td>Key segment is descending.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
