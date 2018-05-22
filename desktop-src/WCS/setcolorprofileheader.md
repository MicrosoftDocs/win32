---
title: SetColorProfileHeader function
description: The SetColorProfileHeader function sets the header data in a specified ICC color profile.
ms.assetid: 'a174712b-9977-4d3c-8baa-1b6e502db166'
keywords: ["SetColorProfileHeader function Windows Color System"]
topic_type:
- apiref
api_name:
- SetColorProfileHeader
api_location:
- mscms.dll
api_type:
- DllExport
---

# SetColorProfileHeader function

The **SetColorProfileHeader** function sets the header data in a specified ICC color profile.

## Syntax


```C++
BOOL WINAPI SetColorProfileHeader(
   HPROFILE       hProfile,
   PPROFILEHEADER pHeader
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the ICC color profile in question.

</dd> <dt>

*pHeader* 
</dt> <dd>

Pointer to the profile header data to write to the specified profile.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

If the color profile was not opened with read/write permission, **SetColorProfileHeader** fails.

**SetColorProfileHeader** overwrites the current header in the ICC profile.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP; because profile elements are implicitly associated with and hard coded to ICC tag types and there exist many robust XML parsing libraries.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**PROFILEHEADER**](profileheader.md)
</dt> </dl>

 

 





