---
description: "Learn more about: JET_INDEXRANGE Structure"
title: JET_INDEXRANGE Structure
TOCTitle: JET_INDEXRANGE Structure
ms:assetid: 8e437f7d-1e21-4a0b-a5a5-1c78235a4f80
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269335(v=EXCHG.10)
ms:contentKeyID: 32765624
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

# JET_INDEXRANGE Structure


_**Applies to:** Windows | Windows Server_

## JET_INDEXRANGE Structure

The **JET_INDEXRANGE** structure identifies an index range when it is used with the [JetIntersectIndexes](./jetintersectindexes-function.md) function.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_TABLEID tableid;
      JET_GRBIT grbit;
    } JET_INDEXRANGE;
```

### Members

**cbStruct**

The size, in bytes, of the **JET_INDEXRANGE**.

**tableid**

A cursor that has previously had an index range set with [JetSetIndexRange](./jetsetindexrange-function.md).

**grbit**

A bitmask composed of exactly one of the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitRecordInIndex</p> | <p>Specifies that the index range should be treated normally.</p> | 
| <p>JET_bitRecordNotInIndex</p> | <p>Reserved for future use. Do not use.</p> | 



### Remarks

Each **JET_INDEXRANGE** structure that is passed to [JetIntersectIndexes](./jetintersectindexes-function.md) represents an index range, which will be intersected by the API call. The cursor that is given in **JET_INDEXRANGE** must have a valid index range set on it already, with a successful call to [JetSetIndexRange](./jetsetindexrange-function.md).

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_COLUMNID](./jet-columnid.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetIntersectIndexes](./jetintersectindexes-function.md)  
[JetSetIndexRange](./jetsetindexrange-function.md)
