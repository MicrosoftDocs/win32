---
description: "Learn more about: JetConfigureProcessForCrashDump Function"
title: JetConfigureProcessForCrashDump Function
TOCTitle: JetConfigureProcessForCrashDump Function
ms.date: 05/17/2023
ms.topic: reference
api_name: 
- JetConfigureProcessForCrashDump
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

# JetConfigureProcessForCrashDump Function


_**Applies to:** Windows | Windows Server_

## JetConfigureProcessForCrashDump Function

The **JetConfigureProcessForCrashDump** function configures crash dump options for Watson..

```cpp
    JET_ERR JET_API JetConfigureProcessForCrashDump(
    _In_ const JET_GRBIT grbit )
```

### Parameters

*grbit*

A [JET_GRBIT](jet-grbit.md) representing crash dump options.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInternalError</p> | <p>An internal error occured</p> | 



#### Remarks



#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also


