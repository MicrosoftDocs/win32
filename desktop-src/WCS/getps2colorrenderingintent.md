---
title: GetPS2ColorRenderingIntent function
description: The GetPS2ColorRenderingIntent function retrieves the PostScript Level 2 color rendering intent from an ICC color profile.
ms.assetid: 2cb056d1-a3d5-4492-80ed-07c34f80c8db
keywords:
- GetPS2ColorRenderingIntent function Windows Color System
topic_type:
- apiref
api_name:
- GetPS2ColorRenderingIntent
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

# GetPS2ColorRenderingIntent function

The **GetPS2ColorRenderingIntent** function retrieves the PostScript Level 2 color [rendering intent](https://www.bing.com/search?q=rendering intent) from an ICC color profile.

## Syntax


```C++
BOOL WINAPI GetPS2ColorRenderingIntent(
   HPROFILE hProfile,
   DWORD    dwIntent,
   PBYTE    pBuffer,
   PDWORD   pcbSize
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

Specifies the desired rendering intent to retrieve. Valid values are:

INTENT\_PERCEPTUAL

 

INTENT\_SATURATION

 

INTENT\_RELATIVE\_COLORIMETRIC

 

INTENT\_ABSOLUTE\_COLORIMETRIC

For more information, see [Rendering Intents](rendering-intents.md).

</dd> <dt>

*pBuffer* 
</dt> <dd>

Points to a buffer in which the color rendering intent is to be placed. If the *pBuffer* pointer is set to **NULL**, the buffer size required is returned in *\*pcbSize*.

</dd> <dt>

*pcbSize* 
</dt> <dd>

Points to a variable containing the buffer size in bytes. On return, this variable contains the number of bytes actually copied.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**. If this function succeeds, the return value is **TRUE**. It also returns **TRUE** if the *pBuffer* parameter is **NULL** and the size required for the buffer is copied into *pcbSize.*

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

The rendering intent returned by **GetPS2ColorRenderingIntent** can be used as the operand for the PostScript Level 2 findcolorrendering operator.

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

 

 





