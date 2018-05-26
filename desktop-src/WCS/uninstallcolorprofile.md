---
title: UninstallColorProfile function
description: UninstallColorProfile removes a specified color profile from a specified computer. Associated files are optionally deleted from the system.
ms.assetid: 2c5a2055-9f5f-4e21-bcbb-a9aa50105598
keywords:
- UninstallColorProfile function Windows Color System
topic_type:
- apiref
api_name:
- UninstallColorProfile
- UninstallColorProfileA
- UninstallColorProfileW
api_location:
- mscms.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UninstallColorProfile function

**UninstallColorProfile** removes a specified color profile from a specified computer. Associated files are optionally deleted from the system.

## Syntax


```C++
BOOL WINAPI UninstallColorProfile(
   PCTSTR pMachineName,
   PCTSTR pProfileName,
   BOOL   bDelete
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved. Must be **NULL**. This parameter is intended to point to the name of the machine from which to uninstall the specified profile. A **NULL** pointer indicates the local machine.

</dd> <dt>

*pProfileName* 
</dt> <dd>

Points to the file name of the profile to uninstall.

</dd> <dt>

*bDelete* 
</dt> <dd>

If set to **TRUE**, the function deletes the profile from the COLOR directory. If set to **FALSE**, this function has no effect.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>      |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl>  |
| Unicode and ANSI names<br/>   | **UninstallColorProfileW** (Unicode) and **UninstallColorProfileA** (ANSI)<br/> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





