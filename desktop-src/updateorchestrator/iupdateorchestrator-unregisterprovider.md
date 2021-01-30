---
title: IUpdateOrchestrator::UnregisterProvider method
description: Unregisters the given update provider. 
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestrator::UnregisterProvider method

Unregisters the given update provider. 

## Syntax
```cpp
HRESULT UnregisterProvider(
    [in] REFIID classId);
```

## Parameters

`classId`

## Returns
Returns **S_OK** if the update provider was successfully unregistered or an error in case of a failure.

## See Also

[IUpdateOrchestrator](iupdateorchestrator.md)

[IUpdateOrchestrator::RegisterProvider](iupdateorchestrator-registerprovider.md)
