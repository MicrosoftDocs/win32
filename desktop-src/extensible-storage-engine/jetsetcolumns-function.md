---
description: "Learn more about: JetSetColumns Function"
title: JetSetColumns Function
TOCTitle: JetSetColumns Function
ms:assetid: a5b011dc-0da6-44bf-aaf5-352d8a57e5bf
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294050(v=EXCHG.10)
ms:contentKeyID: 32765649
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetColumns
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

# JetSetColumns Function


_**Applies to:** Windows | Windows Server_

## JetSetColumns Function

The **JetSetColumns** function is similar in behavior to [JetSetColumn](./jetsetcolumn-function.md) but allows an application to set multiple column values in a single operation. An array of [JET_SETCOLUMN](./jet-setcolumn-structure.md) structures is used to describe the set of column values to be set, and to describe input buffers for each column value to be set.

```cpp
    JET_ERR JET_API JetSetColumns(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in_out_opt  JET_SETCOLUMN* psetcolumn,
      __in          unsigned long csetcolumn
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*psetcolumn*

A pointer to an array of one or more [JET_SETCOLUMN](./jet-setcolumn-structure.md) structures. Each structure includes descriptions of which column value to set and from where to get column data to set.

*csetcolumn*

The number of [JET_SETCOLUMN](./jet-setcolumn-structure.md) structures in the array given by *psetcolumn*.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errBadColumnId</p> | <p>The column ID given is outside the legal limits of a column ID.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errColumnIllegalNull</p> | <p>Same as JET_errNullInvalid.</p> | 
| <p>JET_errColumnNotFound</p> | <p>The column described by the given <em>columnid</em> does not exist in the table.</p> | 
| <p>JET_errColumnNotUpdatable</p> | <p>An illegal attempt was made to update a long value during a insert copy delete original update operation.</p> | 
| <p>JET_errColumnTooBig</p> | <p>The given column value data given in the input buffer exceeds the size limitation either natural for a fixed length column or configured for fixed length text or binary columns. This error is also returned when passing more than 1024 bytes of data for a long column and setting the JET_bitSetIntrinsicLV flag.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidBufferSize</p> | <p>The given column value data size does not match what is natural for the fixed length data type.</p> | 
| <p>JET_errInvalidColumnType</p> | <p>An illegal attempt was made to update an auto-increment column either during an insert or update operation, or to update a version column during a replace operation.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>The options supplied are unknown or an illegal combination of known bit settings.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The given psetinfo-&gt;cbStruct is not a valid size for the <a href="gg294090(v=exchg.10).md">JET_SETINFO</a> structure.</p> | 
| <p>JET_errMultiValuedDuplicate</p> | <p>The set column operation attempted to create a duplicate value and specified either JET_bitSetUniqueMultiValues or JET_bitSetUniqueNormalizedMultiValues.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errNotInTransaction</p> | <p>An illegal attempt was made to update a long column value when the calling session was not in a transaction.</p> | 
| <p>JET_errNullInvalid</p> | <p>An illegal attempt was made to set a non-NULL column to NULL.</p> | 
| <p>JET_errRecordTooBig</p> | <p>The column value could not be set to the value in the input buffer because it would have caused the record to exceed its page size related size limitation. Columns of type <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a> or <a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a> can be stored separately from the remaining record data. However, other columns must be stored with the record and can cause the record size limitation to be exceeded. Even long columns require 5-bytes of space within the record as a linkage and this too can lead to JET_errRecordTooBig being returned.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errUpdateNotPrepared</p> | <p>The cursor is not currently in the process of either inserting a new record or updating an existing record.</p> | 
| <p>JET_wrnColumnMaxTruncated</p> | <p>The column value in the input buffer exceeded the maximum configured length for a variable length column and was truncated.</p> | 



On success, for each column described in the psetcolumns, the desired portion of the column value is set with data copied from the input buffer. The column data set may have been truncated if it exceeded the maximum length specified for a variable length column.

On failure, the cursor location is left unchanged and no column value data is updated in the copy buffer.

#### Remarks

If any individual set column operation returns an error then the whole **JetSetColumns** operation will return an error. Warnings, in general, are returned in the psetcolumns-\>error and not in the return code from this function. However, if the last column set has a warning, then this warning will be returned from **JetSetColumns** itself.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_SETCOLUMN](./jet-setcolumn-structure.md)  
[JetRetrieveColumns](./jetretrievecolumns-function.md)  
[JetSetColumn](./jetsetcolumn-function.md)
