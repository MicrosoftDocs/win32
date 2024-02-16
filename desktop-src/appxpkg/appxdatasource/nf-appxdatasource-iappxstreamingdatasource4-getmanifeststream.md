---
UID: NF:appxdatasource.IAppxStreamingDataSource4.GetManifestStream
title: IAppxStreamingDataSource4::GetManifestStream
description: Retrieves the appx manifest stream of an MSIXVC package.
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
 - IAppxStreamingDataSource4::GetManifestStream
f1_keywords:
 - IAppxStreamingDataSource4::GetManifestStream
 - appxdatasource/IAppxStreamingDataSource4::GetManifestStream
dev_langs:
 - c++
helpviewer_keywords:
 - GetManifestStream
---

# IAppxStreamingDataSource4::GetManifestStream method

Retrieves the appx manifest stream of an MSIXVC package. Once this call returns, the manifest must be accessible.

## Syntax

```cpp
HRESULT GetManifestStream(
  [in, string] LPCWSTR manifestFileName,
  [out, retval] IStream** manifestStream
);
```

## Parameters

`manifestFileName`

The manifest file name. This will be set to, for example, `appxmanifest.xml`.

`manifestStream`

The manifest file stream. The callee must call **AddRef** the stream, and then the caller will call **Release** on it after use.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
