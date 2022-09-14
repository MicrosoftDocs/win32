---
UID: NS:dstorage.DSTORAGE_SOURCE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_SOURCE
ms.date: 08/25/2022
targetos: Windows
description: Describes the source specified for a DirectStorage request.
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
 - DSTORAGE_SOURCE
f1_keywords:
 - DSTORAGE_SOURCE
 - dstorage/DSTORAGE_SOURCE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_SOURCE
---

# DSTORAGE_SOURCE union (dstorage.h)

Describes the source specified for a DirectStorage request. For a request, the value of `request.Options.SourceType` determines which of these union fields is active. See [IDStorageQueue::EnqueueRequest](nf-dstorage-idstoragequeue-enqueuerequest.md).

## Syntax

```cpp
union DSTORAGE_SOURCE {
  DSTORAGE_SOURCE_MEMORY Memory;
  DSTORAGE_SOURCE_FILE   File;
};
```

## Members

`Memory`

See [DSTORAGE_SOURCE_MEMORY](ns-dstorage-dstorage_source_memory.md).

`File`

See [DSTORAGE_SOURCE_FILE](ns-dstorage-dstorage_source_file.md).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
