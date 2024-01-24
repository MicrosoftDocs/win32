---
description: "Learn more about: JET_coltyp enumeration"
title: JET_coltyp enumeration
TOCTitle: JET_coltyp enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_coltyp
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_coltyp(v=EXCHG.10)
ms:contentKeyID: 39511169
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_coltyp.Nil
- Microsoft.Isam.Esent.Interop.JET_coltyp.IEEEDouble
- Microsoft.Isam.Esent.Interop.JET_coltyp.LongBinary
- Microsoft.Isam.Esent.Interop.JET_coltyp.LongText
- Microsoft.Isam.Esent.Interop.JET_coltyp.Text
- Microsoft.Isam.Esent.Interop.JET_coltyp.IEEESingle
- Microsoft.Isam.Esent.Interop.JET_coltyp.DateTime
- Microsoft.Isam.Esent.Interop.JET_coltyp.Binary
- Microsoft.Isam.Esent.Interop.JET_coltyp.UnsignedByte
- Microsoft.Isam.Esent.Interop.JET_coltyp.Currency
- Microsoft.Isam.Esent.Interop.JET_coltyp.Bit
- Microsoft.Isam.Esent.Interop.JET_coltyp.Long
- Microsoft.Isam.Esent.Interop.JET_coltyp
- Microsoft.Isam.Esent.Interop.JET_coltyp.Short
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_coltyp.Binary
- Microsoft.Isam.Esent.Interop.JET_coltyp.Short
- Microsoft.Isam.Esent.Interop.JET_coltyp.Bit
- Microsoft.Isam.Esent.Interop.JET_coltyp.UnsignedByte
- Microsoft.Isam.Esent.Interop.JET_coltyp.IEEEDouble
- Microsoft.Isam.Esent.Interop.JET_coltyp.IEEESingle
- Microsoft.Isam.Esent.Interop.JET_coltyp
- Microsoft.Isam.Esent.Interop.JET_coltyp.Currency
- Microsoft.Isam.Esent.Interop.JET_coltyp.Nil
- Microsoft.Isam.Esent.Interop.JET_coltyp.DateTime
- Microsoft.Isam.Esent.Interop.JET_coltyp.LongBinary
- Microsoft.Isam.Esent.Interop.JET_coltyp.Long
- Microsoft.Isam.Esent.Interop.JET_coltyp.LongText
- Microsoft.Isam.Esent.Interop.JET_coltyp.Text
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_coltyp enumeration

ESENT column types.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Enumeration JET_coltyp
'Usage
Dim instance As JET_coltyp
```

``` csharp
public enum JET_coltyp
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
<td>Nil</td>
<td>Null column type. Invalid for column creation.</td>
</tr>
<tr class="even">
<td></td>
<td>Bit</td>
<td>True, False or NULL.</td>
</tr>
<tr class="odd">
<td></td>
<td>UnsignedByte</td>
<td>1-byte integer, unsigned.</td>
</tr>
<tr class="even">
<td></td>
<td>Short</td>
<td>2-byte integer, signed.</td>
</tr>
<tr class="odd">
<td></td>
<td>Long</td>
<td>4-byte integer, signed.</td>
</tr>
<tr class="even">
<td></td>
<td>Currency</td>
<td>8-byte integer, signed.</td>
</tr>
<tr class="odd">
<td></td>
<td>IEEESingle</td>
<td>4-byte IEEE single-precisions.</td>
</tr>
<tr class="even">
<td></td>
<td>IEEEDouble</td>
<td>8-byte IEEE double-precision.</td>
</tr>
<tr class="odd">
<td></td>
<td>DateTime</td>
<td>Integral date, fractional time.</td>
</tr>
<tr class="even">
<td></td>
<td>Binary</td>
<td>Binary data, up to 255 bytes.</td>
</tr>
<tr class="odd">
<td></td>
<td>Text</td>
<td>Text data, up to 255 bytes.</td>
</tr>
<tr class="even">
<td></td>
<td>LongBinary</td>
<td>Binary data, up to 2GB.</td>
</tr>
<tr class="odd">
<td></td>
<td>LongText</td>
<td>Text data, up to 2GB.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
