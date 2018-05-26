---
Description: The Font common dialog box simplifies the process of creating and selecting fonts.
ms.assetid: 7183be25-a8e4-47a0-a34a-63eadf6ca10d
title: Font Creation and Selection
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Font Creation and Selection

The **Font** common dialog box simplifies the process of creating and selecting fonts. By initializing the [**CHOOSEFONT**](_win32_choosefont_str_cpp) structure and calling the [**ChooseFont**](_win32_choosefont_cpp) function, an application can support the same font-selection interface that previously required many lines of custom code. (For more information about the **Font** common dialog box, see [Common Dialog Box Library](_win32_common_dialog_box_library_cpp).)

## Selection by the User

Most font creation and selection operations involve the user. For example, word processing applications let the user select unique fonts for headings, footnotes, and body text. After the user selects a font by using the **Font** dialog box and presses the **OK** button, the [**ChooseFont**](_win32_choosefont_cpp) function initializes the members of a [**LOGFONT**](/windows/win32/Wingdi/ns-wingdi-taglogfonta?branch=master) structure with the attributes of the requested font. To use this font for text-output operations, an application must first create a logical font and then select that font into its device context. A *logical font* is an application-supplied description of an ideal font. A developer can create a logical font by calling the [**CreateFont**](/windows/win32/Wingdi/nf-wingdi-createfonta?branch=master) or the [**CreateFontIndirect**](/windows/win32/Wingdi/nf-wingdi-createfontindirecta?branch=master) functions. In this case, the application would call [**CreateFontIndirect**](gdi.CreateFontIndirect) and supply a pointer to the [**LOGFONT**](gdi.LOGFONT) structure initialized by [**CHOOSEFONT**](_win32_choosefont_str_cpp). In general, it is more efficient to call **CreateFontIndirect** because [**CreateFont**](gdi.CreateFont) requires several parameters while **CreateFontIndirect** requires only one pointer to **LOGFONT**.

Before an application can actually begin drawing text with a logical font, it must find the closest match from the fonts stored internally on the device and the fonts whose resources have been loaded into the operating system. The fonts stored on the device or in the operating system are called *physical fonts*. The process of finding the physical font that most closely matches a specified logical font is called font mapping. This process occurs when an application calls the [**SelectObject**](/windows/win32/Wingdi/nf-wingdi-selectobject?branch=master) function and supplies a handle identifying a logical font. Font mapping is performed by using an internal algorithm that compares the attributes of the requested logical font against the attributes of available physical fonts. When the font mapper algorithm completes its search and determines the closest possible match, the [**SelectObject**](gdi.SelectObject) function returns and the application can begin drawing text with the new font.

The [**SetMapperFlags**](/windows/win32/Wingdi/nf-wingdi-setmapperflags?branch=master) function specifies whether the font mapper algorithm searches only for physical fonts with aspect ratios that match the physical device. The aspect ratio for a device is the ratio formed by the width and the height of a pixel on that device.

The system font (also known as the shell or default font) is the font used for text in the title bars, menus, and dialog boxes.

## Special Font Selection Considerations

Although most font selection operations involve the user, there are some instances where this is not true. For example, a developer may want to use a unique font in an application to draw text in a control window. To select an appropriate font, the application must be able to determine what fonts are available, create a logical font that describes one of these available fonts, and then select that font into the appropriate device context.

An application can enumerate the available fonts by using the [**EnumFonts**](/windows/win32/Wingdi/nf-wingdi-enumfontsa?branch=master) or [**EnumFontFamilies**](/windows/win32/Wingdi/nf-wingdi-enumfontfamiliesa?branch=master) functions. [**EnumFontFamilies**](gdi.EnumFontFamilies) is recommended because it enumerates all the styles associated with a family name. This can be useful for fonts with many or unusual styles and for fonts that cross international borders.

Once an application has enumerated the available fonts and located an appropriate match, it should use the values returned by the font enumeration function to initialize the members of a [**LOGFONT**](/windows/win32/Wingdi/ns-wingdi-taglogfonta?branch=master) structure. Then it can call the [**CreateFontIndirect**](/windows/win32/Wingdi/nf-wingdi-createfontindirecta?branch=master) function, passing to it a pointer to the initialized [**LOGFONT**](gdi.LOGFONT) structure. If the [**CreateFontIndirect**](gdi.CreateFontIndirect) function is successful, the application can then select the logical font by calling the [**SelectObject**](/windows/win32/Wingdi/nf-wingdi-selectobject?branch=master) function. When initializing the members of the **LOGFONT** structure, be sure to specify a specific character set in the **lfCharSet** member. This member is important in the font mapping process and the results will be inconsistent if this member is not initialized correctly. If you specify a typeface name in the **lfFaceName** member of the **LOGFONT** structure, make sure that the **lfCharSet** value matches the character set of the typeface specified in **lfFaceName**. For example, if you want to select a font such as MS Mincho, **lfCharSet** must be set to the predefined value SHIFTJIS\_CHARSET.

The fonts for many East Asian languages have two typeface names: an English name and a localized name. [**CreateFont**](/windows/win32/Wingdi/nf-wingdi-createfonta?branch=master), [**CreateFontIndirect**](/windows/win32/Wingdi/nf-wingdi-createfontindirecta?branch=master), and [**CreateFontIndirectEx**](/windows/win32/Wingdi/nf-wingdi-createfontindirectexa?branch=master) take the localized typeface name for a system locale that matches the language, but they take the English typeface name for all other system locales. The best method is to try one name and, on failure, try the other. Note that [**EnumFonts**](gdi.EnumFonts), [**EnumFontFamilies**](gdi.EnumFontFamilies), and [**EnumFontFamiliesEx**](/windows/win32/Wingdi/nf-wingdi-enumfontfamiliesexa?branch=master) return the English typeface name if the system locale does not match the language of the font. Starting with Windows 2000, this is no longer a problem because the font mapper for [**CreateFont**](gdi.CreateFont), [**CreateFontIndirect**](gdi.CreateFontIndirect), and [**CreateFontIndirectEx**](gdi.CreateFontIndirectEx) recognizes either typeface name, regardless of locale.

 

 



