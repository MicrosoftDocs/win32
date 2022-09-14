---
description: Locates the target function of the specified import and replaces the function pointer in the import thunk with the target of the function implementation.
ms.assetid: 4ab79b7c-81d1-40bf-a76b-217d93567e40
title: ResolveDelayLoadedAPI function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ResolveDelayLoadedAPI
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-DelayLoad-l1-1-1.dll
- kernelbase.dll
- mincoredload.dll
- minkernelbase.dll
---

# ResolveDelayLoadedAPI function

Locates the target function of the specified import and replaces the function pointer in the import thunk with the target of the function implementation.

## Syntax


```C++
PVOID WINAPI ResolveDelayLoadedAPI(
  _In_       PVOID                             ParentModuleBase,
  _In_       PCIMAGE_DELAYLOAD_DESCRIPTOR      DelayloadDescriptor,
  _In_opt_   PDELAYLOAD_FAILURE_DLL_CALLBACK   FailureDllHook,
  _In_opt_   PDELAYLOAD_FAILURE_SYSTEM_ROUTINE FailureSystemHook,
  _Out_      PIMAGE_THUNK_DATA                 ThunkAddress,
  _Reserved_ ULONG                             Flags
);
```



## Parameters

<dl> <dt>

*ParentModuleBase* \[in\]
</dt> <dd>

The address of the base of the module importing a delay-loaded function.

</dd> <dt>

*DelayloadDescriptor* \[in\]
</dt> <dd>

The descriptor for the module to be loaded.

</dd> <dt>

*FailureDllHook* \[in, optional\]
</dt> <dd>

The address of the failure hook.

</dd> <dt>

*FailureSystemHook* \[in, optional\]
</dt> <dd>

The address of the system failure hook. See [**DelayLoadFailureHook**](delayloadfailurehook.md).

</dd> <dt>

*ThunkAddress* \[out\]
</dt> <dd>

The thunk data for the target function. Used to find the specific name table entry of the function.

</dd> <dt>

*Flags* 
</dt> <dd>

Reserved; must be 0.

</dd> </dl>

## Return value

The address of the import, or the failure stub for it.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012<br/>                                    |
| Library<br/> | <dl> <dt>Kernel32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[Linker Support for Delay-Loaded DLLs](https://msdn.microsoft.com/library/151kt790(v=VS.71).aspx)
</dt> </dl>

 

 




