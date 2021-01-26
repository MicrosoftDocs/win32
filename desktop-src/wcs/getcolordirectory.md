---
title: GetColorDirectory function
description: The GetColorDirectory function retrieves the path of the Windows COLOR directory on a specified machine.
ms.assetid: 9e26e58b-0497-4879-963c-fae91f5740bf
keywords:
- GetColorDirectory function Windows Color System
topic_type:
- apiref
api_name:
- GetColorDirectory
- GetColorDirectoryA
- GetColorDirectoryW
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# GetColorDirectory function

The **GetColorDirectory** function retrieves the path of the Windows COLOR directory on a specified machine.

## Syntax


```C++
BOOL WINAPI GetColorDirectory(
   PCTSTR pMachineName,
   PTSTR  pBuffer,
   PDWORD pdwSize
);
```



## Parameters

<dl> <dt>

*pMachineName* 
</dt> <dd>

Reserved; must be **NULL**. This parameter is intended to point to the name of the machine on which the profile is to be installed. A **NULL** pointer indicates the local machine.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Points to the buffer in which the color directory path is to be placed.

</dd> <dt>

*pdwSize* 
</dt> <dd>

Points to a variable containing the size in bytes of the buffer pointed to by *pBuffer*. On return, the variable contains the size of the buffer actually used or needed.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

**Per-user/LUA support**

Color directory is still system wide. This function is executable in LUA context.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **GetColorDirectoryW** (Unicode) and **GetColorDirectoryA** (ANSI)<br/>        |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





