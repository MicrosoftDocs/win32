---
UID: NE:dstorage.DSTORAGE_REQUEST_DESTINATION_TYPE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_REQUEST_DESTINATION_TYPE
ms.date: 08/25/2022
targetos: Windows
description: Defines constants that specify the destination type of a DirectStorage request.
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
 - DSTORAGE_REQUEST_DESTINATION_TYPE
f1_keywords:
 - DSTORAGE_REQUEST_DESTINATION_TYPE
 - dstorage/DSTORAGE_REQUEST_DESTINATION_TYPE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_REQUEST_DESTINATION_TYPE
---

# DSTORAGE_REQUEST_DESTINATION_TYPE enumeration (dstorage.h)

Defines constants that specify the destination type of a DirectStorage request.

## Syntax

```cpp
enum DSTORAGE_REQUEST_DESTINATION_TYPE {
  DSTORAGE_REQUEST_DESTINATION_MEMORY,
  DSTORAGE_REQUEST_DESTINATION_BUFFER,
  DSTORAGE_REQUEST_DESTINATION_TEXTURE_REGION,
  DSTORAGE_REQUEST_DESTINATION_MULTIPLE_SUBRESOURCES,
  DSTORAGE_REQUEST_DESTINATION_TILES
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_REQUEST_DESTINATION_MEMORY` <br> Specifies that the destination of the DirectStorage request is a block of memory. |
| `DSTORAGE_REQUEST_DESTINATION_BUFFER` <br> Specifies that the destination of the DirectStorage request is an [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) that is a buffer.|
| `DSTORAGE_REQUEST_DESTINATION_TEXTURE_REGION` <br> Specifies that the destination of the DirectStorage request is an [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) that is a texture.|
| `DSTORAGE_REQUEST_DESTINATION_MULTIPLE_SUBRESOURCES` <br> Specifies that the destination of the DirectStorage request is an [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) that is a texture that will receive all subresources in a single request.|
| `DSTORAGE_REQUEST_DESTINATION_TILES` <br> Specifies that the destination of the DirectStorage request is an [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) that is tiled.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
