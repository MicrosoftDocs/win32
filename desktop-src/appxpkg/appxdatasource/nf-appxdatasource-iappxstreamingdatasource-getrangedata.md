---
UID: NF:appxdatasource.IAppxStreamingDataSource.GetRangeData
title: IAppxStreamingDataSource::GetRangeData
description: Requests a range of data synchronously, which is handled at the highest priority.
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
 - IAppxStreamingDataSource::GetRangeData
f1_keywords:
 - IAppxStreamingDataSource::GetRangeData
 - appxdatasource/IAppxStreamingDataSource::GetRangeData
dev_langs:
 - c++
helpviewer_keywords:
 - GetRangeData
---

# IAppxStreamingDataSource::GetRangeData method

Requests a range of data synchronously, which is handled at the highest priority.

## Syntax

```cpp
HRESULT GetRangeData(
  __RPC__out_ecount_full(size) BYTE *data,
  UINT64 offset,
  UINT32 size
);
```

## Parameters

`data`

Buffer for requested data.

`offset`

Offset into the resource for the specified range.

`size`

Size of the requested range.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
