---
UID: NS:dstorage.DSTORAGE_CONFIGURATION2
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_CONFIGURATION2
ms.date: 10/30/2026
targetos: Windows
description: DirectStorage configuration; adds an option to specify a global CreatorID for the Direct3D 12 command queues that DirectStorage creates.
prerelease: true
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
 - DSTORAGE_CONFIGURATION2
f1_keywords:
 - DSTORAGE_CONFIGURATION2
 - dstorage/DSTORAGE_CONFIGURATION2
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_CONFIGURATION2
---

# DSTORAGE_CONFIGURATION2 structure (dstorage.h)

DirectStorage configuration; adds an option to specify a global CreatorID for the Direct3D 12 command queues that DirectStorage creates. Zero-initializing this will result in the default values.

## Syntax

```cpp
struct DSTORAGE_CONFIGURATION2 {
  UINT32 NumSubmitThreads;
  INT32  NumBuiltInCpuDecompressionThreads;
  BOOL   ForceMappingLayer;
  BOOL   DisableBypassIO;
  BOOL   DisableTelemetry;
  BOOL   DisableGpuDecompressionMetacommand;
  BOOL   DisableGpuDecompression;
  BOOL   ForceFileBuffering;
  GUID   CreatorID;
};
```

## Members

`NumSubmitThreads`

Sets the number of threads to use for submitting IO operations. Specifying 0 means use the system's best guess at a good value. Default == 0.

`NumBuiltInCpuDecompressionThreads`

Sets the number of threads to be used by the DirectStorage runtime to decompress data using the CPU for built-in compressed formats that can't be decompressed using the GPU. Specifying 0 means to use the system's best guess at a good value. Specifying **DSTORAGE_DISABLE_BUILTIN_CPU_DECOMPRESSION** means that no decompression threads will be created, and the title is fully responsible for checking the custom decompression queue and pulling off *all* entries to decompress. Default == 0.

`ForceMappingLayer`

Forces the use of the IO mapping layer, even when running on an operating system that doesn't require it. This might be useful during development, but should be set to `FALSE` for release. Default == `FALSE`.

`DisableBypassIO`

Disables the use of the bypass IO optimization, even if it is available. This might be useful during development, but should be set to `FALSE` for release; unless you set *ForceFileBuffering* to `TRUE`. Default == `FALSE`.

`DisableTelemetry`

Disables the reporting of telemetry data when set to `TRUE`. Telemetry data is enabled by default in the DirectStorage runtime. Default == `FALSE`.

`DisableGpuDecompressionMetacommand`

Disables the use of a decompression metacommand, even if one is available. This will force the runtime to use the built-in GPU decompression fallback shader. This may be useful during development, but should be set to `FALSE` for release. Default == FALSE.

`DisableGpuDecompression`

Disables the use of GPU based decompression, even if it is available. This will force the runtime to use the CPU. Default == `FALSE`.

`ForceFileBuffering`

Forces the use of the built-in file caching behaviors supported within the Windows operating system by not setting **FILE_FLAG_NO_BUFFERING** when opening files (see [File buffering](/windows/win32/fileio/file-buffering)). Default == `FALSE`.

You must set *DisableBypassIO* to `TRUE` when using this option, otherwise **E_DSTORAGE_FILEBUFFERING_REQUIRES_DISABLED_BYPASSIO** will be returned. It's the title's responsibility to know when to use this setting. This feature should be enabled only for slower HDD drives that will benefit from the OS file buffering features.

> [!WARNING]
> Enabling file buffering on high speed drives might reduce overall performance when reading from that drive because BypassIO is also disabled.

`CreatorID`

Specifies a global CreatorID that DirectStorage applies to all of the Direct3D 12 command queues that it creates on each device. For more info about CreatorIDs, see [ID3D12Device9::CreateCommandQueue1](/windows/win32/api/d3d12/nf-d3d12-id3d12device9-createcommandqueue1). If a device doesn't support **ID3D12Device9**, DirectStorage creates the command queues for that device without a CreatorID. Default == `GUID_NULL`.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
