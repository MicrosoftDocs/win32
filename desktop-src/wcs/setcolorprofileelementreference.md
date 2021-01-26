---
title: SetColorProfileElementReference function
description: SetColorProfileElementReference creates in a specified ICC color profile a new tag which references the same data as an existing tag.
ms.assetid: 385a291c-6c15-4b8b-8b48-62d8a6513834
keywords:
- SetColorProfileElementReference function Windows Color System
topic_type:
- apiref
api_name:
- SetColorProfileElementReference
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# SetColorProfileElementReference function

**SetColorProfileElementReference** creates in a specified ICC color profile a new tag which references the same data as an existing tag.

## Syntax


```C++
BOOL WINAPI SetColorProfileElementReference(
   HPROFILE hProfile,
   TAGTYPE  newTag,
   TAGTYPE  refTag
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the ICC color profile in question.

</dd> <dt>

*newTag* 
</dt> <dd>

Identifies the new tag to create.

</dd> <dt>

*refTag* 
</dt> <dd>

Identifies the existing tag whose data is to be referenced by the new tag.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

If *newTag* already exists or *refTag* does not exist, **SetColorProfileElementReference** fails.

If the color profile was not opened with read/write permission, **SetColorProfileElementReference** fails.

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
</dt> </dl>

 

 





