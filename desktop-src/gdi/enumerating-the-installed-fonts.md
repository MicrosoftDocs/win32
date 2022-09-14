---
description: In some instances, an application must be able to enumerate the available fonts and select the one most appropriate for a particular operation.
ms.assetid: 18db1b03-6e3c-4be3-b637-a21bf41cc080
title: Enumerating the Installed Fonts
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating the Installed Fonts

In some instances, an application must be able to enumerate the available fonts and select the one most appropriate for a particular operation. An application can enumerate the available fonts by calling the [EnumFonts](/windows/desktop/api/Wingdi/nf-wingdi-enumfontsa) or [EnumFontFamilies](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesa) function. These functions send information about the available fonts to a callback function that the application supplies. The callback function receives information in [LOGFONT](/windows/win32/api/wingdi/ns-wingdi-logfonta) and [NEWTEXTMETRIC](/windows/win32/api/wingdi/ns-wingdi-newtextmetrica) structures. (The [**NEWTEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-newtextmetrica) structure contains information about a TrueType font. When the callback function receives information about a non-TrueType font, the information is contained in a [TEXTMETRIC](/windows/win32/api/wingdi/ns-wingdi-textmetrica) structure.) By using this information, an application can limit the user's choices to only those fonts that are available.

The [**EnumFontFamilies**](/windows/win32/api/wingdi/nf-wingdi-enumfontfamiliesa) function is similar to the [**EnumFonts**](/windows/win32/api/wingdi/nf-wingdi-enumfontsa) function but includes some extra functionality. **EnumFontFamilies** allows an application to take advantage of styles available with TrueType fonts. New and upgraded applications should use **EnumFontFamilies** instead of **EnumFonts**.

TrueType fonts are organized around a typeface name (for example, Courier New) and style names (for example, italic, bold, and extra-bold). The [**EnumFontFamilies**](/windows/win32/api/wingdi/nf-wingdi-enumfontfamiliesa) function enumerates all the styles associated with a specified family name, not simply the bold and italic attributes. For example, when the system includes a TrueType font called Courier New Extra-Bold, **EnumFontFamilies** lists it with the other Courier New fonts. The capabilities of **EnumFontFamilies** are helpful for fonts with many or unusual styles and for fonts that cross international borders.

If an application does not supply a typeface name, the [EnumFonts](/windows/desktop/api/Wingdi/nf-wingdi-enumfontsa) and [EnumFontFamilies](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesa) functions supply information about one font in each available family. To enumerate all the fonts in a device context, the application can specify **NULL** for the typeface name, compile a list of the available typefaces, and then enumerate each font in each typeface.

The following example uses the [**EnumFontFamilies**](/windows/win32/api/wingdi/nf-wingdi-enumfontfamiliesa) function to retrieve the number of available raster, vector, and TrueType font families.


```C++
    UINT uAlignPrev; 
    int aFontCount[] = { 0, 0, 0 }; 
    char szCount[8];
        HRESULT hr;
        size_t * pcch; 
 
    EnumFontFamilies(hdc, (LPCTSTR) NULL, 
        (FONTENUMPROC) EnumFamCallBack, (LPARAM) aFontCount); 
 
    uAlignPrev = SetTextAlign(hdc, TA_UPDATECP); 
 
    MoveToEx(hdc, 10, 50, (LPPOINT)NULL); 
    TextOut(hdc, 0, 0, "Number of raster fonts: ", 24); 
    itoa(aFontCount[0], szCount, 10); 
        
        hr = StringCchLength(szCount, 9, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        }
    TextOut(hdc, 0, 0, szCount, *pcch); 
 
    MoveToEx(hdc, 10, 75, (LPPOINT)NULL); 
    TextOut(hdc, 0, 0, "Number of vector fonts: ", 24); 
    itoa(aFontCount[1], szCount, 10);
        hr = StringCchLength(szCount, 9, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        } 
    TextOut(hdc, 0, 0, szCount, *pcch); 
 
    MoveToEx(hdc, 10, 100, (LPPOINT)NULL); 
    TextOut(hdc, 0, 0, "Number of TrueType fonts: ", 26); 
    itoa(aFontCount[2], szCount, 10);
        hr = StringCchLength(szCount, 9, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        }
    TextOut(hdc, 0, 0, szCount, *pcch); 
 
    SetTextAlign(hdc, uAlignPrev); 
 
BOOL CALLBACK EnumFamCallBack(LPLOGFONT lplf, LPNEWTEXTMETRIC lpntm, DWORD FontType, LPVOID aFontCount) 
{ 
    int far * aiFontCount = (int far *) aFontCount; 
 
    // Record the number of raster, TrueType, and vector  
    // fonts in the font-count array.  
 
    if (FontType & RASTER_FONTTYPE) 
        aiFontCount[0]++; 
    else if (FontType & TRUETYPE_FONTTYPE) 
        aiFontCount[2]++; 
    else 
        aiFontCount[1]++; 
 
    if (aiFontCount[0] || aiFontCount[1] || aiFontCount[2]) 
        return TRUE; 
    else 
        return FALSE; 
 
    UNREFERENCED_PARAMETER( lplf ); 
    UNREFERENCED_PARAMETER( lpntm ); 
} 
```



This example uses two masks, RASTER\_FONTTYPE and TRUETYPE\_FONTTYPE, to determine the type of font being enumerated. If the RASTER\_FONTTYPE bit is set, the font is a raster font. If the TRUETYPE\_FONTTYPE bit is set, the font is a TrueType font. If neither bit is set, the font is a vector font. A third mask, DEVICE\_FONTTYPE, is set when a device (for example, a laser printer) supports downloading TrueType fonts; it is zero if the device is a display adapter, dot-matrix printer, or other raster device. An application can also use the DEVICE\_FONTTYPE mask to distinguish GDI-supplied raster fonts from device-supplied fonts. The system can simulate bold, italic, underline, and strikeout attributes for GDI-supplied raster fonts, but not for device-supplied fonts.

An application can also check bits 1 and 2 in the **tmPitchAndFamily** member of the [NEWTEXTMETRIC](/windows/win32/api/wingdi/ns-wingdi-newtextmetrica) structure to identify a TrueType font. If bit 1 is 0 and bit 2 is 1, the font is a TrueType font.

Vector fonts are categorized as OEM\_CHARSET instead of ANSI\_CHARSET. Some applications identify vector fonts by using this information, checking the **tmCharSet** member of the [**NEWTEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-newtextmetrica) structure. This categorization usually prevents the font mapper from choosing vector fonts unless they are specifically requested. (Most applications no longer use vector fonts because their strokes are single lines and they take longer to draw than TrueType fonts, which offer many of the same scaling and rotation features that required vector fonts.)

 

 
