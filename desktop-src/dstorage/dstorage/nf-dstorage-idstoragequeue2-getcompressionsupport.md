---
UID: NF:dstorage.IDStorageQueue2.GetCompressionSupport
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue2::GetCompressionSupport
ms.date: 03/07/2023
targetos: Windows
description: Retrieves support information about the queue for a specified compression format.
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
 - IDStorageQueue2::GetCompressionSupport
f1_keywords:
 - IDStorageQueue2::GetCompressionSupport
 - dstorage/IDStorageQueue2::GetCompressionSupport
dev_langs:
 - c++
helpviewer_keywords:
 - GetCompressionSupport
---

# IDStorageQueue2::GetCompressionSupport method (dstorage.h)

Retrieves support information about the queue for a specified compression format. Includes the chosen path that the DirectStorage runtime will take when decompressing content. That info is useful if the title wants to take a different loading path based on things such as CPU decompression being used over GPU decompression.

## Syntax

```cpp
DSTORAGE_COMPRESSION_SUPPORT GetCompressionSupport(
  DSTORAGE_COMPRESSION_FORMAT format
);
```

## Parameters

`format`

Type: **[DSTORAGE_COMPRESSION_FORMAT](/windows/win32/dstorage/dstorage/ne-dstorage-dstorage_compression_format)**

Specifies the compression format about which to retrieve information.

## Return value

Type: **[DSTORAGE_COMPRESSION_SUPPORT](/windows/win32/dstorage/dstorage/ne-dstorage-dstorage_compression_support)**

Tells the title exactly how the runtime has configured itself for decompressing content&mdash;whether it's using the optimized path, the fallback shader path, or has dropped all the way down to CPU fallback path.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
