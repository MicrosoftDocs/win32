---
UID: NS:dstorage.DSTORAGE_DESTINATION_BUFFER
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_DESTINATION_BUFFER
ms.date: 08/25/2022
targetos: Windows
description: Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_BUFFER](ne-dstorage-dstorage_request_destination_type.md).
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
 - DSTORAGE_DESTINATION_BUFFER
f1_keywords:
 - DSTORAGE_DESTINATION_BUFFER
 - dstorage/DSTORAGE_DESTINATION_BUFFER
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_DESTINATION_BUFFER
---

# DSTORAGE_DESTINATION_BUFFER structure (dstorage.h)

Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_BUFFER](ne-dstorage-dstorage_request_destination_type.md).

## Syntax

```cpp
struct DSTORAGE_DESTINATION_BUFFER {
  ID3D12Resource *Resource;
  UINT64         Offset;
  UINT32         Size;
};
```

## Members

`Resource`

Address of the resource to receive the final result of this request.

`Offset`

The offset, in bytes, in the buffer resource to write into.

`Size`

Number of bytes to write to the destination buffer.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
