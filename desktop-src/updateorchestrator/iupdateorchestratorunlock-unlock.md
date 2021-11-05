---
title: IUpdateOrchestratorUnlock::Unlock method
description: Unlocks the RegisterProvider and UnregisterProvider methods.
ms.date: 01/29/2020
ms.topic: method
---

# IUpdateOrchestratorUnlock::Unlock method

Unlocks the [RegisterProvider](iupdateorchestrator-registerprovider.md) and [UnregisterProvider](iupdateorchestrator-unregisterprovider.md) methods. 

> [!NOTE]
> If Unlock is not called, the call will fail with **E_ACCESSDENIED**.

## Syntax
```cpp
HRESULT Unlock(
    [in] LPCWSTR token);
```
## Parameters

`token`

## Returns
Returns **S_OK** if the instance was unlocked and has permission to the methods in IUpdateOrchestrator.

## Remarks

This routine must be called on the object before access the functions in IUpdateOrchestrator are available.

## See Also

[IUpdateOrchestrator::RegisterProvider](iupdateorchestrator-registerprovider.md)

[IUpdateOrchestrator::UnregisterProvider](iupdateorchestrator-unregisterprovider.md)