---
UID: NE:dstorage.DSTORAGE_STAGING_BUFFER_SIZE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_STAGING_BUFFER_SIZE
ms.date: 08/25/2022
targetos: Windows
description: Defines constants that specify common staging buffer sizes.
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
 - DSTORAGE_STAGING_BUFFER_SIZE
f1_keywords:
 - DSTORAGE_STAGING_BUFFER_SIZE
 - dstorage/DSTORAGE_STAGING_BUFFER_SIZE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_STAGING_BUFFER_SIZE
---

# DSTORAGE_STAGING_BUFFER_SIZE enumeration (dstorage.h)

Defines constants that specify common staging buffer sizes.

## Syntax

```cpp
enum DSTORAGE_STAGING_BUFFER_SIZE {
  DSTORAGE_STAGING_BUFFER_SIZE_0,
  DSTORAGE_STAGING_BUFFER_SIZE_32MB
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_STAGING_BUFFER_SIZE_0` <br> Specifies that there is no staging buffer. Use this value to force DirectStorage to deallocate any memory it has allocated for staging buffers.|
| `DSTORAGE_STAGING_BUFFER_SIZE_32MB` <br> Specifies the default staging buffer size of 32MB.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
