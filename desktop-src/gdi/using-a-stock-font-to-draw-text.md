---
description: The system provides six stock fonts.
ms.assetid: 349ea57f-dd25-4e33-bbdf-63a320eae3a0
title: Using a Stock Font to Draw Text
ms.topic: article
ms.date: 05/31/2018
---

# Using a Stock Font to Draw Text

The system provides six stock fonts. A stock font is a logical font that an application can obtain by calling the [GetStockObject](/windows/desktop/api/Wingdi/nf-wingdi-getstockobject) function and specifying the requested font. The following list contains the values that you can specify to obtain a stock font.



| Value                 | Meaning                                                                                                                                                                                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ANSI\_FIXED\_FONT     | Specifies a monospace font based on the Windows character set. A Courier font is typically used.                                                                                                                                                                                                |
| ANSI\_VAR\_FONT       | Specifies a proportional font based on the Windows character set. MS Sans Serif is typically used.                                                                                                                                                                                              |
| DEVICE\_DEFAULT\_FONT | Specifies the preferred font for the specified device. This is typically the System font for display devices; however, for some dot-matrix printers this is a font that is resident on the device. (Printing with this font is usually faster than printing with a downloaded, bitmap font).    |
| OEM\_FIXED\_FONT      | Specifies a monospace font based on an OEM character set. For IBM computers and compatibles, the OEM font is based on the IBM PC character set.                                                                                                                                                 |
| SYSTEM\_FONT          | Specifies the System font. This is a proportional font based on the Windows character set, and is used by the operating system to display window titles, menu names, and text in dialog boxes. The System font is always available. Other fonts are available only if they have been installed. |
| SYSTEM\_FIXED\_FONT   | Specifies a monospace font compatible with the System font in early versions of Windows.                                                                                                                                                                                                        |



 

For more information on fonts, see [About Fonts](about-fonts.md).

The following example retrieves a handle to the variable stock font, selects it into a device context, and then writes a string using that font:


```C++
HFONT hFont, hOldFont; 

// Retrieve a handle to the variable stock font.  
hFont = (HFONT)GetStockObject(ANSI_VAR_FONT); 

// Select the variable stock font into the specified device context. 
if (hOldFont = (HFONT)SelectObject(hdc, hFont)) 
{
    // Display the text string.  
    TextOut(hdc, 10, 50, L"Sample ANSI_VAR_FONT text", 25); 

    // Restore the original font.        
    SelectObject(hdc, hOldFont); 
}
```



If other stock fonts are not available, [GetStockObject](/windows/desktop/api/Wingdi/nf-wingdi-getstockobject) returns a handle to the System font (SYSTEM\_FONT). You should use stock fonts only if the mapping mode for your application's device context is MM\_TEXT.

 

 



