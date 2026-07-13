---
UID: NF:appxdatasource.IAppxStreamingDataSource4.Remove
title: IAppxStreamingDataSource4::Remove
description: Cancels any outstanding Run calls (causing them to return), and removes the package contents.
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
 - IAppxStreamingDataSource4::Remove
f1_keywords:
 - IAppxStreamingDataSource4::Remove
 - appxdatasource/IAppxStreamingDataSource4::Remove
dev_langs:
 - c++
helpviewer_keywords:
 - Remove
---

# IAppxStreamingDataSource4::Remove method

Cancels any outstanding [Run](./nf-appxdatasource-iappxstreamingdatasource4-run.md) calls (causing them to return), and removes the package contents. This call also allows the removal of orphaned package roots where there's no corresponding `staterepo entry`. That's necessary in order to take care of operating system (OS) uninstall scenarios where the old OS package root can be left around for a period without the corresponding package in `staterepo`.

## Syntax

```cpp
HRESULT Remove(
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
