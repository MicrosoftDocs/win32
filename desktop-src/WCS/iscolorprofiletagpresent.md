---
title: IsColorProfileTagPresent function
description: The IsColorProfileTagPresent function reports whether a specified International Color Consortium (ICC) tag is present in the specified color profile.
ms.assetid: '6cd5fed1-37ee-47b0-991b-f843b3028b17'
keywords: ["IsColorProfileTagPresent function Windows Color System"]
topic_type:
- apiref
api_name:
- IsColorProfileTagPresent
api_location:
- mscms.dll
api_type:
- DllExport
---

# IsColorProfileTagPresent function

The **IsColorProfileTagPresent** function reports whether a specified International Color Consortium (ICC) tag is present in the specified color profile.

## Syntax


```C++
BOOL WINAPI IsColorProfileTagPresent(
   HPROFILE hProfile,
   TAGTYPE  tag,
   PBOOL    pbPresent
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the ICC profile in question.

</dd> <dt>

*tag* 
</dt> <dd>

Specifies the ICC tag to check.

</dd> <dt>

*pbPresent* 
</dt> <dd>

Pointer to a variable that is set to **TRUE** on return if the specified ICC tag is present, or **FALSE** if not.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

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
</dt> </dl>

 

 





