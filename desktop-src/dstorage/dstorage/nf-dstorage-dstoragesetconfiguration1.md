---
UID: NF:dstorage.DStorageSetConfiguration1
ms.topic: reference
tech.root: dstorage
title: DStorageSetConfiguration1
ms.date: 03/06/2023
targetos: Windows
description: Configures DirectStorage; with an additional option to enable file buffering.
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
 - DStorageSetConfiguration1
f1_keywords:
 - DStorageSetConfiguration1
 - dstorage/DStorageSetConfiguration1
dev_langs:
 - c++
helpviewer_keywords:
 - DStorageSetConfiguration1
---

# DStorageSetConfiguration1 function (dstorage.h)

Configures DirectStorage; with an additional option to enable file buffering. You must call **DStorageSetConfiguration1** before your first call to [DStorageGetFactory](nf-dstorage-dstoragegetfactory.md). If you don't, then default values are used.

## Syntax

```cpp
HRESULT DStorageSetConfiguration1(
  DSTORAGE_CONFIGURATION1 const *configuration
);
```

## Parameters

`configuration`

Type: **[DSTORAGE_CONFIGURATION1](ns-dstorage-dstorage_configuration1.md1**

Specifies the configuration.

## Return value

Standard HRESULT error code. The configuration can be changed only when no queue is created and no files are open; otherwise, **E_DSTORAGE_STAGING_BUFFER_LOCKED** is returned.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
