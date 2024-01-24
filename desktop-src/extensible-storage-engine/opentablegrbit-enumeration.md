---
description: "Learn more about: OpenTableGrbit enumeration"
title: OpenTableGrbit enumeration
TOCTitle: OpenTableGrbit enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.OpenTableGrbit
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.opentablegrbit(v=EXCHG.10)
ms:contentKeyID: 39510721
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.NoCache
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.DenyWrite
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.DenyRead
- Microsoft.Isam.Esent.Interop.OpenTableGrbit
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.Updatable
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.Preread
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass9
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass15
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass6
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass14
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass3
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass8
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass7
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.Sequential
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass5
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass2
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.ReadOnly
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass4
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.None
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass10
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass13
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass12
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass1
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.PermitDDL
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass11
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass1
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass11
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass14
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.Sequential
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass2
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass5
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass8
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.DenyRead
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.DenyWrite
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.PermitDDL
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass10
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass12
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass3
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.NoCache
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass9
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.Updatable
- Microsoft.Isam.Esent.Interop.OpenTableGrbit
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.None
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass4
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass7
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.Preread
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.ReadOnly
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass13
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass15
- Microsoft.Isam.Esent.Interop.OpenTableGrbit.TableClass6
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# OpenTableGrbit enumeration

Options for JetOpenTable.

This enumeration has a [FlagsAttribute](/dotnet/api/system.flagsattribute) attribute that allows a bitwise combination of its member values.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<FlagsAttribute> _
Public Enumeration OpenTableGrbit
'Usage
Dim instance As OpenTableGrbit
```

``` csharp
[FlagsAttribute]
public enum OpenTableGrbit
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
<td>DenyWrite</td>
<td>This table cannot be opened for write access by another session.</td>
</tr>
<tr class="odd">
<td></td>
<td>DenyRead</td>
<td>This table cannot be opened for read access by another session.</td>
</tr>
<tr class="even">
<td></td>
<td>ReadOnly</td>
<td>Request read-only access to the table.</td>
</tr>
<tr class="odd">
<td></td>
<td>Updatable</td>
<td>Request write access to the table.</td>
</tr>
<tr class="even">
<td></td>
<td>PermitDDL</td>
<td>Allow DDL modifications to a table flagged as FixedDDL. This option must be used with DenyRead.</td>
</tr>
<tr class="odd">
<td></td>
<td>NoCache</td>
<td>Do not cache pages for this table.</td>
</tr>
<tr class="even">
<td></td>
<td>Preread</td>
<td>Provides a hint that the table is probably not in the buffer cache, and that pre-reading may be beneficial to performance.</td>
</tr>
<tr class="odd">
<td></td>
<td>Sequential</td>
<td>Assume a sequential access pattern and prefetch database pages.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass1</td>
<td>Table belongs to stats class 1.</td>
</tr>
<tr class="odd">
<td></td>
<td>TableClass2</td>
<td>Table belongs to stats class 2.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass3</td>
<td>Table belongs to stats class 3.</td>
</tr>
<tr class="odd">
<td></td>
<td>TableClass4</td>
<td>Table belongs to stats class 4.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass5</td>
<td>Table belongs to stats class 5.</td>
</tr>
<tr class="odd">
<td></td>
<td>TableClass6</td>
<td>Table belongs to stats class 6.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass7</td>
<td>Table belongs to stats class 7.</td>
</tr>
<tr class="odd">
<td></td>
<td>TableClass8</td>
<td>Table belongs to stats class 8.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass9</td>
<td>Table belongs to stats class 9.</td>
</tr>
<tr class="odd">
<td></td>
<td>TableClass10</td>
<td>Table belongs to stats class 10.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass11</td>
<td>Table belongs to stats class 11.</td>
</tr>
<tr class="odd">
<td></td>
<td>TableClass12</td>
<td>Table belongs to stats class 12.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass13</td>
<td>Table belongs to stats class 13.</td>
</tr>
<tr class="odd">
<td></td>
<td>TableClass14</td>
<td>Table belongs to stats class 14.</td>
</tr>
<tr class="even">
<td></td>
<td>TableClass15</td>
<td>Table belongs to stats class 15.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
