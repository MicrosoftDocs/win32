---
description: "Learn more about: SpaceHintsGrbit enumeration"
title: SpaceHintsGrbit enumeration
TOCTitle: SpaceHintsGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.SpaceHintsGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.spacehintsgrbit(v=EXCHG.10)
ms:contentKeyID: 39516304
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.CreateHintHotpointSequential
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.CreateHintAppendSequential
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.DeleteHintTableSequential
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.None
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintReserve2
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintReserve1
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintTableScanForward
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintTableScanBackward
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintReserve3
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.SpaceHintUtilizeParentSpace
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintReserve3
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.CreateHintHotpointSequential
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.CreateHintAppendSequential
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintTableScanBackward
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.SpaceHintUtilizeParentSpace
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintReserve2
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.DeleteHintTableSequential
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintTableScanForward
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.None
- Microsoft.Isam.Esent.Interop.SpaceHintsGrbit.RetrieveHintReserve1
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SpaceHintsGrbit enumeration

Options for [JET_SPACEHINTS](./jet-spacehints-class.md).

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration SpaceHintsGrbit
'Usage
Dim instance As SpaceHintsGrbit
```

``` csharp
[FlagsAttribute]
public enum SpaceHintsGrbit
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
<td>SpaceHintUtilizeParentSpace</td>
<td>This changes the internal allocation policy to get space hierarchically from a B-Tree's immediate parent.</td>
</tr>
<tr class="odd">
<td></td>
<td>CreateHintAppendSequential</td>
<td>This bit will enable Append split behavior to grow according to the growth dynamics of the table (set by cbMinExtent, ulGrowth, cbMaxExtent).</td>
</tr>
<tr class="even">
<td></td>
<td>CreateHintHotpointSequential</td>
<td>This bit will enable Hotpoint split behavior to grow according to the growth dynamics of the table (set by cbMinExtent, ulGrowth, cbMaxExtent).</td>
</tr>
<tr class="odd">
<td></td>
<td>RetrieveHintReserve1</td>
<td>Reserved and ignored.</td>
</tr>
<tr class="even">
<td></td>
<td>RetrieveHintTableScanForward</td>
<td>By setting this the client indicates that forward sequential scan is the predominant usage pattern of this table.</td>
</tr>
<tr class="odd">
<td></td>
<td>RetrieveHintTableScanBackward</td>
<td>By setting this the client indicates that backwards sequential scan is the predominant usage pattern of this table.</td>
</tr>
<tr class="even">
<td></td>
<td>RetrieveHintReserve2</td>
<td>Reserved and ignored.</td>
</tr>
<tr class="odd">
<td></td>
<td>RetrieveHintReserve3</td>
<td>Reserved and ignored.</td>
</tr>
<tr class="even">
<td></td>
<td>DeleteHintTableSequential</td>
<td>The application expects this table to be cleaned up in-order sequentially (from lowest key to highest key).</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
