---
title: GetColorProfileElementTag function
description: The GetColorProfileElementTag function retrieves the tag name specified by dwIndex in the tag table of a given International Color Consortium (ICC) color profile, where dwIndex is a one-based index into that table.
ms.assetid: 6f3172ac-19e0-43c7-a0a7-587ae31ec2fa
keywords:
- GetColorProfileElementTag function Windows Color System
topic_type:
- apiref
api_name:
- GetColorProfileElementTag
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# GetColorProfileElementTag function

The **GetColorProfileElementTag** function retrieves the tag name specified by *dwIndex* in the tag table of a given International Color Consortium (ICC) color profile, where *dwIndex* is a one-based index into that table.

## Syntax


```C++
BOOL WINAPI GetColorProfileElementTag(
   HPROFILE hProfile,
   DWORD    dwIndex,
   PTAGTYPE pTag
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the ICC color profile in question.

</dd> <dt>

*dwIndex* 
</dt> <dd>

Specifies the one-based index of the tag to retrieve.

</dd> <dt>

*pTag* 
</dt> <dd>

Pointer to a variable in which the tag name is to be placed.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

**GetColorProfileElementTag** can be used to enumerate all tags in a profile after getting the number of tags in the profile using [**GetCountColorProfileElements**](getcountcolorprofileelements.md).

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP; because profile elements are implicitly associated with, and hard coded to, ICC tag types and there exist many robust XML parsing libraries.

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

 

 





