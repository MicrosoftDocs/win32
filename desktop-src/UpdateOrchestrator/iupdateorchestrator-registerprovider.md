---
title: IUpdateOrchestrator::RegisterProvider method
ms.date: 03/20/2020
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

## Parameters

`classId`

`providerId`

## Returns
Returns **S_OK** if the update provider was succesfully registered or an error in case of a failure.

## Remarks
It is not an error if the provider is already registered.
