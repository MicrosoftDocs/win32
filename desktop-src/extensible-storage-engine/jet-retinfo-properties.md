---
description: "Learn more about: JET_RETINFO properties"
title: JET_RETINFO properties
TOCTitle: JET_RETINFO properties
ms:assetid: Properties.T:Microsoft.Isam.Esent.Interop.JET_RETINFO
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_retinfo_properties(v=EXCHG.10)
ms:contentKeyID: 55103867
ms.date: 07/30/2014
ms.topic: article
---

# JET_RETINFO properties

Include protected members  
Include inherited members  

The [JET_RETINFO](./jet-retinfo-class.md) type exposes the following members.

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
<td><a href="dn335221(v=exchg.10).md">columnidNextTagged</a></td>
<td>Gets the columnid of the retrieved tagged, multi-valued or sparse, column when all tagged columns are retrieved by passing 0 as the columnid to JetRetrieveColumn.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335220(v=exchg.10).md">ibLongValue</a></td>
<td>Gets or sets the offset to the first byte to be retrieved from a column of type <a href="hh577895(v=exchg.10).md">LongBinary</a>, or <a href="hh577895(v=exchg.10).md">LongText</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351035(v=exchg.10).md">itagSequence</a></td>
<td>Gets or sets the sequence number of value in a multi-valued column. The array of values is one-based. The first value is sequence 1, not 0. If the record column has only one value then 1 should be passed as the itagSequence.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_RETINFO class](./jet-retinfo-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
