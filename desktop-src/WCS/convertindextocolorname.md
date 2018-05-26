---
title: ConvertIndexToColorName function
description: The ConvertIndexToColorName transforms indices in a color space to an array of names in a named color space.
ms.assetid: 47506ccf-6106-46db-b5dc-90ba34135191
keywords:
- ConvertIndexToColorName function Windows Color System
topic_type:
- apiref
api_name:
- ConvertIndexToColorName
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

# ConvertIndexToColorName function

The **ConvertIndexToColorName** transforms indices in a color space to an array of names in a named color space.

## Syntax


```C++
BOOL WINAPI ConvertIndexToColorName(
   HPROFILE    hProfile,
   PDWORD      paIndex,
   PCOLOR_NAME paColorName,
   DWORD       dwCount
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

The handle to an International Color Consortium (ICC) color space profile.

</dd> <dt>

*paIndex* 
</dt> <dd>

Pointer to an array of color-space index numbers. The indices begin with one, not zero.

</dd> <dt>

*paColorName* 
</dt> <dd>

Pointer to an array of color name structures.

</dd> <dt>

*dwCount* 
</dt> <dd>

The number of indices to convert.

</dd> </dl>

## Return value

If this conversion function succeeds, the return value is **TRUE**.

If this conversion function fails, the return value is **FALSE**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP; because named profiles are explicit ICC profile types.

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

 

 





