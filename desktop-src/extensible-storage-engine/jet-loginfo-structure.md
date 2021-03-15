---
description: "Learn more about: JET_LOGINFO Structure"
title: JET_LOGINFO Structure
TOCTitle: JET_LOGINFO Structure
ms:assetid: b34b3f24-5d19-4e11-a657-a0e59204d628
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294063(v=EXCHG.10)
ms:contentKeyID: 32765678
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_LOGINFO Structure


_**Applies to:** Windows | Windows Server_

## JET_LOGINFO Structure

The **JET_LOGINFO** structure returns structured information about the set of transaction log files that should be a part of a backup file set. The **JET_LOGINFO** structure is the minimal set of information needed to represent a range of logs that is retrieved with [JetGetLogInfoInstance2](./jetgetloginfoinstance2-function.md) or specified for a hard recovery with [JetExternalRestore2](./jetexternalrestore2-function.md).

```cpp
typedef struct {
  unsigned long cbSize;
  unsigned long ulGenLow;
  unsigned long ulGenHigh;
  tchar szBaseName[JET_BASE_NAME_LENGTH + 1];
} JET_LOGINFO;
```

### Members

**cbSize**

The size of the structure, in bytes.

This member enables future expansion of this structure while enabling backwards compatibility. It should always be set to sizeof( JET_LOGINFO ).

**ulGenLow**

The lowest (or oldest) log file number that is restored. The full fidelity of an unsigned long should be preserved, but in current versions of the engine this number is a hexadecimal number in the range from 0x00000 to 0xFFFFF. This might change in future versions.

**ulGenHigh**

The highest (or most recent) log file number that is restored. The full fidelity of a unsigned long should be preserved, but in current versions of the engine this number is a hexadecimal number in the range from 0x00000 to 0xFFFFF. This might change in future versions.

**szBaseName**

The prefix used to name the transaction log files.

The value that is returned in this member is always equal to the setting for [JET_paramBaseName](./transaction-log-parameters.md) for the instance that generated this information.

### Remarks

Transaction log files are named according to the instance base name and the generation number of the log file. The name is of the format BBBXXXXX.LOG. BBB corresponds to the base name for the log file and is always three characters in length. XXXXX corresponds to the generation number of the log file in zero padded hexadecimal and is always five characters in length. LOG is the file extension that is always given to transaction log files by the engine.

Use of this structured information is discouraged because it causes the application to have intimate knowledge of this naming scheme for transaction log files. If the naming scheme ever changes in the future then such an application will no longer function properly. It is conceivable that the log format will change to incorporate 8 hex digits in the future. Applications should use the explicit list of file names returned by [JetGetLogInfo](./jetgetloginfo-function.md) instead.

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista or Windows XP.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008 or Windows Server 2003.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Implemented as <strong>JET_LOGINFO_W</strong> (Unicode) and <strong>JET_LOGINFO_A</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


### See Also

[JetExternalRestore2](./jetexternalrestore2-function.md)  
[JetGetLogInfo](./jetgetloginfo-function.md)  
[JetGetLogInfoInstance2](./jetgetloginfoinstance2-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
