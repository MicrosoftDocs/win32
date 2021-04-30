---
description: Registers for notification when a DLL is first loaded. This notification occurs before dynamic linking takes place.
ms.assetid: c2757aa0-76fa-427a-a4f6-cb26e7f7d0d1
title: LdrRegisterDllNotification function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LdrRegisterDllNotification
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# LdrRegisterDllNotification function

\[This function may be changed or removed from Windows without further notice.\]

Registers for notification when a DLL is first loaded. This notification occurs before dynamic linking takes place.

## Syntax


```C++
NTSTATUS NTAPI LdrRegisterDllNotification(
  _In_     ULONG                          Flags,
  _In_     PLDR_DLL_NOTIFICATION_FUNCTION NotificationFunction,
  _In_opt_ PVOID                          Context,
  _Out_    PVOID                          *Cookie
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter must be zero.

</dd> <dt>

*NotificationFunction* \[in\]
</dt> <dd>

A pointer to an [*LdrDllNotification*](ldrdllnotification.md) notification callback function to call when the DLL is loaded.

</dd> <dt>

*Context* \[in, optional\]
</dt> <dd>

A pointer to context data for the callback function.

</dd> <dt>

*Cookie* \[out\]
</dt> <dd>

A pointer to a variable to receive an identifier for the callback function. This identifier is used to unregister the notification callback function.

</dd> </dl>

## Return value

If the function succeeds, it returns **STATUS\_SUCCESS**.

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

[*LdrDllNotification*](ldrdllnotification.md)
</dt> <dt>

[**LdrUnregisterDllNotification**](ldrunregisterdllnotification.md)
</dt> </dl>

 

 
