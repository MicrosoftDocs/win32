---
title: JET_ENUMCOLUMNVALUE members (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_ENUMCOLUMNVALUE members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNVALUE
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_enumcolumnvalue_members(v=EXCHG.10)
ms:contentKeyID: 55103510
ms.date: 07/30/2014
ms.topic: article
---

# JET_ENUMCOLUMNVALUE members

Include protected members  
Include inherited members  

Enumerates the column values of a record using the JetEnumerateColumns function. [JetEnumerateColumns(JET_SESID, JET_TABLEID, Int32, \[\], Int32, \[\], JET_PFNREALLOC, IntPtr, Int32, EnumerateColumnsGrbit)](dn292148\(v=exchg.10\).md) returns an array of JET_ENUMCOLUMNVALUE structures. The array is returned in memory that was allocated using the callback that was supplied to that function.

The [JET_ENUMCOLUMNVALUE](dn335142\(v=exchg.10\).md) type exposes the following members.

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
<td><a href="dn335095(v=exchg.10).md">JET_ENUMCOLUMNVALUE</a></td>
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
<td><a href="dn335097(v=exchg.10).md">cbData</a></td>
<td>Gets the size of the column value for the column.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335144(v=exchg.10).md">err</a></td>
<td>Gets the column status code resulting from the enumeration of the column value.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335102(v=exchg.10).md">itagSequence</a></td>
<td>Gets the column value (by one-based index) that was enumerated.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335149(v=exchg.10).md">pvData</a></td>
<td>Gets the value that was enumerated for the column.</td>
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
<td><a href="https://msdn.microsoft.com/en-us/library/bsc2ak47">Equals</a></td>
<td>(Inherited from <a href="https://msdn.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="https://msdn.microsoft.com/en-us/library/4k87zsw7">Finalize</a></td>
<td>(Inherited from <a href="https://msdn.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="https://msdn.microsoft.com/en-us/library/zdee4b3y">GetHashCode</a></td>
<td>(Inherited from <a href="https://msdn.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="https://msdn.microsoft.com/en-us/library/dfwy45w9">GetType</a></td>
<td>(Inherited from <a href="https://msdn.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="https://msdn.microsoft.com/en-us/library/57ctke0a">MemberwiseClone</a></td>
<td>(Inherited from <a href="https://msdn.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335096(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="https://msdn.microsoft.com/en-us/library/s1wwdcbf">String</a> that represents the current <a href="dn335142(v=exchg.10).md">JET_ENUMCOLUMNVALUE</a>. (Overrides <a href="https://msdn.microsoft.com/en-us/library/7bxwbwt2">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_ENUMCOLUMNVALUE class](dn335142\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

