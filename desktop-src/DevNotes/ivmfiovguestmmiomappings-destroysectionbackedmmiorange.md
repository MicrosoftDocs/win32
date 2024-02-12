---
description: Unmaps a section previously mapped via CreateSectionBackedMmioRange.
title: IVmFiovGuestMmioMappings::DestroySectionBackedMmioRange method
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmFiovGuestMmioMappings::DestroySectionBackedMmioRange
api_type: 
- COM
api_location: 
- NA
---

# IVmFiovGuestMmioMappings::DestroySectionBackedMmioRange method

Unmaps a section previously mapped via [CreateSectionBackedMmioRange](ivmfiovguestmmiomappings-createsectionbackedmmiorange.md). The caller is responsible for pausing and resuming the VPs around this call if the updates to the device space are to appear atomic.

## Syntax


```C++
HRESULT DestroySectionBackedMmioRange(
    [in]                             FIOV_BAR_SELECTOR     BarIndex,
    [in]                             ULONG64               BarOffsetInPages
);                             
```

## Parameters

### BarIndex [in]

The index of the BAR containing the MMIO space.

### BarOffsetInPages [in]

The offset within the BAR of the first mapped page.

## Return value

An HRESULT.

## Remarks 

The **FIOV_BAR_SELECTOR** enumeration that provides values for the *BarIndex* is documented in the remarks of [RegisterDoorbell](ivmfiovguestmemoryfastnotification-registerdoorbell.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |


## See also



 

 
