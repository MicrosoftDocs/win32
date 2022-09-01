---
UID: NF:dstorage.IDStorageFactory.SetStagingBufferSize
ms.topic: reference
tech.root: dstorage
title: IDStorageFactory::SetStagingBufferSize
ms.date: 08/25/2022
targetos: Windows
description: Sets the size of staging buffer(s) used to temporarily store content loaded from the storage device before they are decompressed.
prerelease: false
req.assembly: 
req.construct-type: function
req.ddi-compliance: 
req.dll: 
req.header: dstorage.h
req.idl: 
req.include-header: 
req.irql: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - dstorage.h
api_name:
 - IDStorageFactory::SetStagingBufferSize
f1_keywords:
 - IDStorageFactory::SetStagingBufferSize
 - dstorage/IDStorageFactory::SetStagingBufferSize
dev_langs:
 - c++
helpviewer_keywords:
 - SetStagingBufferSize
---

# IDStorageFactory::SetStagingBufferSize method (dstorage.h)

Sets the size of staging buffer(s) used to temporarily store content loaded from the storage device before they are decompressed. If only uncompressed memory sourced queues writing to cpu memory destinations are used, then the staging buffer may be 0-sized.

## Syntax

```cpp
HRESULT SetStagingBufferSize(
  UINT32 size
);
```

## Parameters

`size`

Size, in bytes, of each staging buffer used to complete a request.

## Return value

Standard HRESULT error code.

## Remarks

The default staging buffer is [DSTORAGE_STAGING_BUFFER_SIZE_32MB](ne-dstorage-dstorage_staging_buffer_size.md). If multiple staging buffers are necessary to complete a request, then each separate staging buffer is allocated to this staging buffer size.

If the destination is a GPU resource, then some but not all of the staging buffers will be allocated from VRAM.

Requests that exceed the specified size to **SetStagingBufferSize** will fail.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
