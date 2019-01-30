---
Description: 'This topic lists the constructors of the Font class. For a complete class listing, see Font Class.'
ms.assetid: 'a0169751-50f6-41d9-bd59-3c85aec1bb78'
title: 'Font.Font constructors'
---

# Font.Font constructors

This topic lists the constructors of the [**Font**](https://msdn.microsoft.com/library/ms534437(v=VS.85).aspx) class. For a complete class listing, see **Font Class**.

### Overload list



| Constructor                                                                                                                   | Description                                                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Font(HDC,HFONT)**](https://msdn.microsoft.com/library/ms536204(v=VS.85).aspx)                                                                | Creates a [**Font::Font**](https://msdn.microsoft.com/library/ms536204(v=VS.85).aspx) object indirectly from a GDI logical font by using a handle to a GDI **LOGFONT** structure.<br/>                                                                                                                                   |
| [**Font(HDC,LOGFONTA\*)**](https://msdn.microsoft.com/library/ms536205(v=VS.85).aspx)                                            | Creates a [**Font::Font**](https://msdn.microsoft.com/library/ms536205(v=VS.85).aspx) object directly from a GDI logical font. The GDI logical font is a **LOGFONTA** structure, which is the one-byte character version of a logical font. This constructor is provided for compatibility with GDI.<br/> |
| [**Font(HDC,LOGFONTW\*)**](https://msdn.microsoft.com/library/ms536206(v=VS.85).aspx)                                            | Creates a [**Font::Font**](https://msdn.microsoft.com/library/ms536206(v=VS.85).aspx) object directly from a GDI logical font. The GDI logical font is a **LOGFONTW** structure, which is the wide character version of a logical font. This constructor is provided for compatibility with GDI.<br/>     |
| [**Font(FontFamily\*,REAL,INT,Unit)**](https://msdn.microsoft.com/library/ms536203(v=VS.85).aspx)                                | Creates a [**Font::Font**](https://msdn.microsoft.com/library/ms536203(v=VS.85).aspx) object based on a [**FontFamily**](https://msdn.microsoft.com/library/ms534439(v=VS.85).aspx) object, a size, a font style, and a unit of measurement.<br/>                                                                               |
| [**Font(WCHAR\*,REAL,INT,Unit,FontCollection\*)**](https://msdn.microsoft.com/library/ms536207(v=VS.85).aspx) | Creates a [**Font::Font**](https://msdn.microsoft.com/library/ms536207(v=VS.85).aspx) object based on a font family, a size, a font style, a unit of measurement, and a [**FontCollection**](https://msdn.microsoft.com/library/ms534438(v=VS.85).aspx) object.<br/>                                     |
| [**Font(HDC)**](https://msdn.microsoft.com/library/ms536208(v=VS.85).aspx)                                                                            | Creates a [**Font::Font**](https://msdn.microsoft.com/library/ms536208(v=VS.85).aspx) object based on the GDI font object that is currently selected into a specified device context. This constructor is provided for compatibility with GDI. <br/>                                                                           |



 

 




