---
Description: The EXTTEXTMETRIC structure is used to specify font-specific information within Unidrv font metrics files (.ufm files).
ms.assetid: d3d2397c-71c3-4904-a1ad-96a94698e50c
title: EXTTEXTMETRIC structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# EXTTEXTMETRIC structure

The EXTTEXTMETRIC structure is used to specify font-specific information within [Unidrv font metrics files](https://www.bing.com/search?q=Unidrv font metrics files) (.ufm files).

## Syntax


```C++
typedef struct _EXTTEXTMETRIC {
  short emSize;
  short emPointSize;
  short emOrientation;
  short emMasterHeight;
  short emMinScale;
  short emMaxScale;
  short emMasterUnits;
  short emCapHeight;
  short emXHeight;
  short emLowerCaseAscent;
  short emLowerCaseDescent;
  short emSlant;
  short emSuperScript;
  short emSubScript;
  short emSuperScriptSize;
  short emSubScriptSize;
  short emUnderlineOffset;
  short emUnderlineWidth;
  short emDoubleUpperUnderlineOffset;
  short emDoubleLowerUnderlineOffset;
  short emDoubleUpperUnderlineWidth;
  short emDoubleLowerUnderlineWidth;
  short emStrikeOutOffset;
  short emStrikeOutWidth;
  WORD  emKernPairs;
  WORD  emKernTracks;
} EXTTEXTMETRIC, *PEXTTEXTMETRIC;
```



## Members

<dl> <dt>

**emSize**
</dt> <dd>

Specifies the size of the structure, in bytes.

</dd> <dt>

**emPointSize**
</dt> <dd>

Specifies the nominal point size of this font, in twips (1/20 of a point, or 1/1440 inch). This is the intended size of the font; the actual size may differ slightly depending on the resolution of the device.

</dd> <dt>

**emOrientation**
</dt> <dd>

Specifies the orientation of the font. The **emOrientation** member can be any of the following values:



| Value        | Meaning                                              |
|--------------|------------------------------------------------------|
| 0<br/> | Either portrait or landscape orientation <br/> |
| 1<br/> | Portrait orientation<br/>                      |
| 2<br/> | Landscape orientation<br/>                     |



 

</dd> <dt>

**emMasterHeight**
</dt> <dd>

Specifies the font size, in device units, for which the values in this font's extent table are exact.

</dd> <dt>

**emMinScale**
</dt> <dd>

Specifies the minimum valid point size for this font. The following equation illustrates how the minimum point size is determined:


```
smallest point size = (emMinScale * 72) / dfVertRes 
```



The value 72 represents the number of points per inch. The *dfVertRes* value is the number of dots per inch.

</dd> <dt>

**emMaxScale**
</dt> <dd>

Specifies the maximum valid point size for this font. The following equation illustrates how the maximum point size is determined:


```
largest point size = (etmMaxScale * 72) / dfVertRes 
```



The value 72 represents the number of points per inch. The *dfVertRes* value is the number of dots per inch.

</dd> <dt>

**emMasterUnits**
</dt> <dd>

Specifies the integral number of units per em, where an em equals the value of the **emMasterHeight** member. (That is, **emMasterUnits** is **emMasterHeight** expressed in font units instead of device units.)

</dd> <dt>

**emCapHeight**
</dt> <dd>

Specifies the height, in font units, of uppercase characters in the font. Typically, this is the height of uppercase H.

</dd> <dt>

**emXHeight**
</dt> <dd>

Specifies the height, in font units, of lowercase characters in the font. Typically, this is the height of lowercase x.

</dd> <dt>

**emLowerCaseAscent**
</dt> <dd>

Specifies the distance, in font units, that the ascender of lowercase letters extends above the base line. Typically, this is the height of lowercase d.

</dd> <dt>

**emLowerCaseDescent**
</dt> <dd>

Specifies the distance, in font units, that the descender of lowercase letters extends below the base line. Typically, this is specified for the descender of lowercase p.

</dd> <dt>

**emSlant**
</dt> <dd>

For an italic or slanted font, specifies the angle of the slant measured in tenths of a degree clockwise from the upright version of the font.

</dd> <dt>

**emSuperScript**
</dt> <dd>

Specifies the recommended amount, in font units, to offset superscript characters from the base line. This is typically a negative value.

</dd> <dt>

**emSubScript**
</dt> <dd>

Specifies the recommended amount, in font units, to offset subscript characters from the base line. This is typically a positive value.

</dd> <dt>

**emSuperScriptSize**
</dt> <dd>

Specifies the recommended size, in font units, of superscript characters for this font.

</dd> <dt>

**emSubScriptSize**
</dt> <dd>

Specifies the recommended size, in font units, of subscript characters for this font.

</dd> <dt>

**emUnderlineOffset**
</dt> <dd>

Specifies the offset, in font units, downward from the base line, where the top of a single underline bar should appear.

</dd> <dt>

**emUnderlineWidth**
</dt> <dd>

Specifies the thickness, in font units, of the underline bar.

</dd> <dt>

**emDoubleUpperUnderlineOffset**
</dt> <dd>

Specifies the offset, in font units, downward from the base line, where the top of the upper double-underline bar should appear.

</dd> <dt>

**emDoubleLowerUnderlineOffset**
</dt> <dd>

Specifies the offset, in font units, downward from the base line, where the top of the lower double-underline bar should appear.

</dd> <dt>

**emDoubleUpperUnderlineWidth**
</dt> <dd>

Specifies the thickness, in font units, of the upper underline bar.

</dd> <dt>

**emDoubleLowerUnderlineWidth**
</dt> <dd>

Specifies the thickness, in font units, of the lower underline bar.

</dd> <dt>

**emStrikeOutOffset**
</dt> <dd>

Specifies the offset, in font units, upward from the base line, where the top of a strikeout bar should appear.

</dd> <dt>

**emStrikeOutWidth**
</dt> <dd>

Specifies the thickness, in font units, of the strikeout bar.

</dd> <dt>

**emKernPairs**
</dt> <dd>

Specifies the number of character kerning pairs defined for this font.

</dd> <dt>

**emKernTracks**
</dt> <dd>

Specifies the number of kerning tracks defined for this font.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EXTTEXTMETRIC%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




