---
description: Provides a management interface for managing VM virtual devices.
title: IVmVirtualDeviceAccess interface
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmVirtualDeviceAccess
api_type: 
- COM
api_location: 
- NA
---

# IVmVirtualDeviceAccess interface

Provides a management interface for managing VM virtual devices.

## Syntax

```c++
[
    object,
    uuid( 3e57bd3c-5a5d-4bdc-a0a6-5b4193d4b719 ),
    pointer_default( unique )
]
interface IVmVirtualDeviceAccess : IUnknown
{
    ...
};
```

## Members

The **IVmVirtualDeviceAccess** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IVmVirtualDeviceAccess** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVmVirtualDeviceAccess** interface has these methods.



| Method                                                   | Description                                                                                                           |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| **ReservedMethod1** |  This method is reserved and is listed here to indicate the offset of other methods in the virtual method table for the interface. |
| **ReservedMethod2** |  This method is reserved and is listed here to indicate the offset of other methods in the virtual method table for the interface. |
| [**GetDevice**](ivmvirtualdeviceaccess-getdevice.md)                   | vmprox.dll |

## Remarks


## Requirements

| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |



 

 
