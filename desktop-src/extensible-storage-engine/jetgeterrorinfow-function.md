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
<td><p>JET_ErrorInfoSpecificErr</p></td>
<td><p><em>pvContext</em> is interpreted as a <a href="gg269297(v=exchg.10).md">JET_ERR</a>/error code, <em>pvResult</em> is interpreted as a <a href="hh475861(v=exchg.10).md">JET_ERRINFOBASIC_W</a>, and the fields of the <a href="hh475861(v=exchg.10).md">JET_ERRINFOBASIC_W</a> structure are filled in appropriately.</p></td>
</tr>
</tbody>
</table>


*grbit*

Reserved.

### Return Value

This function returns the [JET_ERR](./extensible-storage-engine-error-codes.md) data type with one of the return codes listed in the following table. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

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
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contains an unexpected value or contains a value that does not make sense when combined with the value of another parameter. This can happen for <strong>JetGetErrorInfo</strong> when the following occurs:</p>
<ul>
<li><p>The specified <em>InfoLevel</em> parameter value is invalid.</p></li>
<li><p>The specified <em>grbit</em> value is invalid.</p></li>
<li><p>The specified <em>pvResult</em> parameter buffer’s <em>cbMax</em> value is less than the required size for output of this <em>InfoLevel</em> parameter.</p></li>
<li><p>For <em>InfoLevel</em> = JET_ErrorInfoSpecificErr, the <a href="gg294092(v=exchg.10).md">JET_ERR</a> value passed in is unknown to the engine.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>JET_errDisabledFunctionality</p></td>
<td><p>If this SKU of windows doesn’t support this function, this error will be returned.</p></td>
</tr>
</tbody>
</table>


On success, the output buffer that is appropriate for the requested error context/value will be set to the extended error info requested.

On failure, the state of the output buffers will be undefined.

### Remarks

The [JET_ERRINFOBASIC_W](./jet-errinfobasic-w-structure.md) function and [JET_ERRCAT](./jet-errcat.md) group of constants contain documentation about the extended error information that is returned for *InfoLevel* = JET_ErrorInfoSpecificErr.

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows 8.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows 8 Server.</p></td>
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
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Note: Only the <strong>JetGetErrorInfoW</strong> (Unicode) is implemented. This API does not have an A (ANSI) version.</p></td>
</tr>
</tbody>
</table>
