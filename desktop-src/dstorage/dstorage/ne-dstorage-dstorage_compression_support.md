---
UID: NE:dstorage.DSTORAGE_COMPRESSION_SUPPORT
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_COMPRESSION_SUPPORT
ms.date: 11/22/2022
targetos: Windows
description: Defines constants that specify features used by the runtime to decompress content.
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
 - DSTORAGE_COMPRESSION_SUPPORT
f1_keywords:
 - DSTORAGE_COMPRESSION_SUPPORT
 - dstorage/DSTORAGE_COMPRESSION_SUPPORT
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_COMPRESSION_SUPPORT
---

# DSTORAGE_COMPRESSION_SUPPORT enumeration (dstorage.h)

Defines constants that specify features used by the runtime to decompress content. Returned by [IDStorageQueue2::GetCompressionSupport](./nf-dstorage-idstoragequeue2-getcompressionsupport.md).

## Syntax

```cpp
enum DSTORAGE_COMPRESSION_SUPPORT : UINT32 {
  DSTORAGE_COMPRESSION_SUPPORT_NONE = 0,
  DSTORAGE_COMPRESSION_SUPPORT_GPU_OPTIMIZED = 1,
  DSTORAGE_COMPRESSION_SUPPORT_GPU_FALLBACK = 2,
  DSTORAGE_COMPRESSION_SUPPORT_CPU_FALLBACK = 4,
  DSTORAGE_COMPRESSION_SUPPORT_USES_COMPUTE_QUEUE = 8,
  DSTORAGE_COMPRESSION_SUPPORT_USES_COPY_QUEUE = 0x010
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_COMPRESSION_FORMAT_NONE` <br> Specifies no support.|
| `DSTORAGE_COMPRESSION_SUPPORT_GPU_OPTIMIZED` <br> Specifies optimized driver support for GPU decompression.|
| `DSTORAGE_COMPRESSION_SUPPORT_GPU_FALLBACK` <br> Specifies the built-in GPU decompression fallback shader. This can apply if optimized driver support isn't available and the D3D12 device used for this DirectStorage queue supports the required capabilities.|
| `DSTORAGE_COMPRESSION_SUPPORT_CPU_FALLBACK` <br> Specifies a CPU fallback implementation. This can apply if: optimized driver support and built-in GPU decompression isn't available; or GPU decompression support has been explicitly disabled using **DSTORAGE_CONFIGURATION**; or the DirectStorage runtime encounters a failure during initialization of its GPU decompression system..|
| `DSTORAGE_COMPRESSION_SUPPORT_USES_COMPUTE_QUEUE` <br> Specifies that work executes on a compute queue.|
| `DSTORAGE_COMPRESSION_SUPPORT_USES_COPY_QUEUE` <br> Specifies that work executes on a copy queue.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
