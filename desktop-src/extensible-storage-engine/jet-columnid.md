---
description: "Learn more about: JET_COLUMNID"
title: JET_COLUMNID
TOCTitle: JET_COLUMNID
ms:assetid: d6c74c5c-ba61-4e1c-a1b1-495e925b6b68
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294104(v=EXCHG.10)
ms:contentKeyID: 32765719
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

# JET_COLUMNID


_**Applies to:** Windows | Windows Server_

## JET_COLUMNID

The **JET_COLUMNID** data type identifies a column within a table.

```cpp
    typedef unsigned long JET_COLUMNID;
```

### Data Types

JET_COLUMNID

Identifies a column within a table.

### Remarks

Column IDs are unique within a single table. Once a column is known to have a certain column ID, it will always have that column ID. Restore from backup will not change the value of a column ID. However, if one or more table columns, prior to a specific table column, are deleted, a compact database can then change the value of a column ID.

In some cases, column IDs are the only means of identifying columns. When a temporary table is created, its columns do not have names, but an array of column IDs is returned by the create function.

Columns in different tables can have the same column ID.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 


