---
title: JetStopServiceInstance2 Function
TOCTitle: JetStopServiceInstance2 Function
ms:assetid: ac021e13-ec83-42eb-9aef-a906d7a7ed39
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/JJ835046(v=EXCHG.10)
ms:contentKeyID: 49894668
ms.date: 04/11/2016
ms.topic: article
dev_langs:
- c++
api_name: 
- JetStopServiceInstance2
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetStopServiceInstance2 Function


_**Applies to:** Windows | Windows Server_

The **JetStopServiceInstance2** function prepares an instance prior to Suspend, and prepares an instance after Resume. Suspend and Resume are execution states of the Windows Store App lifecycle model.

The **JetStopServiceInstance2** function was introduced in Windows 8.

``` c++
JET_ERR JET_API JetStopServiceInstance2(
  _In_          JET_INSTANCE       instance
  _In_          const JET_GRBIT    grbit
);
```

### Parameters

*instance*

The target instance. The **JET\_INSTANCE** data type is a handle to the instance of the database to use for a call to the JET API. This handle is obtained when you create an instance of the database by calling the [JetCreateInstance](gg269354\(v=exchg.10\).md), [JetCreateInstance2](gg269202\(v=exchg.10\).md), [JetInit](gg294068\(v=exchg.10\).md), or [JetInit2](gg294065\(v=exchg.10\).md) functions.

*grbit*

A group of bits that specifies one or more of the values listed and defined in the following table.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_bitStopServiceAll</p></td>
<td><p>Stops all Extensible Storage Engine (ESE) services for the specified instance.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitStopServiceBackgroundUserTasks</p></td>
<td><p>Stops restartable client-specified background maintenance tasks (B+ Tree Defrag, for example).</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitStopServiceQuiesceCaches</p></td>
<td><p>Quiesces all dirty caches to disk. This value is asynchronous and can be canceled.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitStopServiceResume</p></td>
<td><p>Resumes previously issued StopService operations; that is, it restarts the service. This value can be combined with the <em>grbits</em> parameter to resume specific services, or with JET_bitStopServiceAll to Resume all previously stopped services. This bit can only be used to resume StopServiceBackgroundUserTasks and JET_bitStopServiceQuiesceCaches. If you previously called with JET_bitStopServiceAll, an attempt to use JET_bitStopServiceResume will fail. If the second resume step does not get called, the application will have degraded performance. In this situation the checkpoint is kept at zero.</p></td>
</tr>
</tbody>
</table>


### Return value

This function returns the [JET\_ERR](gg294092\(v=exchg.10\).md) data type with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

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
</tbody>
</table>


#### Remarks

This function allows a JET application to move the database cache to a clean or nearly clean state (with the operating system I/O idle), such that if the application were to be terminated, recovery would be quick. This approach is preferred over terminating JET by calling the [JetTerm](gg269298\(v=exchg.10\).md) or [JetDetachDatabase](gg269266\(v=exchg.10\).md) functions, so that in the more common scenario, the application is just unsuspended, and later the application has the whole cache and is ready to go as soon as possible.

If this function succeeds, it prepares the database cache for an imminent suspension. This function queues work to a background worker thread and returns to the caller immediately. The function should be called based on the PLM VisibilityNotice as opposed to calling from the application's suspension event handler to ensure that JET has time to flush dirty buffers before PLM suspends/terminates the process. Internally, JET triggers an immediate dispatch of checkpoint maintenance upon configuration change (either checkpoint update or this new quiesce caches bit). For more information about VisibilityNotice events, see [VisibilityChangedEventArgs class](http://msdn.microsoft.com/en-us/library/windows/apps/windows.ui.core.visibilitychangedeventargs.aspx).

This function must be called twice. It is called after the application receives the suspension notice from the operating system, but before the application has been suspended. Then it is called again after the operating system resumes the application. For example:

When called to Suspend: JET\_ERR JET\_API JetStopServiceInstance2( instance, JET\_bitStopServiceQuiesceCaches);

When Resumed: JET\_ERR JET\_API JetStopServiceInstance2( instance, JET\_bitStopServiceQuiesceCaches|JET\_bitStopServiceResume );

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows 8.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2012.</p></td>
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


#### See also

[JET\_ERR](gg294092\(v=exchg.10\).md)  
[JET\_INSTANCE](gg294048\(v=exchg.10\).md)  
[JetCloseDatabase](gg294123\(v=exchg.10\).md)  
[JetCloseTable](gg294087\(v=exchg.10\).md)  
[JetDetachDatabase](gg269266\(v=exchg.10\).md)  
[JetEndSession](gg294054\(v=exchg.10\).md)  
[JetResetSessionContext](gg269250\(v=exchg.10\).md)  
[JetRollback](gg269273\(v=exchg.10\).md)  
[JetTerm](gg269298\(v=exchg.10\).md)  
[JetTerm2](gg269223\(v=exchg.10\).md)

