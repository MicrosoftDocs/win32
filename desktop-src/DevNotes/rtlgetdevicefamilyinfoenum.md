---
description: Retrieves values representing the device family and form factor of the current device. 
title: RtlGetDeviceFamilyInfoEnum  function
ms.topic: reference
ms.date: 01/31/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetDeviceFamilyInfoEnum 
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# RtlGetDeviceFamilyInfoEnum  function

Retrieves values representing the device family and form factor of the current device.

## Syntax


```C++
VOID
NTAPI
RtlGetDeviceFamilyInfoEnum(
    _Out_opt_ ULONGLONG *pullUAPInfo,
    _Out_opt_ DWORD *pulDeviceFamily,
    _Out_opt_ DWORD *pulDeviceForm
);
```



## Parameters

### pullUAPInfo \[out\]

Receives the UAP version of the current device.

### pulDeviceFamily \[out\]

Receives a DWORD specifying the device family of the current device. The returned value is one of the following:

- 
| Device family | Value |
| DEVICEFAMILYINFOENUM_DESKTOP          |          0x00000003
| DEVICEFAMILYINFOENUM_XBOX             |          0x00000005
| DEVICEFAMILYINFOENUM_TEAM             |          0x00000006
| DEVICEFAMILYINFOENUM_SERVER           |          0x00000009
| DEVICEFAMILYINFOENUM_HOLOGRAPHIC      |          0x0000000A
| DEVICEFAMILYINFOENUM_SERVER_NANO      |          0x0000000D
| DEVICEFAMILYINFOENUM_WINDOWS_CORE     |          0x00000010


### pulDeviceForm \[out\]

Receives a DWORD specifying the form factor of the current device.

- DEVICEFAMILYDEVICEFORM_TABLET
- DEVICEFAMILYDEVICEFORM_CONVERTIBLE
- DEVICEFAMILYDEVICEFORM_DETACHABLE
- 
| Form factor | Value |
| DEVICEFAMILYDEVICEFORM_TABLET | 0x00000002
| DEVICEFAMILYDEVICEFORM_CONVERTIBLE | 0x00000005
|DEVICEFAMILYDEVICEFORM_DETACHABLE | 0x00000006




## Return value

VOID

## Remarks



## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |
| DLL                      | ntdll.dll |



 

 




