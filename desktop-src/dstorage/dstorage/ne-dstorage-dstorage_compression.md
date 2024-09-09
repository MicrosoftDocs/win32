---
UID: NE:dstorage.DSTORAGE_COMPRESSION
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_COMPRESSION
ms.date: 11/22/2022
targetos: Windows
description: Defines constants that specify DirectStorage compression codec behavior.
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
 - DSTORAGE_COMPRESSION
f1_keywords:
 - DSTORAGE_COMPRESSION
 - dstorage/DSTORAGE_COMPRESSION
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_COMPRESSION
---

# DSTORAGE_COMPRESSION enumeration (dstorage.h)

Defines constants that specify DirectStorage compression codec behavior.

## Syntax

```cpp
enum DSTORAGE_COMPRESSION : INT32 {
  DSTORAGE_COMPRESSION_FASTEST = -1,
  DSTORAGE_COMPRESSION_DEFAULT = 0,
  DSTORAGE_COMPRESSION_BEST_RATIO = 1
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_COMPRESSION_FASTEST` <br> Specifies compressing data at a fast rate that might not yield the best compression ratio.|
| `DSTORAGE_COMPRESSION_DEFAULT` <br> Specifies compressing data at an average rate with a good compression ratio.|
| `DSTORAGE_COMPRESSION_BEST_RATIO` <br> Specifies compressing data at a slow rate with the best compression ratio.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
