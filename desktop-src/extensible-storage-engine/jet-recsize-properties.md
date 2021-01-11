---
description: "Learn more about: JET_RECSIZE properties"
title: JET_RECSIZE properties (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: JET_RECSIZE properties
ms:assetid: Properties.T:Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_recsize_properties(v=EXCHG.10)
ms:contentKeyID: 39513545
ms.date: 07/30/2014
ms.topic: article
---

# JET_RECSIZE properties

Include protected members  
Include inherited members  

The [JET_RECSIZE](./jet-recsize-structure2.md) type exposes the following members.

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
<td><a href="hh557581(v=exchg.10).md">cbData</a></td>
<td>Gets the user data set in the record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh596280(v=exchg.10).md">cbDataCompressed</a></td>
<td>Gets the compressed size of user data in record. This is the same as <a href="hh557581(v=exchg.10).md">cbData</a> if no intrinsic long-values are compressed).</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh557913(v=exchg.10).md">cbLongValueData</a></td>
<td>Gets the user data set in the record, but stored in the long-value tree.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh566144(v=exchg.10).md">cbLongValueDataCompressed</a></td>
<td>Gets the compressed size of user data in the long-value tree. This is the same as <a href="hh557913(v=exchg.10).md">cbLongValueData</a> if no separated long values are compressed.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh558003(v=exchg.10).md">cbLongValueOverhead</a></td>
<td>Gets the overhead of the long-value data.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh565836(v=exchg.10).md">cbOverhead</a></td>
<td>Gets the overhead of the ESENT record structure for this record. This includes the record's key size.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh566154(v=exchg.10).md">cCompressedColumns</a></td>
<td>Gets the total number of columns in the record which are compressed.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh596288(v=exchg.10).md">cLongValues</a></td>
<td>Gets the total number of long values stored in the long-value tree for this record. This does not include intrinsic long values.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh577486(v=exchg.10).md">cMultiValues</a></td>
<td>Gets the accumulation of the total number of values beyond the first for all columns in the record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh578172(v=exchg.10).md">cNonTaggedColumns</a></td>
<td>Gets the total number of fixed and variable columns set in this record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="hh566034(v=exchg.10).md">cTaggedColumns</a></td>
<td>Gets the total number of tagged columns set in this record.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_RECSIZE structure](./jet-recsize-structure2.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
