---
UID: NS:dstorage.DSTORAGE_QUEUE_DESC1
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_QUEUE_DESC1
ms.date: 10/30/2026
targetos: Windows
description: Contains the properties of a DirectStorage queue for the queue's creation, including the compression format that the queue services.
prerelease: true
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
 - DSTORAGE_QUEUE_DESC1
f1_keywords:
 - DSTORAGE_QUEUE_DESC1
 - dstorage/DSTORAGE_QUEUE_DESC1
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_QUEUE_DESC1
---

# DSTORAGE_QUEUE_DESC1 structure (dstorage.h)

Contains the properties of a DirectStorage queue for the queue's creation, including the compression format that the queue services.

## Syntax

```cpp
struct DSTORAGE_QUEUE_DESC1 {
  DSTORAGE_REQUEST_SOURCE_TYPE SourceType;
  UINT16                       Capacity;
  DSTORAGE_PRIORITY            Priority;
  const CHAR                   *Name;
  ID3D12Device                 *Device;
  DSTORAGE_COMPRESSION_FORMAT  CompressionFormat;
  BOOL                         UsesGaclShuffleTransform;
};
```

## Members

`SourceType`

Type: **[DSTORAGE_REQUEST_SOURCE_TYPE](ne-dstorage-dstorage_request_source_type.md)**

The source type of requests that this DirectStorage queue can accept.

`Capacity`

The maximum number of requests that the queue can hold.

`Priority`

Type: **[DSTORAGE_PRIORITY](ne-dstorage-dstorage_priority.md)**

The priority of the requests in this queue.

`Name`

Optional name of the queue. Used for debugging.

`Device`

Type: **[ID3D12Device](/windows/win32/api/d3d12/nn-d3d12-id3d12device) \***

Optional device to use for writing to destination resources, and performing GPU decompression. The destination resource's device must match this device.

This member may be null. If you specify a null device, then the destination type must be [DSTORAGE_REQUEST_DESTINATION_MEMORY](ne-dstorage-dstorage_request_destination_type.md).

`CompressionFormat`

Type: **[DSTORAGE_COMPRESSION_FORMAT](ne-dstorage-dstorage_compression_format.md)**

A [DSTORAGE_COMPRESSION_FORMAT](ne-dstorage-dstorage_compression_format.md) enum value that specifies the compression format serviced by the queue.

`UsesGaclShuffleTransform`

Specifies whether the queue submits requests that use a GACL shuffle transform. Requires `CompressionFormat` to be `DSTORAGE_COMPRESSION_FORMAT_ZSTD` and a non-null `Device`.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
