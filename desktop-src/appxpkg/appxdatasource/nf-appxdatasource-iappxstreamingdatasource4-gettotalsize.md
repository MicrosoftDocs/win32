---
UID: NF:appxdatasource.IAppxStreamingDataSource4.GetTotalSize
title: IAppxStreamingDataSource4::GetTotalSize
description: Returns the total download size of the MSIXVC package.
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
 - IAppxStreamingDataSource4::GetTotalSize
f1_keywords:
 - IAppxStreamingDataSource4::GetTotalSize
 - appxdatasource/IAppxStreamingDataSource4::GetTotalSize
dev_langs:
 - c++
helpviewer_keywords:
 - GetTotalSize
---

# IAppxStreamingDataSource4::GetTotalSize method

Returns the total download size of the MSIXVC package.

## Syntax

```cpp
HRESULT GetTotalSize(
  [out, retval] UINT64* totalSizeBytes
);
```

## Parameters

`totalSizeBytes`

Total size of the `msixvc` (the value can be used in download progress estimates).

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
