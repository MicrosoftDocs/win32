---
UID: NF:appxdatasource.IAppxStreamingDataSource4.Run
title: IAppxStreamingDataSource4::Run
description: Initiates the streaming operation (request).
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
 - IAppxStreamingDataSource4::Run
f1_keywords:
 - IAppxStreamingDataSource4::Run
 - appxdatasource/IAppxStreamingDataSource4::Run
dev_langs:
 - c++
helpviewer_keywords:
 - Run
---

# IAppxStreamingDataSource4::Run method

Initiates the streaming operation (request). The function operates synchronously, and doesn't return until the job completes, or is canceled, or otherwise errors out. This call can block for some time; but from another thread you can still send other requests to the data source, such as [Pause](./nf-appxdatasource-iappxstreamingdatasource4-pause.md), whereupon **Run** will stop blocking, and will return **E_ABORT**.

## Syntax

```cpp
HRESULT Run(
  [in, string] LPCWSTR packageFullName,
  [in, string] LPCWSTR realPackageRootPath,
  [in] APPX_DATA_SOURCE_JOB_PRIORITY priority,
  [in] IAppxStreamingDataSourceProgress* downloadProgressHandler,
  [in] RunOptions options
);
```

## Parameters

`packageFullName`

The package full name.

`realPackageRootPath`

The real package root path. This will point to the package root on a non-system volume if the app has been installed on other media.

`priority`

The priority of the request.

`downloadProgressHandler`

A pointer to the callback interface that will receive the download progress.

`options`

The options for the **Run** request.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10). **E_ABORT** if the data source was paused; **HRESULT_FROM_WIN32(ERROR_BUSY)** if more than one **Run** call is made concurrently.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
