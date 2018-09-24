---
title: JetBeginExternalBackupInstance Function
TOCTitle: JetBeginExternalBackupInstance Function
ms:assetid: f1c5a73d-b1cc-4ee4-942b-b5e4ef51bc2f
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294132(v=EXCHG.10)
ms:contentKeyID: 32765746
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
api_name: 
- JetBeginExternalBackupInstance
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

# JetBeginExternalBackupInstance Function


_**Applies to:** Windows | Windows Server_

## JetBeginExternalBackupInstance Function

The **JetBeginExternalBackupInstance** function initiates an external backup while the engine and database are online and active.

**Windows XP:  JetBeginExternalBackupInstance** is introduced in Windows XP.

    JET_ERR JET_API JetBeginExternalBackupInstance(
      __in          JET_INSTANCE instance,
      __in          JET_GRBIT grbit
    );

### Parameters

*instance*

The database instance to use for this call.

For Windows 2000, the API variant that accepts this parameter is not available because only one instance is supported. The use of this one global instance is implied in this case.

For Windows XP and later releases, the API variant that does not accept this parameter may only be called when the engine is in legacy mode (Windows 2000 compatibility mode) where only one instance is supported. Otherwise, the operation will fail with JET\_errRunningInMultiInstanceMode.

*grbit*

A group of bits specifying zero or more of the following options.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_bitBackupAtomic</p></td>
<td><p>This flag is deprecated. Usage of this bit will result in JET_errInvalidgrbit being returned.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitBackupIncremental</p></td>
<td><p>Creates an incremental backup as opposed to a full backup. This means that only the log files since the last full or incremental backup will be backed up.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitBackupSnapshot</p></td>
<td><p>Reserved for future use. Defined for Windows XP.</p></td>
</tr>
</tbody>
</table>


### Return Value

The system may generate success or failure codes as a result of a call to this function. For a complete list of errors for this API, see [Extensible Storage Engine Error Codes](gg269297\(v=exchg.10\).md).

See [JetBeginExternalBackup](gg269292\(v=exchg.10\).md).

#### Remarks

**JetBeginExternalBackupInstance** is the first function in a series of functions that must be called to execute a successful online (non-VSS based) backup. See also [JetBeginExternalBackup](gg269292\(v=exchg.10\).md) and [JetStopBackupInstance](gg269309\(v=exchg.10\).md).

An external backup can be used to implement full, incremental, or differential backups.

The backup will be fuzzy, in that the backup will be consistent to a single point in time in the transaction history, but controlling the exact point in time is not possible at this time.

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

[JET\_ERR](gg294092\(v=exchg.10\).md)  
[JET\_GRBIT](gg294066\(v=exchg.10\).md)  
[JET\_INSTANCE](gg294048\(v=exchg.10\).md)  
[JetAttachDatabase](gg294074\(v=exchg.10\).md)  
[JetBeginExternalBackup](gg269292\(v=exchg.10\).md)  
[JetCloseFile](gg294127\(v=exchg.10\).md)  
[JetEndExternalBackup](gg269176\(v=exchg.10\).md)  
[JetEndExternalBackupInstance2](gg294047\(v=exchg.10\).md)  
[JetGetAttachInfo](gg269286\(v=exchg.10\).md)  
[JetGetLogInfo](gg294055\(v=exchg.10\).md)  
[JetOpenFile](gg269249\(v=exchg.10\).md)  
[JetReadFile](gg269257\(v=exchg.10\).md)  
[JetStopBackup](gg294067\(v=exchg.10\).md)  
[JetTruncateLog](gg269263\(v=exchg.10\).md)

