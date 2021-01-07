---
description: "Learn more about: JET_ERRCAT"
title: JET_ERRCAT
TOCTitle: JET_ERRCAT
ms:assetid: 96551dc8-8df5-417c-850f-278b5231b0b6
ms:mtpsurl: https://msdn.microsoft.com/library/Hh475860(v=EXCHG.10)
ms:contentKeyID: 37033566
ms.date: 04/11/2016
ms.topic: article
---

# JET_ERRCAT


_**Applies to:** Windows | Windows Server_

## JET_ERRCAT

The **JET_ERRCAT** group of constants describes higher-level classifications or categories of errors. This group of constants enables applications to define default treatment for a classification of errors, rather than handling each error case individually. It also ensures that the application does not have to handle new error conditions that are included in existing classifications.

Note: This documentation is based on a preliminary release of the Extensible Storage Engine. This information is subject to change.

The **JET_ERRCAT** constants are arranged in a specific hierarchy of conditions and subconditions, as follows:

|--- Error |--- Operation(al) | |--- Fatal | |--- IO | |--- Resource | |--- Memory | |--- Quota | |--- Disk | |--- Data | |--- Corruption | |--- Inconsistent | |--- Fragmentation | |--- Api |--- Usage |--- State

The following table lists the **JET_ERRCAT** constants and provides a description and recovery information, as applicable.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Constant/value</p></th>
<th><p>Description</p></th>
<th><p>Recovery</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errcatUnknown 0</p></td>
<td><p>An invalid error category.</p></td>
<td><p>N/A.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatError 1</p></td>
<td><p>The top level category (no errors should be of this class).</p></td>
<td><p>See the specific error constants.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatOperation 2</p></td>
<td><p>Represents errors that can happen at any time due to uncontrollable conditions and are often temporary. See subcategories if specified.</p></td>
<td><p>Retry and if the error continues, inform the operator.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatFatal 3</p></td>
<td><p>Represents fatal errors that, when they occur, create a risk that ESE cannot continue in a safe (often transactional) way, and data may become corrupted.</p></td>
<td><p>Restart the instance or process. If the problem persists, inform the operator.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatIO 4</p></td>
<td><p>Represents IO errors, which come from the operating system, and are out of ESE's control. This type of error may be temporary.</p></td>
<td><p>Retry, and if the error continues, ask the operator to check the disk.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatResource 5</p></td>
<td><p>Represents a category of errors related to lack of resource conditions.</p></td>
<td><p>See subcategories.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatMemory 6</p></td>
<td><p>Represents an error caused by lack of memory.</p></td>
<td><p>Retry after a period of time, free up memory, or quit.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatQuota 7</p></td>
<td><p>Certain &quot;specialty&quot; resources are in pools of a certain size, making it easier to detect leaks of these resources.</p></td>
<td><p>The application should <strong>Assert()</strong> to detect these issues during development . However, in retail code, the application should treat this as a memory error.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatDisk 8</p></td>
<td><p>Represents an error caused by lack of disk space.</p></td>
<td><p>Retry later to determine whether more disk space is available, or ask the operator to free some disk space.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatData 9</p></td>
<td><p>Represents a top-level category for errors related to data.</p></td>
<td><p>See subcategories.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatCorruption 10</p></td>
<td><p>Represents a corruption issue, which is often permanent without corrective action.</p></td>
<td><p>Restore from backup by using the ESE utilities repair operation (this operation restores only the data that is left/lossy). Also when the recovery(JetInit) method is used, recovery can be performed by allowing data loss (for more information, see <a href="gg269296(v=exchg.10).md">JET_bitReplayIgnoreLostLogs</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatInconsistent 11</p></td>
<td><p>Represents an error in which the database and/or log files are in a state that is inconsistent and cannot be reconciled. This error might be caused by application/administrator mishandling.</p></td>
<td><p>Restore from backup by using the ESE utilities repair operation (which only restores the data that is left/lossy). Also in the case of the <strong>recovery(JetInit)</strong> operation, recovery can be performed by allowing data loss (for more information, see <a href="gg269296(v=exchg.10).md">JET_bitReplayIgnoreLostLogs</a>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatFragmentation 12</p></td>
<td><p>Represents a class of errors in which some persisted internal resource ran out.</p></td>
<td><p>For database errors, offline defragmentation will fix the problem. For the log files, first recover all attached databases to a clean shutdown, and then delete all the log files and the checkpoint.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatApi 13</p></td>
<td><p>See subcategories.</p></td>
<td><p>See subcategories.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatUsage 14</p></td>
<td><p>Represents a usage error. The client code did not pass the correct arguments to the <strong>JET</strong> API. This error will persist with retry.</p></td>
<td><p>Client code should use the <strong>Assert()</strong> method to ensure that this class of errors is not returned, so issues can be caught during development. In retail, the application should notify the operator about the error.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatState 15</p></td>
<td><p>Represents a class of messages that the API can return to describe the state of the database. For example, the <a href="gg294103(v=exchg.10).md">JetSeek()</a> method might return <strong>JET_errRecordNotFound</strong> when the requested record was not found.</p></td>
<td><p>Varies based on the API.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errcatObsolete 16</p></td>
<td><p>Represents errors that are from a previous version of the engine. These errors should not be returned by the current engine.</p></td>
<td><p>Unknown.</p></td>
</tr>
<tr class="even">
<td><p>JET_errcatMax 17</p></td>
<td><p>A constant that indicates the end of the enumeration.</p></td>
<td><p>N/A.</p></td>
</tr>
</tbody>
</table>


### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows 8.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows 8 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>

