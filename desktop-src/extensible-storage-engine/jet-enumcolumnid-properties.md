---
title: JET_ENUMCOLUMNID properties
TOCTitle: JET_ENUMCOLUMNID properties
ms:assetid: Properties.T:Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNID
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_enumcolumnid_properties(v=EXCHG.10)
ms:contentKeyID: 55103627
ms.date: 07/30/2014
ms.topic: article
---

# JET_ENUMCOLUMNID properties

Include protected members  
Include inherited members  

The [JET_ENUMCOLUMNID](dn335139\(v=exchg.10\).md) type exposes the following members.

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
<td><a href="dn335141(v=exchg.10).md">columnid</a></td>
<td>Gets or sets the columnid ID to enumerate.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335092(v=exchg.10).md">ctagSequence</a></td>
<td>Gets or sets the count of column values (by one-based index) to enumerate for the specified column ID. If ctagSequence is 0 (zero) then rgtagSequence is ignored and all column values for the specified column ID will be enumerated.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335093(v=exchg.10).md">rgtagSequence</a></td>
<td>Gets or sets the array of one-based indices into the array of column values for a given column. A single element is an itagSequence which is defined in JET_RETRIEVECOLUMN. An itagSequence of 0 (zero) means &quot;skip&quot;. An itagSequence of 1 means return the first column value of the column, 2 means the second, and so on.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_ENUMCOLUMNID class](dn335139\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

