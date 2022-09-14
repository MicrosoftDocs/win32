---
UID: NE:dstorage.DSTORAGE_COMPRESSION_FORMAT
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_COMPRESSION_FORMAT
ms.date: 08/25/2022
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
enum DSTORAGE_COMPRESSION_FORMAT {
  DSTORAGE_COMPRESSION_FORMAT_NONE,
  DSTORAGE_COMPRESSION_FORMAT_1,
  DSTORAGE_CUSTOM_COMPRESSION_0
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_COMPRESSION_FORMAT_NONE` <br> Specifies that the data is uncompressed.|
| `DSTORAGE_COMPRESSION_FORMAT_1` <br> Placeholder; don't use.|
| `DSTORAGE_CUSTOM_COMPRESSION_0` <br> Specifies that the data is stored in an application-defined custom format. Your application must use [IDStorageCustomDecompressionQueue](nn-dstorage-idstoragecustomdecompressionqueue.md) to implement custom decompression. You can use additional custom compression formats; for example, `(DSTORAGE_CUSTOM_COMPRESSION_0 + 1)`.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
