---
title: SetColorProfileElementSize function
description: SetColorProfileElementSize sets the size of a tagged element in an ICC color profile.
ms.assetid: 59552ca3-5b53-465c-9634-a1cc68bb7c3e
keywords:
- SetColorProfileElementSize function Windows Color System
topic_type:
- apiref
api_name:
- SetColorProfileElementSize
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

# SetColorProfileElementSize function

**SetColorProfileElementSize** sets the size of a tagged element in an ICC color profile.

## Syntax


```C++
BOOL WINAPI SetColorProfileElementSize(
   HPROFILE hProfile,
   TAGTYPE  tag,
   DWORD    cbSize
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the ICC color profile in question.

</dd> <dt>

*tag* 
</dt> <dd>

Identifies the tagged element.

</dd> <dt>

*cbSize* 
</dt> <dd>

Specifies the size to set the tagged element to. If *cbSize* is zero, this function deletes the specified tagged element. If the tag is a reference, only the tag table entry is deleted, not the data.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

To create a new tagged element in a color profile, use **SetColorProfileElementSize** to set the size, then use [**SetColorProfileElement**](setcolorprofileelement.md) to set the element value.

If the specified tag already exists in the profile, **SetColorProfileElementSize** changes the size of the element by truncating it or adding zeroes at the end as the case may be.

If the specified tag already exists and is a reference to another tag, **SetColorProfileElementSize** creates a new data area for the tag that is not shared.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP; because profile elements are implicitly associated with and hard coded to ICC tag types and there exist many robust XML parsing libraries.

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
</dt> <dt>

[**SetColorProfileElement**](setcolorprofileelement.md)
</dt> </dl>

 

 





