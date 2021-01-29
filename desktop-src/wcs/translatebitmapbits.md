---
title: TranslateBitmapBits function
description: The TranslateBitmapBits function translates the colors of a bitmap having a defined format so as to produce another bitmap in a requested format.
ms.assetid: c37f821c-fb03-4b98-9ee0-c0ad7fff4685
keywords:
- TranslateBitmapBits function Windows Color System
topic_type:
- apiref
api_name:
- TranslateBitmapBits
api_location:
- Mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# TranslateBitmapBits function

The **TranslateBitmapBits** function translates the colors of a bitmap having a defined format so as to produce another bitmap in a requested format.

## Syntax


```C++
BOOL WINAPI TranslateBitmapBits(
   HTRANSFORM    hColorTransform,
   PVOID         pSrcBits,
   BMFORMAT      bmInput,
   DWORD         dwWidth,
   DWORD         dwHeight,
   DWORD         dwInputStride,
   PVOID         pDestBits,
   BMFORMAT      bmOutput,
   DWORD         dwOutputStride,
   PBMCALLBACKFN pfnCallback,
   LPARAM        ulCallbackData
);
```



## Parameters

<dl> <dt>

*hColorTransform* 
</dt> <dd>

Identifies the color transform to use.

</dd> <dt>

*pSrcBits* 
</dt> <dd>

Pointer to the bitmap to translate.

</dd> <dt>

*bmInput* 
</dt> <dd>

Specifies the format of the input bitmap. Must be set to one of the values of the [**BMFORMAT**](/windows/win32/api/icm/ne-icm-bmformat) enumerated type.

> [!Note]  
> This function does not support [**BM\_XYZTRIPLETS**](/windows/win32/api/icm/ne-icm-bmformat) or **BM\_YxyTRIPLETS** as inputs.

 

</dd> <dt>

*dwWidth* 
</dt> <dd>

Specifies the number of pixels per scan line in the input bitmap.

</dd> <dt>

*dwHeight* 
</dt> <dd>

Specifies the number of scan lines in the input bitmap.

</dd> <dt>

*dwInputStride* 
</dt> <dd>

Specifies the number of bytes from the beginning of one scan line to the beginning of the next in the input bitmap; if set to zero, the function assumes that scan lines are padded so as to be **DWORD**-aligned.

</dd> <dt>

*pDestBits* 
</dt> <dd>

Pointer to the buffer in which to place the translated bitmap.

</dd> <dt>

*bmOutput* 
</dt> <dd>

Specifies the format of the output bitmap. Must be set to one of the values of the [**BMFORMAT**](/windows/win32/api/icm/ne-icm-bmformat) enumerated type.

</dd> <dt>

*dwOutputStride* 
</dt> <dd>

Specifies the number of bytes from the beginning of one scan line to the beginning of the next in the output bitmap; if set to zero, the function assumes that scan lines should be padded to be **DWORD**-aligned.

</dd> <dt>

*pfnCallback* 
</dt> <dd>

Pointer to a callback function called periodically by **TranslateBitmapBits** to report progress and allow the calling process to cancel the translation. (See [**ICMProgressProcCallback**](icmprogressproccallback.md) )

</dd> <dt>

*ulCallbackData* 
</dt> <dd>

Data passed back to the callback function, for example, to identify the translation that is reporting progress.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the input and output formats are not compatible with the color transform, this function fails.

When either of the floating point BMFORMATs, BM\_32b\_scARGB or BM\_32b\_scRGB are used, the color data being translated should not contain NaN or infinity. NaN and infinity are not considered to represent legitimate color component values, and the result of translating pixels containing NaN or infinity is meaningless in color terms. NaN or infinity values in the color data being processed will be handled silently, and an error will not be returned.

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

[**ICMProgressProcCallback**](icmprogressproccallback.md)
</dt> <dt>

[Windows Bitmap Header Structures](using-structures-in-wcs-1-0.md)
</dt> <dt>

[**BMFORMAT**](/windows/win32/api/icm/ne-icm-bmformat)
</dt> </dl>

 

 





