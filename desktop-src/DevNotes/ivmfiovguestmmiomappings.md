---
description: Allows the user mode emulation driver to map memory into device MMIO space, so instead of being intercepted on access it is backed by the given host memory.
title: IVmFiovGuestMmioMappings interface
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmFiovGuestMmioMappings
api_type: 
- COM
api_location: 
- NA
---

# IVmFiovGuestMmioMappings interface

Allows the user mode emulation driver to map memory into device MMIO space, so instead of being intercepted on access it is backed by the given host memory.

## Syntax

```c++
[
    object,
    uuid(9d416457-abbc-46cf-8b93-901c68bec627),
    helpstring("IVmFiovGuestMmioMappings Interface"),
    pointer_default(unique),
]
interface IVmFiovGuestMmioMappings : IUnknown
{
    ...
};
```

## Members

The **IVmFiovGuestMmioMappings** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IVmFiovGuestMmioMappings** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVmFiovGuestMmioMappings** interface has these methods.



| Method                                                   | Description                                                                                                           |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**CreateSectionBackedMmioRange**](ivmfiovguestmmiomappings-createsectionbackedmmiorange.md)                   |  Maps a section into device MMIO space, so that accesses to those addresses will be backed by the section. |
| [**DestroySectionBackedMmioRange**](ivmfiovguestmmiomappings-destroysectionbackedmmiorange.md)                   | Unmaps a section previously mapped via **CreateSectionBackedMmioRange**. |

## Remarks

## Requirements

| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |



 

 
