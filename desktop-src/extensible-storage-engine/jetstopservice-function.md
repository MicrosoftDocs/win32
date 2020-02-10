---
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

This function returns the [JET_ERR](gg294092\(v=exchg.10\).md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

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
<td><p>JET_errRunningInMultiInstanceMode</p></td>
<td><p>It is not clear which instance to prepare for termination when using <strong>JetStopService</strong> with multiple instance mode.</p>
<p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p></td>
</tr>
</tbody>
</table>


If this function succeeds, it prepares for a future termination. The steps taken to prepare for a termination include the following:

  - Stop online defragmentation if it is running.

  - Start a version store clean-up.

  - Reduce the checkpoint depth by starting to flush dirty pages in the buffer manager.

  - Prevent future calls to most functions for that instance.

If this function fails, none of the steps to prepare for an instance termination will be taken, so no change to the instance state will occur.

#### Remarks

This function reduces the work the instance will have to do when terminated, but will not terminate the instance. As a result, this function is just an optimization and is not mandatory to use. Note that the amount of work done in preparation was less in Windows 2000 and Windows XP. Once the function succeeds, calling functions that are no longer allowed will return JET_errClientRequestToStopJetService. Functions that are still allowed after this call are: [JetRollback](gg269273\(v=exchg.10\).md), [JetCloseTable](gg294087\(v=exchg.10\).md), [JetEndSession](gg294054\(v=exchg.10\).md), [JetCloseDatabase](gg294123\(v=exchg.10\).md), [JetDetachDatabase](gg269266\(v=exchg.10\).md) and [JetResetSessionContext](gg269250\(v=exchg.10\).md).

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
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

[JET_ERR](gg294092\(v=exchg.10\).md)  
[JET_INSTANCE](gg294048\(v=exchg.10\).md)  
[JetCloseDatabase](gg294123\(v=exchg.10\).md)  
[JetCloseTable](gg294087\(v=exchg.10\).md)  
[JetDetachDatabase](gg269266\(v=exchg.10\).md)  
[JetEndSession](gg294054\(v=exchg.10\).md)  
[JetResetSessionContext](gg269250\(v=exchg.10\).md)  
[JetRollback](gg269273\(v=exchg.10\).md)  
[JetTerm](gg269298\(v=exchg.10\).md)  
[JetTerm2](gg269223\(v=exchg.10\).md)

