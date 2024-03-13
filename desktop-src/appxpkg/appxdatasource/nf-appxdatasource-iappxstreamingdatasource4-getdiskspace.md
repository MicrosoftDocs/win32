---
UID: NF:appxdatasource.IAppxStreamingDataSource4.GetDiskSpace
title: IAppxStreamingDataSource4::GetDiskSpace
description: Retrieves a value representing the total disk space used by the package.
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
 - IAppxStreamingDataSource4::GetDiskSpace
f1_keywords:
 - IAppxStreamingDataSource4::GetDiskSpace
 - appxdatasource/IAppxStreamingDataSource4::GetDiskSpace
dev_langs:
 - c++
helpviewer_keywords:
 - GetDiskSpace
---

# IAppxStreamingDataSource4::GetDiskSpace method

Retrieves a value representing the total disk space used by the package.

## Syntax

```cpp
HRESULT GetDiskSpace(
  [in, string] LPCWSTR packageFullName,
  [out, retval] UINT64* diskSpaceBytes
);
```

## Parameters

`packageFullName`

The package full name.

`diskSpaceBytes`

The total disk space used by the package.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
