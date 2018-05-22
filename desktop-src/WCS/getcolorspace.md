---
title: GetColorSpace function
description: The GetColorSpace function retrieves the handle to the input color space from a specified device context.
ms.assetid: '6d092755-2c7a-46a7-9127-df72c26c3ae9'
keywords: ["GetColorSpace function Windows Color System"]
topic_type:
- apiref
api_name:
- GetColorSpace
api_location:
- gdi32.dll
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32Full.dll
api_type:
- DllExport
---

# GetColorSpace function

The **GetColorSpace** function retrieves the handle to the input [color space](c.md#-color-wcs-1-0-glossary-color-space-gloss) from a specified device context.

## Syntax


```C++
HCOLORSPACE WINAPI GetColorSpace(
   HDC hDC
);
```



## Parameters

<dl> <dt>

*hDC* 
</dt> <dd>

Specifies a device context that is to have its input color space handle retrieved.

</dd> </dl>

## Return value

If the function succeeds, the return value is the current input color space handle.

If this function fails, the return value is **NULL**.

## Remarks

**GetColorSpace** obtains the handle to the input color space regardless of whether color management is enabled for the device context.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Gdi32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gdi32.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





