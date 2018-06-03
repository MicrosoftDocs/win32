---
title: TranslateColors function
description: The TranslateColors function translates an array of colors from the source color space to the destination color space as defined by a color transform.
ms.assetid: 5c775e36-ee45-4b8a-ac12-6219063e185a
keywords:
- TranslateColors function Windows Color System
topic_type:
- apiref
api_name:
- TranslateColors
api_location:
- Mscms.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TranslateColors function

The **TranslateColors** function translates an array of colors from the source [color space](https://www.bing.com/search?q=color space) to the destination color space as defined by a color transform.

## Syntax


```C++
BOOL WINAPI TranslateColors(
   HTRANSFORM hColorTransform,
   PCOLOR     paInputColors,
   DWORD      nColors,
   COLORTYPE  ctInput,
   PCOLOR     paOutputColors,
   COLORTYPE  ctOutput
);
```



## Parameters

<dl> <dt>

*hColorTransform* 
</dt> <dd>

Identifies the color transform to use.

</dd> <dt>

*paInputColors* 
</dt> <dd>

Pointer to an array of *nColors*[**COLOR**](https://www.bing.com/search?q=**COLOR**) structures to translate.

</dd> <dt>

*nColors* 
</dt> <dd>

Contains the number of elements in the arrays pointed to by *paInputColors* and *paOutputColors*.

</dd> <dt>

*ctInput* 
</dt> <dd>

Specifies the input color type.

</dd> <dt>

*paOutputColors* 
</dt> <dd>

Pointer to an array of *nColors***COLOR** structures that receive the translated colors.

</dd> <dt>

*ctOutput* 
</dt> <dd>

Specifies the output color type.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the input and the output color types are not compatible with the color transform, this function fails.

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

 

 





