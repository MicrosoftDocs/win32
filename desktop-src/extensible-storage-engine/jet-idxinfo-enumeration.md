---
description: "Learn more about: JET_IdxInfo enumeration"
title: JET_IdxInfo enumeration
TOCTitle: JET_IdxInfo enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_IdxInfo
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_idxinfo(v=EXCHG.10)
ms:contentKeyID: 39512789
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.VarSegMac
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.KeyMost
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.IndexId
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.SysTabCursor
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.OLC
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.Default
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.ResetOLC
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.SpaceAlloc
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.Langid
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.LCID
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.List
- Microsoft.Isam.Esent.Interop.JET_IdxInfo
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.Count
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.LCID
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.IndexId
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.SpaceAlloc
- Microsoft.Isam.Esent.Interop.JET_IdxInfo
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.List
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.VarSegMac
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.KeyMost
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.OLC
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.ResetOLC
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.SysTabCursor
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.Count
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.Default
- Microsoft.Isam.Esent.Interop.JET_IdxInfo.Langid
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_IdxInfo enumeration

Info levels for retrieve index information with JetGetIndexInfo. and JetGetTableIndexInfo.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Enumeration JET_IdxInfo
'Usage
Dim instance As JET_IdxInfo
```

``` csharp
public enum JET_IdxInfo
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
<td>Default</td>
<td>Returns a <a href="dn335123(v=exchg.10).md">JET_INDEXLIST</a> structure with information about the index.</td>
</tr>
<tr class="even">
<td></td>
<td>List</td>
<td>Returns a <a href="dn335123(v=exchg.10).md">JET_INDEXLIST</a> structure with information about the index.</td>
</tr>
<tr class="odd">
<td></td>
<td>SysTabCursor</td>
<td><strong>Obsolete.</strong> SysTabCursor is obsolete.</td>
</tr>
<tr class="even">
<td></td>
<td>OLC</td>
<td><strong>Obsolete.</strong> OLC is obsolete.</td>
</tr>
<tr class="odd">
<td></td>
<td>ResetOLC</td>
<td><strong>Obsolete.</strong> Reset OLC is obsolete.</td>
</tr>
<tr class="even">
<td></td>
<td>SpaceAlloc</td>
<td>Returns an integer with the space usage of the index.</td>
</tr>
<tr class="odd">
<td></td>
<td>LCID</td>
<td>Returns an integer with the LCID of the index.</td>
</tr>
<tr class="even">
<td></td>
<td>Langid</td>
<td><strong>Obsolete.</strong> Langid is obsolete. Use LCID instead.</td>
</tr>
<tr class="odd">
<td></td>
<td>Count</td>
<td>Returns an integer with the count of indexes in the table.</td>
</tr>
<tr class="even">
<td></td>
<td>VarSegMac</td>
<td>Returns a ushort with the value of cbVarSegMac the index was created with.</td>
</tr>
<tr class="odd">
<td></td>
<td>IndexId</td>
<td>Returns a <a href="hh557060(v=exchg.10).md">JET_INDEXID</a> identifying the index.</td>
</tr>
<tr class="even">
<td></td>
<td>KeyMost</td>
<td>Introduced in Windows Vista. Returns a ushort with the value of cbKeyMost the index was created with.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
