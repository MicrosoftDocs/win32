---
description: Maps a section into device MMIO space, so that accesses to those addresses will be backed by the section.
title: IVmFiovGuestMmioMappings::CreateSectionBackedMmioRange method
ms.topic: reference
ms.date: 02/08/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVmFiovGuestMmioMappings::CreateSectionBackedMmioRange
api_type: 
- COM
api_location: 
- vmidl.dll
---

# IVmFiovGuestMmioMappings::CreateSectionBackedMmioRange method

Maps a section into device MMIO space, so that accesses to those addresses will be backed by the section. The caller is responsible for pausing and resuming the VPs around this call if the updates to the device space are to appear atomic.

## Syntax


```C++
HRESULT CreateSectionBackedMmioRange(
    [in]                             FIOV_BAR_SELECTOR     BarIndex,
    [in]                             ULONG64               BarOffsetInPages,
    [in]                             UINT64                PageCount,
    [in]                             FiovMmioMappingFlags  MappingFlags,
    [in, system_handle(sh_section)]  HANDLE                SectionHandle,
    [in]                             UINT64                SectionOffsetInPages
);
```



## Parameters

### BarIndex [in]

The index of the BAR containing MMIO space.

### BarOffsetInPages [in]

The offset within the BAR to the first page to be mapped.

### PageCount [in]

The number of pages from the section mapped into MMIO space.

### MappingFlags [in]

Specifies flags used when creating the guest mapping.

### SectionHandle [in]

The handle to the section object.

### SectionOffsetInPages [in]

The offset within the section to the first page to map.


## Return value

An HRESULT.

## Remarks 

The **FIOV_BAR_SELECTOR** enumeration that provides values for the *BarIndex* is documented in the remarks of [RegisterDoorbell](ivmfiovguestmemoryfastnotification-registerdoorbell.md).

The **FiovMmioMappingFlags** enumeration that provides values for the *MappingFlags* has the following definition:


```c++
typedef [v1_enum] enum
{
    FiovMmioMappingFlagNone = 0x00000000,
    FiovMmioMappingFlagWriteable = 0x00000001,
    FiovMmioMappingFlagExecutable = 0x00000002
 
} FiovMmioMappingFlags;
``````

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |



## See also



 

 
