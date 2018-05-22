---
title: ConvertColorNameToIndex function
description: The ConvertColorNameToIndex function converts color names in a named color space to index numbers in an International Color Consortium (ICC) color profile.
ms.assetid: '07d7774d-ccab-42aa-9801-2ab38435396d'
keywords: ["ConvertColorNameToIndex function Windows Color System"]
topic_type:
- apiref
api_name:
- ConvertColorNameToIndex
api_location:
- mscms.dll
api_type:
- DllExport
---

# ConvertColorNameToIndex function

The **ConvertColorNameToIndex** function converts color names in a named color space to index numbers in an International Color Consortium (ICC) color profile.

## Syntax


```C++
BOOL WINAPI ConvertColorNameToIndex(
   HPROFILE    hProfile,
   PCOLOR_NAME paColorName,
   PDWORD      paIndex,
   DWORD       dwCount
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

The handle to an ICC named color profile.

</dd> <dt>

*paColorName* 
</dt> <dd>

Pointer to an array of color name structures.

</dd> <dt>

*paIndex* 
</dt> <dd>

Pointer to an array of **DWORDS** that this function fills with the indices. The indices begin with one, not zero.

</dd> <dt>

*dwCount* 
</dt> <dd>

The number of color names to convert.

</dd> </dl>

## Return value

If this function succeeds with the conversion, the return value is **TRUE**.

If the conversion function fails, the return value is **FALSE**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP; because named profiles are explicit ICC profile types.

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

 

 





