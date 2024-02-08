---
description: TBD
title: GetVmWorkerProcess function
ms.topic: reference
ms.date: 02/06/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtCreateWaitCompletionPacket
api_type: 
- DllExport
api_location: 
- ntdll.dllvmwpctrl.dll
---

# GetVmWorkerProcess function

TBD

## Syntax


```C++
STDAPI
GetVmWorkerProcess(
    _In_ REFGUID VirtualMachineId,
    _In_ REFIID InterfaceId,
    _Outptr_opt_ IUnknown** Object
    );
```

## Parameters

### VirtualMachineId [in]

TBD

### InterfaceId [in]

TBD

### Object [out]

TBD

## Return value

An HRESULT.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from vmwpctrl.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | vmwpctrl.dll              |




 
