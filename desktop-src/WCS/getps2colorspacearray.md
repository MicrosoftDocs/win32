---
title: GetPS2ColorSpaceArray function
description: The GetPS2ColorSpaceArray function retrieves the PostScript Level 2 color space array from an ICC color profile.
ms.assetid: 2d7178e0-1535-48ce-8dbe-abd0d95cc294
keywords:
- GetPS2ColorSpaceArray function Windows Color System
topic_type:
- apiref
api_name:
- GetPS2ColorSpaceArray
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

# GetPS2ColorSpaceArray function

The **GetPS2ColorSpaceArray** function retrieves the PostScript Level 2 [color space](https://www.bing.com/search?q=color space) array from an ICC color profile.

## Syntax


```C++
BOOL WINAPI GetPS2ColorSpaceArray(
   HPROFILE hProfile,
   DWORD    dwIntent,
   DWORD    dwCSAType,
   PBYTE    pBuffer,
   PDWORD   pcbSize,
   PBOOL    pbBinary
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Specifies a handle to the ICC profile from which to retrieve the PostScript Level 2 color space array.

</dd> <dt>

*dwIntent* 
</dt> <dd>

Specifies the desired rendering intent for the color space array. This field may take one of the following values:

INTENT\_PERCEPTUAL

 

INTENT\_SATURATION

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_ABSOLUTE\_COLORIMETRIC

For more information, see [Rendering Intents](rendering-intents.md).

</dd> <dt>

*dwCSAType* 
</dt> <dd>

Specifies the type of color space array. See [Color Space Type Identifiers](color-space-type-identifiers.md).

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a buffer in which the color space array is to be placed. If the *pBuffer* pointer is set to **NULL**, the function returns the required size of the buffer in the memory location pointed to by *pcbSize*.

</dd> <dt>

*pcbSize* 
</dt> <dd>

Pointer to a variable containing the size of the buffer in bytes. On return, it contains the number of bytes copied into the buffer.

</dd> <dt>

*pbBinary* 
</dt> <dd>

Pointer to a Boolean variable. If set to **TRUE**, the data copied could be binary. If set to **FALSE**, data should be encoded as ASCII85. On return, the memory location pointed to by *pbBinary* indicates whether the data returned actually is binary (**TRUE**) or ASCII85 (**FALSE**).

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**. It also returns **TRUE** if the *pBuffer* parameter is **NULL** and the size required for the buffer is copied into *pcbSize.*

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the color space array is not available in the profile, the **GetPS2ColorSpaceArray** function builds a PostScript Level 2 color space array using the profile contents. This array can then be used as the operand for the PostScript Level2 setcolorspace operator.

This method does not support WCS profiles.

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

 

 





