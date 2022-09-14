---
description: "Learn more about: JetBeginExternalBackupInstance Function"
title: JetBeginExternalBackupInstance Function
TOCTitle: JetBeginExternalBackupInstance Function
ms:assetid: f1c5a73d-b1cc-4ee4-942b-b5e4ef51bc2f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294132(v=EXCHG.10)
ms:contentKeyID: 32765746
ms.date: 04/11/2016
ms.topic: reference
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

```cpp
    JET_ERR JET_API JetBeginExternalBackupInstance(
      __in          JET_INSTANCE instance,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*instance*

The database instance to use for this call.

For Windows 2000, the API variant that accepts this parameter is not available because only one instance is supported. The use of this one global instance is implied in this case.

For Windows XP and later releases, the API variant that does not accept this parameter may only be called when the engine is in legacy mode (Windows 2000 compatibility mode) where only one instance is supported. Otherwise, the operation will fail with JET_errRunningInMultiInstanceMode.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitBackupAtomic</p> | <p>This flag is deprecated. Usage of this bit will result in JET_errInvalidgrbit being returned.</p> | 
| <p>JET_bitBackupIncremental</p> | <p>Creates an incremental backup as opposed to a full backup. This means that only the log files since the last full or incremental backup will be backed up.</p> | 
| <p>JET_bitBackupSnapshot</p> | <p>Reserved for future use. Defined for Windows XP.</p> | 



### Return Value

The system may generate success or failure codes as a result of a call to this function. For a complete list of errors for this API, see [Extensible Storage Engine Error Codes](./extensible-storage-engine-error-codes.md).

See [JetBeginExternalBackup](./jetbeginexternalbackup-function.md).

#### Remarks

**JetBeginExternalBackupInstance** is the first function in a series of functions that must be called to execute a successful online (non-VSS based) backup. See also [JetBeginExternalBackup](./jetbeginexternalbackup-function.md) and [JetStopBackupInstance](./jetstopbackupinstance-function.md).

An external backup can be used to implement full, incremental, or differential backups.

The backup will be fuzzy, in that the backup will be consistent to a single point in time in the transaction history, but controlling the exact point in time is not possible at this time.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetAttachDatabase](./jetattachdatabase-function.md)  
[JetBeginExternalBackup](./jetbeginexternalbackup-function.md)  
[JetCloseFile](./jetclosefile-function.md)  
[JetEndExternalBackup](./jetendexternalbackup-function.md)  
[JetEndExternalBackupInstance2](./jetendexternalbackupinstance2-function.md)  
[JetGetAttachInfo](./jetgetattachinfo-function.md)  
[JetGetLogInfo](./jetgetloginfo-function.md)  
[JetOpenFile](./jetopenfile-function.md)  
[JetReadFile](./jetreadfile-function.md)  
[JetStopBackup](./jetstopbackup-function.md)  
[JetTruncateLog](./jettruncatelog-function.md)
