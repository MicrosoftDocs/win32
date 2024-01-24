---
description: "Learn more about: JET_OSSNAPID"
title: JET_OSSNAPID
TOCTitle: JET_OSSNAPID
ms:assetid: 89b15492-674a-46e4-8aea-991df4f22a6f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269325(v=EXCHG.10)
ms:contentKeyID: 32765615
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

# JET_OSSNAPID


_**Applies to:** Windows | Windows Server_

## JET_OSSNAPID

The **JET_OSSNAPID** data type contains a handle to a snapshot of the database.

```cpp
    typedef JET_API_PTR JET_OSSNAPID;
```

### Data Types

JET_OSSNAPID

A handle to a snapshot of the database. This handle is used in JET API elements that are involved with snapshot backup.

**NULL** can be used to indicate an invalid handle.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 


