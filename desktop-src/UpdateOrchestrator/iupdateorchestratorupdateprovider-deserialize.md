---
title: IUpdateOrchestratorUpdateProvider::Deserialize method
ms.date: 03/20/2020
ms.topic: method
---

# IUpdateOrchestratorUpdateProvider::Deserialize method
Deserialize the bytes into an update 

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

The provider should return the collection of updates that it still needs to complete actions on. This method will be called daily by the UpdateOrchestrator.