---
description: "Learn more about: JetRetrieveColumn Function"
title: JetRetrieveColumn Function
TOCTitle: JetRetrieveColumn Function
ms:assetid: 1e55063f-6033-4416-a9a6-894032fed069
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269198(v=EXCHG.10)
ms:contentKeyID: 32765501
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetRetrieveColumn
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetRetrieveColumn Function


_**Applies to:** Windows | Windows Server_

## JetRetrieveColumn Function

The **JetRetrieveColumn** function retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record. In addition to retrieving the actual column value, **JetRetrieveColumn** can also be used to retrieve the size of a column, before retrieving the column data itself so that application buffers can be sized appropriately.

```cpp
    JET_ERR JET_API JetRetrieveColumn(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          JET_COLUMNID columnid,
      __out_opt     void* pvData,
      __in          unsigned long cbData,
      __out_opt     unsigned long* pcbActual,
      __in          JET_GRBIT grbit,
      __in_out_opt  JET_RETINFO* pretinfo
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*columnid*

The [JET_COLUMNID](./jet-columnid.md) of the column to retrieve.

A *columnid* value of 0 (zero) can be given which does not itself refer to any individual column. When *columnid* 0 (zero) is given, all tagged columns, sparse, and multi-valued columns are treated as a single column. This facilitates retrieving all sparse columns that are present in a record.

*pvData*

The output buffer that receives the column value.

*cbData*

The maximum size, in bytes, of the output buffer.

*pcbActual*

Receives the actual size, in bytes, of the column value.

If this parameter is **NULL**, then the actual size of the column value will not be returned.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following:


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitRetrieveCopy</p> | <p>This flag causes retrieve column to retrieve the modified value instead of the original value. If the value has not been modified, then the original value is retrieved. In this way, a value that has not yet been inserted or updated may be retrieved during the operation of inserting or updating a record.</p> | 
| <p>JET_bitRetrieveFromIndex</p> | <p>This option is used to retrieve column values from the index, if possible, without accessing the record. In this way, unnecessary loading of records can be avoided when needed data is available from index entries themselves. In cases where the original column value cannot be retrieved from the index, because of irreversible transformations or data truncation, the record will be accessed and the data retrieved as normal. This is a performance option and should only be specified when it is likely that the column value can be retrieved from the index. This option should not be specified if the current index is the clustered index, since the index entries for the clustered, or primary, index are the records themselves. This bit cannot be set if JET_bitRetrieveFromPrimaryBookmark is also set.</p> | 
| <p>JET_bitRetrieveFromPrimaryBookmark</p> | <p>This option is used to retrieve column values from the index bookmark, and may differ from the index value when a column appears both in the primary index and the current index. This option should not be specified if the current index is the clustered, or primary, index. This bit cannot be set if JET_bitRetrieveFromIndex is also set.</p> | 
| <p>JET_bitRetrieveTag</p> | <p>This option is used to retrieve the sequence number of a multi-valued column value in pretinfo-&gt;itagSequence. The itagSequence field is commonly an input for retrieving multi-valued column values from a record. However, when retrieving values from an index, it is also possible to associate the index entry with a particular sequence number and retrieve this sequence number as well. Retrieving the sequence number can be a costly operation and should only be done if necessary.</p> | 
| <p>JET_bitRetrieveNull</p> | <p>This option is used to retrieve multi-valued column <strong>NULL</strong> values. If this option is not specified, multi-valued column <strong>NULL</strong> values will automatically be skipped.</p> | 
| <p>JET_bitRetrieveIgnoreDefault</p> | <p>This option affects only multi-valued columns and causes a <strong>NULL</strong> value to be returned when the requested sequence number is 1 and there are no set values for the column in the record.</p> | 
| <p>JET_bitRetrieveLongId</p> | <p>This flag is for internal use only and is not intended to be used in your application.</p> | 
| <p>JET_bitRetrieveLongValueRefCount</p> | <p>This flag is for internal use only and is not intended to be used in your application.</p> | 
| <p>JET_bitRetrieveTuple</p> | <p>This flag will allow the retrieval of a tuple segment of the index. This bit must be specified with JET_bitRetrieveFromIndex.</p> | 



*pretinfo*

If *pretinfo* is give as **NULL** then the function behaves as though an *itagSequence* of 1 and an *ibLongValue* of 0 (zero) were given. This causes column retrieval to retrieve the first value of a multi-valued column, and to retrieve long data at offset 0 (zero).

This parameter is used to provide one or more of the following:


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>ibLongValue</p> | <p>Gives a binary offset into a long column value when retrieving a portion of a column value.</p> | 
| <p>itagSequence</p> | <p>Gives the sequence number of the desired multi-valued column value. Note that this field is only set if the JET_bitRetrieveTag is specified. Otherwise, it is unmodified.</p> | 
| <p>columnidNextTagged</p> | <p>Returns the column ID of the returned column value when retrieving all tagged, sparse and multi-valued, columns using passing <em>columnid</em> of 0 (zero).</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBadColumnId</p> | <p>The column ID given is outside the legal limits of a column ID.</p> | 
| <p>JET_errBadItagSequence</p> | <p>An invalid multi-valued column sequence number value has been passed in pretinfo-&gt;itagSequence. Valid values for the multi-valued column value sequence numbers are 1 or greater. A value of 0 (zero) is invalid for this function.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errColumnNotFound</p> | <p>The column described by the given <em>columnid</em> does not exist in the table.</p> | 
| <p>JET_errIndexTuplesCannotRetrieveFromIndex</p> | <p>Columns indexed as substrings cannot be retrieved from the index, since only a small portion of the column is typically present in each index entry.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidBufferSize</p> | <p>In some cases, the buffer given for the retrieve column must be sufficiently sized in order to return any amount of the column value. For example, escrow updatable columns are adjusted to be consistent for the transactional context of the calling session and this adjustment requires the buffer provided by the caller. If insufficient buffer space is supplied, then JET_errInvalidBufferSize is returned and no column data whatsoever is returned.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One or more of the parameters given is incorrect. This can happen if the retinfo.cbStruct is smaller that the size of <a href="gg294049(v=exchg.10).md">JET_RETINFO</a>.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>The options supplied are unknown or an illegal combination of known bit settings.</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>The cursor is not positioned on a record. This can happen for many different reasons. For example, this will happen if the cursor is currently positioned after the last record on the current index.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_wrnBufferTruncated</p> | <p>The entire column value could not be retrieved because the given buffer is smaller than the size of the column.</p> | 
| <p>JET_wrnColumnNull</p> | <p>The column value retrieved is <strong>NULL</strong>.</p> | 



On success, the column value for the given column, is copied into the given buffer. Less than all of the column value is copied with the warning JET_wrnBufferTruncated is returned. If the *pcbActual* was given, the actual size of the column value is returned. Note that **NULL** values have 0 (zero) length and will thus set the returned size to 0 (zero). If the column retrieved was a multi-valued column, and *pretinfo* was given, and JET_bitReturnTag was set as an option, then the sequence number of the column value is returned in pretinfo-\>itagSequence.

On failure, the cursor location is left unchanged and no data is copied into the provided buffer.

#### Remarks

This call is used just once to retrieve data of fixed or known size for non-multi-valued columns. However, when column data is of unknown size, this call is typically used twice. It is called first to determine the size of the data so it can allocate the necessary storage space. Then, the same call is made again to retrieve the column data. When the actual number of values is unknown, because a column is multi-valued, the call is typically used three times. First to get the number of values and then twice more to allocate storage and retrieve the actual data.

Retrieving all the values for a multi-valued column can be done by repeatedly calling this function with a pretinfo-\>itagSequence value beginning at 1 and increasing on each subsequent call. The last column value is known to be retrieved when a JET_wrnColumnNull is returned from the function. Note that this method cannot be done if the multi-value column has explicit **NULL** values set in its value sequence, since these values would be skipped. If an application desires to retrieve all multi-valued column values, including those explicitly set to **NULL**, then [JetRetrieveColumns](./jetretrievecolumns-function.md) must be used instead of **JetRetrieveColumn**. Note that this function does not return the number of values for a multi-valued function when an *itagSequence* value of 0 (zero) is given. Only [JetRetrieveColumns](./jetretrievecolumns-function.md) will return the number of values of a column value when an *itagSequence* value of 0 (zero) is passed.

If this function is called at transaction level 0 (zero), for example, the calling session is not itself in a transaction, then a transaction is opened and closed within the function. The purpose of this is to return consistent results in the case that a long value spans database pages. Note that the transaction is released between function calls and a series of calls to this function when the session is not in a transaction may return data updated after the first call to this function.

The default column value will be retrieved when the column has not been set explicitly to another value, unless the JET_bitRetrieveIgnoreDefault option is set.

Retrieving the autoincrement column value from the copy buffer prior to insert is a common means of identifying a record uniquely for linkage when inserting normalized data into multiple tables. The autoincrement value is allocated when the insert operation begins and can be retrieved from the copy buffer at any time until the update is complete.

When retrieving all tagged, multi-valued, and sparse columns, by setting *columnid* to 0 (zero), columns are retrieved in *columnid* order from lowest *columnid* to highest *columnid*. The same order of column values is returned each time column values are retrieved. The order is deterministic.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_RETINFO](./jet-retinfo-structure.md)  
[JetSetColumn](./jetretrievekey-function.md)  
[JetRetrieveColumns](./jetretrievecolumns-function.md)
