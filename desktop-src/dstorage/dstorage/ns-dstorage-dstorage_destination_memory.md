---
UID: NS:dstorage.DSTORAGE_DESTINATION_MEMORY
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_DESTINATION_MEMORY
ms.date: 08/25/2022
targetos: Windows
description: Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_MEMORY](ne-dstorage-dstorage_request_destination_type.md).
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
 - DSTORAGE_DESTINATION_MEMORY
f1_keywords:
 - DSTORAGE_DESTINATION_MEMORY
 - dstorage/DSTORAGE_DESTINATION_MEMORY
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_DESTINATION_MEMORY
---

# DSTORAGE_DESTINATION_MEMORY structure (dstorage.h)

Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_MEMORY](ne-dstorage-dstorage_request_destination_type.md).

## Syntax

```cpp
struct DSTORAGE_DESTINATION_MEMORY {
  void   *Buffer;
  UINT32 Size;
};
```

## Members

`Buffer`

Address of the buffer to receive the final result of this request.

`Size`

Number of bytes to write to the destination buffer.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
