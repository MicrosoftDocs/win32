---
UID: NS:dstorage.DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST
ms.date: 08/25/2022
targetos: Windows
description: A custom decompression request. Use [IDStorageCustomDecompressionQueue](nn-dstorage-idstoragecustomdecompressionqueue.md) to retrieve these requests.
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
 - DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST
f1_keywords:
 - DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST
 - dstorage/DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST
---

# DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST structure (dstorage.h)

A custom decompression request. Use [IDStorageCustomDecompressionQueue](nn-dstorage-idstoragecustomdecompressionqueue.md) to retrieve these requests.

## Syntax

```cpp
struct DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST {
  UINT64                              Id;
  DSTORAGE_COMPRESSION_FORMAT         CompressionFormat;
  UINT8                               Reserved[3];
  DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS Flags;
  UINT64                              SrcSize;
  void const                          *SrcBuffer;
  UINT64                              DstSize;
  void                                *DstBuffer;
};
```

## Members

`Id`

An identifier provided by DirectStorage. This should be used to identify the request in [DSTORAGE_CUSTOM_DECOMPRESSION_RESULT](ns-dstorage-dstorage_custom_decompression_result.md). This identifier is unique among uncompleted requests, but may be reused after a request has completed.

`CompressionFormat`

The compression format. This will be >= [DSTORAGE_CUSTOM_COMPRESSION_0](ne-dstorage-dstorage_compression_format.md).

`Reserved`

Reserved for future use.

`Flags`

Flags containing additional details about the decompression request.

`SrcSize`

The size of *SrcBuffer* in bytes.

`SrcBuffer`

The compressed source buffer.

`DstSize`

The size of *DstBuffer* in bytes.

`DstBuffer`

The uncompressed destination buffer. *SrcBuffer* should be decompressed to *DstBuffer*.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
