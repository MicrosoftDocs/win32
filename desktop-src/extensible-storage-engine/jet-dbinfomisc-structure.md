---
description: "Learn more about: JET_DBINFOMISC Structure"
title: JET_DBINFOMISC Structure
TOCTitle: JET_DBINFOMISC Structure
ms:assetid: ff287087-35b8-495e-9922-418ec2439e19
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294147(v=EXCHG.10)
ms:contentKeyID: 32765761
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

# JET_DBINFOMISC Structure


_**Applies to:** Windows | Windows Server_

## JET_DBINFOMISC Structure

The **JET_DBINFOMISC** structure holds miscellaneous information about a database. This is the information that is contained in the database header.

```cpp
    typedef struct {
      unsigned long ulVersion;
      unsigned long ulUpdate;
      JET_SIGNATURE signDb;
      unsigned long dbstate;
      JET_LGPOS lgposConsistent;
      JET_LOGTIME logtimeConsistent;
      JET_LOGTIME logtimeAttach;
      JET_LGPOS lgposAttach;
      JET_LOGTIME logtimeDetach;
      JET_LGPOS lgposDetach;
      JET_SIGNATURE signLog;
      JET_BKINFO bkinfoFullPrev;
      JET_BKINFO bkinfoIncPrev;
      JET_BKINFO bkinfoFullCur;
      unsigned long fShadowingDisabled;
      unsigned long fUpgradeDb;
      unsigned long dwMajorVersion;
      unsigned long dwMinorVersion;
      unsigned long dwBuildNumber;
      long lSPNumber;
      unsigned long cbPageSize;
    } JET_DBINFOMISC;
```

### Members

**ulVersion**

The native version of the database engine that created the database. See [JetGetVersion](./jetgetversion-function.md) to retrieve the native version for the current database engine.

**ulUpdate**

Tracks incremental database format updates that are backward compatible.


| <p>ulVersion, ulUpdate =</p> | <p>Meaning</p> | 
|------------------------------|----------------|
| <p>0x620,0</p> | <p>Original operating system Beta format (4/22/97).</p> | 
| <p>0x620,1</p> | <p>Add columns in the catalog for conditional indexing and OLD (5/29/97).</p> | 
| <p>0x620,2</p> | <p>Add the fLocalizedText flag in IDB (6/5/97).</p> | 
| <p>0x620,3</p> | <p>Add SPLIT_BUFFER to space tree root pages (10/30/97).</p> | 
| <p>0x620,2</p> | <p>Revert revision in order for ESE97 to remain forward-compatible (1/28/98).</p> | 
| <p>0x620,3</p> | <p>Add new tagged columns to catalog ("CallbackData" and "CallbackDependencies").</p> | 
| <p>0x620,4</p> | <p>SLV support: signSLV, fSLVExists in db header (5/5/98).</p> | 
| <p>0x620,5</p> | <p>New SLV space tree (5/29/98).</p> | 
| <p>0x620,6</p> | <p>SLV space map (10/12/98).</p> | 
| <p>0x620,7</p> | <p>4-byte IDXSEG (12/10/98).</p> | 
| <p>0x620,8</p> | <p>New template column format (1/25/99).</p> | 
| <p>0x620,9</p> | <p>Sorted template columns (6/24/99).</p> | 
| <p>0x623,0</p> | <p>New Space Manager (5/15/99).</p> | 



**signDb**

Signature of the database (including creation time). This structure is 28 bytes.

**dbstate**

This is the database state.

The following options are available for this member.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_dbstateJustCreated<br />1</p> | <p>The database was just created.</p> | 
| <p>JET_dbstateDirtyShutdown<br />2</p> | <p>The database requires hard or soft recovery to be run in order to become usable or moveable. One should not try to move databases in this state.</p> | 
| <p>JET_dbstateCleanShutdown<br />3</p> | <p>The database is in a clean state. The database can be attached without any log files.</p> | 
| <p>JET_dbstateBeingConverted<br />4</p> | <p>The database is being upgraded.</p> | 
| <p>JET_dbstateForceDetach<br />5</p> | <p>Internal.</p> | 



**lgposConsistent**

Null if the database is in a dirty state. This is the log position that was used when the database was last brought to a clean shutdown state.

**logtimeConsistent**

Null if the database is in a dirty state. This is the time when the database was last brought to a clean shutdown state.

**logtimeAttach**

The time when the database was last attached with [JetAttachDatabase](./jetattachdatabase-function.md).

**lgposAttach**

The log position that was used the last time the database was attached with [JetAttachDatabase](./jetattachdatabase-function.md).

**logtimeDetach**

The time when the database was last detached with [JetDetachDatabase](./jetdetachdatabase-function.md).

**lgposDetach**

The log position that was used the last time the database was detached with [JetDetachDatabase](./jetdetachdatabase-function.md).

**signLog**

Supports the ESE infrastructure and cannot be used in your code.

**bkinfoFullPrev**

Supports the ESE infrastructure and cannot be used in your code.

**bkinfoIncPrev**

Supports the ESE infrastructure and cannot be used in your code.

**bkinfoFullCur**

Supports the ESE infrastructure and cannot be used in your code.

**fShadowingDisabled**

Supports the ESE infrastructure and cannot be used in your code.

**fUpgradeDb**

Supports the ESE infrastructure and cannot be used in your code.

**dwMajorVersion**

Represents the Windows NT version numbers when the databases indexes were updated. Used for updating indexes.

**dwMinorVersion**

Represents the Windows NT version numbers when the databases indexes were updated. Used for updating indexes.

**dwBuildNumber**

Represents the Windows NT version numbers when the databases indexes were updated. Used for updating indexes.

**lSPNumber**

Represents the Windows NT version numbers when the databases indexes were updated. Used for updating indexes.

**cbPageSize**

Database page size. 0 means the page size is 4 KB.

This value is retrieved only if JET_DbInfoMisc was passed to [JetGetDatabaseInfo](./jetgetdatabaseinfo-function.md) or [JetGetDatabaseFileInfo](./jetgetdatabasefileinfo-function.md).

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_BKINFO](./jet-bkinfo-structure.md)  
[JET_LOGTIME](./jet-logtime-structure.md)  
[JET_LGPOS](./jet-lgpos-structure.md)  
[JET_SIGNATURE](./jet-signature-structure.md)  
[JetGetDatabaseInfo](./jetgetdatabaseinfo-function.md)  
[JetGetDatabaseFileInfo](./jetgetdatabasefileinfo-function.md)
