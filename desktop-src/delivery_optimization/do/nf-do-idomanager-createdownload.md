---
title: IDOManager::CreateDownload method
description: Creates a new download.
keywords:
- IDOManager::CreateDownload method
topic_type:
- apiref
api_name:
- IDOManager.CreateDownload
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDOManager::CreateDownload method

Creates a new download.

## Syntax

```cpp
HRESULT CreateDownload(
  IDODownload **download
);
```

## Parameters

`download`

The address of an **IDODownload** interface pointer.

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
