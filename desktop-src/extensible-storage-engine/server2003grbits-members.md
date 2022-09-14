---
description: "Learn more about: Server2003Grbits members"
title: Server2003Grbits members (Microsoft.Isam.Esent.Interop.Server2003)
TOCTitle: Server2003Grbits members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.Server2003.Server2003Grbits
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.server2003.server2003grbits_members(v=EXCHG.10)
ms:contentKeyID: 55107767
ms.date: 07/30/2014
ms.topic: article
---

# Server2003Grbits members

Include protected members  
Include inherited members  

Grbits that have been added to the Windows Server 2003 version of ESENT.

The [Server2003Grbits](./server2003grbits-class.md) type exposes the following members.

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
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351203(v=exchg.10).md">EnumerateIgnoreUserDefinedDefault</a></td>
<td>If a given column is not present in the record and it has a user defined default value then no column value will be returned. This option will prevent the callback that computes the user defined default value for the column from being called when enumerating the values for that column.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351284(v=exchg.10).md">ForwardOnly</a></td>
<td>This option requests that the temporary table only be created if the temporary table manager can use the implementation optimized for intermediate query results. If any characteristic of the temporary table would prevent the use of this optimization then the operation will fail with JET_errCannotMaterializeForwardOnlySort. A side effect of this option is to allow the temporary table to contain records with duplicate index keys. See <a href="hh558517(v=exchg.10).md">Unique</a> for more information.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351209(v=exchg.10).md">WaitAllLevel0Commit</a></td>
<td>All transactions previously committed by any session that have not yet been flushed to the transaction log file will be flushed immediately. This API will wait until the transactions have been flushed before returning to the caller. This option may be used even if the session is not currently in a transaction. This option cannot be used in combination with any other option.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[Server2003Grbits class](./server2003grbits-class.md)

[Microsoft.Isam.Esent.Interop.Server2003 namespace](./microsoft.isam.esent.interop.server2003-namespace.md)
