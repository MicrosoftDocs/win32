---
UID: NS:dstorage.DSTORAGE_CONFIGURATION
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_CONFIGURATION
ms.date: 08/25/2022
targetos: Windows
description: DirectStorage configuration.
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
 - DSTORAGE_CONFIGURATION
f1_keywords:
 - DSTORAGE_CONFIGURATION
 - dstorage/DSTORAGE_CONFIGURATION
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_CONFIGURATION
---

# DSTORAGE_CONFIGURATION structure (dstorage.h)

DirectStorage configuration. Zero-initializing this will result in the default values.

## Syntax

```cpp
struct DSTORAGE_CONFIGURATION {
  UINT32 NumSubmitThreads;
  BOOL   ForceMappingLayer;
  BOOL   DisableBypassIO;
  BOOL   DisableTelemetry;
};
```

## Members

`NumSubmitThreads`

Sets the number of threads to use for submitting IO operations. Specifying 0 means use the system's best guess at a good value. Default == 0.

`ForceMappingLayer`

Forces the use of the IO mapping layer, even when running on an operating system that doesn't require it. This might be useful during development, but should be set to `FALSE` for release. Default == `FALSE`.

`DisableBypassIO`

Disables the use of the bypass IO optimization, even if it is available. This might be useful during development, but should be set to `FALSE` for release. Default == `FALSE`.

`DisableTelemetry`

Disables the reporting of telemetry data when set to `TRUE`. Telemetry data is enabled by default in the DirectStorage runtime. Default == `FALSE`.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
