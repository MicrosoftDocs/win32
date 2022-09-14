---
title: GetPhysicalMonitorDescription function
description: Gets a description of a physical monitor.
ms.assetid: 81789eaf-7831-4833-87e1-7f318f831c96
keywords:
- GetPhysicalMonitorDescription function Monitor Configuration
topic_type:
- apiref
api_name:
- GetPhysicalMonitorDescription
api_location:
- gdi32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# GetPhysicalMonitorDescription function

> [!IMPORTANT]
> This function is used by the monitor configuration API to access functionality in the display driver. Applications should not call this function.

 

Gets a description of a physical monitor.

## Syntax


```C++
NTSTATUS WINAPI GetPhysicalMonitorDescription(
  _In_  HANDLE hMonitor,
  _In_  DWORD  dwPhysicalMonitorDescriptionSizeInChars,
  _Out_ LPWSTR szPhysicalMonitorDescription
);
```



## Parameters

<dl> <dt>

*hMonitor* \[in\]
</dt> <dd>

A handle to a physical monitor.

</dd> <dt>

*dwPhysicalMonitorDescriptionSizeInChars* \[in\]
</dt> <dd>

The number of characters in the *szPhysicalMonitorDescription* array.

</dd> <dt>

*szPhysicalMonitorDescription* \[out\]
</dt> <dd>

A pointer to an array that receives the description. The number of elements in the array should be at least **PHYSICAL\_MONITOR\_DESCRIPTION\_SIZE**.

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

 

