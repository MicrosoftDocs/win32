---
UID: NF:dstorage.IDStorageCompressionCodec.DecompressBuffer
ms.topic: reference
tech.root: dstorage
title: IDStorageCompressionCodec::DecompressBuffer
ms.date: 11/22/2022
targetos: Windows
description: Decompresses data previously compressed using [CompressBuffer](nf-dstorage-idstoragecompressioncodec-compressbuffer.md).
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
 - IDStorageCompressionCodec::DecompressBuffer
f1_keywords:
 - IDStorageCompressionCodec::DecompressBuffer
 - dstorage/IDStorageCompressionCodec::DecompressBuffer
dev_langs:
 - c++
helpviewer_keywords:
 - GetRequests
---

# IDStorageCompressionCodec::DecompressBuffer method (dstorage.h)

Decompresses data previously compressed using [CompressBuffer](nf-dstorage-idstoragecompressioncodec-compressbuffer.md).

## Syntax

```cpp
HRESULT DecompressBuffer(
  const void*          compressedData,
  size_t               compressedDataSize,
  void*                uncompressedBuffer,
  size_t               uncompressedBufferSize,
  size_t*              uncompressedDataSize
);
```

## Parameters

`compressedData`

Points to a buffer containing compressed data.

`compressedDataSize`

Size, in bytes, of the compressed data buffer.

`uncompressedBuffer`

Points to a buffer where uncompressed data will be written.

`uncompressedBufferSize`

Size, in bytes, of the buffer that will receive the uncompressed data.

`uncompressedDataSize`

Size, in bytes, of the actual data written to *uncompressedBuffer*.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
