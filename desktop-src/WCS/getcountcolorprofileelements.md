---
title: GetCountColorProfileElements function
description: The GetCountColorProfileElements function retrieves the number of tagged elements in a given color profile.
ms.assetid: f8df63ff-9c8c-4131-b38d-ee39c9160a06
keywords:
- GetCountColorProfileElements function Windows Color System
topic_type:
- apiref
api_name:
- GetCountColorProfileElements
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

# GetCountColorProfileElements function

The **GetCountColorProfileElements** function retrieves the number of tagged elements in a given color profile.

## Syntax


```C++
BOOL WINAPI GetCountColorProfileElements(
   HPROFILE hProfile,
   PDWORD   pnCount
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the profile in question.

</dd> <dt>

*pnCount* 
</dt> <dd>

Pointer to a variable in which to place the number of tagged elements in the profile.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP.

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

 

 





