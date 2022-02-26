---
title: DO_DOWNLOAD_RANGE structure
description: Identifies a single range of bytes to download from a file.
keywords:
- DO_DOWNLOAD_RANGE structure
topic_type:
- apiref
api_name:
- DO_DOWNLOAD_RANGE
api_location:
- deliveryoptimizationdownloadtypes.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/03/2019
---

# DO_DOWNLOAD_RANGE structure

The **DO_DOWNLOAD_RANGE** structure identifies a single range of bytes to download from a file. The **DO_DOWNLOAD_RANGE** structure is included within **DO_DOWNLOAD_RANGES_INFO** structure to provide an array of ranges to download.

## Syntax
```cpp
typedef struct _DO_DOWNLOAD_RANGE
{
  UINT64 Offset;
  UINT64 Length;
} DO_DOWNLOAD_RANGE;
```

## Members

`Offset`

Zero-based offset to the beginning of the range of bytes to download from a file.

`Length`

The length of the range, in bytes. Do not specify a zero-byte length. To indicate that the range extends to the end of the file, specify **DO_LENGTH_TO_EOF**.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | DeliveryOptimizationDownloadTypes.h |
