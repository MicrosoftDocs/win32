---
UID: NE:dstorage.DSTORAGE_REQUEST_SOURCE_TYPE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_REQUEST_SOURCE_TYPE
ms.date: 08/25/2022
targetos: Windows
description: Defines constants that specify the source type of a DirectStorage request.
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
 - DSTORAGE_REQUEST_SOURCE_TYPE
f1_keywords:
 - DSTORAGE_REQUEST_SOURCE_TYPE
 - dstorage/DSTORAGE_REQUEST_SOURCE_TYPE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_REQUEST_SOURCE_TYPE
---

# DSTORAGE_REQUEST_SOURCE_TYPE enumeration (dstorage.h)

Defines constants that specify the source type of a DirectStorage request.

## Syntax

```cpp
enum DSTORAGE_REQUEST_SOURCE_TYPE {
  DSTORAGE_REQUEST_SOURCE_FILE,
  DSTORAGE_REQUEST_SOURCE_MEMORY
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_REQUEST_SOURCE_FILE` <br> Specifies that the source of the DirectStorage request is a file. |
| `DSTORAGE_REQUEST_SOURCE_MEMORY` <br> Specifies that the source of the DirectStorage request is a block of memory. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
