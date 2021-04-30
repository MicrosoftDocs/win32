---
description: "Learn more about: JetTerm2 Function"
title: JetTerm2 Function
TOCTitle: JetTerm2 Function
ms:assetid: 36464e24-1cc0-4cda-9d7a-f64555c622bf
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269223(v=EXCHG.10)
ms:contentKeyID: 32765525
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetTerm2
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetTerm2 Function


_**Applies to:** Windows | Windows Server_

## JetTerm2 Function

The **JetTerm2** function initiates the shutdown of an instance that has been initialized by [JetInit](./jetinit-function.md).

**JetTerm2** can also destroy an uninitialized instance that was created by [JetCreateInstance](./jetcreateinstance-function.md).

```cpp
    JET_ERR JET_API JetTerm2(
      __in          JET_INSTANCE instance,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*instance*

The instance to use for this call.

**Windows 2000:**  This parameter is ignored and should always be **NULL**.

**Windows XP and later releases:**  This parameter is overloaded. If the engine is operating in legacy mode (Windows 2000 compatibility mode) where only one instance is supported, then this parameter might be **NULL** or might contain the actual instance that is returned by [JetInit](./jetinit-function.md). If the engine is operating in multi-instance mode, then this parameter must be a pointer to an instance that was created using [JetCreateInstance](./jetcreateinstance-function.md).

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following values.

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
<td><p>JET_bitTermComplete</p></td>
<td><p>Requests that the instance be shut down cleanly. Any optional cleanup work that would ordinarily be done in the background at run time is completed immediately.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitTermAbrupt</p></td>
<td><p>Requests that the instance be shut down as quickly as possible. Any optional work that would ordinarily be done in the background at run time is abandoned.</p>
<p><strong>Note</strong>  This option can cause temporary or permanent space loss in the database. This lost space can always be recovered through an offline defragmentation of the database.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitTermStopBackup</p></td>
<td><p>Requests that the instance be shut down even if there is currently a backup in progress. Ordinarily, a pending backup would cause <a href="gg269298(v=exchg.10).md">JetTerm</a> to fail with JET_errBackupInProgress. When this parameter is not present, its value is presumed to be JET_bitTermAbrupt.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitTermDirty</p></td>
<td><p>Requests that the instance be shut down with all the attached databases left in a dirty state.</p>
<p>Windows 7: JET_bitTermDirty is introduced in Windows 7.</p></td>
</tr>
</tbody>
</table>


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
<td><p>JET_errBackupInProgress</p></td>
<td><p>The operation cannot complete because a backup operation is in progress on the instance.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters that was provided contained an unexpected value, or the combination of several parameters yielded an unexpected result. This error will be returned by <a href="gg269298(v=exchg.10).md">JetTerm</a> when the engine is in multi-instance mode and when <em>pinstance</em> refers to an invalid instance.</p>
<p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>JET_errNotInitialized</p></td>
<td><p>The operation cannot complete because the instance has not yet been initialized.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTermInProgress</p></td>
<td><p>The operation cannot complete because the instance is being shut down.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTooManyActiveUsers</p></td>
<td><p>The instance cannot be shut down because there are currently sessions with active transactions for the specified instance. This error occurs only if the JET_bitTermComplete is used.</p></td>
</tr>
</tbody>
</table>


If this function succeeds, the specified instance will be shut down. The instance handle will also be closed and made unavailable to any API that takes an instance handle. All other objects that are associated with the instance, such as sessions, will also be closed. The state of the checkpoint file, transaction log files, and the database files attached to the instance will be modified during the shutdown process.

If this function fails as a result of a usage error, then the instance remains in an initialized state and nothing changes. Otherwise, the instance is still shut down as stated for the success case. The difference is that the instance will need to go through crash recovery when it is next initialized. The engine will try to flush as much data as possible to minimize the amount of recovery that is required. Conceptually, such a failure of [JetTerm](./jetterm-function.md) is no different than a process crash.

#### Remarks

See [JetTerm](./jetterm-function.md).

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

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JetInit](./jetinit-function.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetTerm](./jetterm-function.md)
