---
description: "Learn more about: Microsoft.Isam.Esent.Interop.Windows8 namespace"
title: Microsoft.Isam.Esent.Interop.Windows8 namespace ()
TOCTitle: '@NoTitle'
ms:assetid: N:Microsoft.Isam.Esent.Interop.Windows8
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows8(v=EXCHG.10)
ms:contentKeyID: 55104389
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8
dev_langs:
- CSharp
- JScript
- VB
- other
---

# Microsoft.Isam.Esent.Interop.Windows8 namespace

## Classes

<table>
<thead>
<tr class="header">
<th> </th>
<th>Class</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335323(v=exchg.10).md">DurableCommitCallback</a></td>
<td>Wraps the callback dealing with durable commits.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335448(v=exchg.10).md">JET_COMMIT_ID</a></td>
<td>Information context surrounded data emitted from JET_PFNEMITLOGDATA.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335334(v=exchg.10).md">JET_ERRINFOBASIC</a></td>
<td>Contains the information about an error.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335349(v=exchg.10).md">JET_INDEX_COLUMN</a></td>
<td>Contains filter definition for <a href="dn335382(v=exchg.10).md">JetPrereadIndexRanges(JET_SESID, JET_TABLEID, [], Int32, Int32, Int32, [], PrereadIndexRangesGrbit)</a> and <a href="dn335383(v=exchg.10).md">JetSetCursorFilter(JET_SESID, JET_TABLEID, [], CursorFilterGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335481(v=exchg.10).md">JET_INDEX_RANGE</a></td>
<td>Contains definition for <a href="dn335382(v=exchg.10).md">JetPrereadIndexRanges(JET_SESID, JET_TABLEID, [], Int32, Int32, Int32, [], PrereadIndexRangesGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335490(v=exchg.10).md">Windows8Api</a></td>
<td>Api calls introduced in Windows 8.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335391(v=exchg.10).md">Windows8Grbits</a></td>
<td>System parameters that were introduced in Windows 8.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335399(v=exchg.10).md">Windows8IdxInfo</a></td>
<td>Column info levels that have been added to the Windows 8 version of ESENT.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335398(v=exchg.10).md">Windows8Param</a></td>
<td>System parameters that were introduced in Windows 8.</td>
</tr>
</tbody>
</table>


## Delegates

<table>
<thead>
<tr class="header">
<th> </th>
<th>Delegate</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/hh596136.pubdelegate(exchg.10).gif" title="Public delegate" alt="Public delegate" /></td>
<td><a href="dn335363(v=exchg.10).md">JET_PFNDURABLECOMMITCALLBACK</a></td>
<td>Callback for JET_paramDurableCommitCallback.</td>
</tr>
</tbody>
</table>


## Enumerations

<table>
<thead>
<tr class="header">
<th> </th>
<th>Enumeration</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335440(v=exchg.10).md">CursorFilterGrbit</a></td>
<td>Options passed while setting cursor filters.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335446(v=exchg.10).md">DurableCommitCallbackGrbit</a></td>
<td>Options passed to log flush callback.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335447(v=exchg.10).md">ErrorInfoGrbit</a></td>
<td>Options for <a href="dn335493(v=exchg.10).md">JetGetErrorInfo(JET_err, JET_ERRINFOBASIC)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335469(v=exchg.10).md">JET_ERRCAT</a></td>
<td>The error category. The hierarchy is as follows: JET_errcatError | |-- JET_errcatOperation | |-- JET_errcatFatal | |-- JET_errcatIO // bad IO issues, may or may not be transient. | |-- JET_errcatResource | |-- JET_errcatMemory // out of memory (all variants) | |-- JET_errcatQuota | |-- JET_errcatDisk // out of disk space (all variants) |-- JET_errcatData | |-- JET_errcatCorruption | |-- JET_errcatInconsistent // typically caused by user Mishandling | |-- JET_errcatFragmentation |-- JET_errcatApi |-- JET_errcatUsage |-- JET_errcatState |-- JET_errcatObsolete</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335352(v=exchg.10).md">JET_ErrorInfo</a></td>
<td>The valid values of InfoLevel for JetGetErrorInfo.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335486(v=exchg.10).md">JET_sesparam</a></td>
<td>ESENT session parameters.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335365(v=exchg.10).md">JetIndexColumnGrbit</a></td>
<td>Options for <a href="dn335349(v=exchg.10).md">JET_INDEX_COLUMN</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335491(v=exchg.10).md">JetRelop</a></td>
<td>Comparison operation for filter defined as <a href="dn335349(v=exchg.10).md">JET_INDEX_COLUMN</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335366(v=exchg.10).md">PrereadIndexRangesGrbit</a></td>
<td>Options for <a href="dn335382(v=exchg.10).md">JetPrereadIndexRanges(JET_SESID, JET_TABLEID, [], Int32, Int32, Int32, [], PrereadIndexRangesGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335369(v=exchg.10).md">ResizeDatabaseGrbit</a></td>
<td>Options for <a href="dn335496(v=exchg.10).md">JetResizeDatabase(JET_SESID, JET_DBID, Int32, Int32, ResizeDatabaseGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335370(v=exchg.10).md">StopServiceGrbit</a></td>
<td>Options for <a href="dn335494(v=exchg.10).md">JetStopServiceInstance2(JET_INSTANCE, StopServiceGrbit)</a>.</td>
</tr>
</tbody>
</table>

