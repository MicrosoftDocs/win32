---
description: "Learn more about: IdleGrbit enumeration"
title: IdleGrbit enumeration
TOCTitle: IdleGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.IdleGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.idlegrbit(v=EXCHG.10)
ms:contentKeyID: 39514282
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.IdleGrbit
- Microsoft.Isam.Esent.Interop.IdleGrbit.Compact
- Microsoft.Isam.Esent.Interop.IdleGrbit.FlushBuffers
- Microsoft.Isam.Esent.Interop.IdleGrbit.GetStatus
- Microsoft.Isam.Esent.Interop.IdleGrbit.None
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IdleGrbit.Compact
- Microsoft.Isam.Esent.Interop.IdleGrbit.FlushBuffers
- Microsoft.Isam.Esent.Interop.IdleGrbit
- Microsoft.Isam.Esent.Interop.IdleGrbit.None
- Microsoft.Isam.Esent.Interop.IdleGrbit.GetStatus
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IdleGrbit enumeration

Options for [JetIdle(JET_SESID, IdleGrbit)](./api.jetidle-method.md).

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration IdleGrbit
'Usage
Dim instance As IdleGrbit
```

``` csharp
[FlagsAttribute]
public enum IdleGrbit
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
<td>FlushBuffers</td>
<td>Triggers cleanup of the version store.</td>
</tr>
<tr class="odd">
<td></td>
<td>Compact</td>
<td>Reserved for future use. If this flag is specified, the API will return <a href="hh564840(v=exchg.10).md">InvalidGrbit</a>.</td>
</tr>
<tr class="even">
<td></td>
<td>GetStatus</td>
<td>Returns <a href="hh557250(v=exchg.10).md">IdleFull</a> if version store is more than half full.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
