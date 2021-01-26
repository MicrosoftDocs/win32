---
title: CreateProfileFromLogColorSpace function
description: The CreateProfileFromLogColorSpace function converts a logical color space to a device profile.
ms.assetid: ac2fddd4-ac93-49a8-883a-cf888b542812
keywords:
- CreateProfileFromLogColorSpace function Windows Color System
topic_type:
- apiref
api_name:
- CreateProfileFromLogColorSpace
- CreateProfileFromLogColorSpaceA
- CreateProfileFromLogColorSpaceW
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# CreateProfileFromLogColorSpace function

The **CreateProfileFromLogColorSpace** function converts a logical [color space](c.md) to a [device profile](d.md).

## Syntax


```C++
BOOL WINAPI CreateProfileFromLogColorSpace(
   LPLOGCOLORSPACE pLogColorSpace,
   PBYTE           *pBuffer
);
```



## Parameters

<dl> <dt>

*pLogColorSpace* 
</dt> <dd>

A pointer to a logical color space structure. See [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea) for details. The **lcsFilename** \[0\] member of the structure must be set to the **null** character ('\\0') or this function call will fail with the return value of INVALID\_PARAMETER.

</dd> <dt>

*pBuffer* 
</dt> <dd>

A pointer to a pointer to a buffer where the device profile will be created. This function allocates the buffer and fills it with profile information if it is successful. If not, the pointer is set to **NULL**. The caller is responsible for freeing this buffer when it is no longer needed.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**.

If the **lcsFilename** \[0\] member if the [**LOGCOLORSPACE**](/windows/desktop/api/Wingdi/ns-wingdi-taglogcolorspacea) structure pointed to by *pLogColorSpace* is not '\\0', this function returns INVALID\_PARAMETER.

## Remarks

This function can be used with ASCII or Unicode strings. The buffer created by this function must be freed by the caller when it is no longer needed or there will be a memory leak. The [GlobalFree](/windows/win32/api/winbase/nf-winbase-globalfree) function should be used to free this buffer.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP.

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>                        |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl>                    |
| Unicode and ANSI names<br/>   | **CreateProfileFromLogColorSpaceW** (Unicode) and **CreateProfileFromLogColorSpaceA** (ANSI)<br/> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[GlobalFree](/windows/win32/api/winbase/nf-winbase-globalfree)
</dt> </dl>

 

