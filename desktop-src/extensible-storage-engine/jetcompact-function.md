---
description: "Learn more about: JetCompact Function"
title: JetCompact Function
TOCTitle: JetCompact Function
ms:assetid: 6944bd61-893d-4269-869b-56590e22580a
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269284(v=EXCHG.10)
ms:contentKeyID: 32765576
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetCompactW
- JetCompactA
- JetCompact
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

# JetCompact Function


_**Applies to:** Windows | Windows Server_

## JetCompact Function

The **JetCompact** function makes a copy of an existing database. The copy is compacted to a state optimal for usage. Data in the copied data will be packed according to the measures chosen for the indexes at index create. In this way, compacted data may be stored as densely as possible. Alternatively, compacted data may reserve space for subsequent record growth or index insertions.

```cpp
    JET_ERR JET_API JetCompact(
      __in          JET_SESID sesid,
      __in          JET_PCSTR szDatabaseSrc,
      __in          JET_PCSTR szDatabaseDest,
      __in          JET_PFNSTATUS pfnStatus,
      __in_opt      JET_CONVERT* pconvert,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*szDatabaseSrc*

The source database that will be compacted.

*szDatabaseDest*

The name to use for the compacted database.

*pfnStatus*

A callback function that can be called periodically through the database compact operation to report progress.

*pconvert*

A pointer used to designate an alternative ESE DLL that can be used to read the source database, and to provide optional parameters for a **JetCompact** operation that is converting a database from an earlier to a later version format. This feature was discontinued in Windows Server 2003.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitCompactRepair</p> | <p>Used when the source database is known to be corrupt. It enables a whole set of new behaviors intended to salvage as much data as possible from the source database. <strong>JetCompact</strong> with this option set may return JET_errSuccess but not copy all of the data created in the source database. Data that was in damaged portions of the source database will be skipped.</p> | 
| <p>JET_bitCompactStats</p> | <p>Causes <strong>JetCompact</strong> to dump statistics on the source database to a file named DFRGINFO.TXT. Statistics include the name of each table in source database, number of rows in each table, total size in bytes of all rows in each table, total size in bytes of all columns of type <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a> or <a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a> that were large enough to be stored separate from the record, number of clustered index leaf pages, and the number of long value leaf pages. In addition, summary statistics including the size of the source database, destination database, time required for database compaction, temporary database space are all dumped as well.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errFeatureNotAvailable</p> | <p>A non-NULL <em>pconvert</em> pointer has been supplied but the version of ESE being used does not support the convert feature. This feature was removed in the Windows Server 2003 version of ESE.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInTransaction</p> | <p>The calling session is within a transaction. <strong>JetCompact</strong> must be called by a session outside of any transaction.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the source database is copied to the destination database. The destination database is in an optimal state, for example, all table indexes are located in adjacent logical disk space. Each index page is padded to the amount configured when the indexes were originally created in the source database. All data and metadata settings are copied with full fidelity, unless the repair option was specified. If the repair option was specified, some data from the source database may not have been copied.

On failure, the destination database may exist but is not a full copy of the source database.

#### Remarks

Compacting a database is also used to upgrade a database from an earlier version format to a more modern version. An optional parameter is *pconvert*, which contains a structure that can hold a description for an earlier version DLL to use for reading the source database format. This feature was discontinued in Windows Server 2003. Subsequent to Windows Server 2003, new versions of ESE are always able to read older versions of the database format and hence this feature is not needed.

The desired density of data after a compact operation is specified when tables and indexes are created. The density must be between 20% and 100%. If a database is primarily read and not updated, applications will set the density to 100% to reduce the number of I/O operations during query processing. However, if the data is updated frequently with operations that increase the size of data stored together with the record, or new data is frequently inserted, the application will choose a lower density so that updates will more often find needed resources available. The operation of compacting the database causes the database to be ideally laid out according to the fill chosen by the application.

Database compaction is an off-line operation. It cannot be performed while the database is in use. As a result, it is typically done as part of a build process of developing an application which delivers a data set as part of itself.

Offline database compaction touches every bit of data in a database and can be used as a means of checking the consistency of a database. If a database is suspect then it can be compacted. If no error is found from compaction then it will be known that the database is in a valid state for ESE.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetCompactW</strong> (Unicode) and <strong>JetCompactA</strong> (ANSI).</p> | 



#### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JetDefragment](./jetdefragment-function.md)  
[JetStopService](./jetstopservice-function.md)
