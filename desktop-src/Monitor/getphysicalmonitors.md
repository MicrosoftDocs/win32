---
title: GetPhysicalMonitors function
description: Gets the physical monitors associated with a display device.
ms.assetid: 8bbbad0a-2e45-439c-9312-f922a920c7fd
keywords:
- GetPhysicalMonitors function Monitor Configuration
topic_type:
- apiref
api_name:
- GetPhysicalMonitors
api_location:
- gdi32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# GetPhysicalMonitors function

> [!IMPORTANT]
> This function is used by the monitor configuration API to access functionality in the display driver. Applications should not call this function.

 

Gets the physical monitors associated with a display device.

## Syntax


```C++
NTSTATUS WINAPI GetPhysicalMonitors(
  _In_  UNICODE_STRING *pstrDeviceName,
  _In_  DWORD          dwPhysicalMonitorArraySize,
  _Out_ DWORD          *pdwNumPhysicalMonitorHandlesInArray,
  _Out_ HANDLE         *phPhysicalMonitorArray
);
```



## Parameters

<dl> <dt>

*pstrDeviceName* \[in\]
</dt> <dd>

A pointer to a [**UNICODE\_STRING**](/windows/desktop/api/subauth/ns-subauth-unicode_string) structure that contains the name of the display device, as returned by the [**GetMonitorInfo**](/windows/desktop/api/winuser/nf-winuser-getmonitorinfoa) function.

</dd> <dt>

*dwPhysicalMonitorArraySize* \[in\]
</dt> <dd>

The number of elements in the *pdwNumPhysicalMonitorHandlesInArray* array. To get the required size of the array, call [**GetNumberOfPhysicalMonitors**](getnumberofphysicalmonitors.md).

</dd> <dt>

*pdwNumPhysicalMonitorHandlesInArray* \[out\]
</dt> <dd>

Receives the number of items that the function copies to the *phPhysicalMonitorArray* array.

</dd> <dt>

*phPhysicalMonitorArray* \[out\]
</dt> <dd>

An array that receives handles to the physical monitors. Each handle must be released by calling [**DestroyPhysicalMonitor**](/windows/desktop/api/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-destroyphysicalmonitor).

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

Instead of using this function, applications should call one of the following functions:

-   [**GetPhysicalMonitorsFromHMONITOR**](/windows/desktop/api/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getphysicalmonitorsfromhmonitor)
-   [**GetPhysicalMonitorsFromIDirect3DDevice9**](/windows/desktop/api/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getphysicalmonitorsfromidirect3ddevice9)

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Gdi32.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Gdi32.dll</dt> </dl> |



## See also

<dl> <dt>

[Monitor Configuration Functions](monitor-configuration-functions.md)
</dt> </dl>

 

