---
description: "Learn more about: SnapshotEndGrbit enumeration"
title: SnapshotEndGrbit enumeration (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: SnapshotEndGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.Vista.SnapshotEndGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.snapshotendgrbit(v=EXCHG.10)
ms:contentKeyID: 39510894
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.SnapshotEndGrbit
- Microsoft.Isam.Esent.Interop.Vista.SnapshotEndGrbit.AbortSnapshot
- Microsoft.Isam.Esent.Interop.Vista.SnapshotEndGrbit.None
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.SnapshotEndGrbit.AbortSnapshot
- Microsoft.Isam.Esent.Interop.Vista.SnapshotEndGrbit.None
- Microsoft.Isam.Esent.Interop.Vista.SnapshotEndGrbit
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SnapshotEndGrbit enumeration

Options for [JetOSSnapshotEnd(JET_OSSNAPID, SnapshotEndGrbit)](./vistaapi.jetossnapshotend-method.md).

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration SnapshotEndGrbit
'Usage
Dim instance As SnapshotEndGrbit
```

``` csharp
[FlagsAttribute]
public enum SnapshotEndGrbit
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
<td>AbortSnapshot</td>
<td>The snapshot session aborted.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
