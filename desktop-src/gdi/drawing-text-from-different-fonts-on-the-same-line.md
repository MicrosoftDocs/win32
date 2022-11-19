---
description: Different type styles within a font family can have different widths.
ms.assetid: d21613ef-1ba4-40bb-b922-afe287556441
title: Drawing Text from Different Fonts on the Same Line
ms.topic: article
ms.date: 05/31/2018
---

# Drawing Text from Different Fonts on the Same Line

Different type styles within a font family can have different widths. For example, bold and italic styles of a family are always wider than the roman style for a specified point size. When you display or print several type styles on a single line, you must keep track of the width of the line to avoid having characters displayed or printed on top of one another.

You can use two functions to retrieve the width (or extent) of text in the current font. The [GetTabbedTextExtent](/windows/desktop/api/Winuser/nf-winuser-gettabbedtextextenta) function computes the width and height of a character string. If the string contains one or more tab characters, the width of the string is based upon a specified array of tab-stop positions. The [GetTextExtentPoint32](/windows/desktop/api/Wingdi/nf-wingdi-gettextextentpoint32a) function computes the width and height of a line of text.

When necessary, the system synthesizes a font by changing the character bitmaps. To synthesize a character in a bold font, the system draws the character twice: at the starting point, and again one pixel to the right of the starting point. To synthesize a character in an italic font, the system draws two rows of pixels at the bottom of the character cell, moves the starting point one pixel to the right, draws the next two rows, and continues until the character has been drawn. By shifting pixels, each character appears to be sheared to the right. The amount of shear is a function of the height of the character.

One way to write a line of text that contains multiple fonts is to use the [**GetTextExtentPoint32**](/windows/win32/api/wingdi/nf-wingdi-gettextextentpoint32a) function after each call to [TextOut](/windows/desktop/api/Wingdi/nf-wingdi-textouta) and add the length to a current position. The following example writes the line "This is a sample string." using bold characters for "This is a", switches to italic characters for "sample", then returns to bold characters for "string." After printing all the strings, it restores the system default characters.


```C++
int XIncrement; 
int YStart; 
TEXTMETRIC tm; 
HFONT hfntDefault, hfntItalic, hfntBold; 
SIZE sz; 
LPSTR lpszString1 = "This is a "; 
LPSTR lpszString2 = "sample "; 
LPSTR lpszString3 = "string."; 
HRESULT hr;
size_t * pcch;
 
// Create a bold and an italic logical font.  
 
hfntItalic = MyCreateFont(); 
hfntBold = MyCreateFont(); 
 
 
// Select the bold font and draw the first string  
// beginning at the specified point (XIncrement, YStart).  
 
XIncrement = 10; 
YStart = 50; 
hfntDefault = SelectObject(hdc, hfntBold); 
hr = StringCchLength(lpszString1, 11, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        }
TextOut(hdc, XIncrement, YStart, lpszString1, *pcch); 
 
// Compute the length of the first string and add  
// this value to the x-increment that is used for the  
// text-output operation.  

hr = StringCchLength(lpszString1, 11, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        } 
GetTextExtentPoint32(hdc, lpszString1, *pcch, &sz); 
XIncrement += sz.cx; 
 
// Retrieve the overhang value from the TEXTMETRIC  
// structure and subtract it from the x-increment.  
// (This is only necessary for non-TrueType raster  
// fonts.)  
 
GetTextMetrics(hdc, &tm); 
XIncrement -= tm.tmOverhang; 
 
// Select an italic font and draw the second string  
// beginning at the point (XIncrement, YStart).  
 
hfntBold = SelectObject(hdc, hfntItalic); 
GetTextMetrics(hdc, &tm); 
XIncrement -= tm.tmOverhang;
hr = StringCchLength(lpszString2, 8, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        } 
TextOut(hdc, XIncrement, YStart, lpszString2, *pcch); 
 
// Compute the length of the second string and add  
// this value to the x-increment that is used for the  
// text-output operation.  

hr = StringCchLength(lpszString2, 8, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        }  
GetTextExtentPoint32(hdc, lpszString2, *pcch, &sz); 
XIncrement += sz.cx; 
 
// Reselect the bold font and draw the third string  
// beginning at the point (XIncrement, YStart).  
 
SelectObject(hdc, hfntBold);
hr = StringCchLength(lpszString3, 8, pcch);
        if (FAILED(hr))
        {
        // TODO: write error handler 
        }  
TextOut(hdc, XIncrement - tm.tmOverhang, YStart, lpszString3, 
            *pcch); 
 
// Reselect the original font.  
 
SelectObject(hdc, hfntDefault); 
 
// Delete the bold and italic fonts.  
 
DeleteObject(hfntItalic); 
DeleteObject(hfntBold); 
```



In this example, the [GetTextExtentPoint32](/windows/desktop/api/Wingdi/nf-wingdi-gettextextentpoint32a) function initializes the members of a [SIZE](/windows/win32/api/windef/ns-windef-size) structure with the length and height of the specified string. The [GetTextMetrics](/windows/desktop/api/Wingdi/nf-wingdi-gettextmetrics) function retrieves the overhang for the current font. Because the overhang is zero if the font is a TrueType font, the overhang value does not change the string placement. For raster fonts, however, it is important to use the overhang value.

The overhang is subtracted from the bold string once, to bring subsequent characters closer to the end of the string if the font is a raster font. Because overhang affects both the beginning and end of the italic string in a raster font, the glyphs start at the right of the specified location and end at the left of the endpoint of the last character cell. (The [**GetTextExtentPoint32**](/windows/win32/api/wingdi/nf-wingdi-gettextextentpoint32a) function retrieves the extent of the character cells, not the extent of the glyphs.) To account for the overhang in the raster italic string, the example subtracts the overhang before placing the string and subtracts it again before placing subsequent characters.

The [SetTextJustification](/windows/desktop/api/Wingdi/nf-wingdi-settextjustification) function adds extra space to the break characters in a line of text. You can use the [GetTextExtentPoint](/windows/desktop/api/WinGdi/nf-wingdi-gettextextentpointa) function to determine the extent of a string, then subtract that extent from the total amount of space the line should occupy, and use the [**SetTextJustification**](/windows/win32/api/wingdi/nf-wingdi-settextjustification) function to distribute the extra space among the break characters in the string. The [SetTextCharacterExtra](/windows/desktop/api/Wingdi/nf-wingdi-settextcharacterextra) function adds extra space to every character cell in the selected font, including the break character. (You can use the [GetTextCharacterExtra](/windows/desktop/api/Wingdi/nf-wingdi-gettextcharacterextra) function to determine the current amount of extra space being added to the character cells; the default setting is zero.)

You can place characters with greater precision by using the [GetCharWidth32](/windows/desktop/api/Wingdi/nf-wingdi-getcharwidth32a) or [GetCharABCWidths](/windows/desktop/api/Wingdi/nf-wingdi-getcharabcwidthsa) function to retrieve the widths of individual characters in a font. The [**GetCharABCWidths**](/windows/win32/api/wingdi/nf-wingdi-getcharabcwidthsa) function is more accurate than the [**GetCharWidth32**](/windows/win32/api/wingdi/nf-wingdi-getcharwidth32a) function, but it can only be used with TrueType fonts.

ABC spacing also allows an application to perform very accurate text alignment. For example, when the application right aligns a raster roman font without using ABC spacing, the advance width is calculated as the character width. This means the white space to the right of the glyph in the bitmap is aligned, not the glyph itself. By using ABC widths, applications have more flexibility in the placement and removal of white space when aligning text, because they have information that allows them to finely control intercharacter spacing.

 

 
