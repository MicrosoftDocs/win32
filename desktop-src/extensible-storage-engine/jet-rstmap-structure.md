---
description: "Learn more about: JET_RSTMAP Structure"
title: JET_RSTMAP Structure
TOCTitle: JET_RSTMAP Structure
ms:assetid: bddf95e4-1bd4-4e3a-ad3e-d01f6564e33b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294077(v=EXCHG.10)
ms:contentKeyID: 32765692
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_RSTMAP Structure


_**Applies to:** Windows | Windows Server_

## JET_RSTMAP Structure

The **JET_RSTMAP** structure enables the remapping of database file paths that are stored in the transaction logs during recovery, when used by the [JetInit](./jetinit-function.md) and [JetExternalRestore](./jetexternalrestore-function.md) functions. This enables the databases to be moved when offline or when restored from backup.

```cpp
    typedef struct {
      xRPC_STRING tchar* szDatabaseName;
      xRPC_STRING tchar* szNewDatabaseName;
    } JET_RSTMAP;
```

### Members

**szDatabaseName**

The current absolute path of a database that is associated with the transaction logs that are replayed during recovery.

**szNewDatabaseName**

The new absolute path for the database.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_RSTMAP_W</strong> (Unicode) and <strong>JET_RSTMAP_A</strong> (ANSI).</p> | 



### See Also

[JetExternalRestore](./jetexternalrestore-function.md)  
[JetInit](./jetinit-function.md)
