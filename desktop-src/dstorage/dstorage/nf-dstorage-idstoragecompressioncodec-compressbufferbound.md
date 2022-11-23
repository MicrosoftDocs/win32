---
UID: NF:dstorage.IDStorageCompressionCodec.CompressBufferBound
ms.topic: reference
tech.root: dstorage
title: IDStorageCompressionCodec::CompressBufferBound
ms.date: 11/22/2022
targetos: Windows
description: Retrieves an upper bound estimated size, in bytes, required to compress the specified data size.
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
 - IDStorageCompressionCodec::CompressBufferBound
f1_keywords:
 - IDStorageCompressionCodec::CompressBufferBound
 - dstorage/IDStorageCompressionCodec::CompressBufferBound
dev_langs:
 - c++
helpviewer_keywords:
 - GetRequests
---

# IDStorageCompressionCodec::CompressBufferBound method (dstorage.h)

Retrieves an upper bound estimated size, in bytes, required to compress the specified data size.

## Syntax

```cpp
size_t CompressBufferBound(
  size_t uncompressedDataSize
);
```

## Parameters

`uncompressedDataSize`

Size, in bytes, of the data to be compressed.

## Return value

An upper bound estimated size, in bytes, required to compress the specified data size.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
