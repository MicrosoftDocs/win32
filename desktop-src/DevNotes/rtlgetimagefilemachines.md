---
description: Identifies the architectures which an image is compatible with / can execute under.
title: RtlGetImageFileMachines function (Wdm.h)
ms.topic: reference
ms.date: 02/22/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetImageFileMachines
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlGetImageFileMachines function

This function identifies the architectures which an image is compatible with / can execute under. Most binaries contain code which can be used on a single architecture. However, there are cases, such as ILOnly-AnyCPU and Arm64X / Chameleon binaries, there a single binary may support executing are more than one architecture. For more information, see [Build Arm64X binaries](/windows/arm/arm64x-build).

## Syntax


```C++
NTSTATUS
RtlGetImageFileMachines (
    _In_ PCWSTR DosFileName,
    _Out_ IMAGE_FILE_MACHINES * MachineTypeFlags
    );
```



## Parameters

### DosFileName \[in\]

Provides a pointer to a UNICODE string containing the full binary pathname to be inspected.

### MachineTypeFlags \[out\]

Provides a pointer to a `IMAGE_FILE_MACHINES` structure which contains a Bitfield through which the API will indicate the architectures this binary contains / is compatible with.

The `IMAGE_FILE_MACHINES` struct has the following definition.

```cpp
typedef struct _IMAGE_FILE_MACHINES {
    union {
        ULONG Value;
        struct {
            ULONG MachineX86 : 1;
            ULONG MachineAmd64 : 1;
            ULONG MachineArm : 1;
            ULONG MachineArm64 : 1;
            ULONG MachineArm64EC : 1;
        };
    };
} IMAGE_FILE_MACHINES;
```

## Return value

This function returns zero on success. (More detail).

See [NTSTATUS Values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55) for a list of NTSTATUS values.


## Remarks

This function does not validate the image's dependencies. For example: If A.DLL is an Arm64X / Chameleon DLL with Arm64 and Arm64EC code and depends on B.DLL but B.DLL is only available for Arm64, this API will still indicate A.DLL as being compatible with both Arm64 and Arm64EC. The same can be said for ILOnly-AnyCPU binaries. A.DLL can be ILOnly-AnyCPU (thus it can potentially load on a process of any architecture) so this API will return all the bits set for all architectures even if the .net framework (just like any dependency) may not be present for all architectures.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11 22H2 \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2025 \[desktop apps only\]<br/>                                                                                    |
| Target platform<br/>          | <dl> <dt>[Universal](https://msdn.microsoft.com/Library/Windows/Hardware/EB2264A4-BAE8-446B-B9A5-19893936DDCA)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl>                                                    |



## See also

 

 
