---
description: "Learn more about: JET_prep enumeration"
title: JET_prep enumeration
TOCTitle: JET_prep enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_prep
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_prep(v=EXCHG.10)
ms:contentKeyID: 39510193
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_prep.Replace
- Microsoft.Isam.Esent.Interop.JET_prep.InsertCopy
- Microsoft.Isam.Esent.Interop.JET_prep.Cancel
- Microsoft.Isam.Esent.Interop.JET_prep.Insert
- Microsoft.Isam.Esent.Interop.JET_prep.InsertCopyDeleteOriginal
- Microsoft.Isam.Esent.Interop.JET_prep
- Microsoft.Isam.Esent.Interop.JET_prep.ReplaceNoLock
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_prep.InsertCopyDeleteOriginal
- Microsoft.Isam.Esent.Interop.JET_prep.ReplaceNoLock
- Microsoft.Isam.Esent.Interop.JET_prep
- Microsoft.Isam.Esent.Interop.JET_prep.Cancel
- Microsoft.Isam.Esent.Interop.JET_prep.InsertCopy
- Microsoft.Isam.Esent.Interop.JET_prep.Insert
- Microsoft.Isam.Esent.Interop.JET_prep.Replace
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_prep enumeration

Update types for JetPrepareUpdate.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Enumeration JET_prep
'Usage
Dim instance As JET_prep
```

``` csharp
public enum JET_prep
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
<td>Insert</td>
<td>This flag causes the cursor to prepare for an insert of a new record. All the data is initialized to the default state for the record. If the table has an auto-increment column, then a new value is assigned to this record regardless of whether the update ultimately succeeds, fails or is cancelled.</td>
</tr>
<tr class="even">
<td></td>
<td>Replace</td>
<td>This flag causes the cursor to prepare for a replace of the current record. If the table has a version column, then the version column is set to the next value in its sequence. If this update does not complete, then the version value in the record will be unaffected. An update lock is taken on the record to prevent other sessions from updating this record before this session completes.</td>
</tr>
<tr class="odd">
<td></td>
<td>Cancel</td>
<td>This flag causes JetPrepareUpdate to cancel the update for this cursor.</td>
</tr>
<tr class="even">
<td></td>
<td>ReplaceNoLock</td>
<td>This flag is similar to JET_prepReplace, but no lock is taken to prevent other sessions from updating this record. Instead, this session may receive JET_errWriteConflict when it calls JetUpdate to complete the update.</td>
</tr>
<tr class="odd">
<td></td>
<td>InsertCopy</td>
<td>This flag causes the cursor to prepare for an insert of a copy of the existing record. There must be a current record if this option is used. The initial state of the new record is copied from the current record. Long values that are stored off-record are virtually copied.</td>
</tr>
<tr class="even">
<td></td>
<td>InsertCopyDeleteOriginal</td>
<td>This flag causes the cursor to prepare for an insert of the same record, and a delete or the original record. It is used in cases in which the primary key has changed.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
