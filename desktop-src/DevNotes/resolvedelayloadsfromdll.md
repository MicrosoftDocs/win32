---
description: Forwards the work in resolving delay-loaded imports from the parent binary to a target binary.
ms.assetid: 65629d7b-36b0-426b-a20d-ec736b8461dc
title: ResolveDelayLoadsFromDll function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ResolveDelayLoadsFromDll
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-DelayLoad-l1-1-1.dll
- kernelbase.dll
- mincoredload.dll
- minkernelbase.dll
---

# ResolveDelayLoadsFromDll function

Forwards the work in resolving delay-loaded imports from the parent binary to a target binary.

## Syntax


```C++
NTSTATUS WINAPI ResolveDelayLoadsFromDll(
  _In_       PVOID  ParentBase,
  _In_       LPCSTR TargetDllName,
  _Reserved_ ULONG  Flags
);
```



## Parameters

<dl> <dt>

*ParentBase* \[in\]
</dt> <dd>

The base address of the module that delay loads another binary.

</dd> <dt>

*TargetDllName* \[in\]
</dt> <dd>

The name of the target DLL.

</dd> <dt>

*Flags* 
</dt> <dd>

Reserved; must be 0.

</dd> </dl>

## Return value

Returns an **NTSTATUS** or error code.

| Return code | Description |
|--------------|--------------|
| STATUS_SUCCESS | The operation completed successfully |
| STATUS_DLL_NOT_FOUND | The Target DLL could not be found |

The forms and significance of **NTSTATUS** error codes are listed in the Ntstatus.h header file available in the WDK, and are described in the WDK documentation.


## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012<br/>                                    |
| Library<br/> | <dl> <dt>Kernel32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Kernel32.dll</dt> </dl> |


## See also

<dl> <dt>

[Linker Support for Delay-Loaded DLLs](https://msdn.microsoft.com/library/151kt790(v=VS.71).aspx)
</dt> </dl>

 

 




