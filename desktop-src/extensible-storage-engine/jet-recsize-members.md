---
description: "Learn more about: JET_RECSIZE members"
title: JET_RECSIZE members (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: JET_RECSIZE members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.Vista.JET_RECSIZE
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_recsize_members(v=EXCHG.10)
ms:contentKeyID: 39510137
ms.date: 07/30/2014
ms.topic: article
---

# JET_RECSIZE members

Include protected members  
Include inherited members  

Used by [JetGetRecordSize(JET_SESID, JET_TABLEID, JET_RECSIZE, GetRecordSizeGrbit)](./vistaapi.jetgetrecordsize-method.md) to return information about a record's usage requirements in user data space, number of set columns, number of values, and ESENT record structure overhead space.

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
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="hh538879(v=exchg.10).md">Add</a></td>
<td>Add the sizes in two JET_RECSIZE structures.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="hh558506(v=exchg.10).md">Equals(Object)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance. (Overrides <a href="/dotnet/api/system.valuetype.equals#System_ValueType_Equals_System_Object_">ValueType.Equals(Object)</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="hh577992(v=exchg.10).md">Equals(JET_RECSIZE)</a></td>
<td>Returns a value indicating whether this instance is equal to another instance.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="/dotnet/api/system.object.finalize#System_Object_Finalize">Finalize</a></td>
<td>(Inherited from <a href="/dotnet/api/system.object">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="hh557078(v=exchg.10).md">GetHashCode</a></td>
<td>Returns the hash code for this instance. (Overrides <a href="/dotnet/api/system.valuetype.gethashcode#System_ValueType_GetHashCode">ValueType.GetHashCode()</a>.)</td>
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
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="hh579561(v=exchg.10).md">Subtract</a></td>
<td>Calculate the difference in sizes between two JET_RECSIZE structures.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="/dotnet/api/system.valuetype.tostring#System_ValueType_ToString">ToString</a></td>
<td>(Inherited from <a href="/dotnet/api/system.valuetype">ValueType</a>.)</td>
</tr>
</tbody>
</table>


Top

## Operators

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
<td><img src="../images/dn350944.puboperator(exchg.10).gif" title="Public operator" alt="Public operator" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="hh578675(v=exchg.10).md">Addition</a></td>
<td>Add the sizes in two JET_RECSIZE structures.</td>
</tr>
<tr class="even">
<td><img src="../images/dn350944.puboperator(exchg.10).gif" title="Public operator" alt="Public operator" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="hh596362(v=exchg.10).md">Equality</a></td>
<td>Determines whether two specified instances of JET_RECSIZE are equal.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn350944.puboperator(exchg.10).gif" title="Public operator" alt="Public operator" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="hh578809(v=exchg.10).md">Inequality</a></td>
<td>Determines whether two specified instances of JET_RECSIZE are not equal.</td>
</tr>
<tr class="even">
<td><img src="../images/dn350944.puboperator(exchg.10).gif" title="Public operator" alt="Public operator" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="hh596696(v=exchg.10).md">Subtraction</a></td>
<td>Calculate the difference in sizes between two JET_RECSIZE structures.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_RECSIZE structure](./jet-recsize-structure2.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
