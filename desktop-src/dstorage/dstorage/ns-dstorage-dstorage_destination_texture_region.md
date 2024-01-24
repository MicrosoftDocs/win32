---
UID: NS:dstorage.DSTORAGE_DESTINATION_TEXTURE_REGION
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_DESTINATION_TEXTURE_REGION
ms.date: 08/25/2022
targetos: Windows
description: Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_TEXTURE_REGION](ne-dstorage-dstorage_request_destination_type.md).
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
 - DSTORAGE_DESTINATION_TEXTURE_REGION
f1_keywords:
 - DSTORAGE_DESTINATION_TEXTURE_REGION
 - dstorage/DSTORAGE_DESTINATION_TEXTURE_REGION
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_DESTINATION_TEXTURE_REGION
---

# DSTORAGE_DESTINATION_TEXTURE_REGION structure (dstorage.h)

Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_TEXTURE_REGION](ne-dstorage-dstorage_request_destination_type.md).

## Syntax

```cpp
struct DSTORAGE_DESTINATION_TEXTURE_REGION {
  ID3D12Resource *Resource;
  UINT           SubresourceIndex;
  D3D12_BOX      Region;
};
```

## Members

`Resource`

Address of the resource to receive the final result of this request.

`SubresourceIndex`

Describes the destination texture copy location. The subresource referred to must be in the [D3D12_RESOURCE_STATE_COMMON](/windows/win32/api/d3d12/ne-d3d12-d3d12_resource_states) state.

`Region`

Coordinates and size of the destination region to copy, in pixels.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
