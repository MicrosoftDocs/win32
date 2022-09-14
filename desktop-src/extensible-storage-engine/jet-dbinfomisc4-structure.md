---
description: "Learn more about: JET_DBINFOMISC4 Structure"
title: JET_DBINFOMISC4 Structure
TOCTitle: JET_DBINFOMISC4 Structure
ms:assetid: 63f446bc-98b7-4a60-9575-d6b4757fb0fa
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269269(v=EXCHG.10)
ms:contentKeyID: 32765571
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

# JET_DBINFOMISC4 Structure


_**Applies to:** Windows | Windows Server_

## JET_DBINFOMISC4 Structure

The **JET_DBINFOMISC4** structure holds miscellaneous information about a database. This is the information that is contained in the database header.

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
      unsigned long genMinRequired;
      unsigned long genMaxRequired;
      JET_LOGTIME logtimeGenMaxCreate;
      unsigned long ulRepairCount;
      JET_LOGTIME logtimeRepair;
      unsigned long ulRepairCountOld;
      unsigned long ulECCFixSuccess;
      JET_LOGTIME logtimeECCFixSuccess;
      unsigned long ulECCFixSuccessOld;
      unsigned long ulECCFixFail;
      JET_LOGTIME logtimeECCFixFail;
      unsigned long ulECCFixFailOld;
      unsigned long ulBadChecksum;
      JET_LOGTIME logtimeBadChecksum;
      unsigned long ulBadChecksumOld;
      unsigned long genCommitted;
      JET_BKINFO bkinfoCopyPrev;
      JET_BKINFO bkinfoDiffPrev;
    } JET_DBINFOMISC4;
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
| <p>0x620,A</p> | <p>Merged code base (3/26/2003).</p> | 
| <p>0x620,B</p> | <p>New checksum format (1/08/2004).</p> | 
| <p>0x620,C</p> | <p>Increased max key length to 1000/2000 bytes for 4/8kb pages (1/15/2004).</p> | 
| <p>0x620,D</p> | <p>Catalog space hints, space_header.v2 (7/15/2007).</p> | 
| <p>0x620,E</p> | <p>Add new node/extent format to space manager, use it for reserved pools of space (8/9/2007).</p> | 
| <p>0x620,F</p> | <p>Compression for intrinsic long-values (10/30/2007).</p> | 
| <p>0x620,10</p> | <p>Compression for separated long-values (12/05/2007).</p> | 
| <p>0x620,11</p> | <p>New LV chunk size for large pages (12/29/2007).</p> | 



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

**genMinRequired**

Represents the minimum log generation required for replaying the logs. This is typically used as the checkpoint generation.

**genMaxRequired**

Represents the maximum log generation required for replaying the logs.

**logtimeGenMaxCreate**

Represents the creation date and time of the genMax log file.

**ulRepairCount**

The number of times a repair has been called on this database.

**logtimeRepair**

Represents the date and time the last repair was run.

**ulRepairCountOld**

The number of times the repair had been run on this database before the last defragmentation.

**ulECCFixSuccess**

The number of times a one bit error was fixed and resulted in a good page.

**logtimeECCFixSuccess**

Represents the date and time the last one bit error was fixed and resulted in a good page.

**ulECCFixSuccessOld**

Represents the number of times a one bit error was fixed and resulted in a good page before last repair.

**ulECCFixFail**

The number of times a one bit error was fixed and resulted in a bad page.

**logtimeECCFixFail**

Represents the date and time the last one bit error was fixed and resulted in a bad page.

**ulECCFixFailOld**

The number of times a one bit error was fixed and resulted in a bad page before last repair.

**ulBadChecksum**

The number of times a non-correctable ECC/checksum error was found.

**logtimeBadChecksum**

Represents the date and time the last non-correctable ECC/checksum error was found.

**ulBadChecksumOld**

The number of times a non-correctable ECC/checksum error was found before last repair.

**genCommitted**

The maximum number of log generations committed to the database. Typically the current log generation.

**bkinfoCopyPrev**

The last successful Copy backup.

**bkinfoDiffPrev**

The last successful Differential backup. This value is reset when bkinfoFullPrev is set.

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
