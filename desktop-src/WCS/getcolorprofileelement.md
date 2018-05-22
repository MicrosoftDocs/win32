---
title: GetColorProfileElement function
description: The GetColorProfileElement function copies data from a specified tagged profile element of a specified color profile into a buffer.
ms.assetid: '37bcfafc-7316-4c72-80df-c3424d639181'
keywords: ["GetColorProfileElement function Windows Color System"]
topic_type:
- apiref
api_name:
- GetColorProfileElement
api_location:
- mscms.dll
api_type:
- DllExport
---

# GetColorProfileElement function

The **GetColorProfileElement** function copies data from a specified tagged profile element of a specified color profile into a buffer.

## Syntax


```C++
BOOL WINAPI GetColorProfileElement(
   HPROFILE hProfile,
   TAGTYPE  tag,
   DWORD    dwOffset,
   PDWORD   pcbSize,
   PVOID    pBuffer,
   PBOOL    pbReference
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the International Color Consortium (ICC) color profile in question.

</dd> <dt>

*tag* 
</dt> <dd>

Identifies the tagged element from which to copy.

</dd> <dt>

*dwOffset* 
</dt> <dd>

Specifies the offset from the first byte of the tagged element data at which to begin copying.

</dd> <dt>

*pcbSize* 
</dt> <dd>

Pointer to a variable specifying the number of bytes to copy. On return, the variable contains the number of bytes actually copied.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer into which the tagged element data is to be copied. The buffer must contain at least as many bytes as are specified by the variable pointed to by *pcbSize*. If the *pBuffer* pointer is set to **NULL**, the size of the entire tagged element data in bytes is returned in the memory location pointed to by *pcbSize,* and *dwOffset* is ignored. In this case, the function will return **FALSE**.

</dd> <dt>

*pbReference* 
</dt> <dd>

Points to a Boolean value that is set to **TRUE** if more than one tag in the color profile refers to the same data as the specified tag refers to, or **FALSE** if not.

</dd> </dl>

## Return value

If this function succeeds, the return value is nonzero.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

This function will fail if *hProfile* is not a valid International Color Consortium (ICC) profile.

If the *pBuffer* pointer is set to **NULL**, the size of the entire tagged element data in bytes is returned in the variable pointed to by *pcbSize,* and *dwOffset* is ignored.

This function does not support Windows Color System (WCS) profiles CAMP, DMP, and GMMP; because profile elements are implicitly associated with, and hard coded to, ICC tag types and there exist many robust XML parsing libraries.

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

 

 





