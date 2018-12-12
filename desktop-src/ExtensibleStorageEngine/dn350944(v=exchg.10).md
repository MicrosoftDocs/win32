---
title: Instance members (Microsoft.Isam.Esent.Interop)
TOCTitle: Instance members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.Instance
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.instance_members(v=EXCHG.10)
ms:contentKeyID: 55103299
ms.date: 07/30/2014
ms.topic: article
---

# Instance members

Include protected members  
Include inherited members  

A class that encapsulates a [JET\_INSTANCE](hh564593\(v=exchg.10\).md) in a disposable object. The instance must be closed last and closing the instance releases all other resources for the instance.

The [Instance](dn350923\(v=exchg.10\).md) type exposes the following members.

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
<td><a href="dn350924(v=exchg.10).md">Instance(String)</a></td>
<td>Initializes a new instance of the Instance class. The underlying JET_INSTANCE is allocated, but not initialized.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350927(v=exchg.10).md">Instance(String, String)</a></td>
<td>Initializes a new instance of the Instance class. The underlying JET_INSTANCE is allocated, but not initialized.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350948(v=exchg.10).md">Instance(String, String, TermGrbit)</a></td>
<td>Initializes a new instance of the Instance class. The underlying JET_INSTANCE is allocated, but not initialized.</td>
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
<td><a href="http://msdn2.microsoft.com/en-us/library/k25x6640">IsClosed</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/15b8sk08">IsInvalid</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/s07831kw">SafeHandleZeroOrMinusOneIsInvalid</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn350941(v=exchg.10).md">JetInstance</a></td>
<td>Gets the JET_INSTANCE that this instance contains.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn350962(v=exchg.10).md">Parameters</a></td>
<td>Gets the InstanceParameters for this instance.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn350964(v=exchg.10).md">TermGrbit</a></td>
<td>Gets or sets the TermGrbit for this instance.</td>
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
<td><a href="http://msdn2.microsoft.com/en-us/library/k296d386">Close</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/a1cssf5t">DangerousAddRef</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/277heftx">DangerousGetHandle</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/k2ba91w2">DangerousRelease</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/4h5yzadk">Dispose()</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/ms146715">Dispose(Boolean)</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/bsc2ak47">Equals</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/f967bh71">Finalize</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/zdee4b3y">GetHashCode</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/dfwy45w9">GetType</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350932(v=exchg.10).md">Init()</a></td>
<td>Initialize the JET_INSTANCE.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350954(v=exchg.10).md">Init(InitGrbit)</a></td>
<td>Initialize the JET_INSTANCE.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350934(v=exchg.10).md">Init(JET_RSTINFO, InitGrbit)</a></td>
<td>Initialize the JET_INSTANCE. This API requires at least the Vista version of ESENT.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/57ctke0a">MemberwiseClone</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350956(v=exchg.10).md">ReleaseHandle</a></td>
<td>Release the handle for this instance. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/22ywedf6">SafeHandle.ReleaseHandle()</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292116.protmethod(exchg.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/9s47xzk4">SetHandle</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/18fth6d8">SetHandleAsInvalid</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350935(v=exchg.10).md">Term</a></td>
<td>Terminate the JET_INSTANCE.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350960(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="http://msdn2.microsoft.com/en-us/library/s1wwdcbf">String</a> that represents the current <a href="dn350923(v=exchg.10).md">Instance</a>. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/7bxwbwt2">Object.ToString()</a>.)</td>
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
<td><a href="dn350950(v=exchg.10).md">Implicit(Instance to JET_INSTANCE)</a></td>
<td>Provide implicit conversion of an Instance object to a JET_INSTANCE structure. This is done so that an Instance can be used anywhere a JET_INSTANCE is required.</td>
</tr>
</tbody>
</table>


Top

## Fields

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
<td><img src="../images/dn350944.protfield(exchg.10).gif" title="Protected field" alt="Protected field" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/exzskf0s">handle</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/7s3yckbh">SafeHandle</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[Instance class](dn350923\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

