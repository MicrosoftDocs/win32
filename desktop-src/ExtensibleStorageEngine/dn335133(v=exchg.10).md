---
title: JET_ENUMCOLUMN members (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_ENUMCOLUMN members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMN
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_enumcolumn_members(v=EXCHG.10)
ms:contentKeyID: 55103614
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
---

# JET\_ENUMCOLUMN members

Include protected members  
Include inherited members  

Enumerates the column values of a record using the JetEnumerateColumns function. JetEnumerateColumns returns an array of JET\_ENUMCOLUMNVALUE structures. The array is returned in memory that was allocated using the callback that was supplied to that function.

The [JET\_ENUMCOLUMN](dn335081\(v=exchg.10\).md) type exposes the following members.

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
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335131(v=exchg.10).md">JET_ENUMCOLUMN</a></td>
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
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335137(v=exchg.10).md">cbData</a></td>
<td>Gets the size of the value that was enumerated for the column. This member is only used if <a href="dn335086(v=exchg.10).md">err</a> is equal to <a href="hh557250(v=exchg.10).md">ColumnSingleValue</a>.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335085(v=exchg.10).md">cEnumColumnValue</a></td>
<td>Gets the number of column values enumerated for the column. This member is only used if <a href="dn335086(v=exchg.10).md">err</a> is not <a href="hh557250(v=exchg.10).md">ColumnSingleValue</a>.</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335135(v=exchg.10).md">columnid</a></td>
<td>Gets the columnid ID that was enumerated.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335086(v=exchg.10).md">err</a></td>
<td>Gets the column status code that results from the enumeration.</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335087(v=exchg.10).md">pvData</a></td>
<td>Gets the the value that was enumerated for the column. This member is only used if <a href="dn335086(v=exchg.10).md">err</a> is equal to <a href="hh557250(v=exchg.10).md">ColumnSingleValue</a>. This points to memory allocated with the <a href="hh566077(v=exchg.10).md">JET_PFNREALLOC</a> allocator callback passed to <a href="dn292148(v=exchg.10).md">JetEnumerateColumns(JET_SESID, JET_TABLEID, Int32, [], Int32, [], JET_PFNREALLOC, IntPtr, Int32, EnumerateColumnsGrbit)</a>. Remember to release the memory when finished.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292128.pubproperty(EXCHG.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335089(v=exchg.10).md">rgEnumColumnValue</a></td>
<td>Gets the enumerated column values for the column. This member is only used if <a href="dn335086(v=exchg.10).md">err</a> is not <a href="hh557250(v=exchg.10).md">ColumnSingleValue</a>.</td>
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
<td><a href="http://msdn2.microsoft.com/en-us/library/bsc2ak47">Equals</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/4k87zsw7">Finalize</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/zdee4b3y">GetHashCode</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/dfwy45w9">GetType</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/57ctke0a">MemberwiseClone</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn335132(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="http://msdn2.microsoft.com/en-us/library/s1wwdcbf">String</a> that represents the current <a href="dn335081(v=exchg.10).md">JET_ENUMCOLUMN</a>. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/7bxwbwt2">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET\_ENUMCOLUMN class](dn335081\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

