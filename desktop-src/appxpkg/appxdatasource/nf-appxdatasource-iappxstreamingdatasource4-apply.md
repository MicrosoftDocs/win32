---
UID: NF:appxdatasource.IAppxStreamingDataSource4.Apply
title: IAppxStreamingDataSource4::Apply
description: Applies an update from an outdated package to an updating package.
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
 - IAppxStreamingDataSource4::Apply
f1_keywords:
 - IAppxStreamingDataSource4::Apply
 - appxdatasource/IAppxStreamingDataSource4::Apply
dev_langs:
 - c++
helpviewer_keywords:
 - Apply
---

# IAppxStreamingDataSource4::Apply method

Applies an update from an outdated package to an updating package (for example, from `package_v1` to `package_v2`), making the package ready for activation. If *outdatedPackageFullName* is `nullptr`, then this is a fresh install.

## Syntax

```cpp
HRESULT Apply(
  [in, string, unique] LPCWSTR outdatedPackageFullName,
  [in, string] LPCWSTR updatingPackageFullName,
  [in] UINT64 deploymentOptions
);
```

## Parameters

`outdatedPackageFullName`

The outdated package's full name.

`updatingPackageFullName`

The updating package's full name.

`deploymentOptions`

Specifies the `forceshutdown` flag or not. If specified, shuts down all running apps using this package (cross-session app shutdown may need to be done).

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10). **HRESULT_FROM_WIN32(ERROR_PACKAGES_IN_USE)** if the package is in use, and can't be updated.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
