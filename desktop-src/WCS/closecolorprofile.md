---
title: CloseColorProfile function
description: This CloseColorProfile closes an open profile handle.
ms.assetid: 49656afa-64fc-4421-8948-34a65c9f829e
keywords:
- CloseColorProfile function Windows Color System
topic_type:
- apiref
api_name:
- CloseColorProfile
api_location:
- Mscms.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CloseColorProfile function

This **CloseColorProfile** closes an open profile handle.

## Syntax


```C++
BOOL WINAPI CloseColorProfile(
   HPROFILE hProfile
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Handle to the profile to be closed. The function determines whether the HPROFILE contains ICC or WCS profile information.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call [GetLastError](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





