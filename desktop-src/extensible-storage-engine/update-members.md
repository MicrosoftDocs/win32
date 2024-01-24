---
description: "Learn more about: Update members"
title: Update members
TOCTitle: Update members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.Update
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.update_members(v=EXCHG.10)
ms:contentKeyID: 55104188
ms.date: 07/30/2014
ms.topic: article
---

# Update members

Include protected members  
Include inherited members  

A class that encapsulates an update on a JET_TABLEID.

The [Update](./update-class.md) type exposes the following members.

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
<td><a href="dn351261(v=exchg.10).md">Update</a></td>
<td>Initializes a new instance of the Update class. This automatically begins an update. The update will be cancelled if not explicitly saved.</td>
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
<td><img src="../images/dn292128.protproperty(exchg.10).gif" title="Protected property" alt="Protected property" /></td>
<td><a href="dn350578(v=exchg.10).md">HasResource</a></td>
<td>Gets a value indicating whether the underlying resource is currently allocated. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
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
<td><a href="dn351266(v=exchg.10).md">Cancel</a></td>
<td>Cancel the update.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350541(v=exchg.10).md">CheckObjectIsNotDisposed</a></td>
<td>Throw an exception if this object has been disposed. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350553(v=exchg.10).md">Dispose()</a></td>
<td>Dispose of this object, releasing the underlying Esent resource. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350543(v=exchg.10).md">Dispose(Boolean)</a></td>
<td>Called by Dispose and the finalizer. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="/dotnet/api/system.object.equals#System_Object_Equals_System_Object_">Equals</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350552(v=exchg.10).md">Finalize</a></td>
<td>Finalizes an instance of the EsentResource class. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
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
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn351268(v=exchg.10).md">ReleaseResource</a></td>
<td>Called when the transaction is being disposed while active. This should rollback the transaction. (Overrides <a href="dn350545(v=exchg.10).md">EsentResource.ReleaseResource()</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350576(v=exchg.10).md">ResourceWasAllocated</a></td>
<td>Called by a subclass when a resource is allocated. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350577(v=exchg.10).md">ResourceWasReleased</a></td>
<td>Called by a subclass when a resource is freed. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351270(v=exchg.10).md">Save()</a></td>
<td>Update the tableid.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351199(v=exchg.10).md">Save([], Int32, Int32)</a></td>
<td>Update the tableid.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351272(v=exchg.10).md">SaveAndGotoBookmark</a></td>
<td>Update the tableid and position the tableid on the record that was modified. This can be useful when inserting a record because by default the tableid remains in its old location.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351192(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="/dotnet/api/system.string">String</a> that represents the current <a href="dn351191(v=exchg.10).md">Update</a>. (Overrides <a href="/dotnet/api/system.object.tostring#System_Object_ToString">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[Update class](./update-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
