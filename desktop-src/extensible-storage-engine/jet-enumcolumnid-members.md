---
description: "Learn more about: JET_ENUMCOLUMNID members"
title: JET_ENUMCOLUMNID members
TOCTitle: JET_ENUMCOLUMNID members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNID
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_enumcolumnid_members(v=EXCHG.10)
ms:contentKeyID: 55103504
ms.date: 07/30/2014
ms.topic: article
---

# JET_ENUMCOLUMNID members

Include protected members  
Include inherited members  

Enumerates a specific set of columns and, optionally, a specific set of multiple values for those columns when the JetEnumerateColumns function is used. JetEnumerateColumns optionally takes an array of JET_ENUMCOLUMNID structures.

The [JET_ENUMCOLUMNID](./jet-enumcolumnid-class.md) type exposes the following members.

## Constructors

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
<td><a href="dn335140(v=exchg.10).md">JET_ENUMCOLUMNID</a></td>
<td></td>
</tr>
</tbody>
</table>


Top

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
<td><a href="/dotnet/api/system.object.equals#System_Object_Equals_System_Object_">Equals</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="/dotnet/api/system.object.finalize#System_Object_Finalize">Finalize</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="/dotnet/api/system.object.gethashcode#System_Object_GetHashCode">GetHashCode</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="/dotnet/api/system.object.gettype#System_Object_GetType">GetType</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="/dotnet/api/system.object.memberwiseclone#System_Object_MemberwiseClone">MemberwiseClone</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335091(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="/dotnet/api/system.string">String</a> that represents the current <a href="dn335139(v=exchg.10).md">JET_ENUMCOLUMNID</a>. (Overrides <a href="/dotnet/api/system.object.tostring#System_Object_ToString">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_ENUMCOLUMNID class](./jet-enumcolumnid-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
