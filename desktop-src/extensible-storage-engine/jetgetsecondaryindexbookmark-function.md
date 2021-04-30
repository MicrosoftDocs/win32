---
description: "Learn more about: JetGetSecondaryIndexBookmark Function"
title: JetGetSecondaryIndexBookmark Function
TOCTitle: JetGetSecondaryIndexBookmark Function
ms:assetid: 6953eda4-9420-4814-80f4-eb9e3e5540d8
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269285(v=EXCHG.10)
ms:contentKeyID: 32765577
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetSecondaryIndexBookmark
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

# JetGetSecondaryIndexBookmark Function


_**Applies to:** Windows | Windows Server_

## JetGetSecondaryIndexBookmark Function

The **JetGetSecondaryIndexBookmark** function retrieves a special bookmark for the secondary index entry at the current position of a cursor. This bookmark can then be used to efficiently reposition that cursor back to the same index entry using [JetGotoSecondaryIndexBookmark](./jetgotosecondaryindexbookmark-function.md). This is most useful when repositioning on a secondary index that contains duplicate keys or that contains multiple index entries for the same record.

**Windows XP:  JetGetSecondaryIndexBookmark** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetGetSecondaryIndexBookmark(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out_opt     void* pvSecondaryKey,
      __in          unsigned long cbSecondaryKeyMax,
      __out_opt     unsigned long* pcbSecondaryKeyActual,
      __out_opt      void* pvPrimaryBookmark,
      __in          unsigned long cbPrimaryBookmarkMax,
      __out_opt     unsigned long* pcbPrimaryKeyActual,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pvSecondaryKey*

The output buffer that receives the secondary key.

*cbSecondaryKeyMax*

The maximum size, in bytes, of the output buffer for the secondary key.

*pcbSecondaryKeyActual*

Receives the actual size in bytes of the secondary key.

If this parameter is NULL, the actual size of the secondary key will not be returned.

If the output buffer is too small, the actual size of the secondary key will still be returned. That means that this number will be larger than the size of the output buffer.

*pvPrimaryBookmark*

The output buffer that receives the primary key bookmark.

*cbPrimaryBookmarkMax*

The maximum size, in bytes, of the output buffer for the primary key bookmark.

*pcbPrimaryKeyActual*

Receives the actual size, in bytes, of the primary key bookmark.

If this parameter is NULL then the actual size of the primary key bookmark will not be returned.

If the output buffer is too small, the actual size of the primary key bookmark will still be returned. That means that this number will be larger than the size of the output buffer.

*grbit*

Reserved for future use.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

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
<td><p>JET_errBufferTooSmall</p></td>
<td><p>The operation completed successfully, but one of the output buffers was too small to receive the requested data.</p>
<p>The output buffer has been filled with as much of the bookmark as would fit. The actual size of the bookmark has also been returned, if requested.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNoCurrentIndex</p></td>
<td><p>The cursor is not currently on a secondary index.</p>
<p>It is not meaningful to retrieve a secondary index bookmark when the cursor is not currently using a secondary index. <a href="gg269221(v=exchg.10).md">JetGetBookmark</a> should be used when the cursor is not on a secondary index.</p></td>
</tr>
<tr class="even">
<td><p>JET_errNoCurrentRecord</p></td>
<td><p>The cursor is not positioned on a record.</p>
<p>This can happen for many different reasons. For example, this will happen if the cursor is currently positioned after the last record on the current index.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errSessionSharingViolation</p></td>
<td><p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
</tbody>
</table>


On success, the secondary index bookmark for the index entry at the current position of a cursor will be returned in the output buffers. No change to the database state will occur.

On failure, the state of the output buffers and the actual size of the secondary index bookmark will be undefined unless JET_errBufferTooSmall was returned. In the event that JET_errBufferTooSmall is returned, the output buffers will contain as much of the secondary index bookmark as will fit in the space provided and the actual size of the secondary index bookmark will be accurate. In any case, no change to the database state will occur.

#### Remarks

Bookmarks should generally be treated as opaque chunks of data. No attempt should be made to exploit the internal structure of this data. However, the following properties can be known about all ESENT bookmarks:

  - A bookmark uniquely identifies a record in a given table.

  - The bookmark of a record will not change for the lifetime of that record.

  - The bookmark of a record is the same as the key of that record on the primary index over the table containing that record. If no primary index is defined over that table, the database engine will create its own bookmark for the record.

  - Bookmarks may be compared against each other using [memcmp](/previous-versions/visualstudio/visual-studio-6.0/aa246467(v=vs.60)) to establish their relative ordering in the primary index over the table of the source records. If no primary index is defined over that table, the relative ordering of bookmarks from that table is not meaningful.

  - It is meaningless to compare bookmarks of records from different tables against each other.

  - A bookmark is always less than or equal to JET_cbBookmarkMost (256) bytes in length prior to Windows Vista. On Windows Vista and later releases, bookmarks can be larger. The maximum size of a bookmark is equal to the current value of JET_paramKeyMost + 1.

Keys should generally be treated as opaque chunks of data. No attempt should be made to exploit the internal structure of this data. However, the following properties can be known about all ESENT keys:

  - Keys may be compared against each other using [memcmp](/previous-versions/visualstudio/visual-studio-6.0/aa246467(v=vs.60)) to establish their relative ordering in the originating index over the table of the source index entries.

  - It is meaningless to compare keys of index entries from different indexes against each other.

  - A key is always less than or equal to JET_cbKeyMost (255) bytes in length prior to Windows Vista. On Windows Vista and later releases, keys can be larger. The maximum size of a key is equal to the current value of JET_paramKeyMost.

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

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetBookmark](./jetgetbookmark-function.md)  
[JetGotoSecondaryIndexBookmark](./jetgotosecondaryindexbookmark-function.md)  
[JetRetrieveKey](./jetretrievekey-function.md)  
[memcmp](/previous-versions/visualstudio/visual-studio-6.0/aa246467(v=vs.60))
