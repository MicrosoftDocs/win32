---
title: IDODownload::Finalize method
description: Finalizes the download.
keywords:
- IDODownload::Finalize method
topic_type:
- apiref
api_name:
- IDODownload.Finalize
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownload::Finalize method

Finalizes the download. Once finalized, a download cannot be resumed by calling **Start**.

## Syntax

```cpp
HRESULT Finalize();
```

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
