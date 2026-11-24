---
UID: NE:dstorage.DSTORAGE_COMPRESSION_FORMAT
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_COMPRESSION_FORMAT
ms.date: 11/21/2026
targetos: Windows
description: Defines constants that specify the type of compression format used at the decompression stage.
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
 - DSTORAGE_COMPRESSION_FORMAT
f1_keywords:
 - DSTORAGE_COMPRESSION_FORMAT
 - dstorage/DSTORAGE_COMPRESSION_FORMAT
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_COMPRESSION_FORMAT
---

# DSTORAGE_COMPRESSION_FORMAT enumeration (dstorage.h)

Defines constants that specify the type of compression format used at the decompression stage. Your application can implement custom decompressors, starting from **DSTORAGE_CUSTOM_COMPRESSION_0**.

## Syntax

```cpp
enum DSTORAGE_COMPRESSION_FORMAT : UINT8 {
  DSTORAGE_COMPRESSION_FORMAT_NONE = 0,
  DSTORAGE_COMPRESSION_FORMAT_GDEFLATE = 1,
  DSTORAGE_COMPRESSION_FORMAT_ZSTD = 2,
  DSTORAGE_COMPRESSION_FORMAT_UNSPECIFIED = 0x7F,
  DSTORAGE_CUSTOM_COMPRESSION_0 = 0x80
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_COMPRESSION_FORMAT_NONE` <br> Specifies that the data is uncompressed.|
| `DSTORAGE_COMPRESSION_FORMAT_GDEFLATE` <br> Specifies that the data is compressed using the built-in *GDeflate* format; intended to be decompressed by using the GPU.|
| `DSTORAGE_COMPRESSION_FORMAT_ZSTD` <br> Specifies that the data is compressed using the built-in Zstd format. DirectStorage decompresses only the first data frame in each Zstd request and ignores any subsequent frames. A Zstd request requires a queue created with [IDStorageFactory1::CreateQueue1](nf-dstorage-idstoragefactory1-createqueue1.md) that declares `DSTORAGE_COMPRESSION_FORMAT_ZSTD`.|
| `DSTORAGE_COMPRESSION_FORMAT_UNSPECIFIED` <br> Specifies that no compression format was declared for the queue. This value is output-only (reported by [IDStorageQueue4::Query1](nf-dstorage-idstoragequeue4-query1.md)) and is not valid for requests or queue creation.|
| `DSTORAGE_CUSTOM_COMPRESSION_0` <br> Specifies that the data is stored in an application-defined custom format. Your application must use [IDStorageCustomDecompressionQueue](nn-dstorage-idstoragecustomdecompressionqueue.md) to implement custom decompression. You can use additional custom compression formats; for example, `(DSTORAGE_CUSTOM_COMPRESSION_0 + 1)`.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
