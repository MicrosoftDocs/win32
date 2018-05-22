---
title: InstallColorProfile function
description: The InstallColorProfile function installs a given profile for use on a specified machine. The profile is also copied to the COLOR directory.
ms.assetid: '494b2080-a0a8-4fda-bc12-3bf196a6840c'
keywords: ["InstallColorProfile function Windows Color System"]
topic_type:
- apiref
api_name:
- InstallColorProfile
- InstallColorProfileA
- InstallColorProfileW
api_location:
- mscms.dll
api_type:
- DllExport
---

# InstallColorProfile function

The **InstallColorProfile** function installs a given profile for use on a specified machine. The profile is also copied to the COLOR directory.

## Syntax


```C++
BOOL WINAPI InstallColorProfile(
   PCTSTR pMachineName,
   PCTSTR pProfileName
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved. Must be **NULL**. This parameter is intended to point to the name of the computer on which the profile is to be installed. A **NULL** pointer indicates the local computer.

</dd> <dt>

*pProfileName* 
</dt> <dd>

Pointer to the fully qualified path name of the profile to install.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **InstallColorProfileW** (Unicode) and **InstallColorProfileA** (ANSI)<br/>    |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





