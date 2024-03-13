---
UID: NF:appxdatasource.IAppxStreamingDataSource4.Move
title: IAppxStreamingDataSource4::Move
description: Moves the package from the current volume to another.
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
 - IAppxStreamingDataSource4::Move
f1_keywords:
 - IAppxStreamingDataSource4::Move
 - appxdatasource/IAppxStreamingDataSource4::Move
dev_langs:
 - c++
helpviewer_keywords:
 - Move
---

# IAppxStreamingDataSource4::Move method

Moves the package from the current volume to another. The source package root path of the **Move** should have already been set as *sourceUri* when the data source was created. For the **MoveOptions::RollbackMove** option, the same set of parameters will be passed in for *packageFullName*, *targetVolume*, and *targetRootPath* as with the **BeginMove** and **EndMove** options; and the data source should consider the target as the aborted move destination, which needs to be cleaned up.

## Syntax

```cpp
HRESULT Move(
  [in, string] LPCWSTR packageFullName,
  [in, string] LPCWSTR targetVolume,
  [in, string] LPCWSTR targetPackageRootPath,
  [in] UINT64 deploymentOptions,
  [in, unique] IAppxStreamingDataSourceProgress* moveProgressHandler,
  [in] MoveOptions options
);
```

## Parameters

`packageFullName`

The package full name.

`targetVolume`

The target volume, such as `G:\`. The package contents are expected to move to `G:\Program Files\WindowsApps\<PackageFullName>`.

`targetPackageRootPath`

The target package root path; for example, `G:\Program Files\WindowsApps\<PackageFullName>`.

`deploymentOptions`

Specifies the `forceshutdown` flag or not. If specified, shuts down all running apps using this package.

`moveProgressHandler`

The move progress handler. Pass `nullptr` for the **MoveOptions::RollbackMove** option.

`options`

Move options that determine the actions the data source should take, such as: copying files from the source volume to the destination volume (for **BeginMove**); deleting the source volume files (for **EndMove**); or restoring files to the source volume (for **RollbackMove**). The data source can assume that either `Move(BeginMove)->Move(EndMove)` will be called on deployment success, or `Move(BeginMove)->Move(RollbackMove)` will be called on deployment failure.

## Return value

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10). **HRESULT_FROM_WIN32(ERROR_PACKAGES_IN_USE)** if the package is in use, and can't be moved.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
