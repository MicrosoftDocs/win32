---
description: Registers the Shell Dynamic Data Exchange (DDE) services in the current process, notifying the system that the current process wishes to host DDE objects.
ms.assetid: d7f65d6a-a697-475b-a739-c7950b7f4d5d
title: ShellDDEInit function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellDDEInit
api_type: 
- DllExport
api_location: 
- Shdocvw.dll
---

# ShellDDEInit function

Registers the Shell Dynamic Data Exchange (DDE) services in the current process, notifying the system that the current process wishes to host DDE objects.

## Syntax


```C++
void ShellDDEInit(
  _In_ BOOL init
);
```



## Parameters

<dl> <dt>

*init* \[in\]
</dt> <dd>

Type: **BOOL**

**TRUE** to register the current process as DDE host; **FALSE** to unregister it.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The process that calls this function acts as the Shell and is used to view the content of folders opened with the [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) 'open' verb.

This function does not have an associated header or library file so it must be called by ordinal value. Call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (Shdocvw.dll) to obtain a module handle. Then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with that module handle and the function ordinal number 118 to get the address of the function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shdocvw.dll (version 6.0 or later)</dt> </dl> |



 

 
