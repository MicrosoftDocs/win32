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


| <p>Constant/value</p> | <p>Description</p> | <p>Recovery</p> | 
|-----------------------|--------------------|-----------------|
| <p>JET_errcatUnknown 0</p> | <p>An invalid error category.</p> | <p>N/A.</p> | 
| <p>JET_errcatError 1</p> | <p>The top level category (no errors should be of this class).</p> | <p>See the specific error constants.</p> | 
| <p>JET_errcatOperation 2</p> | <p>Represents errors that can happen at any time due to uncontrollable conditions and are often temporary. See subcategories if specified.</p> | <p>Retry and if the error continues, inform the operator.</p> | 
| <p>JET_errcatFatal 3</p> | <p>Represents fatal errors that, when they occur, create a risk that ESE cannot continue in a safe (often transactional) way, and data may become corrupted.</p> | <p>Restart the instance or process. If the problem persists, inform the operator.</p> | 
| <p>JET_errcatIO 4</p> | <p>Represents IO errors, which come from the operating system, and are out of ESE's control. This type of error may be temporary.</p> | <p>Retry, and if the error continues, ask the operator to check the disk.</p> | 
| <p>JET_errcatResource 5</p> | <p>Represents a category of errors related to lack of resource conditions.</p> | <p>See subcategories.</p> | 
| <p>JET_errcatMemory 6</p> | <p>Represents an error caused by lack of memory.</p> | <p>Retry after a period of time, free up memory, or quit.</p> | 
| <p>JET_errcatQuota 7</p> | <p>Certain "specialty" resources are in pools of a certain size, making it easier to detect leaks of these resources.</p> | <p>The application should <strong>Assert()</strong> to detect these issues during development . However, in retail code, the application should treat this as a memory error.</p> | 
| <p>JET_errcatDisk 8</p> | <p>Represents an error caused by lack of disk space.</p> | <p>Retry later to determine whether more disk space is available, or ask the operator to free some disk space.</p> | 
| <p>JET_errcatData 9</p> | <p>Represents a top-level category for errors related to data.</p> | <p>See subcategories.</p> | 
| <p>JET_errcatCorruption 10</p> | <p>Represents a corruption issue, which is often permanent without corrective action.</p> | <p>Restore from backup by using the ESE utilities repair operation (this operation restores only the data that is left/lossy). Also when the recovery(JetInit) method is used, recovery can be performed by allowing data loss (for more information, see <a href="gg269296(v=exchg.10).md">JET_bitReplayIgnoreLostLogs</a>.</p> | 
| <p>JET_errcatInconsistent 11</p> | <p>Represents an error in which the database and/or log files are in a state that is inconsistent and cannot be reconciled. This error might be caused by application/administrator mishandling.</p> | <p>Restore from backup by using the ESE utilities repair operation (which only restores the data that is left/lossy). Also in the case of the <strong>recovery(JetInit)</strong> operation, recovery can be performed by allowing data loss (for more information, see <a href="gg269296(v=exchg.10).md">JET_bitReplayIgnoreLostLogs</a>.</p> | 
| <p>JET_errcatFragmentation 12</p> | <p>Represents a class of errors in which some persisted internal resource ran out.</p> | <p>For database errors, offline defragmentation will fix the problem. For the log files, first recover all attached databases to a clean shutdown, and then delete all the log files and the checkpoint.</p> | 
| <p>JET_errcatApi 13</p> | <p>See subcategories.</p> | <p>See subcategories.</p> | 
| <p>JET_errcatUsage 14</p> | <p>Represents a usage error. The client code did not pass the correct arguments to the <strong>JET</strong> API. This error will persist with retry.</p> | <p>Client code should use the <strong>Assert()</strong> method to ensure that this class of errors is not returned, so issues can be caught during development. In retail, the application should notify the operator about the error.</p> | 
| <p>JET_errcatState 15</p> | <p>Represents a class of messages that the API can return to describe the state of the database. For example, the <a href="gg294103(v=exchg.10).md">JetSeek()</a> method might return <strong>JET_errRecordNotFound</strong> when the requested record was not found.</p> | <p>Varies based on the API.</p> | 
| <p>JET_errcatObsolete 16</p> | <p>Represents errors that are from a previous version of the engine. These errors should not be returned by the current engine.</p> | <p>Unknown.</p> | 
| <p>JET_errcatMax 17</p> | <p>A constant that indicates the end of the enumeration.</p> | <p>N/A.</p> | 



### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows 8 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 


