---
Description: You can use the Font common dialog box to display available fonts.
ms.assetid: 317ea311-0592-432a-87b5-58296de003aa
title: Creating a Logical Font
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a Logical Font

You can use the **Font** common dialog box to display available fonts. The **ChooseFont** dialog box is displayed after an application initializes the members of a [**CHOOSEFONT**](_win32_choosefont_str_cpp) structure and calls the [**ChooseFont**](_win32_choosefont_cpp) function. After the user selects one of the available fonts and presses the **OK** button, the **ChooseFont** function initializes a [**LOGFONT**](/windows/win32/Wingdi/ns-wingdi-taglogfonta?branch=master) structure with the relevant data. Your application can then call the [**CreateFontIndirect**](/windows/win32/Wingdi/nf-wingdi-createfontindirecta?branch=master) function and create a logical font based on the user's request. The following example demonstrates how this is done.


```C++
HFONT FAR PASCAL MyCreateFont( void ) 
{ 
    CHOOSEFONT cf; 
    LOGFONT lf; 
    HFONT hfont; 
 
    // Initialize members of the CHOOSEFONT structure.  
 
    cf.lStructSize = sizeof(CHOOSEFONT); 
    cf.hwndOwner = (HWND)NULL; 
    cf.hDC = (HDC)NULL; 
    cf.lpLogFont = &amp;lf; 
    cf.iPointSize = 0; 
    cf.Flags = CF_SCREENFONTS; 
    cf.rgbColors = RGB(0,0,0); 
    cf.lCustData = 0L; 
    cf.lpfnHook = (LPCFHOOKPROC)NULL; 
    cf.lpTemplateName = (LPSTR)NULL; 
    cf.hInstance = (HINSTANCE) NULL; 
    cf.lpszStyle = (LPSTR)NULL; 
    cf.nFontType = SCREEN_FONTTYPE; 
    cf.nSizeMin = 0; 
    cf.nSizeMax = 0; 
 
    // Display the CHOOSEFONT common-dialog box.  
 
    ChooseFont(&amp;cf); 
 
    // Create a logical font based on the user's  
    // selection and return a handle identifying  
    // that font.  
 
    hfont = CreateFontIndirect(cf.lpLogFont); 
    return (hfont); 
} 
```



 

 



