---
description: "Learn more about: JetFreeBuffer Function"
title: JetFreeBuffer Function
TOCTitle: JetFreeBuffer Function
ms:assetid: f37d35f6-4bea-46ba-a334-7b8ad7a1568c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294134(v=EXCHG.10)
ms:contentKeyID: 32765748
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetFreeBuffer
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

# JetFreeBuffer Function


_**Applies to:** Windows | Windows Server_

## JetFreeBuffer Function

The **JetFreeBuffer** function frees memory that was allocated by a database engine call.

**Windows XP:  JetFreeBuffer** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetFreeBuffer(
      __in          char* pbBuf
    );
```

### Parameters

*pbBuf*

Pointer to a region of memory that was previously allocated by a call to the database engine. **NULL** is acceptable, and will be ignored.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 



#### Remarks

It is undefined behavior to pass memory that was not allocated by the database engine in to *pbBuf*.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JetGetInstanceInfo](./jetgetinstanceinfo-function.md)
