---
title: IUpdateOrchestratorUpdateProvider::Deserialize method
description: Deserializes the bytes into an update.
ms.date: 12/01/2020
ms.topic: method
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
Returns **S_OK** if successful, a failure otherwise.

## Remarks


## See Also

[IUpdateOrchestratorUpdateProvider](iupdateorchestratorupdateprovider.md)

[IUpdateOrchestratorUpdateProvider::CancelScan](iupdateorchestratorupdateprovider-cancelscan.md)

[IUpdateOrchestratorUpdateProvider::ScanAttemptFrequencyInMinutes](iupdateorchestratorupdateprovider-scanattemptfrequencyinminutes.md)

[IUpdateOrchestratorUpdateProvider::ScanForPendingUpdates](iupdateorchestratorupdateprovider-scanforpendingupdates.md) 

[IUpdateOrchestratorUpdateProvider::ScanSlaInMinutes](iupdateorchestratorupdateprovider-scanslainminutes.md)