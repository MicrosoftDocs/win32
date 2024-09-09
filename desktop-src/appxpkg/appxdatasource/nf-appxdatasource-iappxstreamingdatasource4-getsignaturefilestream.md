---
UID: NF:appxdatasource.IAppxStreamingDataSource4.GetSignatureFileStream
title: IAppxStreamingDataSource4::GetSignatureFileStream
description: Retrieves the signature file stream of an MSIXVC package.
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
 - IAppxStreamingDataSource4::GetSignatureFileStream
f1_keywords:
 - IAppxStreamingDataSource4::GetSignatureFileStream
 - appxdatasource/IAppxStreamingDataSource4::GetSignatureFileStream
dev_langs:
 - c++
helpviewer_keywords:
 - GetSignatureFileStream
---

# IAppxStreamingDataSource4::GetSignatureFileStream method

Returns the signature file stream of an MSIXVC package (`appxsignature.p7x`, for example). Once this call returns, the signature file must be accessible.

## Syntax

```cpp
HRESULT GetSignatureFileStream(
  [in, string] LPCWSTR signatureFileName,
  [in] SignatureStreamFlags flags,
  [out, retval] IStream** signatureFileStream
);
```

## Parameters

`signatureFileName`

The signature file name. This will be set to, for example, `appxsignature.p7x`.

`flags`

Flags that indicate whether the `.p7x` header must be added, etc.

`manifestStream`

The signature file stream. The callee must call **AddRef** the stream, and then the caller will call **Release** on it after use.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
