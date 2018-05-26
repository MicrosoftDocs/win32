---
title: SetColorProfileElement function
description: The SetColorProfileElement function sets the element data for a tagged profile element in an ICC color profile.
ms.assetid: 9991cdf7-4ab4-49da-b1ea-70dbeff77f4c
keywords:
- SetColorProfileElement function Windows Color System
topic_type:
- apiref
api_name:
- SetColorProfileElement
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

# SetColorProfileElement function

The **SetColorProfileElement** function sets the element data for a tagged profile element in an ICC color profile.

## Syntax


```C++
BOOL WINAPI SetColorProfileElement(
   HPROFILE hProfile,
   TAGTYPE  tag,
   DWORD    dwOffset,
   PDWORD   pcbSize,
   PVOID    pBuffer
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

Identifies the tagged element.

</dd> <dt>

*dwOffset* 
</dt> <dd>

Specifies the offset from the first byte of the tagged element data at which to start writing.

</dd> <dt>

*pcbSize* 
</dt> <dd>

Pointer to a variable containing the number of bytes of data to write. On return, it contains the number of bytes actually written.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer containing the data to write to the tagged element in the color profile.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid ICC profile.

If the color profile is not opened for read/write permission, this function fails.

If *dwOffset* exceeds the size set for the specified tagged element, this function fails.

If *dwOffset* + *\*pcbSize* is greater than the size of the specified element, this function only writes as many bytes as will fit within the current size of the element.

Any existing data in the specified portion of the tagged element is overwritten when this function succeeds.

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

 

 





