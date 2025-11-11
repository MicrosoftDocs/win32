---
description: Sets the control bits of a security descriptor.
title: RtlSetControlSecurityDescriptor function
ms.topic: reference
ms.date: 11/10/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlSetControlSecurityDescriptor
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# RtlSetControlSecurityDescriptor function

Sets the control bits of a security descriptor.

## Syntax


```cpp
NTSTATUS NTAPI RtlSetControlSecurityDescriptor (
     IN PSECURITY_DESCRIPTOR pSecurityDescriptor,
     IN SECURITY_DESCRIPTOR_CONTROL ControlBitsOfInterest,
     IN SECURITY_DESCRIPTOR_CONTROL ControlBitsToSet
     );
```

## Parameters

### SecurityDescriptor [in]

A pointer to a [SECURITY_DESCRIPTOR](/windows/win32/api/winnt/ns-winnt-security_descriptor) structure whose control and revision information are set.

### ControlBitsOfInterest [in]

A [SECURITY_DESCRIPTOR_CONTROL](/windows/desktop/SecAuthZ/security-descriptor-control) mask that indicates the control bits to set.

### ControlBitsToSet [in]

A [SECURITY_DESCRIPTOR_CONTROL](/windows/desktop/SecAuthZ/security-descriptor-control) mask that indicates the new values for the control bits specified by the *ControlBitsOfInterest* mask.

## Return value

An NTSTATUS code. For more information, see [Using NTSTATUS values](/windows-hardware/drivers/kernel/using-ntstatus-values).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
