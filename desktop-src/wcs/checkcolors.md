---
title: CheckColors function
description: The CheckColors function determines whether the colors in an array lie within the output gamut of a specified transform.
ms.assetid: 405b0d35-e15f-4b1d-b5de-619432a5c65b
keywords:
- CheckColors function Windows Color System
topic_type:
- apiref
api_name:
- CheckColors
api_location:
- mscms.dll
api_type:
- DllExport
ms.localizationpriority: high


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# CheckColors function

The **CheckColors** function determines whether the colors in an array lie within the output [gamut](g.md) of a specified transform.

## Syntax


```C++
BOOL WINAPI CheckColors(
   HTRANSFORM hColorTransform,
   PCOLOR     paInputColors,
   DWORD      nColors,
   COLORTYPE  ctInput,
   PBYTE      paResult
);
```



## Parameters

<dl> <dt>

*hColorTransform* 
</dt> <dd>

Handle to the color transform to use.

</dd> <dt>

*paInputColors* 
</dt> <dd>

Pointer to an array of *nColors* [**COLOR**](color.md) structures to translate.

</dd> <dt>

*nColors* 
</dt> <dd>

Contains the number of elements in the arrays pointed to by *paInputColors* and *paResult*.

</dd> <dt>

*ctInput* 
</dt> <dd>

Specifies the input color type.

</dd> <dt>

*paResult* 
</dt> <dd>

Pointer to an array of *nColors* bytes that receives the results of the test.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the input color type is not compatible with the color transform, **CheckColors** fails.

The function places results of the tests in the array pointed to by *paResult*. Each byte in the array corresponds to a **COLOR** element in the array pointed to by *paInputColors* and has an unsigned value between 0 and 255. The value 0 denotes that the color is in gamut, while a nonzero value denotes that it is out of gamut. For any integer *n* such that 0 &lt; *n* &lt; 255, a result value of *n* +1 indicates that the corresponding color is at least as far out of gamut as would be indicated by a result value of *n*.

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

[**The COLOR Structure**](color.md)
</dt> </dl>

 

 





