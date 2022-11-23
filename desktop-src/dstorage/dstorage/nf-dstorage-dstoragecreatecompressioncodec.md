---
UID: NF:dstorage.DStorageCreateCompressionCodec
ms.topic: reference
tech.root: dstorage
title: DStorageCreateCompressionCodec
ms.date: 08/25/2022
targetos: Windows
description: Retrieves a DirectStorage object used to compress/decompress content.
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
 - DllExport
api_location:
 - dstorage.h
api_name:
 - DStorageCreateCompressionCodec
f1_keywords:
 - DStorageCreateCompressionCodec
 - dstorage/DStorageCreateCompressionCodec
dev_langs:
 - c++
helpviewer_keywords:
 - DStorageCreateCompressionCodec
---

# DStorageCreateCompressionCodec function (dstorage.h)

Retrieves a DirectStorage object used to compress/decompress content. Compression codecs are not thread safe, so multiple instances are required if the codecs need to be used by multiple threads.

## Syntax

```cpp
HRESULT DStorageCreateCompressionCodec(
  DSTORAGE_COMPRESSION_FORMAT format,
  UINT32 numThreads,
  REFIID riid,
  void   **ppv
);
```

## Parameters

`format`

Type: **[DSTORAGE_COMPRESSION_FORMAT](ne-dstorage-dstorage_compression_format.md)**

Specifies how the data is compressed.

`numThreads`

Specifies the maximum number of threads that this codec will use. Specifying 0 means to use the system's best guess at a good value.

`riid`

Specifies the DirectStorage compressor/decompressor interface, such as `__uuidof(IDStorageCompressionCodec)`.

`ppv`

Receives the DirectStorage factory object.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
