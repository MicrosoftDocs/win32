---
Description: .
ms.assetid: 02E54636-0B8D-40FE-8405-0FB130139828
title: STDVARIABLEINDEX enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STDVARIABLEINDEX enumeration

## Syntax


```C++
typedef enum _STDVARIABLEINDEX { 
  SVI_NUMDATABYTES,
  SVI_WIDTHINBYTES,
  SVI_HEIGHTINPIXELS,
  SVI_COPIES,
  SVI_PRINTDIRECTION,
  SVI_DESTX,
  SVI_DESTY,
  SVI_DESTXREL,
  SVI_DESTYREL,
  SVI_LINEFEEDSPACING,
  SVI_RECTXSIZE,
  SVI_RECTYSIZE,
  SVI_GRAYPERCENT,
  SVI_NEXTFONTID,
  SVI_NEXTGLYPH,
  SVI_PHYSPAPERLENGTH,
  SVI_PHYSPAPERWIDTH,
  SVI_FONTHEIGHT,
  SVI_FONTWIDTH,
  SVI_FONTMAXWIDTH,
  SVI_FONTBOLD,
  SVI_FONTITALIC,
  SVI_FONTUNDERLINE,
  SVI_FONTSTRIKETHRU,
  SVI_CURRENTFONTID,
  SVI_TEXTYRES,
  SVI_TEXTXRES,
  SVI_GRAPHICSYRES,
  SVI_GRAPHICSXRES,
  SVI_ROP3,
  SVI_REDVALUE,
  SVI_GREENVALUE,
  SVI_BLUEVALUE,
  SVI_PALETTEINDEXTOPROGRAM,
  SVI_CURRENTPALETTEINDEX,
  SVI_PATTERNBRUSH_TYPE,
  SVI_PATTERNBRUSH_ID,
  SVI_PATTERNBRUSH_SIZE,
  SVI_CURSORORIGINX,
  SVI_CURSORORIGINY,
  SVI_PAGENUMBER,
  SVI_MAX
} STDVARIABLEINDEX;
```



## Constants

<dl> <dt>

<span id="SVI_NUMDATABYTES"></span><span id="svi_numdatabytes"></span>**SVI\_NUMDATABYTES**
</dt> <dd>

The number of data bytes.

</dd> <dt>

<span id="SVI_WIDTHINBYTES"></span><span id="svi_widthinbytes"></span>**SVI\_WIDTHINBYTES**
</dt> <dd>

The raster data width in bytes.

</dd> <dt>

<span id="SVI_HEIGHTINPIXELS"></span><span id="svi_heightinpixels"></span>**SVI\_HEIGHTINPIXELS**
</dt> <dd>

The raster data height in pixels.

</dd> <dt>

<span id="SVI_COPIES"></span><span id="svi_copies"></span>**SVI\_COPIES**
</dt> <dd>

The number of copies.

</dd> <dt>

<span id="SVI_PRINTDIRECTION"></span><span id="svi_printdirection"></span>**SVI\_PRINTDIRECTION**
</dt> <dd>

The print direction in CC degrees.

</dd> <dt>

<span id="SVI_DESTX"></span><span id="svi_destx"></span>**SVI\_DESTX**
</dt> <dd>

The x destination.

</dd> <dt>

<span id="SVI_DESTY"></span><span id="svi_desty"></span>**SVI\_DESTY**
</dt> <dd>

The y destination.

</dd> <dt>

<span id="SVI_DESTXREL"></span><span id="svi_destxrel"></span>**SVI\_DESTXREL**
</dt> <dd>

The relative x destination.

</dd> <dt>

<span id="SVI_DESTYREL"></span><span id="svi_destyrel"></span>**SVI\_DESTYREL**
</dt> <dd>

The relative y direction.

</dd> <dt>

<span id="SVI_LINEFEEDSPACING"></span><span id="svi_linefeedspacing"></span>**SVI\_LINEFEEDSPACING**
</dt> <dd>

The line feed spacing.

</dd> <dt>

<span id="SVI_RECTXSIZE"></span><span id="svi_rectxsize"></span>**SVI\_RECTXSIZE**
</dt> <dd>

The x rect size.

</dd> <dt>

<span id="SVI_RECTYSIZE"></span><span id="svi_rectysize"></span>**SVI\_RECTYSIZE**
</dt> <dd>

The y rect size.

</dd> <dt>

<span id="SVI_GRAYPERCENT"></span><span id="svi_graypercent"></span>**SVI\_GRAYPERCENT**
</dt> <dd>

The gray percentage.

</dd> <dt>

<span id="SVI_NEXTFONTID"></span><span id="svi_nextfontid"></span>**SVI\_NEXTFONTID**
</dt> <dd>

The next font ID.

</dd> <dt>

<span id="SVI_NEXTGLYPH"></span><span id="svi_nextglyph"></span>**SVI\_NEXTGLYPH**
</dt> <dd>

The next glyph.

</dd> <dt>

<span id="SVI_PHYSPAPERLENGTH"></span><span id="svi_physpaperlength"></span>**SVI\_PHYSPAPERLENGTH**
</dt> <dd>

The physical paper length.

</dd> <dt>

<span id="SVI_PHYSPAPERWIDTH"></span><span id="svi_physpaperwidth"></span>**SVI\_PHYSPAPERWIDTH**
</dt> <dd>

