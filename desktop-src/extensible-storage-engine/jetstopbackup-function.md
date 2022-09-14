---
description: "Learn more about: JetStopBackup Function"
title: JetStopBackup Function
TOCTitle: JetStopBackup Function
ms:assetid: b7545284-2fdb-4470-8466-fc2109ad63c5
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294067(v=EXCHG.10)
ms:contentKeyID: 32765682
ms.date: 04/11/2016
ms.topic: reference
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

[JetStopService](./jetstopservice-function.md) is the legacy call when only one instance is allowed. In this case, the only active instance is the one being prepared for termination.

```cpp
JET_ERR JET_API JetStopBackup(void);
```

### Parameters

This function has no parameters.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errRunningInMultiInstanceMode</p> | <p>It is not clear which instance to prepare for termination when using <a href="gg269240(v=exchg.10).md">JetStopService</a> with multiple instance mode.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 



If this function succeeds, the instance will start failing any new streaming backup APIs.

If this function fails, no steps to prepare for the backup termination on the instance will be taken and no change to the instance state will occur.

#### Remarks

Backup is usually triggered by an event outside the process mechanism and by using this API, the ESENT application itself will make any further calls to the streaming backup APIs to fail. The majority of streaming backup APIs will start failing with JET_errBackupAbortByServer. As such, any streaming backup progress (like [JetReadFileInstance](./jetreadfileinstance-function.md)) will return an error. Backup operations which are part of the backup termination (such as [JetEndExternalBackupInstance](./jetendexternalbackupinstance-function.md)) will still be allowed.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JetEndExternalBackupInstance](./jetendexternalbackupinstance-function.md)  
[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetReadFileInstance](./jetreadfileinstance-function.md)  
[JetStopService](./jetstopservice-function.md)
