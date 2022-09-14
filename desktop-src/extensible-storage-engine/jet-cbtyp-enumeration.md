---
description: "Learn more about: JET_cbtyp enumeration"
title: JET_cbtyp enumeration
TOCTitle: JET_cbtyp enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_cbtyp
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_cbtyp(v=EXCHG.10)
ms:contentKeyID: 39511758
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_cbtyp.BeforeDelete
- Microsoft.Isam.Esent.Interop.JET_cbtyp.Finalize
- Microsoft.Isam.Esent.Interop.JET_cbtyp.OnlineDefragCompleted
- Microsoft.Isam.Esent.Interop.JET_cbtyp.UserDefinedDefaultValue
- Microsoft.Isam.Esent.Interop.JET_cbtyp
- Microsoft.Isam.Esent.Interop.JET_cbtyp.AfterDelete
- Microsoft.Isam.Esent.Interop.JET_cbtyp.FreeCursorLS
- Microsoft.Isam.Esent.Interop.JET_cbtyp.AfterReplace
- Microsoft.Isam.Esent.Interop.JET_cbtyp.FreeTableLS
- Microsoft.Isam.Esent.Interop.JET_cbtyp.Null
- Microsoft.Isam.Esent.Interop.JET_cbtyp.BeforeReplace
- Microsoft.Isam.Esent.Interop.JET_cbtyp.BeforeInsert
- Microsoft.Isam.Esent.Interop.JET_cbtyp.AfterInsert
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_cbtyp.BeforeReplace
- Microsoft.Isam.Esent.Interop.JET_cbtyp.FreeCursorLS
- Microsoft.Isam.Esent.Interop.JET_cbtyp.FreeTableLS
- Microsoft.Isam.Esent.Interop.JET_cbtyp.BeforeDelete
- Microsoft.Isam.Esent.Interop.JET_cbtyp.Null
- Microsoft.Isam.Esent.Interop.JET_cbtyp.AfterReplace
- Microsoft.Isam.Esent.Interop.JET_cbtyp
- Microsoft.Isam.Esent.Interop.JET_cbtyp.AfterDelete
- Microsoft.Isam.Esent.Interop.JET_cbtyp.OnlineDefragCompleted
- Microsoft.Isam.Esent.Interop.JET_cbtyp.AfterInsert
- Microsoft.Isam.Esent.Interop.JET_cbtyp.BeforeInsert
- Microsoft.Isam.Esent.Interop.JET_cbtyp.Finalize
- Microsoft.Isam.Esent.Interop.JET_cbtyp.UserDefinedDefaultValue
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_cbtyp enumeration

Type of progress being reported.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration JET_cbtyp
'Usage
Dim instance As JET_cbtyp
```

``` csharp
[FlagsAttribute]
public enum JET_cbtyp
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
<td>Null</td>
<td>This callback is reserved and always considered invalid.</td>
</tr>
<tr class="even">
<td></td>
<td>Finalize</td>
<td>A finalizable column has gone to zero.</td>
</tr>
<tr class="odd">
<td></td>
<td>BeforeInsert</td>
<td>This callback will occur just before a new record is inserted into a table by a call to JetUpdate.</td>
</tr>
<tr class="even">
<td></td>
<td>AfterInsert</td>
<td>This callback will occur just after a new record has been inserted into a table by a call to JetUpdate but before JetUpdate returns.</td>
</tr>
<tr class="odd">
<td></td>
<td>BeforeReplace</td>
<td>This callback will occur just prior to an existing record in a table being changed by a call to JetUpdate.</td>
</tr>
<tr class="even">
<td></td>
<td>AfterReplace</td>
<td>This callback will occur just after an existing record in a table has been changed by a call to JetUpdate but prior to JetUpdate returning.</td>
</tr>
<tr class="odd">
<td></td>
<td>BeforeDelete</td>
<td>This callback will occur just before an existing record in a table is deleted by a call to JetDelete.</td>
</tr>
<tr class="even">
<td></td>
<td>AfterDelete</td>
<td>This callback will occur just after an existing record in a table is deleted by a call to JetDelete.</td>
</tr>
<tr class="odd">
<td></td>
<td>UserDefinedDefaultValue</td>
<td>This callback will occur when the engine needs to retrieve the user defined default value of a column from the application. This callback is essentially a limited implementation of JetRetrieveColumn that is evaluated by the application. A maximum of one column value can be returned for a user defined default value.</td>
</tr>
<tr class="even">
<td></td>
<td>OnlineDefragCompleted</td>
<td>This callback will occur when the online defragmentation of a database as initiated by JetDefragment has stopped due to either the process being completed or the time limit being reached.</td>
</tr>
<tr class="odd">
<td></td>
<td>FreeCursorLS</td>
<td>This callback will occur when the application needs to clean up the context handle for the Local Storage associated with a cursor that is being released by the database engine. For more information, see JetSetLS. The delegate for this callback reason is configured by means of JetSetSystemParameter with JET_paramRuntimeCallback.</td>
</tr>
<tr class="even">
<td></td>
<td>FreeTableLS</td>
<td>This callback will occur as the result of the need for the application to cleanup the context handle for the Local Storage associated with a table that is being released by the database engine. For more information, see JetSetLS. The delegate for this callback reason is configured by means of JetSetSystemParameter with JET_paramRuntimeCallback.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
