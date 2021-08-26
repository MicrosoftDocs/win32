---
description: "Learn more about: JetGetVersion Function"
title: JetGetVersion Function
TOCTitle: JetGetVersion Function
ms:assetid: f25c3639-ae2b-4357-9947-563ef3df72c6
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294133(v=EXCHG.10)
ms:contentKeyID: 32765747
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetVersion
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

# JetGetVersion Function


_**Applies to:** Windows | Windows Server_

## JetGetVersion Function

The **JetGetVersion** function retrieves the version of the database engine.

```cpp
    JET_ERR JET_API JetGetVersion(
      __in          JET_SESID sesid,
      __out         unsigned long* pwVersion
    );
```

### Parameters

*sesid*

The session to use for this call.

*pwVersion*

A pointer to the version number of the database engine.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 



If this function succeeds, the version of the database engine is retrieved.

There are no known failure modes.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[Error Handling Parameters](./error-handling-parameters.md)  
[Extensible Storage Engine Errors](./extensible-storage-engine-errors.md)  
[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)
