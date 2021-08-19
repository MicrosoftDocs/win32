---
description: "Learn more about: JetGetErrorInfoW Function"
title: JetGetErrorInfoW Function
TOCTitle: JetGetErrorInfoW Function
ms:assetid: 7a84f937-7a16-434e-896d-789f316ee833
ms:mtpsurl: https://msdn.microsoft.com/library/Hh475859(v=EXCHG.10)
ms:contentKeyID: 37033565
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetErrorInfoW
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetGetErrorInfoW Function


_**Applies to:** Windows | Windows Server_

## JetGetErrorInfoW Function

The **JetGetErrorInfoW** function BAS_ of the database engine.

Note: This documentation is based on a preliminary release of the Extensible Storage Engine. This information is subject to change.

```cpp
JET_ERR JET_API JetGetErrorInfoW( 
    _In_opt_ void *                      pvContext, 
    _Out_writes_bytes_( cbMax ) void *   pvResult, 
    _In_ unsigned long                   cbMax, 
    _In_ unsigned long                   InfoLevel, 
    _In_ JET_GRBIT                       grbit );
```

### Parameters

*pvContext*

The context or error value for which the extended error information is needed. The value passed in depends on the *InfoLevel* parameter value.

*pvResult*

A pointer to a buffer that will receive the information. The type of the buffer depends on the *InfoLevel* parameter value. The caller must be configured to align the buffer appropriately.

*cbMax*

The maximum size of the *pvResult* structure that is passed in.

*InfoLevel*

The type of information that will be retrieved for the error info/context is specified by the *pvContext* parameter. The format of the data that is stored in *pvResult* is dependent on *InfoLevel*.

The following table lists the possible values for this parameter.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_ErrorInfoSpecificErr</p> | <p><em>pvContext</em> is interpreted as a <a href="gg269297(v=exchg.10).md">JET_ERR</a>/error code, <em>pvResult</em> is interpreted as a <a href="hh475861(v=exchg.10).md">JET_ERRINFOBASIC_W</a>, and the fields of the <a href="hh475861(v=exchg.10).md">JET_ERRINFOBASIC_W</a> structure are filled in appropriately.</p> | 



*grbit*

Reserved.

### Return Value

This function returns the [JET_ERR](./extensible-storage-engine-error-codes.md) data type with one of the return codes listed in the following table. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contains an unexpected value or contains a value that does not make sense when combined with the value of another parameter. This can happen for <strong>JetGetErrorInfo</strong> when the following occurs:</p><ul><li><p>The specified <em>InfoLevel</em> parameter value is invalid.</p></li><li><p>The specified <em>grbit</em> value is invalid.</p></li><li><p>The specified <em>pvResult</em> parameter buffer’s <em>cbMax</em> value is less than the required size for output of this <em>InfoLevel</em> parameter.</p></li><li><p>For <em>InfoLevel</em> = JET_ErrorInfoSpecificErr, the <a href="gg294092(v=exchg.10).md">JET_ERR</a> value passed in is unknown to the engine.</p></li></ul> | 
| <p>JET_errDisabledFunctionality</p> | <p>If this SKU of windows doesn’t support this function, this error will be returned.</p> | 



On success, the output buffer that is appropriate for the requested error context/value will be set to the extended error info requested.

On failure, the state of the output buffers will be undefined.

### Remarks

The [JET_ERRINFOBASIC_W](./jet-errinfobasic-w-structure.md) function and [JET_ERRCAT](./jet-errcat.md) group of constants contain documentation about the extended error information that is returned for *InfoLevel* = JET_ErrorInfoSpecificErr.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows 8 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Note: Only the <strong>JetGetErrorInfoW</strong> (Unicode) is implemented. This API does not have an A (ANSI) version.</p> | 

