---
title: DDCCIGetCapabilitiesStringLength function
description: Gets the length of a capabilities string for a monitor.
ms.assetid: '8a26d17b-1535-49c7-8cfb-48feb283a3c4'
keywords: ["DDCCIGetCapabilitiesStringLength function Monitor Configuration"]
topic_type:
- apiref
api_name:
- DDCCIGetCapabilitiesStringLength
api_location:
- gdi32.dll
api_type:
- DllExport
---

# DDCCIGetCapabilitiesStringLength function

> \[!Important\]  
> This function is used by the monitor configuration API to access functionality in the display driver. Applications should not call this function.

 

Gets the length of a capabilities string for a monitor.

## Syntax


```C++
NTSTATUS WINAPI DDCCIGetCapabilitiesStringLength(
  _In_  HANDLE hMonitor,
  _Out_ DWORD  *pdwLength
);
```



## Parameters

<dl> <dt>

*hMonitor* \[in\]
</dt> <dd>

A handle to a physical monitor.

</dd> <dt>

*pdwLength* \[out\]
</dt> <dd>

Receives the length of the capabilities string, in characters, including the terminating null character.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

Applications should call [**GetCapabilitiesStringLength**](getcapabilitiesstringlength.md) instead of calling this function.

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

 

 





