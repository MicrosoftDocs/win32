---
description: "Learn more about: JET_COLUMNBASE members"
title: JET_COLUMNBASE members
TOCTitle: JET_COLUMNBASE members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.JET_COLUMNBASE
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_columnbase_members(v=EXCHG.10)
ms:contentKeyID: 55103414
ms.date: 07/30/2014
ms.topic: article
---

# JET_COLUMNBASE members

Include protected members  
Include inherited members  

Describes a column in a table of an ESENT database.

The [JET_COLUMNBASE](./jet-columnbase-class.md) type exposes the following members.

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
<td><a href="dn335065(v=exchg.10).md">cbMax</a></td>
<td>Gets the maximum length of the column. This is only meaningful for columns of type <a href="hh577895(v=exchg.10).md">Text</a>, <a href="hh577895(v=exchg.10).md">LongText</a>, <a href="hh577895(v=exchg.10).md">Binary</a> and <a href="hh577895(v=exchg.10).md">LongBinary</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351019(v=exchg.10).md">coltyp</a></td>
<td>Gets type of the column.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335024(v=exchg.10).md">columnid</a></td>
<td>Gets the columnid of the column.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335066(v=exchg.10).md">cp</a></td>
<td>Gets code page of the column. This is only meaningful for columns of type <a href="hh577895(v=exchg.10).md">Text</a> and <a href="hh577895(v=exchg.10).md">LongText</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351020(v=exchg.10).md">grbit</a></td>
<td>Gets the column options.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335067(v=exchg.10).md">szBaseColumnName</a></td>
<td>Gets the name of the column in the template table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
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
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335062(v=exchg.10).md">Equals(Object)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance. (Overrides <a href="/dotnet/api/system.object.equals#System_Object_Equals_System_Object_">Object.Equals(Object)</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351009(v=exchg.10).md">Equals(JET_COLUMNBASE)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="/dotnet/api/system.object.finalize#System_Object_Finalize">Finalize</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335023(v=exchg.10).md">GetHashCode</a></td>
<td>Returns the hash code for this instance. (Overrides <a href="/dotnet/api/system.object.gethashcode#System_Object_GetHashCode">Object.GetHashCode()</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="/dotnet/api/system.object.gettype#System_Object_GetType">GetType</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="/dotnet/api/system.object.memberwiseclone#System_Object_MemberwiseClone">MemberwiseClone</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335064(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="/dotnet/api/system.string">String</a> that represents the current <a href="dn335045(v=exchg.10).md">JET_COLUMNBASE</a>. (Overrides <a href="/dotnet/api/system.object.tostring#System_Object_ToString">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_COLUMNBASE class](./jet-columnbase-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
