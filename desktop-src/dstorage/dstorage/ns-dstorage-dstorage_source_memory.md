---
UID: NS:dstorage.DSTORAGE_SOURCE_MEMORY
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_SOURCE_MEMORY
ms.date: 08/25/2022
targetos: Windows
description: Describes a source for a request with *SourceType* [DSTORAGE_REQUEST_SOURCE_MEMORY](ne-dstorage-dstorage_request_source_type.md).
prerelease: false
req.construct-type: structure
req.ddi-compliance: 
req.dll: 
req.header: dstorage.h
req.include-header: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - dstorage.h
api_name:
 - DSTORAGE_SOURCE_MEMORY
f1_keywords:
 - DSTORAGE_SOURCE_MEMORY
 - dstorage/DSTORAGE_SOURCE_MEMORY
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_SOURCE_MEMORY
---

# DSTORAGE_SOURCE_MEMORY structure (dstorage.h)

Describes a source for a request with *SourceType* [DSTORAGE_REQUEST_SOURCE_MEMORY](ne-dstorage-dstorage_request_source_type.md).

## Syntax

```cpp
struct DSTORAGE_SOURCE_MEMORY {
  void const *Source;
  UINT32     Size;
};
```

## Members

`Source`

Address of the source buffer to be read from.

`Size`

Number of bytes to read from the source buffer.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
