---
description: TBD
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

TBD

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

Pointer to the first string.

### MachineTypeFlags \[out\]

TBD. For more information, see the **Remarks** section.

## Return value

TBD



| Return code                                                                               | Description                                     |
|-------------------------------------------------------------------------------------------|-------------------------------------------------|
| TBD      | TBD       |


## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.


The **IMAGE_FILE_MACHINES** struct returned in the *MachineTypeFlags* parameter has the following definition.

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

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                    |
| Target platform<br/>          | <dl> <dt>[Universal](https://msdn.microsoft.com/Library/Windows/Hardware/EB2264A4-BAE8-446B-B9A5-19893936DDCA)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl>                                                    |



## See also

 

 
