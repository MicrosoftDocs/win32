---
title: JetInit3 Function
TOCTitle: JetInit3 Function
ms:assetid: 752589b6-1b8f-4b6f-a14a-00f4b1405db5
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269296(v=EXCHG.10)
ms:contentKeyID: 32765588
ms.date: 04/11/2016
ms.topic: article
api_name: 
- JetInit3
- JetInit3A
- JetInit3W
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

# JetInit3 Function


_**Applies to:** Windows | Windows Server_

## JetInit3 Function

The **JetInit3** function puts the database engine into a state in which it can support application use of database files. The engine must already be properly configured for initialization, which you accomplish by using the [JetSetSystemParameter](gg294044\(v=exchg.10\).md) function. Note that database crash recovery occurs automatically as a part of the initialization process.

**Windows Vista:**  **JetInit3** is introduced in Windows Vista.

    JET_ERR JET_API JetInit3(
      __in_out_opt  JET_INSTANCE* pinstance,
      __in_opt      JET_RSTINFO* prstInfo,
      __in          JET_GRBIT grbit
    );

### Parameters

*pinstance*

The instance that you use for a particular call. The use of this parameter depends on the operating mode of the engine. If the engine is operating in legacy mode (Windows 2000 compatibility mode), in which only one instance is supported, you can set this parameter either to **NULL** or to a valid output buffer containing either **NULL** or JET\_instanceNil, which returns the global instance handle created as a side-effect of the initialization. This instance handle can then be passed to any other API that takes an instance. If the engine is operating in multi-instance mode, you must set this parameter to a valid input buffer that contains the instance handle returned by the [JetCreateInstance](gg269354\(v=exchg.10\).md) function that is being initialized.

*prstInfo*

Additional recovery parameters used for remapping databases during recovery, for setting the position where recovery will stop, or for determining the current recovery status.

*grbit*

A group of bits that specifies zero or more of the options listed and defined in the following table.

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
<td><p>JET_bitReplayReplicatedLogFiles</p></td>
<td><p>This value is reserved for future use.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitCreateSFSVolumeIfNotExist</p></td>
<td><p>This value is reserved for future use.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitReplayIgnoreMissingDB</p></td>
<td><p>This value enables the user to run recovery on a set of log files, even in the absence of the databases that were attached to the log file set at some point.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitRecoveryWithoutUndo</p></td>
<td><p>This value enables the user to perform recovery, but only up to (and not including) the Undo phase. Using this value, additional transaction logs can be copied in and applied.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitTruncateLogsAfterRecovery</p></td>
<td><p>This value causes log files to be truncated during a successful soft recovery.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitReplayMissingMapEntryDB</p></td>
<td><p>This value causes a missing database map entry to default to the same location.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitReplayIgnoreLostLogs</p></td>
<td><p>This value causes logs lost from the end of the log stream to be ignored during a recovery.</p>
<p><strong>Windows 7:JET_bitReplayIgnoreLostLogs</strong> is introduced in Windows 7.</p></td>
</tr>
</tbody>
</table>


### Return Value

This function returns the [JET\_ERR](gg294092\(v=exchg.10\).md) data type with one of the following return codes. For more information about the possible Extensible Storage Engine (ESE) errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).


#### Remarks

An instance must be initialized with a call to the **JetInit3** function before it can be used by anything other than the [JetSetSystemParameter](gg294044\(v=exchg.10\).md) function.

An instance is destroyed by a call to the [JetTerm](gg269298\(v=exchg.10\).md) function, even if that instance was never initialized by using the [JetInit](gg294068\(v=exchg.10\).md) function. An instance is the unit of recoverability for the database engine. It controls the life cycle of all the files used to protect the integrity of the data in a set of database files. These files include the checkpoint file and the transaction log files. Note that [JetTerm](gg269298\(v=exchg.10\).md) should not be called if the **JetInit3** function fails. However, [JetTerm](gg269298\(v=exchg.10\).md) should still be called for all instances created by **JetCreateInstance2** if **JetInit3** was never called or if **JetInit3** succeeds.

If recovery is running on a set of logs for which not all of the related databases are present (which will return the error JET\_errAttachedDatabaseMismatch under normal circumstances), and the client wants recovery to continue despite the missing databases, the JET\_bitReplayIgnoreMissingDB error is used to continue recovery for the available databases.

Because crash recovery doesn't usually happen on the same machine (and with the same configuration) as at the time of the crash, a database typically doesn't change location. In certain scenarios, such as moving files to a different machine or restoring snapshot backup to different locations, this is no longer true. The **JetInit3** function enables you to specify a mapping (using the [JET\_RSTINFO](gg269216\(v=exchg.10\).md) and [JET\_RSTMAP](gg294077\(v=exchg.10\).md) structures) between the old database location and its new location. In fact, you need only the new location as long as the database files are present at that location. As soon as you know the locations of the restored databases, the database signature will be used to identify the database through the restore process. You'll need the original database location only if you need to re-create a database, in which case the signature is known.

In addition, if you need to stop a recovery after an Undo operation, you can specify a particular log position at which recovery will stop. Note that this includes the ability to stop at the end of a particular log generation if the specified position is part of the generation but past the end of the actual log.

For more information, see the "Remarks" section in the [JetInit](gg294068\(v=exchg.10\).md) topic.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Client</p></td>
<td><p>Requires Windows Vista.</p></td>
</tr>
<tr class="even">
<td><p>Server</p></td>
<td><p>Requires Windows Server 2008.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p>Library</p></td>
<td><p>Uses ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p>DLL</p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
<tr class="even">
<td><p>Unicode</p></td>
<td><p>Implemented as <strong>JetInit3W</strong> (Unicode) and <strong>JetInit3A</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[Extensible Storage Engine Files](gg294069\(v=exchg.10\).md)  
[JET\_ERR](gg294092\(v=exchg.10\).md)  
[JET\_GRBIT](gg294066\(v=exchg.10\).md)  
[JET\_INSTANCE](gg294048\(v=exchg.10\).md)  
[JET\_RSTINFO](gg269216\(v=exchg.10\).md)  
[JET\_RSTMAP](gg294077\(v=exchg.10\).md)  
[JetCreateInstance](gg269354\(v=exchg.10\).md)  
[JetInit](gg294068\(v=exchg.10\).md)  
[JetInit2](gg294065\(v=exchg.10\).md)  
[JetSetSystemParameter](gg294044\(v=exchg.10\).md)  
[Resource Parameters](gg269201\(v=exchg.10\).md)

