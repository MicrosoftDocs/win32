---
description: Triggers an event when a guest physical address is accessed.
title: IVmFiovGuestMemoryFastNotification::RegisterDoorbell method
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmFiovGuestMemoryFastNotification::RegisterDoorbell
api_type: 
- COM
api_location: 
- NA
---

# IVmFiovGuestMemoryFastNotification::RegisterDoorbell method

Triggers an event when a guest physical address is accessed.

## Syntax


```C++
HRESULT RegisterDoorbell(
  [in] FIOV_BAR_SELECTOR BarIndex,
  [in] UINT64 BarOffset,
  [in] UINT64 TriggerValue,
  [in] UINT64 Flags,
  [in, system_handle(sh_event)] HANDLE NotificationEvent
);
```



## Parameters

### BarIndex [in]

The index of the BAR containing the page to register.

### BarOffset [in]

The page within the BAR to register.

### TriggerValue [in]

The specific value that will trigger the doorbell.

### Flags [in]

Doorbell notification flags.

### NotificationEvent [in]

The event to be signaled as a doorbell.

## Return value

An HRESULT.

## Remarks 


The **FIOV_BAR_SELECTOR** enumeration that provides values for the *BarIndex* has the following definition:

```c++
    typedef enum
    {
        FIOV_BAR0 = 0,
        FIOV_BAR1,
        FIOV_BAR2,
        FIOV_BAR3,
        FIOV_BAR4,
        FIOV_BAR5

    } FIOV_BAR_SELECTOR;
```

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |




## See also



 

 
