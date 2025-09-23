---
description: Returns the specified COM interface from a running worker process.
title: GetVmWorkerProcess function
ms.topic: reference
ms.date: 02/06/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetVmWorkerProcess
api_type: 
- DllExport
api_location: 
- vmwpctrl.dll
---

# GetVmWorkerProcess function

Returns the specified COM interface from a running worker process.

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

Returns the specified COM interface from a running worker process.

### InterfaceId [in]

The REFIID of the COM interface to be retrieved.

### Object [out]

The address of an interface pointer variable that receives the  interface pointer of the Worker Process. Upon successful return, *Object* contains the requested interface pointer to the object. This method calls AddRef on the returned interface pointer. If the requested interface is not supported, this function sets *Object to NULL.

## Return value

An HRESULT.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from vmwpctrl.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | vmwpctrl.dll              |




 
