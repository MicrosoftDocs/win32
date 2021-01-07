---
description: "Learn more about: Windows8Api members"
title: Windows8Api members (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: Windows8Api members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.Windows8.Windows8Api
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows8.windows8api_members(v=EXCHG.10)
ms:contentKeyID: 55104331
ms.date: 07/30/2014
ms.topic: article
---

# Windows8Api members

Include protected members  
Include inherited members  

Api calls introduced in Windows 8.

The [Windows8Api](./windows8api-class.md) type exposes the following members.

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
<td><a href="dn335374(v=exchg.10).md">JetBeginTransaction3</a></td>
<td>Causes a session to enter a transaction or create a new save point in an existing transaction.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335489(v=exchg.10).md">JetCommitTransaction2</a></td>
<td>Commits the changes made to the state of the database during the current save point and migrates them to the previous save point. If the outermost save point is committed then the changes made during that save point will be committed to the state of the database and the session will exit the transaction.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335488(v=exchg.10).md">JetCreateIndex4</a></td>
<td>Creates indexes over data in an ESE database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335377(v=exchg.10).md">JetCreateTableColumnIndex4</a></td>
<td>Creates a table, adds columns, and indices on that table. <a href="dn292129(v=exchg.10).md">JetCreateTableColumnIndex3(JET_SESID, JET_DBID, JET_TABLECREATE)</a></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335493(v=exchg.10).md">JetGetErrorInfo</a></td>
<td>Gets extended information about an error.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335378(v=exchg.10).md">JetOpenTemporaryTable2</a></td>
<td>Creates a temporary table with a single index. A temporary table stores and retrieves records just like an ordinary table created using JetCreateTableColumnIndex. However, temporary tables are much faster than ordinary tables due to their volatile nature. They can also be used to very quickly sort and perform duplicate removal on record sets when accessed in a purely sequential manner. Also see <a href="dn292231(v=exchg.10).md">JetOpenTempTable(JET_SESID, [], Int32, TempTableGrbit, JET_TABLEID, [])</a>, &quot;Api.JetOpenTempTable2&quot;, <a href="dn292233(v=exchg.10).md">JetOpenTempTable3(JET_SESID, [], Int32, JET_UNICODEINDEX, TempTableGrbit, JET_TABLEID, [])</a>. <a href="dn335326(v=exchg.10).md">JetOpenTemporaryTable(JET_SESID, JET_OPENTEMPORARYTABLE)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335382(v=exchg.10).md">JetPrereadIndexRanges</a></td>
<td>If the records with the specified key ranges are not in the buffer cache, then start asynchronous reads to bring the records into the database buffer cache.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335496(v=exchg.10).md">JetResizeDatabase</a></td>
<td>Resizes a currently open database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335383(v=exchg.10).md">JetSetCursorFilter</a></td>
<td>Set an array of simple filters for <a href="dn292217(v=exchg.10).md">JetMove(JET_SESID, JET_TABLEID, Int32, MoveGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335495(v=exchg.10).md">JetSetSessionParameter</a></td>
<td>Sets a parameter on the provided session state, used for the lifetime of this session or until reset.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335494(v=exchg.10).md">JetStopServiceInstance2</a></td>
<td>Prepares an instance for termination. Can also be used to resume a previous quiescing.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335386(v=exchg.10).md">JetTryPrereadIndexRanges</a></td>
<td>If the records with the specified key ranges are not in the buffer cache, then start asynchronous reads to bring the records into the database buffer cache.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn335499(v=exchg.10).md">PrereadKeyRanges</a></td>
<td>If the records with the specified key ranges are not in the buffer cache then start asynchronous reads to bring the records into the database buffer cache.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[Windows8Api class](./windows8api-class.md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](./microsoft.isam.esent.interop.windows8-namespace.md)
