---
title: IDODownload::Start method
description: Starts or resumes a download.
keywords:
- IDODownload::Start method
topic_type:
- apiref
api_name:
- IDODownload.Start
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 07/03/2019
---

# IDODownload::Start method

Starts or resumes a download, passing optional ranges as a pointer to [**DO_DOWNLOAD_RANGES_INFO**](ns-do-do_download_range_info.md) structure.

## Syntax

```cpp
HRESULT Start(
  DO_DOWNLOAD_RANGES_INFO *ranges
);
```

## Parameters

`ranges`

Optional. A pointer to a [**DO_DOWNLOAD_RANGES_INFO**](ns-do-do_download_range_info.md) structure (to download only specific ranges of the file). Pass `nullptr` to download the entire file.

## Return Value

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | Do.h |
