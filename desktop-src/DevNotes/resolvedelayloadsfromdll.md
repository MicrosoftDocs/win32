---
Description: Forwards the work in resolving delay-loaded imports from the parent binary to a target binary.
ms.assetid: 65629d7b-36b0-426b-a20d-ec736b8461dc
title: ResolveDelayLoadsFromDll function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

The address of the delay-load descriptor, if it is found; otherwise, **NULL**.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Kernel32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[Linker Support for Delay-Loaded DLLs](https://msdn.microsoft.com/en-us/library/151kt790(v=VS.71).aspx)
</dt> </dl>

 

 




