---
title: DO_DOWNLOAD_RANGE_INFO structure
description: Identifies an array of ranges of bytes to download from a file.
keywords:
- DO_DOWNLOAD_RANGE_INFO structure
topic_type:
- apiref
api_name:
- DO_DOWNLOAD_RANGE_INFO
api_location:
- do.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/03/2019
---

# DO_DOWNLOAD_RANGE_INFO structure

The **DO_DOWNLOAD_RANGE_INFO** structure identifies an array of ranges of bytes to download from a file. It is typically passed as an optional argument to the **IDODownload::Start** function.

## Syntax
```cpp
typedef struct _DO_DOWNLOAD_RANGES_INFO
{
  UINT RangeCount;
  [size_is(RangeCount)] DO_DOWNLOAD_RANGE Ranges[];
} DO_DOWNLOAD_RANGES_INFO;
```

## Members

`RangeCount`

Number of elements in Ranges.

`Ranges`

Array of one or more **DO_DOWNLOAD_RANGE** structures that specify the ranges to download.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
