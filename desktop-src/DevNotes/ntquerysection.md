---
description: Provides the capability to determine the base address, size, granted access, and allocation of an opened section object.
title: NtQuerySection function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtQuerySection
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# NtQuerySection function

Provides the capability to determine the base address, size, granted access, and allocation of an opened section object.

## Syntax

```cpp
NTSTATUS NTAPI NtQuerySection (
    _In_ HANDLE SectionHandle,
    _In_ SECTION_INFORMATION_CLASS SectionInformationClass,
    _Out_writes_bytes_(SectionInformationLength) PVOID SectionInformation,
    _In_ SIZE_T SectionInformationLength,
    _Out_opt_ PSIZE_T ReturnLength
    )
```

## Parameters

### SectionHandle [in]

An open handle to a section object.

### SectionInformationClass [in]

The section information class about which to retrieve information.

### SectionInformation [out]

A pointer to a buffer that receives the specified information.  The format and content of the buffer depend on the specified section class.

### SectionInformationLength [in]

Specifies the length in bytes of the section information buffer.

### ReturnLength [out]

An optional pointer which, if specified, receives the number of bytes placed in the section information buffer.

## Return value

An NTSTATUS code. For more information, see [Using NTSTATUS values](/windows-hardware/drivers/kernel/using-ntstatus-values).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.


The type of the **SectionInformation** parameter is **PSECTION_BASIC_INFORMATION**

```cpp
typedef struct _SECTIONBASICINFO {
    PVOID BaseAddress;
    ULONG AllocationAttributes;
    LARGE_INTEGER MaximumSize;
} SECTION_BASIC_INFORMATION, *PSECTION_BASIC_INFORMATION;
```
#### PVOID BaseAddress

The base virtual address of the section if the section is based.

#### ULONG AllocationAttributes

The allocation attributes flags.

| Flag | Value | Description |
|------|-------|-------------|
| SEC_BASED |  0x200000 | The section is a based section. |
| SEC_FILE | 0x800000 | The section is backed by a data file. |
| SEC_RESERVE | 0x4000000 | All pages of the section were initially set to the reserved state. |
| SEC_COMMIT |  0x8000000 | All pages of the section were initially set to the committed state. |
| SEC_IMAGE | 0x1000000 | The section was mapped as an executable image file. |

### LARGE_INTEGER MaximumSize

The maximum size of the section in bytes.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
