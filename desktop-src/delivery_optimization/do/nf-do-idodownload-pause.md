---
title: IDODownload::Pause method
description: Pauses the download.
keywords:
- IDODownload::Pause method
topic_type:
- apiref
api_name:
- IDODownload.Pause
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownload::Pause method

Pauses the download.

## Syntax

```cpp
HRESULT Pause();
```

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
