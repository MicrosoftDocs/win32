---
description: Cancels DLL load notification previously registered by calling the LdrRegisterDllNotification function.
ms.assetid: 18c3a027-e3cb-4083-afdc-00f416a70d8c
title: LdrUnregisterDllNotification function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LdrUnregisterDllNotification
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# LdrUnregisterDllNotification function

\[This function may be changed or removed from Windows without further notice.\]

Cancels DLL load notification previously registered by calling the [**LdrRegisterDllNotification**](ldrregisterdllnotification.md) function.

## Syntax


```C++
NTSTATUS NTAPI LdrUnregisterDllNotification(
  _In_ PVOID Cookie
);
```



## Parameters

<dl> <dt>

*Cookie* \[in\]
</dt> <dd>

A pointer to the callback identifier received from the [**LdrRegisterDllNotification**](ldrregisterdllnotification.md) call that registered for notification.

</dd> </dl>

## Return value

Returns an **NTSTATUS** or error code.

If the function succeeds, it returns **STATUS\_SUCCESS**.

If the callback function is not found, the function returns **STATUS\_DLL\_NOT\_FOUND**.

The forms and significance of **NTSTATUS** error codes are listed in the Ntstatus.h header file available in the WDK, and are described in the WDK documentation.

## Remarks

This function has no associated header file. The associated import library, Ntdll.lib, is available in the WDK. You can also use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Ntdll.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**LdrRegisterDllNotification**](ldrregisterdllnotification.md)
</dt> </dl>

 

 
