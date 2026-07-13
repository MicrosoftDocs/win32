---
UID: NF:appxdatasource.IAppxStreamingDataSource.GetAttributes
title: IAppxStreamingDataSource::GetAttributes
description: Returns attributes information specific to the data source.
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
 - IAppxStreamingDataSource::GetAttributes
f1_keywords:
 - IAppxStreamingDataSource::GetAttributes
 - appxdatasource/IAppxStreamingDataSource::GetAttributes
dev_langs:
 - c++
helpviewer_keywords:
 - GetAttributes
---

# IAppxStreamingDataSource::GetAttributes method

Returns attributes information specific to the data source.

## Syntax

```cpp
HRESULT GetAttributes(
  __RPC__out AppxStreamingDataSourceAttributes *attributes
);
```

## Parameters

`attributes`

All attributes associated with a data source.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
