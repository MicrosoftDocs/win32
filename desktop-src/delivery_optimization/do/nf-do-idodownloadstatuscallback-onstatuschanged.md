---
title: IDODownloadStatusCallback::OnStatusChange method
description: Delivery Optimization calls your implementation of this method any time a download status has changed.
keywords:
- IDODownloadStatusCallback::OnStatusChange method
topic_type:
- apiref
api_name:
- IDODownloadStatusCallback.OnStatusChange
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownloadStatusCallback::OnStatusChange method

Delivery Optimization calls your implementation of this method any time a download status has changed.

## Syntax

```cpp
HRESULT OnStatusChange(
  IDODownload *download,
  DO_DOWNLOAD_STATUS *status
);
```

## Parameters

`download`

An pointer to the **IDODownload** interface whose status changed.

`status`

A pointer to a **DO_DOWNLOAD_STATUS** structure containing the download's status.

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
