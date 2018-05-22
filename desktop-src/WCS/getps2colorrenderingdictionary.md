---
title: GetPS2ColorRenderingDictionary function
description: The GetPS2ColorRenderingDictionary function retrieves the PostScript Level 2 color rendering dictionary from the specified ICC color profile.
ms.assetid: 'bf67fd0a-d32d-41e6-8868-ceb7bc8cd2f4'
keywords: ["GetPS2ColorRenderingDictionary function Windows Color System"]
topic_type:
- apiref
api_name:
- GetPS2ColorRenderingDictionary
api_location:
- mscms.dll
api_type:
- DllExport
---

# GetPS2ColorRenderingDictionary function

The **GetPS2ColorRenderingDictionary** function retrieves the PostScript Level 2 color rendering dictionary from the specified ICC color profile.

## Syntax


```C++
BOOL WINAPI GetPS2ColorRenderingDictionary(
   HPROFILE hProfile,
   DWORD    dwIntent,
   PBYTE    pBuffer,
   PDWORD   pcbSize,
   PBOOL    pbBinary
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the ICC color profile in question.

</dd> <dt>

*dwIntent* 
</dt> <dd>

Specifies the desired rendering intent for the color rendering dictionary. Valid values are:

INTENT\_PERCEPTUAL

 

INTENT\_SATURATION

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_ABSOLUTE\_COLORIMETRIC

For more information, see [Rendering Intents](rendering-intents.md).

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer in which the color rendering dictionary is to be placed. If the *pBuffer* pointer is set to **NULL**, the required buffer size is returned in *\*pcbSize*.

</dd> <dt>

*pcbSize* 
</dt> <dd>

Pointer to a variable containing the size of the buffer in bytes. On return, the variable contains the number of bytes actually copied.

</dd> <dt>

*pbBinary* 
</dt> <dd>

Pointer to a Boolean variable. If **TRUE**, the color rendering dictionary could be copied in binary form. If **FALSE**, the dictionary will be encoded in ASCII85 form. On return, this Boolean variable indicates whether the dictionary was actually binary (**TRUE**) or ASCII85 (**FALSE**).

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**. It also returns **TRUE** if the *pBuffer* parameter is **NULL** and the size required for the buffer is copied into *pcbSize.*

If this function fails, the return value is **FALSE**.

## Remarks

If the dictionary is not available in the profile, the **GetPS2ColorRenderingDictionary** function builds one using the profile contents. This dictionary can then be used as the operand for the PostScript Level 2 **setcolorrendering** operator.

This method does not support WCS profiles.

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

 

 





