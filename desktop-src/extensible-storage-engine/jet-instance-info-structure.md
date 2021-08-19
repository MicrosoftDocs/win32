---
description: "Learn more about: JET_INSTANCE_INFO Structure"
title: JET_INSTANCE_INFO Structure
TOCTitle: JET_INSTANCE_INFO Structure
ms:assetid: 8cdd2e48-f1bb-465b-aefc-ffe441bf88a1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269331(v=EXCHG.10)
ms:contentKeyID: 32765621
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

# JET_INSTANCE_INFO Structure


_**Applies to:** Windows | Windows Server_

## JET_INSTANCE_INFO Structure

The **JET_INSTANCE_INFO** structure receives information about running database instances when used with the [JetGetInstanceInfo](./jetgetinstanceinfo-function.md) and [JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md) functions.

```cpp
    typedef struct _JET_INSTANCE_INFO {
      JET_INSTANCE hInstanceId;
      tchar* szInstanceName;
      JET_API_PTR cDatabases;
      tchar** szDatabaseFileName;
      tchar** szDatabaseDisplayName;
      tchar** szDatabaseSLVFileName;
    } JET_INSTANCE_INFO;
```

### Members

**hInstanceId**

The [JET_INSTANCE](./jet-instance.md) of the given instance.

**szInstanceName**

The name of the database instance. This value can be **NULL** if the instance does not have a name.

**cDatabases**

The number of databases that are attached to the database instance. **cDatabases** also holds the size of the arrays of strings that are returned in **szDatabaseFileName**, **szDatabaseDisplayName**, and **szDatabaseSLVFileName**.

**szDatabaseFileName**

An array of strings, each holding the file name of a database that is attached to the database instance. The array has **cDatabases** elements.

**szDatabaseDisplayName**

An array of strings, each holding the display name of a database. Currently the string can be NULL. The array has **cDatabases** elements.

**szDatabaseSLVFileName**

An array of strings, each holding the file name of the SLV file that is attached to the database instance. The array has **cDatabases** elements. SLV files are not supported, so this field should be ignored.

### Remarks

Each database instance can have several databases attached to it.

For a given **JET_INSTANCE_INFO** structure, the array of strings that is returned for the databases are in the same order. For example, "szDatabaseDisplayName\[ i \]" and "szDatabaseFileName\[ i \]" both refer to the same database.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_INSTANCE_INFO_W</strong> (Unicode) and <strong>JET_INSTANCE_INFO _A</strong> (ANSI).</p> | 



### See Also

[JET_API_PTR](./jet-api-ptr.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetGetInstanceInfo](./jetgetinstanceinfo-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)
