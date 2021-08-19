---
description: "Learn more about: JetGetIndexInfo Function"
title: JetGetIndexInfo Function
TOCTitle: JetGetIndexInfo Function
ms:assetid: c6235281-e208-4966-bc66-ec1ab27333c0
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294084(v=EXCHG.10)
ms:contentKeyID: 32765699
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetIndexInfoW
- JetGetIndexInfoA
- JetGetIndexInfo
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

# JetGetIndexInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetIndexInfo Function

The **JetGetIndexInfo** function retrieves information about an index.

```cpp
    JET_ERR JET_API JetGetIndexInfo(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __in          const tchar* szTableName,
      __in          const tchar* szIndexName,
      __out         void* pvResult,
      __in          unsigned long cbResult,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*dbid*

The database identifier to use for the API call.

*szTableName*

The name of the table containing the index with the information to retrieve.

*szIndexName*

The name of the index with the information to retrieve.

*pvResult*

Pointer to a buffer that will receive the desired information. The buffer should be aligned to hold the type required. The type of the buffer is dependent on the *InfoLevel* parameter.

*cbResult*

The size, in bytes, of the buffer passed as *pvResult*.

*InfoLevel*

The information that will be stored in *pvResult*. The following options can be used for this parameter.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_IdxInfo</p> | <p><em>pvResult</em> is interpreted as a <a href="gg269185(v=exchg.10).md">JET_INDEXLIST</a> structure. On success, the <a href="gg269185(v=exchg.10).md">JET_INDEXLIST</a> structure receives information about the index. On failure, the contents of <em>pvBuffer</em> are undefined.</p> | 
| <p>JET_IdxInfoCount</p> | <p><em>pvResult</em> is interpreted as a ULONG. On success, the ULONG holds the count of indexes on the specified table. <em>szIndexName</em> is ignored. On failure, the contents of <em>pvBuffer</em> are undefined.</p> | 
| <p>JET_IdxInfoIndexId</p> | <p><em>pvResult</em> is interpreted as a <a href="gg269327(v=exchg.10).md">JET_INDEXID</a>. On success, the <a href="gg269327(v=exchg.10).md">JET_INDEXID</a> structure receives information about the index. On failure, the contents of <em>pvBuffer</em> are undefined.</p> | 
| <p>JET_IdxInfoLangid</p> | <p>JET_IdxInfoLangid is deprecated. Use JET_IdxInfoLCID and the <a href="/windows/win32/api/winnt/nf-winnt-langidfromlcid">LANGIDFROMLCID</a> macro instead.</p> | 
| <p>JET_IdxInfoLCID</p> | <p><em>pvResult</em> is interpreted as an LCID. On success, the LCID holds the Locale Identifier of the index. On failure, the contents of <em>pvBuffer</em> are undefined.</p><p><strong>Windows XP:  </strong>JET_IdxInfoLCID is introduced in Windows XP.</p> | 
| <p>JET_IdxInfoList</p> | <p><em>pvResult</em> is interpreted as a <a href="gg269185(v=exchg.10).md">JET_INDEXLIST</a> structure. On success, the <a href="gg269185(v=exchg.10).md">JET_INDEXLIST</a> structure receives information about the index. On failure, the contents of <em>pvBuffer</em> are undefined.</p> | 
| <p>JET_IdxInfoOLC</p> | <p>JET_IdxInfoOLC is obsolete.</p> | 
| <p>JET_IdxInfoResetOLC</p> | <p>JET_IdxInfoResetOLC is obsolete.</p> | 
| <p>JET_IdxInfoSpaceAlloc</p> | <p><em>pvResult</em> is interpreted as a ULONG. On success, the ULONG holds the space usage of the index. On failure, the contents of <em>pvBuffer</em> are undefined.</p> | 
| <p>JET_IdxInfoSysTabCursor</p> | <p>JET_IdxInfoSysTabCursor is obsolete.</p> | 
| <p>JET_IdxInfoVarSegMac</p> | <p><em>pvResult</em> is interpreted as a USHORT. On success, the USHORT holds the value of <em>cbVarSegMac</em> used when the index was created. See <a href="gg269186(v=exchg.10).md">JET_INDEXCREATE</a> for a description of <em>cbVarSegMac</em>. On failure, the contents of <em>pvBuffer</em> are undefined.</p> | 
| <p>JET_IdxInfoKeyMost</p> | <p><em>pvResult</em> is interpreted as a USHORT. On success, the USHORT holds the value of <em>cbKeyMost</em> used when the index was created. See <a href="gg269186(v=exchg.10).md">JET_INDEXCREATE</a> for a description of <em>cbKeyMost</em>. On failure, the contents of <em>pvBuffer</em> are undefined.</p><p><strong>Windows Vista:  </strong>JET_IdxInfoKeyMost is introduced in Windows Vista.</p> | 
| <p>JET_IdxInfoCreateIndex</p> | <p><em>pvResult</em> is interpreted as a <a href="gg269186(v=exchg.10).md">JET_INDEXCREATE</a> structure. On failure, the contents of <em>pvBuffer</em> are undefined.</p><p><strong>Windows 7:  </strong>JET_IdxInfoCreateIndex is introduced in Windows 7.</p> | 
| <p>JET_IdxInfoCreateIndex2</p> | <p><em>pvResult</em> is interpreted as a <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure. On failure, the contents of <em>pvBuffer</em> are undefined.</p><p><strong>Windows 7:  </strong>JET_IdxInfoCreateIndex2 is introduced in Windows 7.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errIndexNotFound</p> | <p>The specified index cannot be found in the specified table.</p> | 
| <p>JET_wrnBufferTruncated</p> | <p>The buffer passed in as <em>pvResult</em> was too small. The contents of the buffer are undefined.</p> | 



#### Remarks

**JetGetIndexInfo** and [JetGetTableIndexInfo](./jetgettableindexinfo-function.md) retrieve identical information about an index. The difference is in how the table is specified. **JetGetIndexInfo** expects a database (*dbid*) and name of a table (*szTableName*), while [JetGetTableIndexInfo](./jetgettableindexinfo-function.md) expects a table identifier (*tableid*).

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetGetIndexInfoW</strong> (Unicode) and <strong>JetGetIndexInfoA</strong> (ANSI).</p> | 



#### See Also

[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JET_INDEXID](./jet-indexid-structure.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetTableIndexInfo](./jetgettableindexinfo-function.md)
