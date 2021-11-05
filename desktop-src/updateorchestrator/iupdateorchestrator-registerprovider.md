---
title: IUpdateOrchestrator::RegisterProvider method
description: Registers the update provider with the given CLSID.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestrator::RegisterProvider method

Registers the update provider with the given CLSID.

## Syntax
```cpp
HRESULT RegisterProvider(
    [in] REFIID classId, 
    [in] LPCWSTR providerId);
```

test 
## Parameters

`classId`

`providerId`

## Returns
Returns **S_OK** if the update provider was successfully registered or an error in case of a failure.

## Remarks
It is not an error if the provider is already registered.

## See Also

[IUpdateOrchestrator](iupdateorchestrator.md)

[IUpdateOrchestrator::UnregisterProvider](iupdateorchestrator-unregisterprovider.md)