---
description: This section contains a code sample that enables the user to select a font of a particular point size (by using the Choose Font dialog box), select a clip path (by using text drawn with this font), and then view the result of clipping to the text.
ms.assetid: 3eb5781b-972b-49a4-94db-9abda96fb195
title: Using Paths
ms.topic: article
ms.date: 05/31/2018
---

# Using Paths

This section contains a code sample that enables the user to select a font of a particular point size (by using the Choose Font dialog box), select a clip path (by using text drawn with this font), and then view the result of clipping to the text.

This code sample was used to create the illustration that appears in [Clip Paths](clip-paths.md).


```C++
CHOOSEFONT cf;          // common dialog box font structure  
LOGFONT lf;             // logical font structure  
HFONT hfont;            // new logical font handle  
HFONT hfontOld;         // original logical font handle  
HDC hdc;                // display DC handle  
int nXStart, nYStart;   // drawing coordinates  
RECT rc;                // structure for painting window  
SIZE sz;                // structure that receives text extents  
double aflSin[90];      // sine of 0-90 degrees  
double aflCos[90];      // cosine of 0-90 degrees  
double flRadius,a;      // radius of circle  
int iMode;              // clipping mode  
HRGN hrgn;              // clip region handle  
 
LRESULT APIENTRY MainWndProc( 
    HWND hwnd,                // window handle  
    UINT message,             // type of message  
    WPARAM wParam,            // additional information  
    LPARAM lParam)            // additional information  
 
{ 
 
    PAINTSTRUCT ps; 
 
    switch (message) 
    { 
        case WM_PAINT: 
            hdc = BeginPaint(hwnd, &ps); 
            EndPaint(hwnd, &ps); 
            break; 
 
        case WM_COMMAND:     // command from app's menu  
            switch (wParam) 
            { 
                case IDM_VANISH:  // erases client area  
                    hdc = GetDC(hwnd); 
                    GetClientRect(hwnd, &rc); 
                    FillRect(hdc, &rc, GetStockObject(WHITE_BRUSH)); 
                    ReleaseDC(hwnd, hdc); 
                    break; 
 
                case IDM_AND: // sets clip mode to RGN_AND  
                    iMode = RGN_AND; 
                    break; 
 
                case IDM_COPY: // sets clip mode to RGN_COPY  
                    iMode = RGN_COPY; 
                    break; 
 
                case IDM_DIFF: // sets clip mode to RGN_DIFF  
                    iMode = RGN_DIFF; 
                    break; 
 
                case IDM_OR: // sets clip mode to RGN_OR  
                    iMode = RGN_OR; 
                    break; 
 
                case IDM_XOR: // sets clip mode to RGN_XOR  
                    iMode = RGN_XOR; 
                    break; 
 
                case IDM_CLIP_PATH: 
 
                    // Retrieve a cached DC for the window.  
 
                    hdc = GetDC(hwnd); 
 
                    // Use the font requested by the user in the  
                    // Choose Font dialog box to create a logical 
                    // font, then select that font into the DC.  
 
                    hfont = CreateFontIndirect(cf.lpLogFont); 
                    hfontOld = SelectObject(hdc, hfont); 
 
                    // Retrieve the dimensions of the rectangle  
                    // that surrounds the text.  
 
                    GetTextExtentPoint32(hdc, "Clip Path", 9, &sz); 
 
                    // Set a clipping region using the rect that  
                    // surrounds the text.  
 
                    hrgn = CreateRectRgn(nXStart, nYStart, 
                        nXStart + sz.cx, 
                        nYStart + sz.cy); 
 
                    SelectClipRgn(hdc, hrgn); 
 
                    // Create a clip path using text drawn with  
                    // the user's requested font.  
 
                    BeginPath(hdc); 
                    TextOut(hdc, nXStart, nYStart, "Clip Path", 9); 
                    EndPath(hdc); 
                    SelectClipPath(hdc, iMode); 
 
                    // Compute the sine of 0, 1, ... 90 degrees.  
                    for (i = 0; i < 90; i++) 
                    { 
                        aflSin[i] = sin( (((double)i) / 180.0) 
                                    * 3.14159); 
                    } 
 
                    // Compute the cosine of 0, 1,... 90 degrees.  
                    for (i = 0; i < 90; i++) 
                    { 
                        aflCos[i] = cos( (((double)i) / 180.0) 
                                    * 3.14159); 
                    } 
 
                    // Set the radius value.  
 
                    flRadius = (double)(2 * sz.cx); 
 
                    // Draw the 90 rays extending from the  
                    // radius to the edge of the circle.  
 
                    for (i = 0; i < 90; i++) 
                    { 
                        MoveToEx(hdc, nXStart, nYStart, 
                           (LPPOINT) NULL); 
                        LineTo(hdc, nXStart + ((int) (flRadius 
                            * aflCos[i])), 
                               nYStart + ((int) (flRadius 
                            * aflSin[i]))); 
                    } 
 
                    // Reselect the original font into the DC.  
 
                    SelectObject(hdc, hfontOld); 
 
                    // Delete the user's font.  
 
                    DeleteObject(hfont); 
 
                    // Release the DC.  
 
                    ReleaseDC(hwnd, hdc); 
 
                    break; 
 
 
                case IDM_FONT: 
 
                    // Initialize necessary members.  
 
                    cf.lStructSize = sizeof (CHOOSEFONT); 
                    cf.hwndOwner = hwnd; 
                    cf.lpLogFont = &lf; 
                    cf.Flags = CF_SCREENFONTS | CF_EFFECTS; 
                    cf.rgbColors = RGB(0, 255, 255); 
                    cf.nFontType = SCREEN_FONTTYPE; 
 
                    // Display the Font dialog box, allow the user  
                    // to choose a font, and render text in the  
                    // window with that selection.  
 
                    if (ChooseFont(&cf)) 
                    { 
                        hdc = GetDC(hwnd); 
                        hfont = CreateFontIndirect(cf.lpLogFont); 
                        hfontOld = SelectObject(hdc, hfont); 
                        crOld = SetTextColor(hdc, cf.rgbColors); 
                        TextOut(hdc, nXStart, nYStart, 
                            "Clip Path", 9); 
                        SetTextColor(hdc, crOld); 
                        SelectObject(hdc, hfontOld); 
                        DeleteObject(hfont); 
                        ReleaseDC(hwnd, hdc); 
                    } 
 
                    break; 
 
                default: 
                    return DefWindowProc(hwnd, message, wParam, 
                        lParam); 
            } 
            break; 
 
        case WM_DESTROY:    // window is being destroyed  
            PostQuitMessage(0); 
            break; 
 
        default: 
            return DefWindowProc(hwnd, message, wParam, lParam); 
    } 
    return 0; 
} 
```



 

 



