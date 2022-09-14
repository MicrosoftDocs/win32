---
description: This topic lists the constructors of the Font class. For a complete class listing, see Font Class.
ms.assetid: a0169751-50f6-41d9-bd59-3c85aec1bb78
title: Font.Font constructors
ms.date: 07/02/2019
ms.topic: reference
---

# Font.Font constructors

This topic lists the constructors of the [**Font**](/windows/win32/api/gdiplusheaders/nl-gdiplusheaders-font) class. For a complete class listing, see **Font Class**.

### Overload list



| Constructor                                                                                                                   | Description                                                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Font(HDC,HFONT)**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc_inconsthfont))                                                                | Creates a [**Font::Font**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc_inconsthfont)) object indirectly from a GDI logical font by using a handle to a GDI **LOGFONT** structure.<br/>                                                                                                                                   |
| [**Font(HDC,LOGFONTA\*)**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc_inconstlogfonta))                                            | Creates a [**Font::Font**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc_inconstlogfonta)) object directly from a GDI logical font. The GDI logical font is a **LOGFONTA** structure, which is the one-byte character version of a logical font. This constructor is provided for compatibility with GDI.<br/> |
| [**Font(HDC,LOGFONTW\*)**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc_inconstlogfontw))                                            | Creates a [**Font::Font**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc_inconstlogfontw)) object directly from a GDI logical font. The GDI logical font is a **LOGFONTW** structure, which is the wide character version of a logical font. This constructor is provided for compatibility with GDI.<br/>     |
| [**Font(FontFamily\*,REAL,INT,Unit)**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inconstfontfamily_inreal_inint_inunit))                                | Creates a [**Font::Font**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inconstfontfamily_inreal_inint_inunit)) object based on a [**FontFamily**](/windows/win32/api/gdiplusheaders/nl-gdiplusheaders-fontfamily) object, a size, a font style, and a unit of measurement.<br/>                                                                               |
| [**Font(WCHAR\*,REAL,INT,Unit,FontCollection\*)**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inconstwchar_inreal_inint_inunit_inconstfontcollection)) | Creates a [**Font::Font**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inconstwchar_inreal_inint_inunit_inconstfontcollection)) object based on a font family, a size, a font style, a unit of measurement, and a [**FontCollection**](/windows/win32/api/gdiplusheaders/nl-gdiplusheaders-fontcollection) object.<br/>                                     |
| [**Font(HDC)**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc))                                                                            | Creates a [**Font::Font**](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-font-font(inhdc)) object based on the GDI font object that is currently selected into a specified device context. This constructor is provided for compatibility with GDI. <br/>                                                                           |



 

 
