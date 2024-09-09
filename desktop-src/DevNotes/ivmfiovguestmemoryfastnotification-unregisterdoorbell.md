---
description: Stops notifications registered via RegisterDoorbell.
title: IVmFiovGuestMemoryFastNotification::UnregisterDoorbell method
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmFiovGuestMemoryFastNotification::UnregisterDoorbell
api_type: 
- COM
api_location: 
- NA
---

# IVmFiovGuestMemoryFastNotification::UnregisterDoorbell method

Stops notifications registered via [RegisterDoorbell](ivmfiovguestmemoryfastnotification-registerdoorbell.md).

## Syntax


```C++
HRESULT UnregisterDoorbell(
    [in] FIOV_BAR_SELECTOR    BarIndex,
    [in] UINT64               BarOffset,
    [in] UINT64               TriggerValue,
    [in] UINT64               Flags
);
```



## Parameters

### BarIndex [in]

The index of the BAR containing the doorbell.

### BarOffset [in]

The page within the BAR containing the doorbell.

### TriggerValue [in]

The specific value that will trigger the doorbell.

### Flags [in]

Doorbell notification flags.


## Return value

An HRESULT.

## Remarks 

The **FIOV_BAR_SELECTOR** enumeration that provides values for the *BarIndex* is documented in the remarks of [RegisterDoorbell](ivmfiovguestmemoryfastnotification-registerdoorbell.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |




## See also



 

 
