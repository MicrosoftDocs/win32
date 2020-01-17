---
title: SnapshotPrepareGrbit enumeration
TOCTitle: SnapshotPrepareGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.snapshotpreparegrbit(v=EXCHG.10)
ms:contentKeyID: 39515688
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit.CopySnapshot
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit.IncrementalSnapshot
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit.None
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit.CopySnapshot
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit.IncrementalSnapshot
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit.None
- Microsoft.Isam.Esent.Interop.SnapshotPrepareGrbit
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SnapshotPrepareGrbit enumeration

Options for [JetOSSnapshotPrepare(JET_OSSNAPID, SnapshotPrepareGrbit)](dn292235\(v=exchg.10\).md).

This enumeration has a [FlagsAttribute](https://docs.microsoft.com/dotnet/api/system.flagsattribute?redirectedfrom=MSDN) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration SnapshotPrepareGrbit
'Usage
Dim instance As SnapshotPrepareGrbit
```

``` csharp
[FlagsAttribute]
public enum SnapshotPrepareGrbit
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
<td>IncrementalSnapshot</td>
<td>Only logfiles will be taken.</td>
</tr>
<tr class="odd">
<td></td>
<td>CopySnapshot</td>
<td>A copy snapshot (normal or incremental) with no log truncation.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

