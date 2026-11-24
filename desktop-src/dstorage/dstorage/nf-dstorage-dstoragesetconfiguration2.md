---
UID: NF:dstorage.DStorageSetConfiguration2
ms.topic: reference
tech.root: dstorage
title: DStorageSetConfiguration2
ms.date: 10/30/2026
targetos: Windows
description: Configures DirectStorage, with an additional option to specify a global CreatorID for the Direct3D 12 command queues that DirectStorage creates.
prerelease: true
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
 - DStorageSetConfiguration2
f1_keywords:
 - DStorageSetConfiguration2
 - dstorage/DStorageSetConfiguration2
dev_langs:
 - c++
helpviewer_keywords:
 - DStorageSetConfiguration2
---

# DStorageSetConfiguration2 function (dstorage.h)

Configures DirectStorage, with an additional option to specify a global CreatorID for the Direct3D 12 command queues that DirectStorage creates. You must call **DStorageSetConfiguration2** before your first call to [DStorageGetFactory](nf-dstorage-dstoragegetfactory.md). If you don't, then default values are used.

## Syntax

```cpp
HRESULT DStorageSetConfiguration2(
  DSTORAGE_CONFIGURATION2 const *configuration
);
```

## Parameters

`configuration`

Type: **[DSTORAGE_CONFIGURATION2](ns-dstorage-dstorage_configuration2.md) const \***

Specifies the configuration.

## Return value

Standard HRESULT error code. The configuration can be changed only when no queue is created and no files are open; otherwise, **E_DSTORAGE_STAGING_BUFFER_LOCKED** is returned.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
