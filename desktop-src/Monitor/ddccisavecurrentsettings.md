---
title: DDCCISaveCurrentSettings function
description: Saves the current monitor settings to the display's nonvolatile storage.
ms.assetid: '293b61d4-36d8-43f4-8800-4dbac3ab11b0'
keywords: ["DDCCISaveCurrentSettings function Monitor Configuration"]
topic_type:
- apiref
api_name:
- DDCCISaveCurrentSettings
api_location:
- gdi32.dll
api_type:
- DllExport
---

# DDCCISaveCurrentSettings function

> \[!Important\]  
> This function is used by the monitor configuration API to access functionality in the display driver. Applications should not call this function.

 

Saves the current monitor settings to the display's nonvolatile storage.

## Syntax


```C++
NTSTATUS WINAPI DDCCISaveCurrentSettings(
   HANDLE hMonitor
);
```



## Parameters

<dl> <dt>

*hMonitor* 
</dt> <dd>

A handle to a physical monitor.

</dd> </dl>

## Return value

If the method succeeds, it returns **STATUS\_SUCCESS**. Otherwise, it returns an **NTSTATUS** error code.

## Remarks

Applications should call [**SaveCurrentSettings**](savecurrentsettings.md) instead of calling this function.

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

 

 





