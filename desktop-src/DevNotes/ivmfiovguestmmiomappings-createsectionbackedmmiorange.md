---
description: Maps a section into device MMIO space, so that accesses to those addresses will be backed by the section.
title: IVmFiovGuestMmioMappings::CreateSectionBackedMmioRange method
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from TBD.

The **FIOV_BAR_SELECTOR** enumeration that provides values for the *BarIndex* is documented in the remarks of [RegisterDoorbell](ivmfiovguestmemoryfastnotification-registerdoorbell.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header | N/A    |
| DLL  | TBD |



## See also



 

 
