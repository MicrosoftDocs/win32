---
title: JetStopBackup Function
TOCTitle: JetStopBackup Function
ms:assetid: b7545284-2fdb-4470-8466-fc2109ad63c5
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294067(v=EXCHG.10)
ms:contentKeyID: 32765682
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
api_name: 
- JetStopBackup
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetStopBackup Function


_**Applies to:** Windows | Windows Server_

## JetStopBackup Function

The **JetStopBackup** function prevents any streaming backup-related activity from continuing on a specific running instance, thus ending the streaming backup in a predictable way.

**Windows XP:**  This function is introduced in Windows XP.

[JetStopService](gg269240\(v=exchg.10\).md) is the legacy call when only one instance is allowed. In this case, the only active instance is the one being prepared for termination.

    JET_ERR JET_API JetStopBackup(void);

### Parameters

This function has no parameters.

### Return Value

This function returns the [JET\_ERR](gg294092\(v=exchg.10\).md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errSuccess</p></td>
<td><p>The operation completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRunningInMultiInstanceMode</p></td>
<td><p>It is not clear which instance to prepare for termination when using <a href="gg269240(v=exchg.10).md">JetStopService</a> with multiple instance mode.</p>
<p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p></td>
</tr>
</tbody>
</table>


If this function succeeds, the instance will start failing any new streaming backup APIs.

If this function fails, no steps to prepare for the backup termination on the instance will be taken and no change to the instance state will occur.

#### Remarks

Backup is usually triggered by an event outside the process mechanism and by using this API, the ESENT application itself will make any further calls to the streaming backup APIs to fail. The majority of streaming backup APIs will start failing with JET\_errBackupAbortByServer. As such, any streaming backup progress (like [JetReadFileInstance](gg294060\(v=exchg.10\).md)) will return an error. Backup operations which are part of the backup termination (such as [JetEndExternalBackupInstance](gg269204\(v=exchg.10\).md)) will still be allowed.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
</tbody>
</table>


#### See Also

[JetEndExternalBackupInstance](gg269204\(v=exchg.10\).md)  
[JET\_ERR](gg294092\(v=exchg.10\).md)  
[JET\_INSTANCE](gg294048\(v=exchg.10\).md)  
[JetReadFileInstance](gg294060\(v=exchg.10\).md)  
[JetStopService](gg269240\(v=exchg.10\).md)

