---
description: The expert implements the DllMain function. The operating system calls DllMain to obtain a handle to an instance of the expert.
ms.assetid: 38593ba0-dc37-4620-bb49-2e50c3d9ea3c
title: DllMain Expert callback function (Process.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DllMain
api_type: 
- UserDefined
api_location: 
- process.h
---

# DllMain Expert callback function

The expert implements the [**DllMain**](/windows/desktop/Dlls/dllmain) function. The operating system calls **DllMain** to obtain a handle to an instance of the expert.

## Syntax


```C++
BOOL WINAPI DllMain(
  _Out_ HINSTANCE hInstance,
  _In_  ULONG     ulReason,
        LPVOID    Reserved
);
```



## Parameters

<dl> <dt>

*hInstance* \[out\]
</dt> <dd>

Handle to an instance of the expert.

If the expert uses the Network Monitor user interface, the *hInstance* value must be stored in a global variable. This approach is necessary only when the value of the *ulReason* parameter is set to DLL\_PROCESS\_ATTACH.

</dd> <dt>

*ulReason* \[in\]
</dt> <dd>

Indicator of why the function was called. A value of DLL\_PROCESS\_ATTACH, (which applies when the DLL is first loaded) indicates that the expert should save the *hInstance* value in a global variable.

With any other value, all calls to the [**DllMain**](/windows/desktop/Dlls/dllmain) function can be ignored. For a list of all possible flags set by the operating system, see **DLLMain**.

</dd> <dt>

*Reserved* 
</dt> <dd>

Parameter is not in use.

</dd> </dl>

## Return value

If the function is successful, the return value is **TRUE**.

If the function is unsuccessful, the return value is **FALSE**.

## Remarks

The operating system calls the **DllMain** expert function when a process loads or unloads the expert DLL. The **DllMain** expert function must be exported only if the expert has a user interface for viewing either configuration or results, and then only to return the proper *hInstance* value.

The **DllMain** expert function is based on the dynamic link library [**DllMain**](/windows/desktop/Dlls/dllmain) function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Process.h</dt> </dl> |



 

