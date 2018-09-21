---
title: JET_InstanceMiscInfo enumeration (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: JET_InstanceMiscInfo enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.Vista.JET_InstanceMiscInfo
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_instancemiscinfo(v=EXCHG.10)
ms:contentKeyID: 39516547
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_InstanceMiscInfo
- Microsoft.Isam.Esent.Interop.Vista.JET_InstanceMiscInfo.LogSignature
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_InstanceMiscInfo.LogSignature
- Microsoft.Isam.Esent.Interop.Vista.JET_InstanceMiscInfo
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_InstanceMiscInfo enumeration

Information levels for [JetGetInstanceMiscInfo(JET\_INSTANCE, JET\_SIGNATURE, JET\_InstanceMiscInfo)](dn351258\(v=exchg.10\).md).

This enumeration has a [FlagsAttribute](http://msdn2.microsoft.com/en-us/library/dk06fkbc) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration JET_InstanceMiscInfo
'Usage
Dim instance As JET_InstanceMiscInfo
```

``` csharp
[FlagsAttribute]
public enum JET_InstanceMiscInfo
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
<td>LogSignature</td>
<td>Get the signature of the transaction log associated with this sequence.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