The physical paper width.

</dd> <dt>

<span id="SVI_FONTHEIGHT"></span><span id="svi_fontheight"></span>**SVI\_FONTHEIGHT**
</dt> <dd>

The font height.

</dd> <dt>

<span id="SVI_FONTWIDTH"></span><span id="svi_fontwidth"></span>**SVI\_FONTWIDTH**
</dt> <dd>

The font width.

</dd> <dt>

<span id="SVI_FONTMAXWIDTH"></span><span id="svi_fontmaxwidth"></span>**SVI\_FONTMAXWIDTH**
</dt> <dd>

The max font width.

</dd> <dt>

<span id="SVI_FONTBOLD"></span><span id="svi_fontbold"></span>**SVI\_FONTBOLD**
</dt> <dd>

The font is bold.

</dd> <dt>

<span id="SVI_FONTITALIC"></span><span id="svi_fontitalic"></span>**SVI\_FONTITALIC**
</dt> <dd>

The font is italicized.

</dd> <dt>

<span id="SVI_FONTUNDERLINE"></span><span id="svi_fontunderline"></span>**SVI\_FONTUNDERLINE**
</dt> <dd>

The font is underlined.

</dd> <dt>

<span id="SVI_FONTSTRIKETHRU"></span><span id="svi_fontstrikethru"></span>**SVI\_FONTSTRIKETHRU**
</dt> <dd>

The font has the strikethru style applied.

</dd> <dt>

<span id="SVI_CURRENTFONTID"></span><span id="svi_currentfontid"></span>**SVI\_CURRENTFONTID**
</dt> <dd>

The current font ID.

</dd> <dt>

<span id="SVI_TEXTYRES"></span><span id="svi_textyres"></span>**SVI\_TEXTYRES**
</dt> <dd>

The text y resolution.

</dd> <dt>

<span id="SVI_TEXTXRES"></span><span id="svi_textxres"></span>**SVI\_TEXTXRES**
</dt> <dd>

The text x resolution.

</dd> <dt>

<span id="SVI_GRAPHICSYRES"></span><span id="svi_graphicsyres"></span>**SVI\_GRAPHICSYRES**
</dt> <dd>

The graphics y resolution.

</dd> <dt>

<span id="SVI_GRAPHICSXRES"></span><span id="svi_graphicsxres"></span>**SVI\_GRAPHICSXRES**
</dt> <dd>

The graphics x resolution.

</dd> <dt>

<span id="SVI_ROP3"></span><span id="svi_rop3"></span>**SVI\_ROP3**
</dt> <dd>

The rop3.

</dd> <dt>

<span id="SVI_REDVALUE"></span><span id="svi_redvalue"></span>**SVI\_REDVALUE**
</dt> <dd>

The red value.

</dd> <dt>

<span id="SVI_GREENVALUE"></span><span id="svi_greenvalue"></span>**SVI\_GREENVALUE**
</dt> <dd>

The green value.

</dd> <dt>

<span id="SVI_BLUEVALUE"></span><span id="svi_bluevalue"></span>**SVI\_BLUEVALUE**
</dt> <dd>

The blue value.

</dd> <dt>

<span id="SVI_PALETTEINDEXTOPROGRAM"></span><span id="svi_paletteindextoprogram"></span>**SVI\_PALETTEINDEXTOPROGRAM**
</dt> <dd>

The palette index to program.

</dd> <dt>

<span id="SVI_CURRENTPALETTEINDEX"></span><span id="svi_currentpaletteindex"></span>**SVI\_CURRENTPALETTEINDEX**
</dt> <dd>

The current palette index.

</dd> <dt>

<span id="SVI_PATTERNBRUSH_TYPE"></span><span id="svi_patternbrush_type"></span>**SVI\_PATTERNBRUSH\_TYPE**
</dt> <dd>

The pattern brush type.

</dd> <dt>

<span id="SVI_PATTERNBRUSH_ID"></span><span id="svi_patternbrush_id"></span>**SVI\_PATTERNBRUSH\_ID**
</dt> <dd>

The pattern brush ID.

</dd> <dt>

<span id="SVI_PATTERNBRUSH_SIZE"></span><span id="svi_patternbrush_size"></span>**SVI\_PATTERNBRUSH\_SIZE**
</dt> <dd>

The pattern brush size.

</dd> <dt>

<span id="SVI_CURSORORIGINX"></span><span id="svi_cursororiginx"></span>**SVI\_CURSORORIGINX**
</dt> <dd>

The cursor origin x value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.

</dd> <dt>

<span id="SVI_CURSORORIGINY"></span><span id="svi_cursororiginy"></span>**SVI\_CURSORORIGINY**
</dt> <dd>

The cursor origin y value. This is in master units and in the coordinates of the currently selected orientation. This values is defined as ImageableOrigin minus CursorOrigin.

</dd> <dt>

<span id="SVI_PAGENUMBER"></span><span id="svi_pagenumber"></span>**SVI\_PAGENUMBER**
</dt> <dd>

The page number. This value tracks the number of times DrvStartBand has been called since StartDoc.

</dd> <dt>

<span id="SVI_MAX"></span><span id="svi_max"></span>**SVI\_MAX**
</dt> <dd>

Placeholder. Do not use.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20STDVARIABLEINDEX%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




