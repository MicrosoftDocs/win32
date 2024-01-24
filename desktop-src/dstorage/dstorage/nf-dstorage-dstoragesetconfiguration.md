---
UID: NF:dstorage.DStorageSetConfiguration
ms.topic: reference
tech.root: dstorage
title: DStorageSetConfiguration
ms.date: 11/23/2022
targetos: Windows
description: Configures DirectStorage.
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
 - DStorageSetConfiguration
f1_keywords:
 - DStorageSetConfiguration
 - dstorage/DStorageSetConfiguration
dev_langs:
 - c++
helpviewer_keywords:
 - DStorageSetConfiguration
---

# DStorageSetConfiguration function (dstorage.h)

Configures DirectStorage. You must call **DStorageSetConfiguration** before your first call to [DStorageGetFactory](nf-dstorage-dstoragegetfactory.md). If you don't, then default values are used.

## Syntax

```cpp
HRESULT DStorageSetConfiguration(
  DSTORAGE_CONFIGURATION const *configuration
);
```

## Parameters

`configuration`

Type: **[DSTORAGE_CONFIGURATION](ns-dstorage-dstorage_configuration.md)**

Specifies the configuration.

## Return value

Standard HRESULT error code. The configuration can be changed only when no queue is created and no files are open; otherwise, **E_DSTORAGE_STAGING_BUFFER_LOCKED** is returned.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
