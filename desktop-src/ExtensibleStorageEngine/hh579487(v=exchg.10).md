---
title: LsGrbit enumeration (Microsoft.Isam.Esent.Interop)
TOCTitle: LsGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.LsGrbit
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.lsgrbit(v=EXCHG.10)
ms:contentKeyID: 39514518
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.LsGrbit
- Microsoft.Isam.Esent.Interop.LsGrbit.Cursor
- Microsoft.Isam.Esent.Interop.LsGrbit.None
- Microsoft.Isam.Esent.Interop.LsGrbit.Reset
- Microsoft.Isam.Esent.Interop.LsGrbit.Table
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.LsGrbit
- Microsoft.Isam.Esent.Interop.LsGrbit.Reset
- Microsoft.Isam.Esent.Interop.LsGrbit.None
- Microsoft.Isam.Esent.Interop.LsGrbit.Table
- Microsoft.Isam.Esent.Interop.LsGrbit.Cursor
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# LsGrbit enumeration

Options for [JetSetLS(JET\_SESID, JET\_TABLEID, JET\_LS, LsGrbit)](dn334015\(v=exchg.10\).md) and [JetGetLS(JET\_SESID, JET\_TABLEID, JET\_LS, LsGrbit)](dn292177\(v=exchg.10\).md).

This enumeration has a [FlagsAttribute](http://msdn2.microsoft.com/en-us/library/dk06fkbc) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration LsGrbit
'Usage
Dim instance As LsGrbit
```

``` csharp
[FlagsAttribute]
public enum LsGrbit
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
<td>Reset</td>
<td>The context handle for the chosen object should be reset to JET_LSNil.</td>
</tr>
<tr class="odd">
<td></td>
<td>Cursor</td>
<td>Specifies the context handle should be associated with the given cursor.</td>
</tr>
<tr class="even">
<td></td>
<td>Table</td>
<td>Specifies that the context handle should be associated with the table associated with the given cursor. It is illegal to use this option with Cursor.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

