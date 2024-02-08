---
description: Stops notifications registered via RegisterDoorbell.
title: IVmFiovGuestMemoryFastNotification::UnregisterDoorbell method
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore.GetInfo
api_type: 
- COM
api_location: 
- TBD
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from TBD.

The **FIOV_BAR_SELECTOR** enumeration that provides values for the *BarIndex* is documented in the remarks of [RegisterDoorbell](ivmfiovguestmemoryfastnotification-registerdoorbell.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |
| DLL  | TBD |



## See also



 

 
