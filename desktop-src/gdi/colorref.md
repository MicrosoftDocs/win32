---
Description: The COLORREF value is used to specify an RGB color.
ms.assetid: b87d3de2-7a13-44ef-8253-c6851a75fa54
title: COLORREF
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COLORREF

The COLORREF value is used to specify an [RGB](/windows/win32/Wingdi/nf-wingdi-rgb?branch=master) color.


```C++
typedef DWORD COLORREF;
typedef DWORD* LPCOLORREF;
```



## Remarks

When specifying an explicit [RGB](/windows/win32/Wingdi/nf-wingdi-rgb?branch=master) color, the **COLORREF** value has the following hexadecimal form:

`0x00bbggrr`

The low-order byte contains a value for the relative intensity of red; the second byte contains a value for green; and the third byte contains a value for blue. The high-order byte must be zero. The maximum value for a single byte is 0xFF.

To create a **COLORREF** color value, use the [RGB](/windows/win32/Wingdi/nf-wingdi-rgb?branch=master) macro. To extract the individual values for the red, green, and blue components of a color value, use the [**GetRValue**](/windows/win32/Wingdi/nf-wingdi-getrvalue?branch=master), [GetGValue](/windows/win32/Wingdi/nf-wingdi-getgvalue?branch=master), and [GetBValue](/windows/win32/Wingdi/nf-wingdi-getbvalue?branch=master) macros, respectively.

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>Windef.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Colors Overview](colors.md)
</dt> <dt>

[Color Structures](color-structures.md)
</dt> <dt>

[GetBValue](/windows/win32/Wingdi/nf-wingdi-getbvalue?branch=master)
</dt> <dt>

[GetGValue](/windows/win32/Wingdi/nf-wingdi-getgvalue?branch=master)
</dt> <dt>

[**GetRValue**](/windows/win32/Wingdi/nf-wingdi-getrvalue?branch=master)
</dt> <dt>

[RGB](/windows/win32/Wingdi/nf-wingdi-rgb?branch=master)
</dt> </dl>

 

 




