---
UID: NE:dstorage.DSTORAGE_DEBUG
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_DEBUG
ms.date: 08/25/2022
targetos: Windows
description: Defines constants that specify flags for controlling the DirectStorage debug layer.
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
 - DSTORAGE_DEBUG
f1_keywords:
 - DSTORAGE_DEBUG
 - dstorage/DSTORAGE_DEBUG
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_DEBUG
---

# DSTORAGE_DEBUG enumeration (dstorage.h)

Defines constants that specify flags for controlling the DirectStorage debug layer.

## Syntax

```cpp
enum DSTORAGE_DEBUG {
  DSTORAGE_DEBUG_NONE,
  DSTORAGE_DEBUG_SHOW_ERRORS,
  DSTORAGE_DEBUG_BREAK_ON_ERROR,
  DSTORAGE_DEBUG_RECORD_OBJECT_NAMES
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_DEBUG_NONE` <br> Specifies that the DirectStorage debug layer is disabled. |
| `DSTORAGE_DEBUG_SHOW_ERRORS` <br> Specifies print error information to a debugger. |
| `DSTORAGE_DEBUG_BREAK_ON_ERROR` <br> Specifies to trigger a debug break each time an error is detected. |
| `DSTORAGE_DEBUG_RECORD_OBJECT_NAMES` <br> Specifies to include object names in Event Tracing for Windows (ETW) events. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
