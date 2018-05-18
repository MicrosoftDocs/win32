---
title: GetNumberOfPhysicalMonitors function
description: Gets the number of phyical monitors associated with a display device.
ms.assetid: '498404e7-867d-4971-bea1-16e9f8fd9838'
keywords: ["GetNumberOfPhysicalMonitors function Monitor Configuration"]
topic_type:
- apiref
api_name:
- GetNumberOfPhysicalMonitors
api_location:
- gdi32.dll
api_type:
- DllExport
---

# GetNumberOfPhysicalMonitors function

> \[!Important\]  
> This function is used by the monitor configuration API to access functionality in the display driver. Applications should not call this function.

 

Gets the number of phyical monitors associated with a display device.

## Syntax


```C++
NTSTATUS WINAPI GetNumberOfPhysicalMonitors(
  _In_  UNICODE_STRING *pstrDeviceName,
  _Out_ LPDWORD        pdwNumberOfPhysicalMonitors
);
```



## Parameters

<dl> <dt>

*pstrDeviceName* \[in\]
</dt> <dd>

A pointer to a [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/desktop/aa380518) structure that contains the name of the display device, as returned by the [**GetMonitorInfo**](https://msdn.microsoft.com/library/windows/desktop/dd144901) function.

</dd> <dt>

*pdwNumberOfPhysicalMonitors* \[out\]
</dt> <dd>

Receives the number of physical monitors.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

Instead of using this function, applications should call one of the following functions:

-   [**GetNumberOfPhysicalMonitorsFromHMONITOR**](getnumberofphysicalmonitorsfromhmonitor.md)
-   [**GetNumberOfPhysicalMonitorsFromIDirect3DDevice9**](getnumberofphysicalmonitorsfromidirect3ddevice9.md)

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to Gdi32.dll.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Gdi32.dll</dt> </dl> |



## See also

<dl> <dt>

[Monitor Configuration Functions](monitor-configuration-functions.md)
</dt> </dl>

 

 





