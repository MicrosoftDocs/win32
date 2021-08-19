---
description: "Learn more about: JET_GRBIT"
title: JET_GRBIT
TOCTitle: JET_GRBIT
ms:assetid: b72548cf-3ca2-4ba5-b07a-35eb7e85ed2b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294066(v=EXCHG.10)
ms:contentKeyID: 32765681
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

# JET_GRBIT


_**Applies to:** Windows | Windows Server_

## JET_GRBIT

The **JET_GRBIT** data type is a group of bits that contain constants that are specific to the functions and structures in which it is used.

```cpp
typedef unsigned long JET_GRBIT;
```

### Data Types

JET_GRBIT

In general, the constants that are used as values for this data type reflect the name of the API element in which they are used. For example, all constants passed to [JetRetrieveColumn](./jetretrievecolumn-function.md) begin with "JET_bitRetrieve". Similarly, all constants passed to [JetSetColumn](./jetsetcolumn-function.md) begin with "JET_bitSet".

A value of zero causes the parameter to be ignored.

### Remarks

For more information, see the specific function or structure. The options are usually passed as a set of flags that can be combined.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetRetrieveColumn](./jetretrievecolumn-function.md)  
[JetSetColumn](./jetsetcolumn-function.md)
