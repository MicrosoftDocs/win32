---
title: Transaction methods (Microsoft.Isam.Esent.Interop)
TOCTitle: Transaction methods
ms:assetid: Methods.T:Microsoft.Isam.Esent.Interop.Transaction
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.transaction_methods(v=EXCHG.10)
ms:contentKeyID: 55104163
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
---

# Transaction methods

Include protected members  
Include inherited members  

The [Transaction](dn351174\(v=exchg.10\).md) type exposes the following members.

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
<td><a href="dn351172(v=exchg.10).md">Begin</a></td>
<td>Begin a transaction. This object should not currently be in a transaction.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350541(v=exchg.10).md">CheckObjectIsNotDisposed</a></td>
<td>Throw an exception if this object has been disposed. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351179(v=exchg.10).md">Commit(CommitTransactionGrbit)</a></td>
<td>Commit a transaction. This object should be in a transaction.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351243(v=exchg.10).md">Commit(CommitTransactionGrbit, TimeSpan, JET_COMMIT_ID)</a></td>
<td>Commit a transaction. This object should be in a transaction.</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn350553(v=exchg.10).md">Dispose()</a></td>
<td>Dispose of this object, releasing the underlying Esent resource. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350543(v=exchg.10).md">Dispose(Boolean)</a></td>
<td>Called by Dispose and the finalizer. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="http://msdn2.microsoft.com/en-us/library/bsc2ak47">Equals</a></td>
<td>(Inherited from <a href="http://msdn2.microsoft.com/en-us/library/e5kfa45b">Object</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350552(v=exchg.10).md">Finalize</a></td>
<td>Finalizes an instance of the EsentResource class. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
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
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn351176(v=exchg.10).md">ReleaseResource</a></td>
<td>Called when the transaction is being disposed while active. This should rollback the transaction. (Overrides <a href="dn350545(v=exchg.10).md">EsentResource.ReleaseResource()</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350576(v=exchg.10).md">ResourceWasAllocated</a></td>
<td>Called by a subclass when a resource is allocated. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="even">
<td><img src="images/Dn292116.protmethod(EXCHG.10).gif" title="Protected method" alt="Protected method" /></td>
<td><a href="dn350577(v=exchg.10).md">ResourceWasReleased</a></td>
<td>Called by a subclass when a resource is freed. (Inherited from <a href="dn319890(v=exchg.10).md">EsentResource</a>.)</td>
</tr>
<tr class="odd">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351244(v=exchg.10).md">Rollback</a></td>
<td>Rollback a transaction. This object should be in a transaction.</td>
</tr>
<tr class="even">
<td><img src="images/Dn292146.pubmethod(EXCHG.10).gif" title="Public method" alt="Public method" /></td>
<td><a href="dn351181(v=exchg.10).md">ToString</a></td>
<td>Returns a <a href="http://msdn2.microsoft.com/en-us/library/s1wwdcbf">String</a> that represents the current <a href="dn351174(v=exchg.10).md">Transaction</a>. (Overrides <a href="http://msdn2.microsoft.com/en-us/library/7bxwbwt2">Object.ToString()</a>.)</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[Transaction class](dn351174\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

