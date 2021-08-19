---
description: "Learn more about: JetGetInstanceMiscInfo Function"
title: JetGetInstanceMiscInfo Function
TOCTitle: JetGetInstanceMiscInfo Function
ms:assetid: 0bfe36fe-4ddd-442b-b934-57a7bfb28e5f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269183(v=EXCHG.10)
ms:contentKeyID: 32765486
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetInstanceMiscInfo
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

# JetGetInstanceMiscInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetInstanceMiscInfo Function

The **JetGetInstanceMiscInfo** function retrieves information about the instance, while the instance is online.

**Windows Vista:  JetGetInstanceMiscInfo** is introduced in Windows Vista.

```cpp
    JET_ERR JET_API JetGetInstanceMiscInfo(
      __in          JET_INSTANCE instance,
      __out         void* pvResult,
      __in          unsigned long cbMax,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*instance*

Identifies the database instance that will be used for the API call.

*pvResult*

Pointer to a buffer that will receive the information. The type of the buffer is dependent on *InfoLevel*. The caller is responsible for aligning the buffer appropriately.

*cbMax*

The size, in bytes, of the buffer passed in *pvResult*.

*InfoLevel*

Determines what type of information will be retrieved for the instance specified by *instance*. The format of the data stored in *pvResult* is dependent on *InfoLevel*.

The following options are available for use with this parameter.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_InstanceMiscInfoLogSignature</p> | <p><em>pvResult</em> is interpreted as a <a href="gg269340(v=exchg.10).md">JET_SIGNATURE</a> structure of the transaction log sequence associated with this instance.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBufferTooSmall</p> | <p>The buffer was too small.</p> | 
| <p>JET_errInvalidParameter</p> | <p>Either an invalid <a href="gg294048(v=exchg.10).md">JET_INSTANCE</a> or an invalid <em>InfoLevel</em> was specified.</p> | 



#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_SIGNATURE](./jet-signature-structure.md)
