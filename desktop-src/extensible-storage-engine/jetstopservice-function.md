---
description: "Learn more about: JetStopService Function"
title: JetStopService Function
TOCTitle: JetStopService Function
ms:assetid: 46aeb9ed-ee72-49cc-99e3-791a51a55b02
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269240(v=EXCHG.10)
ms:contentKeyID: 32765542
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetStopService
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

# JetStopService Function


_**Applies to:** Windows | Windows Server_

## JetStopService Function

The **JetStopService** function prepares an instance for termination.

**JetStopService** is the legacy call when only one instance is allowed. In this case, the only active instance is the one being prepared for termination.

```cpp
    JET_ERR JET_API JetStopService(void);
```

### Parameters

This function has no parameters.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errRunningInMultiInstanceMode</p> | <p>It is not clear which instance to prepare for termination when using <strong>JetStopService</strong> with multiple instance mode.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 



If this function succeeds, it prepares for a future termination. The steps taken to prepare for a termination include the following:

  - Stop online defragmentation if it is running.

  - Start a version store clean-up.

  - Reduce the checkpoint depth by starting to flush dirty pages in the buffer manager.

  - Prevent future calls to most functions for that instance.

If this function fails, none of the steps to prepare for an instance termination will be taken, so no change to the instance state will occur.

#### Remarks

This function reduces the work the instance will have to do when terminated, but will not terminate the instance. As a result, this function is just an optimization and is not mandatory to use. Note that the amount of work done in preparation was less in Windows 2000 and Windows XP. Once the function succeeds, calling functions that are no longer allowed will return JET_errClientRequestToStopJetService. Functions that are still allowed after this call are: [JetRollback](./jetrollback-function.md), [JetCloseTable](./jetclosetable-function.md), [JetEndSession](./jetendsession-function.md), [JetCloseDatabase](./jetclosedatabase-function.md), [JetDetachDatabase](./jetdetachdatabase-function.md) and [JetResetSessionContext](./jetresetsessioncontext-function.md).

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetCloseDatabase](./jetclosedatabase-function.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetDetachDatabase](./jetdetachdatabase-function.md)  
[JetEndSession](./jetendsession-function.md)  
[JetResetSessionContext](./jetresetsessioncontext-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetTerm](./jetterm-function.md)  
[JetTerm2](./jetterm2-function.md)
