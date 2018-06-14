---
Description: Returns the address of a delay-load failure callback function for the specified DLL and process.
ms.assetid: db1d34cb-800a-4984-b4a3-d1ce1c6ee86c
title: DelayLoadFailureHook function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DelayLoadFailureHook function

Returns the address of a delay-load failure callback function for the specified DLL and process.

## Syntax


```C++
FARPROC WINAPI DelayLoadFailureHook(
  _In_ LPCSTR pszDllName,
  _In_ LPCSTR pszProcName
);
```



## Parameters

<dl> <dt>

*pszDllName* \[in\]
</dt> <dd>

The name of the DLL.

</dd> <dt>

*pszProcName* \[in\]
</dt> <dd>

The name of the process.

</dd> </dl>

## Return value

The address of the callback function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Kernel32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Kernel32.dll</dt> </dl> |



## See also

<dl> <dt>

[Failure Hooks](https://msdn.microsoft.com/en-us/library/sfcfb0a3(v=VS.71).aspx)
</dt> </dl>

 

 




