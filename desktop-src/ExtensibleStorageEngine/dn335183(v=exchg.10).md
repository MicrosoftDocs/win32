---
title: JET_INSTANCE_INFO members (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_INSTANCE_INFO members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_instance_info_members(v=EXCHG.10)
ms:contentKeyID: 55103693
ms.date: 07/30/2014
ms.topic: article
---

# JET\_INSTANCE\_INFO members

Include protected members  
Include inherited members  

Receives information about running database instances when used with the JetGetInstanceInfo and JetOSSnapshotFreeze functions.

The [JET\_INSTANCE\_INFO](dn335182\(v=exchg.10\).md) type exposes the following members.

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
<td><a href="dn335189(v=exchg.10).md">cDatabases</a></td>
<td>Gets the number of databases that are attached to the database instance.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335190(v=exchg.10).md">hInstanceId</a></td>
<td>Gets the JET_INSTANCE of the given instance.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335193(v=exchg.10).md">szDatabaseFileName</a></td>
<td>Gets a collection of strings, each holding the file name of a database that is attached to the database instance. The array has cDatabases elements.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335194(v=exchg.10).md">szInstanceName</a></td>
<td>Gets the name of the database instance. This value can be null if the instance does not have a name.</td>
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
<td><a href="dn335184(v=exchg.10).md">Equals(Object)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/bsc2ak47">Object.Equals(Object)</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335187(v=exchg.10).md">Equals(JET_INSTANCE_INFO)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/4k87zsw7">Finalize</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335191(v=exchg.10).md">GetHashCode</a></td>
<td>Returns the hash code for this instance. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/zdee4b3y">Object.GetHashCode()</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/dfwy45w9">GetType</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/57ctke0a">MemberwiseClone</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335192(v=exchg.10).md">ToString</a></td>
<td>Generate a string representation of the instance. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/7bxwbwt2">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET\_INSTANCE\_INFO class](dn335182\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

