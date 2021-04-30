---
description: "Learn more about: JET_SETINFO properties"
title: JET_SETINFO properties
TOCTitle: JET_SETINFO properties
ms:assetid: Properties.T:Microsoft.Isam.Esent.Interop.JET_SETINFO
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_setinfo_properties(v=EXCHG.10)
ms:contentKeyID: 55103917
ms.date: 07/30/2014
ms.topic: article
---

# JET_SETINFO properties

Include protected members  
Include inherited members  

The [JET_SETINFO](./jet-setinfo-class.md) type exposes the following members.

## Properties

<table>
<thead>
<tr class="header">
<th> </th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351064(v=exchg.10).md">ibLongValue</a></td>
<td>Gets or sets offset to the first byte to be set in a column of type <a href="hh577895(v=exchg.10).md">LongBinary</a> or <a href="hh577895(v=exchg.10).md">LongText</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351037(v=exchg.10).md">itagSequence</a></td>
<td>Gets or sets the sequence number of value in a multi-valued column to be set. The array of values is one-based. The first value is sequence 1, not 0 (zero). If the record column has only one value then 1 should be passed as the itagSequence if that value is being replaced. A value of 0 (zero) means to add a new column value instance to the end of the sequence of column values.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_SETINFO class](./jet-setinfo-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
