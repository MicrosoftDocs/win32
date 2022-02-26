---
title: IDODownload::GetStatus method
description: Retrieves a pointer to a **DO_DOWNLOAD_STATUS** structure that reflects the current status of the download.
keywords:
- IDODownload::GetStatus method
topic_type:
- apiref
api_name:
- IDODownload.GetStatus
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownload::GetStatus method

Retrieves a pointer to a **DO_DOWNLOAD_STATUS** structure that reflects the current status of the download.

## Syntax

```cpp
HRESULT GetStatus(
  DO_DOWNLOAD_STATUS *status
);
```

## Parameters

`status`

A pointer to a **DO_DOWNLOAD_STATUS** structure.

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
