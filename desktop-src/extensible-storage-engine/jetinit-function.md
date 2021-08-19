---
description: "Learn more about: JetInit Function"
title: JetInit Function
TOCTitle: JetInit Function
ms:assetid: b7f78cca-7268-4045-bda2-20746b1d6370
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294068(v=EXCHG.10)
ms:contentKeyID: 32765683
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetInit
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

# JetInit Function


_**Applies to:** Windows | Windows Server_

## JetInit Function

The **JetInit** function puts the database engine into a state where it can support application use of database files. The engine must already be properly configured for initialization using [JetSetSystemParameter](./jetsetsystemparameter-function.md). Database crash recovery is performed automatically as a part of the initialization process.

```cpp
JET_ERR JET_API JetInit(
  __in_out_opt  JET_INSTANCE* pinstance
);
```

### Parameters

*pinstance*

The instance to use for this call.

For Windows 2000, this parameter is ignored and should always be NULL.

For Windows XP and later releases, the use of this parameter depends on the operating mode of the engine. If the engine is operating in legacy mode (Windows 2000 compatibility mode) where only one instance is supported then this parameter may either be NULL or it may be set to a valid output buffer that will return the global instance handle created as a side effect of the initialization. This output buffer must be set to NULL or JET_instanceNil. This instance handle can then be passed to any other function that uses an instance. If the engine is operating in multi-instance mode then this parameter must be set to a valid input buffer that contains the instance handle returned by the [JetCreateInstance](./jetcreateinstance-function.md) function instance that is being initialized.


#### Remarks

An instance must be initialized with a call to **JetInit** before it can be used by anything other than [JetSetSystemParameter](./jetsetsystemparameter-function.md).

An instance is destroyed by a call to the [JetTerm](./jetterm-function.md) function, even if that instance was never initialized using **JetInit**. An instance is the unit of recoverability for the database engine. It controls the life cycle of all the files used to protect the integrity of the data in a set of database files. These files include the checkpoint file and the transaction log files.

The maximum number of instances that can be created at any one time is controlled by [JET_paramMaxInstances](./resource-parameters.md), which can be configured by a call to [JetSetSystemParameter](./jetsetsystemparameter-function.md). When the database engine is initialized for the first time, **JetInit** will create an initial set of files to support that instance. These files include a checkpoint file (named \<[JET_paramBaseName](./transaction-log-parameters.md)\>.CHK), a set of reserved transaction log files (named RES1.LOG and RES2.LOG), an initial transaction log file (named \<[JET_paramBaseName](./transaction-log-parameters.md)\>.LOG), and a temporary database file (named according to [JET_paramTempPath](./temporary-database-parameters.md)). If [JET_paramRecovery](./transaction-log-parameters.md) is set to "Off" then the checkpoint file and log files will not be created. If [JET_paramMaxTemporaryTables](./temporary-database-parameters.md) is set to zero then the temporary database file will not be created. These files represent the on disk footprint of an instance and must be managed with care. If these files are corrupted individually or with respect to one another then the data stored in the databases associated with the instance may be lost.

When the database engine is initialized with an existing set of transaction log files then those files will be inspected to see if the previous incarnation of the instance suffered from a crash. If a crash is detected then crash recovery will automatically be performed. This process will reconstruct the databases attached to the instance during the previous incarnation of the engine and save the changes back to the database files. The result will be databases that are transaction consistent. It is possible for this process to take quite some time if the number of transaction log files to replay against the databases is large.

Due to the fact that **JetInit** performs crash recovery, it is possible for almost any database engine error to be returned in the event of a failure. In practice, most of the errors seen in deployment fall into two categories: data corruption and file mismanagement. Data corruption will manifest itself most often in the following or similar errors:

  - JET_errReadVerifyFailure

  - JET_errLogFileCorrupt

  - JET_errCheckpointCorrupt

These errors are almost always caused by hardware problems and thus cannot be avoided. File mismanagement will manifest itself most often in the following or similar errors:

  - JET_errMissingLogFile

  - JET_errAttachedDatabaseMismatch

  - JET_errDatabaseSharingViolation

  - JET_errInvalidLogSequence

If recovery is running on a set of logs, for which not all databases is present (which will return the error JET_errAttachedDatabaseMismatch under normal circumstances), and the client wishes recovery to continue despite missing databases, the JET_ bitReplayIgnoreMissingDB can be used to continue recovery for the available databases. These errors are preventable by the application. The application must be careful to protect the repository of these files from manipulation by outside forces such as the user or other applications. If the application desires to destroy an instance entirely then all the files associated with the instance must be deleted. These include the checkpoint file, the transaction log files, and any database files attached to the instance.

The **JetInit** function behaves differently, with respect to database files attached to the instance, between Windows 2000 and later releases.

**Windows 2000:**  In Windows 2000, any database attached to the instance during a previous incarnation of that instance remains attached to the instance after **JetInit** completes successfully. It is not necessary to call [JetAttachDatabase](./jetattachdatabase-function.md) after **JetInit** to insure later database access. If the [JetAttachDatabase](./jetattachdatabase-function.md) function is called after the **JetInit** function, the JET_wrnDatabaseAttached warning will be returned. This warning indicates that the database attachment was preserved and can be ignored.

**Windows XP:**  In Windows XP and later releases, all databases are automatically detached from the instance by **JetInit**. This means that [JetAttachDatabase](./jetattachdatabase-function.md) must always be called after **JetInit** in this case.

Any application written to run on Windows 2000 and on later releases must always call [JetAttachDatabase](./jetattachdatabase-function.md) after **JetInit**. If the application runs on Windows 2000 then it must expect to see JET_wrnDatabaseAttached in some cases. See [JetAttachDatabase](./jetattachdatabase-function.md) for more information.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_paramMaxTemporaryTables](./temporary-database-parameters.md)  
[JET_paramRecovery](./transaction-log-parameters.md)  
[JetAttachDatabase](./jetattachdatabase-function.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit3](./jetinit3-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
