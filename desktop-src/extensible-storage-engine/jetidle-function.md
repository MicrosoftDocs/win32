---
description: "Learn more about: JetIdle Function"
title: JetIdle Function
TOCTitle: JetIdle Function
ms:assetid: 77e036eb-b894-4ff7-b14f-1564bf21873f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269301(v=EXCHG.10)
ms:contentKeyID: 32765593
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetIdle
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

# JetIdle Function


_**Applies to:** Windows | Windows Server_

## JetIdle Function

The **JetIdle** function is defunct, and should only be used for testing purposes. **JetIdle** can be used to perform idle cleanup tasks or check the version store status in ESE.

```cpp
    JET_ERR JET_API JetIdle(
      __in          JET_SESID sesid,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session that will be used for this call.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following bits:

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
<td><p>JET_bitIdleCompact</p></td>
<td><p>Triggers cleanup of the version store.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitIdleFlushBuffers</p></td>
<td><p>Reserved for future use. If this flag is specified, the API will return JET_errInvalidgrbit.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitIdleStatus</p></td>
<td><p>Returns JET_wrnIdleFull if version store is more than half full.</p></td>
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
<td><p>JET_errInvalidParameter</p></td>
<td><p>A <em>grbit</em> parameter that was provided to the API was not valid.</p></td>
</tr>
</tbody>
</table>


If this function succeeds, the appropriate operation will be triggered, or an error code indicating how full the version store is depending on the *grbit* provided.

If this function fails, the requested operation will not have completed successfully.

#### Remarks

The version store maintains ESE's snapshot isolation mechanism. If the version store is more than half full, the program might close long-running transactions. If a long-running transaction exhausts the version store, ESE will stop allowing write operations to the database.

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

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JetCommitTransaction](./jetcommittransaction-function.md)
