---
UID: NF:appxdatasource.IAppxStreamingDataSource4.Pause
title: IAppxStreamingDataSource4::Pause
description: Terminates the request, causing the corresponding Run call to return E_ABORT.
ms.topic: reference
tech.root: appxpkg
ms.date: 02/08/2024
targetos: Windows
prerelease: false
req.assembly: 
req.construct-type: function
req.ddi-compliance: 
req.dll: 
req.header: 
req.idl: 
req.include-header: 
req.irql: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - AppxStreamingDataSourcePS.dll
api_name:
 - IAppxStreamingDataSource4::Pause
f1_keywords:
 - IAppxStreamingDataSource4::Pause
 - appxdatasource/IAppxStreamingDataSource4::Pause
dev_langs:
 - c++
helpviewer_keywords:
 - Pause
---

# IAppxStreamingDataSource4::Pause method

Terminates the request, causing the corresponding [Run](./nf-appxdatasource-iappxstreamingdatasource4-run.md) call to return **E_ABORT**. This call leaves the downloaded bytes in a stable state so that the download can be resumed later.

## Syntax

```cpp
HRESULT Pause(
  [in, string] LPCWSTR packageFullName
);
```

## Parameters

`packageFullName`

The package full name.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
