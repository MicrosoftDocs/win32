---
title: JetEndExternalBackupInstance Function
TOCTitle: JetEndExternalBackupInstance Function
ms:assetid: 2256f63e-91f5-44ad-b67e-506dd71ffa94
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269204(v=EXCHG.10)
ms:contentKeyID: 32765507
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
api_name: 
- JetEndExternalBackupInstance
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetEndExternalBackupInstance Function


_**Applies to:** Windows | Windows Server_

## JetEndExternalBackupInstance Function

The **JetEndExternalBackupInstance** function ends an external backup session. This API is the last API in a series of APIs that must be called to execute a successful online (non-VSS based) backup.

**Windows XP:  JetEndExternalBackupInstance** is introduced in Windows XP.

    JET_ERR JET_API JetEndExternalBackupInstance(
      __in          JET_INSTANCE instance
    );

### Parameters

*instance*

The instance to use for this call.

**Windows 2000:** For Windows 2000, the API variant that accepts this parameter is not available because only one instance is supported. The use of this one global instance is implied in this case.

**Windows XP:** For Windows XP and later releases, the API variant that does not accept this parameter can only be called when the engine is in legacy mode (Windows 2000 compatibility mode) where only one instance is supported. Otherwise, the operation will fail with JET\_errRunningInMultiInstanceMode.

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
<td><p>JET_errBackupAbortByCaller</p></td>
<td><p><strong>Windows XP:  </strong>This return value is introduced in Windows XP.</p>
<p>The caller terminated a backup in the middle of the backup sequence without signaling the intention with <a href="gg294067(v=exchg.10).md">JetStopBackup</a>. This error is the result of a bug in the backup client in Windows Server 2003 and later. On Windows XP this error is returned for an intentional termination of the external backup sequence.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errBackupAbortByServer</p></td>
<td><p><strong>Windows Server 2003:  </strong>This return value is introduced in Windows Server 2003.</p>
<p>The operation failed because the current external backup has been aborted by a call to <a href="gg294067(v=exchg.10).md">JetStopBackup</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p><strong>Windows XP:  </strong>This return value is introduced in Windows XP.</p>
<p>The operation cannot complete because the instance that is associated with the session encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p></td>
</tr>
<tr class="even">
<td><p>JET_errNoBackup</p></td>
<td><p>The operation failed because no external backup is in progress.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNotInitialized</p></td>
<td><p>The operation cannot complete because the instance that is associated with the session has not yet been initialized.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errRunningInMultiInstanceMode</p></td>
<td><p>The operation failed because an attempt was made to use the engine in legacy mode (Windows 2000 compatibility mode) where only one instance is supported, when in fact multiple instances already exist.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTermInProgress</p></td>
<td><p>The operation cannot complete because the instance that is associated with the session is being shut down.</p></td>
</tr>
</tbody>
</table>


If the function succeeds, the external backup was a success. Success indicates that all files (for example, databases and logs) that are appropriate for the type of backup (specified in [JetBeginExternalBackup](gg269292\(v=exchg.10\).md)) were retrieved from the backup engine. The backed up files can be recovered with hard recovery ([JetExternalRestore](gg294088\(v=exchg.10\).md)).

If this function fails, the external backup usually ends. Failure means that the backup is invalid because of a client or an application usage error. It is important to check the return code for this API to verify that the backup sequence was successful.

#### Remarks

If the engine is configured to log events, an event is logged to indicate the resolution of the external backup.

If the backup sequence is not completed in order and with a successful call to [JetEndExternalBackup](gg269176\(v=exchg.10\).md), subsequent incremental backups might contain more data than the application anticipated.

For more information about the external backup API sequence, see [JetBeginExternalBackup](gg269292\(v=exchg.10\).md).

Before Windows Vista, if the log truncation was not done, the engine considered that the backup was a copy backup. However, the backup might be a normal backup for which truncation was not done (for example, if there are detached databases). The JET\_bitBackupTruncateDone option can be used to inform the engine about this and allow proper database header modifications.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista or Windows XP.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008 or Windows Server 2003.</p></td>
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

[Error Handling Parameters](gg269173\(v=exchg.10\).md)  
[Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md)  
[JetAttachDatabase](gg294074\(v=exchg.10\).md)  
[JetBeginExternalBackup](gg269292\(v=exchg.10\).md)  
[JetBeginExternalBackupInstance](gg294132\(v=exchg.10\).md)  
[JetCloseFile](gg294127\(v=exchg.10\).md)  
[JET\_ERR](gg294092\(v=exchg.10\).md)  
[JetExternalRestore](gg294088\(v=exchg.10\).md)  
[JetGetAttachInfo](gg269286\(v=exchg.10\).md)  
[JetGetLogInfo](gg294055\(v=exchg.10\).md)  
[JET\_INSTANCE](gg294048\(v=exchg.10\).md)  
[JetOpenFile](gg269249\(v=exchg.10\).md)  
[JetReadFile](gg269257\(v=exchg.10\).md)  
[JetStopBackup](gg294067\(v=exchg.10\).md)  
[JetStopService](gg269240\(v=exchg.10\).md)  
[JetTruncateLog](gg269263\(v=exchg.10\).md)

