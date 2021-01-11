---
description: "Learn more about: JET_INDEXCREATE members"
title: JET_INDEXCREATE members
TOCTitle: JET_INDEXCREATE members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.JET_INDEXCREATE
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexcreate_members(v=EXCHG.10)
ms:contentKeyID: 55103641
ms.date: 07/30/2014
ms.topic: article
---

# JET_INDEXCREATE members

Include protected members  
Include inherited members  

Contains the information needed to create an index over data in an ESE database. Contains the information needed to create an index over data in an ESE database.

The [JET_INDEXCREATE](./jet-indexcreate-class.md) type exposes the following members.

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
<td><a href="dn335115(v=exchg.10).md">JET_INDEXCREATE</a></td>
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
<td><a href="dn335122(v=exchg.10).md">cbKey</a></td>
<td>Gets or sets the length, in characters, of szKey including the two terminating nulls.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335156(v=exchg.10).md">cbKeyMost</a></td>
<td>Gets or sets the maximum allowable size, in bytes, for keys in the index. The minimum supported maximum key size is JET_cbKeyMostMin (255) which is the legacy maximum key size. The maximum key size is dependent on the database page size <a href="hh596135(v=exchg.10).md">DatabasePageSize</a>. The maximum key size can be retrieved with <a href="dn351156(v=exchg.10).md">KeyMost</a>. This parameter is ignored on Windows XP and Windows Server 2003. Unlike the unmanaged API, <strong>IndexKeyMost()</strong> (JET_bitIndexKeyMost) is not needed, it will be added automatically.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335158(v=exchg.10).md">cbVarSegMac</a></td>
<td>Gets or sets the maximum length, in bytes, of each column to store in the index.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335118(v=exchg.10).md">cConditionalColumn</a></td>
<td>Gets or sets the number of conditional columns.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335157(v=exchg.10).md">err</a></td>
<td>Gets or sets the error code from creating this index.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335119(v=exchg.10).md">grbit</a></td>
<td>Gets or sets index creation options.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335159(v=exchg.10).md">pidxUnicode</a></td>
<td>Gets or sets the optional unicode comparison options.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335120(v=exchg.10).md">pSpaceHints</a></td>
<td>Gets or sets space allocation, maintenance, and usage hints.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335160(v=exchg.10).md">rgconditionalcolumn</a></td>
<td>Gets or sets the optional conditional columns.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335121(v=exchg.10).md">szIndexName</a></td>
<td>Gets or sets the name of the index to create.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335161(v=exchg.10).md">szKey</a></td>
<td>Gets or sets the description of the index key. This is a double null-terminated string of null-delimited tokens. Each token is of the form [direction-specifier][column-name], where direction-specification is either &quot;+&quot; or &quot;-&quot;. for example, a szKey of &quot;+abc\0-def\0+ghi\0&quot; will index over the three columns &quot;abc&quot; (in ascending order), &quot;def&quot; (in descending order), and &quot;ghi&quot; (in ascending order).</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335162(v=exchg.10).md">ulDensity</a></td>
<td>Gets or sets the density of the index.</td>
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
<td><a href="dn335116(v=exchg.10).md">ContentEquals</a></td>
<td>Returns a value indicating whether this instance is equal to another instance.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335153(v=exchg.10).md">DeepClone</a></td>
<td>Returns a deep copy of the object.</td>
</tr>
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
<td><a href="dn335154(v=exchg.10).md">ToString</a></td>
<td>Generate a string representation of the instance. (Overrides <a href="/dotnet/api/system.object.tostring#System_Object_ToString">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_INDEXCREATE class](./jet-indexcreate-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
