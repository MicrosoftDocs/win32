---
title: CheckBitmapBits function
description: The CheckBitmapBits function checks whether the pixels in a specified bitmap lie within the output gamut of a specified transform.
ms.assetid: c5e13ed4-71c8-4c9c-9206-406732a7669e
keywords:
- CheckBitmapBits function Windows Color System
topic_type:
- apiref
api_name:
- CheckBitmapBits
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# CheckBitmapBits function

The **CheckBitmapBits** function checks whether the pixels in a specified bitmap lie within the output [gamut](g.md) of a specified transform.

## Syntax


```C++
BOOL WINAPI CheckBitmapBits(
   HTRANSFORM    hColorTransform,
   PVOID         pSrcBits,
   BMFORMAT      bmInput,
   DWORD         dwWidth,
   DWORD         dwHeight,
   DWORD         dwStride,
   PBYTE         paResult,
   PBMCALLBACKFN pfnCallback,
   LPARAM        lpCallbackData
);
```



## Parameters

<dl> <dt>

*hColorTransform* 
</dt> <dd>

Handle to the color transform to use.

</dd> <dt>

*pSrcBits* 
</dt> <dd>

Pointer to the bitmap to check against the output gamut.

</dd> <dt>

*bmInput* 
</dt> <dd>

Specifies the format of the bitmap. Must be set to one of the values of the [**BMFORMAT**](bmformat.md) enumerated type.

</dd> <dt>

*dwWidth* 
</dt> <dd>

Specifies the number of pixels per scan line of the bitmap.

</dd> <dt>

*dwHeight* 
</dt> <dd>

Specifies the number of scan lines of the bitmap.

</dd> <dt>

*dwStride* 
</dt> <dd>

Specifies the number of bytes from the beginning one scan line to the beginning of the next one. If set to zero, the bitmap scan lines are assumed to be padded so as to be **DWORD**-aligned.

</dd> <dt>

*paResult* 
</dt> <dd>

Pointer to an array of bytes where the test results are to be placed. This results buffer must contain at least as many bytes as there are pixels in the bitmap.

</dd> <dt>

*pfnCallback* 
</dt> <dd>

Pointer to a callback function called periodically by **CheckBitmapBits** to report progress and allow the calling process to cancel the bitmap test. (See [**ICMProgressProcCallback**](icmprogressproccallback.md) )

</dd> <dt>

*lpCallbackData* 
</dt> <dd>

Data passed back to the callback function, for example, to identify the bitmap test about which progress is being reported.

</dd> </dl>

## Return value

If this function succeeds, the return value is a nonzero value.

If this function fails, the return value is zero. For extended error information, call **GetLastError**.

## Remarks

If the input format is not compatible with the color transform, the **CheckBitmapBits** function fails.

This function places results of the tests in the buffer pointed to by *paResult*. Each byte in the buffer corresponds to a pixel in the bitmap, and has an unsigned value between 0 and 255. The value 0 denotes that the color is in gamut, while a nonzero value denotes that it is out of gamut. For any integer *n* such that 0 &lt;*n* &lt; 255, a result value of *n* + 1 indicates that the corresponding color is at least as far out of gamut as would be indicated by a result value of *n*.

When either of the floating point BMFORMATs, BM\_32b\_scARGB or BM\_32b\_scRGB is used, the color data being checked should not contain NaN or infinity. NaN and infinity are not considered to represent legitimate color component values, and the result of checking pixels containing NaN or infinity is meaningless in color terms. NaN or infinity values in the color data being processed will be handled silently, and an error will not be returned.

The out-of-gamut information in the gamut tags created in WCS use the perceptual color distance in CIECAM02, which is the mean square root in CIECAM02 Jab space. The distance in the legacy ICC profile gamut tags is the mean square root in CIELAB space. We recommend that you use the CIECAM02 space when it is available because it provides more perceptually accurate distance metrics.

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

[**BMFORMAT**](bmformat.md)
</dt> </dl>

 

 





