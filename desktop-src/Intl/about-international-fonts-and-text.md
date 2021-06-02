---
description: The topics in this section address the basic functionality of International Fonts.
ms.assetid: a47303b5-f49b-4d6c-b061-9d6475530e83
title: International Font Management
ms.topic: article
ms.date: 05/31/2018
---

# International Font Management

The topics in this section address the basic functionality of International Fonts. For instructions on using the international font technology in your applications, see [International Font Enumeration and Selection](using-international-fonts-and-text.md) and [Using MS Shell Dlg and MS Shell Dlg 2](using-ms-shell-dlg-and-ms-shell-dlg-2.md).

## Font Management Infrastructure

Starting with Windows 7, the font management infrastructure supports the hiding of fonts which are not appropriate for a user's font selection lists. The default system settings will choose to auto-hide fonts which are not designed for the input language(s) (keyboards) enabled on the OS system. In addition, users can choose to manually hide fonts in the Fonts Control Panel. This feature means users need no longer be faced with long lists of inappropriate fonts, and is particularly valuable for international users working in non-Latin scripts.

In Windows 7, there are no APIs for directly querying which fonts are hidden, or for setting fonts to be hidden. However, this does not mean you cannot take advantage of this feature in your application. If you use the Windows [**ChooseFont**](/previous-versions/windows/desktop/legacy/ms646914(v=vs.85)) API (Font common dialog) to enable font selection today, you will get the new behavior for free. The new Windows Scenic Ribbon (Font Controls) introduced in Windows 7 also supports this behavior and provides another reason to "Ribbonize" your applications. For details of using Font Controls in Ribbon and **ChooseFont** to display fonts while filtering out the hidden fonts, please reference [International Font Enumeration and Selection](using-international-fonts-and-text.md).

Note that hiding fonts only impacts font selection UI. It does not impact drawing APIs. When a font is selected into a device context, there is no effect on drawing due to the font being hidden. The [**EnumFontFamiliesEx**](/windows/win32/api/wingdi/nf-wingdi-enumfontfamiliesexa) function continues to enumerate fonts that are set to hidden.

## GDI Font Embedding and Subsetting

International Fonts technology makes use of the Font Embedding Services Library to allow you to bundle TrueType and OpenType fonts into a document or file. Embedding a font in a file guarantees that the font will be present on the computer receiving the file. For more information, see [Font Embedding Reference](../gdi/font-embedding-reference.md).

## Related topics

<dl> <dt>

[International Font Enumeration and Selection](using-international-fonts-and-text.md)
</dt> <dt>

[Using MS Shell Dlg and MS Shell Dlg 2](using-ms-shell-dlg-and-ms-shell-dlg-2.md)
</dt> <dt>

[Font Embedding Reference](../gdi/font-embedding-reference.md)
</dt> </dl>

 

 
