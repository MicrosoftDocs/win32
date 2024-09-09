---
UID: NS:dstorage.DSTORAGE_DESTINATION_TILES
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_DESTINATION_TILES
ms.date: 08/25/2022
targetos: Windows
description: Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_TILES](ne-dstorage-dstorage_request_destination_type.md).
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
 - DSTORAGE_DESTINATION_TILES
f1_keywords:
 - DSTORAGE_DESTINATION_TILES
 - dstorage/DSTORAGE_DESTINATION_TILES
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_DESTINATION_TILES
---

# DSTORAGE_DESTINATION_TILES structure (dstorage.h)

Describes the destination for a request with [DSTORAGE_REQUEST_OPTIONS::DestinationType](ns-dstorage-dstorage_request_options.md) set to [DSTORAGE_REQUEST_DESTINATION_TILES](ne-dstorage-dstorage_request_destination_type.md).

## Syntax

```cpp
struct DSTORAGE_DESTINATION_TILES {
  ID3D12Resource                  *Resource;
  D3D12_TILED_RESOURCE_COORDINATE TiledRegionStartCoordinate;
  D3D12_TILE_REGION_SIZE          TileRegionSize;
};
```

## Members

`Resource`

Address of the resource to receive the final result of this request. The source buffer is expected to contain data arranged as if it were the source to a [CopyTiles](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copytiles) call with these parameters.

`TiledRegionStartCoordinate`

The starting coordinates of the tiled region.

`TileRegionSize`

The size of the tiled region.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
