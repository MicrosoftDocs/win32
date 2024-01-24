---
title: FONTDIRENTRY structure
description: Contains information about an individual font in a font resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 0ada2afe-b299-4ef2-99b7-96da10ee218a
keywords:
- FONTDIRENTRY structure Menus and Other Resources
topic_type:
- apiref
api_name:
- FONTDIRENTRY
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# FONTDIRENTRY structure

Contains information about an individual font in a font resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD  dfVersion;
  DWORD dfSize;
  CHAR  dfCopyright[60];
  WORD  dfType;
  WORD  dfPoints;
  WORD  dfVertRes;
  WORD  dfHorizRes;
  WORD  dfAscent;
  WORD  dfInternalLeading;
  WORD  dfExternalLeading;
  BYTE  dfItalic;
  BYTE  dfUnderline;
  BYTE  dfStrikeOut;
  WORD  dfWeight;
  BYTE  dfCharSet;
  WORD  dfPixWidth;
  WORD  dfPixHeight;
  BYTE  dfPitchAndFamily;
  WORD  dfAvgWidth;
  WORD  dfMaxWidth;
  BYTE  dfFirstChar;
  BYTE  dfLastChar;
  BYTE  dfDefaultChar;
  BYTE  dfBreakChar;
  WORD  dfWidthBytes;
  DWORD dfDevice;
  DWORD dfFace;
  DWORD dfReserved;
  CHAR  szDeviceName;
  CHAR  szFaceName;
} FONTDIRENTRY;
```



## Members

<dl> <dt>

**dfVersion**
</dt> <dd>

Type: **WORD**

</dd> <dd>

A user-defined version number for the resource data that tools can use to read and write resource files.

</dd> <dt>

**dfSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size of the file, in bytes.

</dd> <dt>

**dfCopyright\[60\]**
</dt> <dd>

Type: **CHAR**

</dd> <dd>

The font supplier's copyright information.

</dd> <dt>

**dfType**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The type of font file.

</dd> <dt>

**dfPoints**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The point size at which this character set looks best.

</dd> <dt>

**dfVertRes**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The vertical resolution, in dots per inch, at which this character set was digitized.

</dd> <dt>

**dfHorizRes**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The horizontal resolution, in dots per inch, at which this character set was digitized.

</dd> <dt>

**dfAscent**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The distance from the top of a character definition cell to the baseline of the typographical font.

</dd> <dt>

**dfInternalLeading**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The amount of leading inside the bounds set by the **dfPixHeight** member. Accent marks and other diacritical characters can occur in this area.

</dd> <dt>

**dfExternalLeading**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The amount of extra leading that the application adds between rows.

</dd> <dt>

**dfItalic**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

An italic font if not equal to zero.

</dd> <dt>

**dfUnderline**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

An underlined font if not equal to zero.

</dd> <dt>

**dfStrikeOut**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

A strikeout font if not equal to zero.

</dd> <dt>

**dfWeight**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The weight of the font in the range 0 through 1000. For example, 400 is roman and 700 is bold. If this value is zero, a default weight is used. For additional defined values, see the description of the [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure.

</dd> <dt>

**dfCharSet**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The character set of the font. For predefined values, see the description of the [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure.

</dd> <dt>

**dfPixWidth**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The width of the grid on which a vector font was digitized. For raster fonts, if the member is not equal to zero, it represents the width for all the characters in the bitmap. If the member is equal to zero, the font has variable-width characters.

</dd> <dt>

**dfPixHeight**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The height of the character bitmap for raster fonts or the height of the grid on which a vector font was digitized.

</dd> <dt>

**dfPitchAndFamily**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The pitch and the family of the font. For additional information, see the description of the [**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta) structure.

</dd> <dt>

**dfAvgWidth**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The average width of characters in the font (generally defined as the width of the letter x). This value does not include the overhang required for bold or italic characters.

</dd> <dt>

**dfMaxWidth**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The width of the widest character in the font.

</dd> <dt>

**dfFirstChar**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The first character code defined in the font.

</dd> <dt>

**dfLastChar**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The last character code defined in the font.

</dd> <dt>

**dfDefaultChar**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The character to substitute for characters not in the font.

</dd> <dt>

**dfBreakChar**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The character that will be used to define word breaks for text justification.

</dd> <dt>

**dfWidthBytes**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of bytes in each row of the bitmap. This value is always even so that the rows start on word boundaries. For vector fonts, this member has no meaning.

</dd> <dt>

**dfDevice**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The offset in the file to a null-terminated string that specifies a device name. For a generic font, this value is zero.

</dd> <dt>

**dfFace**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The offset in the file to a null-terminated string that names the typeface.

</dd> <dt>

**dfReserved**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

This member is reserved.

</dd> <dt>

**szDeviceName**
</dt> <dd>

Type: **CHAR**

</dd> <dd>

The name of the device if this font file is designated for a specific device.

</dd> <dt>

**szFaceName**
</dt> <dd>

Type: **CHAR**

</dd> <dd>

The typeface name of the font.

</dd> </dl>

## Remarks

There is one **FONTDIRENTRY** structure for every font in the .res file. Applications that generate .res files with font resources must also add to the file a **FONTDIRENTRY** structure for each font.

Font declarations can be mixed with other resource declarations in the .RC file because fonts do not need to be contiguous in the .res file.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DIRENTRY**](direntry.md)
</dt> <dt>

[**FONTGROUPHDR**](fontgrouphdr.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**LOGFONT**](/windows/win32/api/wingdi/ns-wingdi-logfonta)
</dt> </dl>

 

