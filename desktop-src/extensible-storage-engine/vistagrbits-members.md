---
description: "Learn more about: VistaGrbits members"
title: VistaGrbits members (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: VistaGrbits members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.Vista.VistaGrbits
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.vistagrbits_members(v=EXCHG.10)
ms:contentKeyID: 55104213
ms.date: 07/30/2014
ms.topic: article
---

# VistaGrbits members

Include protected members  
Include inherited members  

Grbits that have been added to the Vista version of ESENT.

The [VistaGrbits](./vistagrbits-class.md) type exposes the following members.

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
<td><a href="dn351283(v=exchg.10).md">ContinueAfterThaw</a></td>
<td>The snapshot session continues after JetOSSnapshotThaw and will require a JetOSSnapshotEnd function call.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335364(v=exchg.10).md">IndexCrossProduct</a></td>
<td>Specifying this flag for an index that has more than one key column that is a multi-valued column will result in an index entry being created for each result of a cross product of all the values in those key columns. Otherwise, the index would only have one entry for each multi-value in the most significant key column that is a multi-valued column and each of those index entries would use the first multi-value from any other key columns that are multi-valued columns. For example, if you specified this flag for an index over column A that has the values &quot;red&quot; and &quot;blue&quot; and over column B that has the values &quot;1&quot; and &quot;2&quot; then the following index entries would be created: &quot;red&quot;, &quot;1&quot;; &quot;red&quot;, &quot;2&quot;; &quot;blue&quot;, &quot;1&quot;; &quot;blue&quot;, &quot;2&quot;. Otherwise, the following index entries would be created: &quot;red&quot;, &quot;1&quot;; &quot;blue&quot;, &quot;1&quot;.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335368(v=exchg.10).md">IndexDisallowTruncation</a></td>
<td>Specifying this flag will cause any update to the index that would result in a truncated key to fail with <a href="hh564840(v=exchg.10).md">KeyTruncated</a>. Otherwise, keys will be silently truncated.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351285(v=exchg.10).md">IndexNestedTable</a></td>
<td>Index over multiple multi-valued columns but only with values of same itagSequence.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335282(v=exchg.10).md">LogStreamMustExist</a></td>
<td>Transaction logs must exist in the log file directory (i.e. can't auto-start a new stream).</td>
</tr>
<tr class="even">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335367(v=exchg.10).md">RecoveryWithoutUndo</a></td>
<td>Perform recovery, but halt at the Undo phase. Allows whatever logs are present to be replayed, then later additional logs can be copied and replayed.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335375(v=exchg.10).md">ReplayMissingMapEntryDB</a></td>
<td>Missing database map entry default to same location.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335283(v=exchg.10).md">TruncateDone</a></td>
<td>The engine can mark the database headers as appropriate (for example, a full backup completed), even though the call to truncate was not completed.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596466.pubfield(exchg.10).gif" title="Public field" alt="Public field" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335371(v=exchg.10).md">TruncateLogsAfterRecovery</a></td>
<td>On successful soft recovery, truncate log files.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[VistaGrbits class](./vistagrbits-class.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
