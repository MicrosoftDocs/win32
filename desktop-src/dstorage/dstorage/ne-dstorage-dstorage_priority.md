---
UID: NE:dstorage.DSTORAGE_PRIORITY
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_PRIORITY
ms.date: 08/25/2022
targetos: Windows
description: Defines constants that specify the priority of a DirectStorage queue.
prerelease: false
req.construct-type: enumeration
req.ddi-compliance: 
req.header: dstorage.h
req.include-header: 
req.kmdf-ver: 
req.max-support: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - dstorage.h
api_name:
 - DSTORAGE_PRIORITY
f1_keywords:
 - DSTORAGE_PRIORITY
 - dstorage/DSTORAGE_PRIORITY
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_PRIORITY
---

# DSTORAGE_PRIORITY enumeration (dstorage.h)

Defines constants that specify the priority of a DirectStorage queue.

## Syntax

```cpp
enum DSTORAGE_PRIORITY {
  DSTORAGE_PRIORITY_LOW,
  DSTORAGE_PRIORITY_NORMAL,
  DSTORAGE_PRIORITY_HIGH,
  DSTORAGE_PRIORITY_REALTIME,
  DSTORAGE_PRIORITY_FIRST,
  DSTORAGE_PRIORITY_LAST,
  DSTORAGE_PRIORITY_COUNT
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_PRIORITY_LOW`<br> Specifies low priority.|
| `DSTORAGE_PRIORITY_NORMAL`<br>  Specifies normal priority.|
| `DSTORAGE_PRIORITY_HIGH`<br>  Specifies high priority.|
| `DSTORAGE_PRIORITY_REALTIME`<br>  Specifies real-time priority.|
| `DSTORAGE_PRIORITY_FIRST` <br> These values can be used for iterating over all priority levels. |
| `DSTORAGE_PRIORITY_LAST` <br> These values can be used for iterating over all priority levels. |
| `DSTORAGE_PRIORITY_COUNT` <br> These values can be used for iterating over all priority levels. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
