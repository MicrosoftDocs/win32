---
description: "Learn more about: Microsoft.Isam.Esent.Interop.Vista namespace"
title: Microsoft.Isam.Esent.Interop.Vista namespace ()
TOCTitle: '@NoTitle'
ms:assetid: N:Microsoft.Isam.Esent.Interop.Vista
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista(v=EXCHG.10)
ms:contentKeyID: 39513319
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista
dev_langs:
- CSharp
- JScript
- VB
- other
---

# Microsoft.Isam.Esent.Interop.Vista namespace

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
<td><a href="dn351217(v=exchg.10).md">JET_OPENTEMPORARYTABLE</a></td>
<td>A collection of parameters for the JetOpenTemporaryTable method.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335321(v=exchg.10).md">VistaApi</a></td>
<td>ESENT APIs that were first supported in Windows Vista.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335342(v=exchg.10).md">VistaColInfo</a></td>
<td>Column info levels that have been added to the Vista version of ESENT.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351274(v=exchg.10).md">VistaColtyp</a></td>
<td>Column types that have been added to the Vista version of ESENT.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335350(v=exchg.10).md">VistaGrbits</a></td>
<td>Grbits that have been added to the Vista version of ESENT.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335284(v=exchg.10).md">VistaParam</a></td>
<td>System parameters that have been added to the Vista version of ESENT.</td>
</tr>
</tbody>
</table>


## Structures

<table>
<thead>
<tr class="header">
<th> </th>
<th>Structure</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh557010(v=exchg.10).md">JET_RECSIZE</a></td>
<td>Used by <a href="dn335320(v=exchg.10).md">JetGetRecordSize(JET_SESID, JET_TABLEID, JET_RECSIZE, GetRecordSizeGrbit)</a> to return information about a record's usage requirements in user data space, number of set columns, number of values, and ESENT record structure overhead space.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh578565(v=exchg.10).md">JET_THREADSTATS</a></td>
<td>Contains cumulative statistics on the work performed by the database engine on the current thread. This information is returned via JetGetThreadStats.</td>
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
<td><a href="hh566355(v=exchg.10).md">JET_InstanceMiscInfo</a></td>
<td>Information levels for <a href="dn351258(v=exchg.10).md">JetGetInstanceMiscInfo(JET_INSTANCE, JET_SIGNATURE, JET_InstanceMiscInfo)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335312(v=exchg.10).md">LegacyFileNames</a></td>
<td>Options for LegacyFileNames</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh564489(v=exchg.10).md">SnapshotEndGrbit</a></td>
<td>Options for <a href="dn351267(v=exchg.10).md">JetOSSnapshotEnd(JET_OSSNAPID, SnapshotEndGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565195(v=exchg.10).md">SnapshotGetFreezeInfoGrbit</a></td>
<td>Options for <a href="dn351269(v=exchg.10).md">JetOSSnapshotGetFreezeInfo(JET_OSSNAPID, Int32, [], SnapshotGetFreezeInfoGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh557462(v=exchg.10).md">SnapshotPrepareInstanceGrbit</a></td>
<td>Options for <a href="dn335341(v=exchg.10).md">JetOSSnapshotPrepareInstance(JET_OSSNAPID, JET_INSTANCE, SnapshotPrepareInstanceGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566281(v=exchg.10).md">SnapshotTruncateLogGrbit</a></td>
<td>Options for <a href="dn335343(v=exchg.10).md">JetOSSnapshotTruncateLog(JET_OSSNAPID, SnapshotTruncateLogGrbit)</a> and <a href="dn351271(v=exchg.10).md">JetOSSnapshotTruncateLogInstance(JET_OSSNAPID, JET_INSTANCE, SnapshotTruncateLogGrbit)</a>.</td>
</tr>
</tbody>
</table>

