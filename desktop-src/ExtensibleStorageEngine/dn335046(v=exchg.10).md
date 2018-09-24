---
title: JET_COLUMNBASE members (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_COLUMNBASE members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.JET_COLUMNBASE
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_columnbase_members(v=EXCHG.10)
ms:contentKeyID: 55103414
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
---

# JET\_COLUMNBASE members

Include protected members  
Include inherited members  

Describes a column in a table of an ESENT database.

The [JET\_COLUMNBASE](dn335045\(v=exchg.10\).md) type exposes the following members.

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
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335065(v=exchg.10).md">cbMax</a></td>
<td>Gets the maximum length of the column. This is only meaningful for columns of type <a href="hh577895(v=exchg.10).md">Text</a>, <a href="hh577895(v=exchg.10).md">LongText</a>, <a href="hh577895(v=exchg.10).md">Binary</a> and <a href="hh577895(v=exchg.10).md">LongBinary</a>.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351019(v=exchg.10).md">coltyp</a></td>
<td>Gets type of the column.</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335024(v=exchg.10).md">columnid</a></td>
<td>Gets the columnid of the column.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335066(v=exchg.10).md">cp</a></td>
<td>Gets code page of the column. This is only meaningful for columns of type <a href="hh577895(v=exchg.10).md">Text</a> and <a href="hh577895(v=exchg.10).md">LongText</a>.</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351020(v=exchg.10).md">grbit</a></td>
<td>Gets the column options.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335067(v=exchg.10).md">szBaseColumnName</a></td>
<td>Gets the name of the column in the template table.</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335026(v=exchg.10).md">szBaseTableName</a></td>
<td>Gets the table from which the current table inherits its DDL.</td>
</tr>
</tbody>
</table>


Top

## Methods

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
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335062(v=exchg.10).md">Equals(Object)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/bsc2ak47">Object.Equals(Object)</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351009(v=exchg.10).md">Equals(JET_COLUMNBASE)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance.</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/4k87zsw7">Finalize</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335023(v=exchg.10).md">GetHashCode</a></td>
<td>Returns the hash code for this instance. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/zdee4b3y">Object.GetHashCode()</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/dfwy45w9">GetType</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/57ctke0a">MemberwiseClone</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335064(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="http://msdn2.microsoft.com/en-us/library/s1wwdcbf">String</a> that represents the current <a href="dn335045(v=exchg.10).md">JET_COLUMNBASE</a>. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/7bxwbwt2">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET\_COLUMNBASE class](dn335045\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

