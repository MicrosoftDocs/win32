---
description: "Learn more about: JetPrereadIndexRanges Function"
title: JetPrereadIndexRanges Function
TOCTitle: JetPrereadIndexRanges Function
ms:assetid: ab49abcc-eaeb-438f-8e6d-b08bc94d7bc3
ms:mtpsurl: https://msdn.microsoft.com/library/JJ835045(v=EXCHG.10)
ms:contentKeyID: 49894667
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
- JetPrereadIndexRanges
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetPrereadIndexRanges Function


_**Applies to:** Windows | Windows Server_

The **JetPrereadIndexRanges** function prereads indexes to improve the performance.

The **JetPrereadIndexRanges** function was introduced in the Windows 8 operating system.

``` c++
JET_ERR JetPrereadIndexRanges(
  __in          const JET_SESID sesid,
  __in          const JET_TABLEID tableid,
  __in_ecount(cIndexRanges)  const JET_INDEX_RANGE* const rgIndexRanges,
  __in          const unsigned long cIndexRanges,
  __out_opt     unsigned long* const pcRangesPreread,
  __in_ecount(ccolumnidPreread)  const JET_COLUMNID* const rgcolumnidPreread,
  __in          const unsigned long ccolumnidPreread,
  __in          const JET_GRBIT grbit
);
```

### Parameters

*sesid*

The database session context to use for the API call.

*tableid*

The table to issue the prereads against.

*rgIndexRanges*

The key ranges to preread.

*cIndexRanges*

The number of key ranges to preread, determined by the number of elements in *rgIndexRanges*.

*pcRangesPreread*

The number of key ranges that were actually preread.

*rgcolumnidPreread*

List of column IDs for long value columns to preread. By default, only the on-page record is preread. If Off-page long value columns need to be preread, their column IDs need to be passed via this parameter.

*ccolumnidPreread*

The number of column IDs for long value columns to preread, determined by the number of elements in *rgcolumnidPreread*.

*grbit*

A group of bits that specifies zero or more of the preread direction values listed in the following table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>Forward</p> | <p>Preread forward.</p> | 
| <p>Backwards</p> | <p>Preread backward.</p> | 
| <p>FirstPageOnly</p> | <p>Preread only the first page of any long column.</p> | 
| <p>NormalizedKey</p> | <p>Normalized key/bookmark provided instead of column value.</p> | 



### Return value

This function returns the [JET_ERR](./jet-err.md) data type with one of the return codes listed in the following table. For more information about the possible Extensible Storage Engine (ESE) errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 



#### Remarks

If the records with the specified key ranges are not in the buffer cache, you should start asynchronous reads to bring the records into the database buffer cache.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2012.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See also

[JET_ERR](./jet-err.md)
