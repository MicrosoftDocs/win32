---
description: "Learn more about: JET_INDEXID Structure"
title: JET_INDEXID Structure
TOCTitle: JET_INDEXID Structure
ms:assetid: 8b1d90f0-bc93-4b30-90d1-b9e93ad26654
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269327(v=EXCHG.10)
ms:contentKeyID: 32765617
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

# JET_INDEXID Structure


_**Applies to:** Windows | Windows Server_

## JET_INDEXID Structure

The **JET_INDEXID** structure holds an index ID. An index ID is a hint that is used to accelerate the selection of the current index using [JetSetCurrentIndex](./jetsetcurrentindex-function.md). It is most useful when there is a very large number of indexes over a table. The index ID can be retrieved using [JetGetIndexInfo](./jetgetindexinfo-function.md) or [JetGetTableIndexInfo](./jetgettableindexinfo-function.md).

```cpp
    typedef struct tagJET_INDEXID {
      unsigned long cbStruct;
      char rgbIndexId[sizeof(JET_API_PRT) + sizeof(unsigned long) + sizeof(unsigned long)];
    } JET_INDEXID;
```

### Members

**cbStruct**

The size, in bytes, of the index ID.

This is the actual size of the index ID that is returned in the output buffer from [JetGetIndexInfo](./jetgetindexinfo-function.md) or [JetGetTableIndexInfo](./jetgettableindexinfo-function.md).

**rgbIndexId**

An opaque BLOB of information that is used by the engine to quickly identify an index in its schema cache.

Do not attempt to interpret the BLOB of information. It is not a set size.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetGetIndexInfo](./jetgetindexinfo-function.md)  
[JetGetTableIndexInfo](./jetgettableindexinfo-function.md)  
[JetGetTableInfo](./jetgettableinfo-function.md)  
[JetSetCurrentIndex](./jetsetcurrentindex-function.md)
