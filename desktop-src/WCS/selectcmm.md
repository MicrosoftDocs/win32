---
title: SelectCMM function
description: SelectCMM allows an application to select the preferred color management module (CMM) to use.
ms.assetid: 3aadd3d6-a74e-4de2-855c-d20c520821ff
keywords:
- SelectCMM function Windows Color System
topic_type:
- apiref
api_name:
- SelectCMM
api_location:
- mscms.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SelectCMM function

**SelectCMM** allows an application to select the preferred color management module (CMM) to use.

## Syntax


```C++
BOOL WINAPI SelectCMM(
   DWORD cmmID
);
```



## Parameters

<dl> <dt>

*cmmID* 
</dt> <dd>

Specifies the signature of the desired CMM as registered with the International Color Consortium (ICC).

**Windows 2000 only:** Setting this parameter to **NULL** causes the WCS system to select the default CMM.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

For **SelectCMM** to succeed, the specified CMM must be registered with the system.

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

 

 





