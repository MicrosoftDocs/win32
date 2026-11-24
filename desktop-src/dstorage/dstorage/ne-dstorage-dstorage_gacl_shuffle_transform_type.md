---
UID: NE:dstorage.DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE
ms.date: 10/30/2026
targetos: Windows
description: Defines the Game Asset Conditioning Library (GACL) shuffle transform that DirectStorage reverses after decompression.
prerelease: true
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
 - DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE
f1_keywords:
 - DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE
 - dstorage/DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE
---

# DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE enumeration (dstorage.h)

Specifies the [Game Asset Conditioning Library (GACL)](https://github.com/microsoft/Game-Asset-Conditioning-Library) shuffle transform applied to the source data. DirectStorage reverses the transform after decompression, before writing the data to the destination.

## Syntax

```cpp
enum DSTORAGE_GACL_SHUFFLE_TRANSFORM_TYPE : UINT8 {
  DSTORAGE_GACL_SHUFFLE_TRANSFORM_NONE = 0,
  DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC1 = 1,
  DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC3 = 2,
  DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC4 = 3,
  DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC5 = 4,
  DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC7 = 5
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_GACL_SHUFFLE_TRANSFORM_NONE` <br> Specifies that no GACL shuffle transform was applied.|
| `DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC1` <br> Specifies the GACL shuffle transform for BC1 data.|
| `DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC3` <br> Specifies the GACL shuffle transform for BC3 data.|
| `DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC4` <br> Specifies the GACL shuffle transform for BC4 data.|
| `DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC5` <br> Specifies the GACL shuffle transform for BC5 data.|
| `DSTORAGE_GACL_SHUFFLE_TRANSFORM_BC7` <br> Specifies the GACL shuffle transform for BC7 data.|

## Remarks

A GACL shuffle transform requires `DSTORAGE_COMPRESSION_FORMAT_ZSTD`. The transform is performed on the GPU and requires a Direct3D 12 device. A request that specifies a transform other than `DSTORAGE_GACL_SHUFFLE_TRANSFORM_NONE` fails if its `CompressionFormat` is not `DSTORAGE_COMPRESSION_FORMAT_ZSTD`, if its destination is system memory, if its queue wasn't created with `UsesGaclShuffleTransform` set to `TRUE`, or if the queue's device does not support GACL shuffle transforms or DirectStorage could not create the transform's resources.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
