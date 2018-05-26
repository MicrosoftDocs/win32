---
title: DDCCIGetVCPFeature function
description: Gets the current value, maximum value, and code type of a Virtual Control Panel (VCP) code for a monitor.
ms.assetid: 7749d45c-a0d5-44ee-8f91-811677cbf59f
keywords:
- DDCCIGetVCPFeature function Monitor Configuration
topic_type:
- apiref
api_name:
- DDCCIGetVCPFeature
api_location:
- gdi32.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DDCCIGetVCPFeature function

> \[!Important\]  
> This function is used by the monitor configuration API to access functionality in the display driver. Applications should not call this function.

 

Gets the current value, maximum value, and code type of a Virtual Control Panel (VCP) code for a monitor.

## Syntax


```C++
NTSTATUS WINAPI DDCCIGetVCPFeature(
  _In_      HANDLE             hMonitor,
  _In_      DWORD              dwVCPCode,
  _Out_opt_ LPMC_VCP_CODE_TYPE pvct,
  _Out_     DWORD              *pdwCurrentValue,
  _Out_opt_ DWORD              *pdwMaximumValue
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

The VCP code to query.

</dd> <dt>

*pvct* \[out, optional\]
</dt> <dd>

Receives the VCP code type, as a member of the [**MC\_VCP\_CODE\_TYPE**](/windows/win32/LowLevelMonitorConfigurationAPI/ne-lowlevelmonitorconfigurationapi-_mc_vcp_code_type?branch=master) enumeration.

</dd> <dt>

*pdwCurrentValue* \[out\]
</dt> <dd>

Receives the current value of the VCP code.

</dd> <dt>

*pdwMaximumValue* \[out, optional\]
</dt> <dd>

Receives the maximum value of the VCP code.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

Applications should call [**GetVCPFeatureAndVCPFeatureReply**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-getvcpfeatureandvcpfeaturereply?branch=master) instead of calling this function.

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to Gdi32.dll.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Gdi32.dll</dt> </dl> |



## See also

<dl> <dt>

[Monitor Configuration Functions](monitor-configuration-functions.md)
</dt> </dl>

 

 





