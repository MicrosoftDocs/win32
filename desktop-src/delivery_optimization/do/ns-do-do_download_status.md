---
title: DO_DOWNLOAD_STATUS structure
description: Used to obtain the status of a specific download.
keywords:
- DO_DOWNLOAD_STATUS structure
topic_type:
- apiref
api_name:
- DO_DOWNLOAD_STATUS
api_location:
- do.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 07/03/2019
---

# DO_DOWNLOAD_STATUS structure

The **DO_DOWNLOAD_STATUS** structure is used to obtain the status of a specific download. It is obtained by calling the **IDODownload::GetStatus** function.

## Syntax
```cpp
typedef struct _DO_DOWNLOAD_STATUS
{
  UINT64 BytesTotal;
  UINT64 BytesTransferred;
  DODownloadState State;
  HRESULT Error;
  HRESULT ExtendedError;
} DO_DOWNLOAD_STATUS;
```

## Members

`BytesTotal`

The total number of bytes to download.

`BytesTransferred`

The number of bytes that have already been downloaded.

`State`

The current download state as defined by the **DODownloadState** enumeration.

`Error`

The error information (if it exists) that is associated with the current download.

`ExtendedError`

The extended error information (if it exists) that is associated with the current download.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
