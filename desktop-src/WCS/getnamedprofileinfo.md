---
title: GetNamedProfileInfo function
description: The GetNamedProfileInfo function retrieves information about the International Color Consortium (ICC) named color profile that is specified in the first parameter.
ms.assetid: '9791d32f-b343-4da7-add3-ed7bcecfd010'
keywords: ["GetNamedProfileInfo function Windows Color System"]
topic_type:
- apiref
api_name:
- GetNamedProfileInfo
api_location:
- mscms.dll
api_type:
- DllExport
---

# GetNamedProfileInfo function

The **GetNamedProfileInfo** function retrieves information about the International Color Consortium (ICC) named color profile that is specified in the first parameter.

## Syntax


```C++
BOOL WINAPI GetNamedProfileInfo(
   HPROFILE            hProfile,
   PNAMED_PROFILE_INFO pNamedProfileInfo
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

The handle to the ICC profile from which the information will be retrieved.

</dd> <dt>

*pNamedProfileInfo* 
</dt> <dd>

A pointer to a **NAMED\_PROFILE\_INFO** structure.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP; because named profiles are explicit ICC profile types.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Gdi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**NAMED\_PROFILE\_INFO**](named-profile-info.md)
</dt> </dl>

 

 





