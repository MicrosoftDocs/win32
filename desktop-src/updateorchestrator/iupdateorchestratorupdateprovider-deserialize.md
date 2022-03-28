---
title: IUpdateOrchestratorUpdateProvider::Deserialize method
description: Deserializes the bytes into an update.
ms.date: 01/29/2020
ms.topic: reference
---

# IUpdateOrchestratorUpdateProvider::Deserialize method

Deserializes the bytes into an update.

## Syntax
```cpp
HRESULT Deserialize(
    [in, size_is(numBytes)] const BYTE* serializedUpdate, 
    [in] DWORD numBytes, 
    [out] IUpdateOrchestratorUpdate** update);
```
## Parameters

`serializedUpdate`

an update that was serialized using IUpdateOrchestratorUpdate::Serialize

`numBytes`

the number of bytes pass in

`update`

output pointer for the deserialized update

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## Remarks


## See Also

[IUpdateOrchestratorUpdateProvider](iupdateorchestratorupdateprovider.md)

[IUpdateOrchestratorUpdateProvider::CancelScan](iupdateorchestratorupdateprovider-cancelscan.md)

[IUpdateOrchestratorUpdateProvider::get_ScanAttemptFrequencyInMinutes](iupdateorchestratorupdateprovider-scanattemptfrequencyinminutes.md)

[IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates](iupdateorchestratorupdateprovider-scanforpendingupdates.md) 

[IUpdateOrchestratorUpdateProvider::get_ScanSlaInMinutes](iupdateorchestratorupdateprovider-scanslainminutes.md)