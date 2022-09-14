---
title: DDCCISetVCPFeature function
description: Sets the value of a Virtual Control Panel (VCP) code for a monitor.
ms.assetid: 1069588b-5f8a-49da-b857-6f0a0c737a11
keywords:
- DDCCISetVCPFeature function Monitor Configuration
topic_type:
- apiref
api_name:
- DDCCISetVCPFeature
api_location:
- gdi32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DDCCISetVCPFeature function

> [!IMPORTANT]
> This function is used by the monitor configuration API to access functionality in the display driver. Applications should not call this function.

 

Sets the value of a Virtual Control Panel (VCP) code for a monitor.

## Syntax


```C++
NTSTATUS WINAPI DDCCISetVCPFeature(
  _In_ HANDLE hMonitor,
  _In_ DWORD  dwVCPCode,
  _In_ DWORD  dwNewValue
);
```



## Parameters

<dl> <dt>

*hMonitor* \[in\]
</dt> <dd>

A handle to a physical monitor.

</dd> <dt>

*dwVCPCode* \[in\]
</dt> <dd>

The VCP code to set.

</dd> <dt>

*dwNewValue* \[in\]
</dt> <dd>

The value of the VCP code.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

Applications should call [**SetVCPFeature**](/windows/desktop/api/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-setvcpfeature) instead of calling this function.

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

 

