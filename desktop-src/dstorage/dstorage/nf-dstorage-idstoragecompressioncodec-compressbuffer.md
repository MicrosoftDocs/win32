---
UID: NF:dstorage.IDStorageCompressionCodec.CompressBuffer
ms.topic: reference
tech.root: dstorage
title: IDStorageCompressionCodec::CompressBuffer
ms.date: 11/22/2022
targetos: Windows
description: Compresses a buffer of data using a known compression format at the specified compression level.
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
 - IDStorageCompressionCodec::CompressBuffer
f1_keywords:
 - IDStorageCompressionCodec::CompressBuffer
 - dstorage/IDStorageCompressionCodec::CompressBuffer
dev_langs:
 - c++
helpviewer_keywords:
 - GetRequests
---

# IDStorageCompressionCodec::CompressBuffer method (dstorage.h)

Compresses a buffer of data using a known compression format at the specified compression level.

## Syntax

```cpp
HRESULT CompressBuffer(
  const void*          uncompressedData,
  size_t               uncompressedDataSize,
  DSTORAGE_COMPRESSION compressionSetting,
  void*                compressedBuffer,
  size_t               compressedBufferSize,
  size_t*              compressedDataSize
);
```

## Parameters

`uncompressedData`

Points to a buffer containing uncompressed data.

`uncompressedDataSize`

Size, in bytes, of the uncompressed data buffer.

`compressionSetting`

Type: **[DSTORAGE_COMPRESSION](ne-dstorage-dstorage_compression.md)**

Specifies the compression settings to use.

`compressedBuffer`

Points to a buffer where compressed data will be written.

`compressedBufferSize`

Size, in bytes, of the buffer that will receive the compressed data.

`compressedDataSize`

Size, in bytes, of the actual data written to *compressedBuffer*.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
