---
description: "Learn more about: JET_DBID"
title: JET_DBID
TOCTitle: JET_DBID
ms:assetid: 516acb79-aa75-4609-81b6-3b2e4e0c95af
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269248(v=EXCHG.10)
ms:contentKeyID: 32765550
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

# JET_DBID


_**Applies to:** Windows | Windows Server_

## JET_DBID

The **JET_DBID** data type contains the handle to the database. A database handle is used to manage the schema of a database. It can also be used to manage the tables inside of that database.

```cpp
    typedef unsigned long JET_DBID;
```

### Data Types

JET_DBID

Handle to the database.

A value of JET_dbidNil indicates that the handle is invalid.

### Remarks

A database handle is created by means of a call to [JetCreateDatabase](./jetcreatedatabase-function.md) or [JetOpenDatabase](./jetopendatabase-function.md).

A database handle can be explicitly closed by [JetCloseDatabase](./jetclosedatabase-function.md) or implicitly closed by [JetEndSession](./jetendsession-function.md) or [JetTerm](./jetterm-function.md).

A database handle can be used only within the session in which it was created. The existence of a database handle corresponds to the logical open of a database. A logical open is different from the physical open of a database, which happens when a database is attached to the system.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetCreateDatabase](./jetcreatedatabase-function.md)  
[JetOpenDatabase](./jetopendatabase-function.md)  
[JetCloseDatabase](./jetclosedatabase-function.md)  
[JetEndSession](./jetendsession-function.md)
