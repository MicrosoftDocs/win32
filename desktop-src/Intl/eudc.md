---
description: The EUDC registry key contains one or more subkeys containing values defining the fonts associated with end-user-defined characters (EUDCs) for a given code page.
ms.assetid: d78a1d8f-a239-4388-aa21-c162953fe355
title: EUDC
ms.topic: article
ms.date: 05/31/2018
---

# EUDC

The EUDC registry key contains one or more subkeys containing values defining the fonts associated with [end-user-defined characters (EUDCs)](end-user-defined-characters.md) for a given code page. It has the following registry location:

HKEY\_CURRENT\_USER\\EUDC

The format is:

EUDC SystemDefaultEUDCFont=TrueTypeEUDCFontFileName TrueTypeFontTypeface=TrueTypeEUDCFontFileName

where:



|                          |                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| SystemDefaultEUDCFont    | Predefined name used to set the system default font. There is no system default EUDC font unless this entry is explicitly specified.     |
| TrueTypeFontTypeface     | User-defined name associated with a non-EUDC TrueType font.                                                                              |
| TrueTypeEUDCFontFileName | String consisting of the file name of a separate EUDC font file. This file identifies a font to be associated with TrueTypeFontTypeface. |



 

The following example shows the EUDC key for code page 932.


```C++
HKEY_CURRENT_USER\EUDC\932
SystemDefaultEUDCFont=EUDC.TTF
MS Mincho=MINEUDC.TTF
MS Gothic=GTEUDC.TTF
```



The following example sets the system default EUDC font to be Eudc.ttf and associates the separate EUDC fonts Mineudc.ttf and Goteudc.ttf with the font names MS Mincho and MS Gothic, respectively.


```C++
SystemDefaultEUDCFont=EUDC.TTF
MS Mincho=MINEUDC.TTF
MS Gothic=GOTEUDC.TTF
```



When the Windows code page (system ACP) associated with the language for non-Unicode programs matches the subkey, the GDI subsystem looks to the subkey value pairs to obtain display information about the character. It first looks for a name matching the current font. If there is none, it examines the SystemDefaultEUDCFont value. If no value is defined, GDI treats the character as undefined.

Note that the text itself does not have to be in the Windows code page. For example, assume that the code page has the identifier 1252, the default Windows code page for English. An application passes the single Unicode code point U+E000, in the Unicode private use area (PUA), to [**DrawText**](/windows/win32/api/winuser/nf-winuser-drawtext). In this case, GDI looks at the registry values under 1252 to obtain the font information for the character display properties.

## Related topics

<dl> <dt>

[EUDC Registry Entries](eudc-registry-entries.md)
</dt> <dt>

[EUDCCodeRange](eudccoderange.md)
</dt> </dl>

 

 
