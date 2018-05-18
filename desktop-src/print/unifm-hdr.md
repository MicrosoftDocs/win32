---
Description: 'The UNIFM\_HDR structure is used to define the contents of Unidrv font metrics files (.ufm files).'
ms.assetid: '9490d090-2156-4653-9e56-a233d23c2fb3'
title: 'UNIFM\_HDR structure'
---

# UNIFM\_HDR structure

The UNIFM\_HDR structure is used to define the contents of [Unidrv font metrics files](print.customized_font_management#ddk-unidrv-font-metrics-files-gg) (.ufm files).

## Syntax


```C++
typedef struct _UNIFM_HDR {
  DWORD dwSize;
  DWORD dwVersion;
  ULONG ulDefaultCodepage;
  LONG  lGlyphSetDataRCID;
  DWORD loUnidrvInfo;
  DWORD loIFIMetrics;
  DWORD loExtTextMetric;
  DWORD loWidthTable;
  DWORD loKernPair;
  DWORD dwReserved[2];
} UNIFM_HDR, *PUNIFM_HDR;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the total size, in bytes, of the .ufm file. Note that this is the total size of all structures used to define the file. This value is not the size of the UNIFM\_HDR structure.

</dd> <dt>

**dwVersion**
</dt> <dd>

Specifies the file version number, as defined in prntfont.h by a constant with a name format of UNIFM\_VERSION\_*x*\_*x*.

</dd> <dt>

**ulDefaultCodepage**
</dt> <dd>

Specifies the code page identifier for the font's default code page. For more information, see the following Remarks section.

</dd> <dt>

**lGlyphSetDataRCID**
</dt> <dd>

Specifies an RC\_GTT resource identifier that identifies a .gtt (Glyph Translation Table) file, or one of the CC\_-prefixed code conversion identifiers defined in prntfont.h. For more information, see the following Remarks section.

</dd> <dt>

**loUnidrvInfo**
</dt> <dd>

Specifies the byte offset from the beginning of the .ufm (Unidrv Font Metrics) file to the location of the file's [**UNIDRVINFO**](unidrvinfo.md) structure.

</dd> <dt>

**loIFIMetrics**
</dt> <dd>

Specifies the byte offset from the beginning of the .ufm file to the location of the file's [**PRINTIFI32**](display.printifi32) structure.

</dd> <dt>

**loExtTextMetric**
</dt> <dd>

Specifies the byte offset from the beginning of the .ufm file to the location of the file's [**EXTTEXTMETRIC**](exttextmetric.md) structure.

</dd> <dt>

**loWidthTable**
</dt> <dd>

Specifies the byte offset from the beginning of the .ufm file to the location of the file's [**WIDTHTABLE**](widthtable.md) structure.

</dd> <dt>

**loKernPair**
</dt> <dd>

Specifies the byte offset from the beginning of the .ufm file to the location of the file's [**KERNDATA**](kerndata.md) structure.

</dd> <dt>

**dwReserved**
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

A UNIFM\_HDR structure must be the first structure contained in a .ufm file.

If **lGlyphSetDataRCID** is not CC\_DEFAULT, then the following rules apply:

-   If **lGlyphSetDataRCID** contains an RC\_GTT resource identifier, the code page number specified for **ulDefaultCodepage** must be the same code page number that is contained in the .gtt (Glyph Translation Table) file's first [**UNI\_CODEPAGEINFO**](uni-codepageinfo.md) structure.

-   If **lGlyphSetDataRCID** contains one of the CC\_-prefixed code conversion identifiers (other than CC\_DEFAULT), the code page number specified for **ulDefaultCodepage** must be the code page number that is associated with the CC\_-prefixed identifier. (These code page numbers are listed in Prntfont.h, next to each CC\_-prefixed identifier.)

    The character conversion codes predefined by the system, listed in Prntfont.h, are as follows:

    ```
    //
    // System predefined character conversion
    //
    // UNIDRV is going to support  following system predefined character conversion.
    // By speciffying these number in UNIFM.dwGlyphSetDataRCID;
    //

    #define CC_NOPRECNV 0x0000FFFF // Not use predefined

    //
    // ANSI
    //
    #define CC_DEFAULT  0 // Default Character Conversion
    #define CC_CP437   -1 // Unicode to IBM Codepage 437
    #define CC_CP850   -2 // Unicode to IBM Codepage 850
    #define CC_CP863   -3 // Unicode to IBM Codepage 863

    //
    // East Asia
    //

    #define CC_BIG5     -10 // Unicode to Chinese Big 5. Codepage 950.
    #define CC_ISC      -11 // Unicode to Korean Industrial Standard. Codepage 949.
    #define CC_JIS      -12 // Unicode to JIS X0208. Codepage 932.
    #define CC_JIS_ANK  -13 // Unicode to JIS X0208 except ANK. Codepage 932.
    #define CC_NS86     -14 // Big-5 to National Standstand conversion. Codepage 950
    #define CC_TCA      -15 // Big-5 to Taipei Computer Association. Codepage 950.
    #define CC_GB2312   -16 // Unicode to GB2312. Codepage 936
    #define CC_SJIS     -17 // Unicode to Shift-JIS. Codepage 932.
    #define CC_WANSUNG  -18 // Unicode to Extented Wansung. Codepage 949.
    ```

    

If **lGlyphSetDataRCID** is CC\_DEFAULT, there are no restrictions on the value specified for **ulDefaultCodepage**, but a default code page must be specified.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**UNIDRVINFO**](unidrvinfo.md)
</dt> <dt>

[**PRINTIFI32**](display.printifi32)
</dt> <dt>

[**EXTTEXTMETRIC**](exttextmetric.md)
</dt> <dt>

[**WIDTHTABLE**](widthtable.md)
</dt> <dt>

[**KERNDATA**](kerndata.md)
</dt> <dt>

[**UNI\_CODEPAGEINFO**](uni-codepageinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UNIFM_HDR%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





