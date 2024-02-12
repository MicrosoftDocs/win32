---
description: Provides fast, event-based notifications of guest memory accesses.
title: IVmFiovGuestMemoryFastNotification interface
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmFiovGuestMemoryFastNotification
api_type: 
- COM
api_location: 
- NA
---

# IVmFiovGuestMemoryFastNotification interface

**IVmFiovGuestMemoryFastNotification** provides fast, event-based notifications of guest memory accesses.

IVmFiovGuestMemoryFastNotification provides a service that allows the user mode emulation
driver to perform work when the guest touches specific physical pages. This is useful for
protocols that have a doorbell mechanism to signal when work is ready, if that doorbell can
be placed on a separate physical page.

## Syntax

```c++
[
    object,
    uuid(f5dfbec1-b9f3-4b26-bf6f-c251448bcf7a),
    helpstring("IVmFiovGuestMemoryFastNotification Interface"),
    pointer_default(unique),
]
interface IVmFiovGuestMemoryFastNotification : IUnknown
{
    ...
};
```

## Members

The **IVmFiovGuestMemoryFastNotification** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IVmFiovGuestMmioMappings** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVmFiovGuestMemoryFastNotification** interface has these methods.



| Method                                                   | Description                                                                                                           |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**RegisterDoorbell**](ivmfiovguestmemoryfastnotification-registerdoorbell.md)                   | Triggers an event when a guest physical address is accessed. |
| [**UnregisterDoorbell**](ivmfiovguestmemoryfastnotification-unregisterdoorbell.md)                   | Stops notifications registered via **RegisterDoorbell**. |

## Remarks



## Requirements

| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |




 

 
