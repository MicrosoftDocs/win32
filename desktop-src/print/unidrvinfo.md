---
Description: The UNIDRVINFO structure is used to specify printer-specific information within Unidrv font metrics files (.ufm files).
ms.assetid: f57514ed-33b2-4895-aaba-5866b6fc01d2
title: UNIDRVINFO structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# UNIDRVINFO structure

The UNIDRVINFO structure is used to specify printer-specific information within [Unidrv font metrics files](https://www.bing.com/search?q=Unidrv font metrics files) (.ufm files).

## Syntax


```C++
typedef struct _UNIDRVINFO {
  DWORD dwSize;
  DWORD flGenFlags;
  WORD  wType;
  WORD  fCaps;
  WORD  wXRes;
  WORD  wYRes;
  short sYAdjust;
  short sYMoved;
  WORD  wPrivateData;
  short sShift;
  INVOC SelectFont;
  INVOC UnSelectFont;
  WORD  wReserved[4];
} UNIDRVINFO, *PUNIDRVINFO;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the UNIDRVINFO structure.

</dd> <dt>

**flGenFlags**
</dt> <dd>

Contains one or more bit flags describing font characteristics. The following flags are defined:



| Flag                     | Definition                                                 |
|--------------------------|------------------------------------------------------------|
| UFM\_CART<br/>     | The font is contained in a cartridge.<br/>           |
| UFM\_SCALABLE<br/> | The font is scalable.<br/>                           |
| UFM\_SOFT<br/>     | The font is a soft font, requiring downloading.<br/> |



 

</dd> <dt>

**wType**
</dt> <dd>

Contains an integer constant describing the font type. The following constants are defined:



| Constant                           | Definition                                  |
|------------------------------------|---------------------------------------------|
| DF\_TYPE\_CAPSL<br/>         | Canon CAPSL scalable font<br/>        |
| DF\_TYPE\_HPINTELLIFONT<br/> | HP Intellifont font<br/>              |
| DF\_TYPE\_OEM1<br/>          | OEM-supplied scalable font<br/>       |
| DF\_TYPE\_OEM2<br/>          | OEM-supplied scalable font<br/>       |
| DF\_TYPE\_PST1<br/>          | Lexmark PPDS scalable font<br/>       |
| DF\_TYPE\_TRUETYPE<br/>      | HP PCLETTO font for LJ4 printers<br/> |



 

</dd> <dt>

**fCaps**
</dt> <dd>

Contains one or more bit flags identifying limitations on the capabilities provided by a device font. The following flags are defined:



| Flag                                 | Definition                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DF\_BKSP\_OK<br/>              | If set, a single backspace character can move the cursor to the beginning of the overstrike region. If not set, an x-movement cursor command must be sent.<br/> (Used only if MTYPE\_PAIRED is specified for the character's [**TRANSDATA**](transdata.md) structure in [**MAPTABLE**](maptable.md). Otherwise ignored.)<br/> |
| DF\_NO\_BOLD<br/>              | The device font cannot be bolded using underline simulation.<br/>                                                                                                                                                                                                                                                                     |
| DF\_NO\_DOUBLE\_UNDERLINE<br/> | The device font cannot be double-underlined using double-underline simulation.<br/>                                                                                                                                                                                                                                                   |
| DF\_NO\_STRIKETHRU<br/>        | The device font cannot be struck through using strike-through simulation.<br/>                                                                                                                                                                                                                                                        |
| DF\_NOITALIC<br/>              | The device font cannot be italicized using italic simulation.<br/>                                                                                                                                                                                                                                                                    |
| DF\_NOUNDER<br/>               | The device font cannot be underlined using underline simulation.<br/>                                                                                                                                                                                                                                                                 |
| DF\_XM\_CR<br/>                | Unidrv must send a carriage return command after each line of text.<br/>                                                                                                                                                                                                                                                              |



 

</dd> <dt>

**wXRes**
</dt> <dd>

Specifies the font's x-resolution.

</dd> <dt>

**wYRes**
</dt> <dd>

Specifies the font's y-resolution.

</dd> <dt>

**sYAdjust**
</dt> <dd>

Specifies the amount of vertical adjustment required before output of double-height characters on dot-matrix printers.

</dd> <dt>

**sYMoved**
</dt> <dd>

Specifies the amount of vertical cursor movement that results when a double-height character is printed on a dot-matrix printer.

</dd> <dt>

**wPrivateData**
</dt> <dd>

Can be used for printer-specific information such as, for example, HP DeskJet permutations.

</dd> <dt>

**sShift**
</dt> <dd>

Specifies the number of pixels by which each character must be shifted. Used for the Microsoft Z1a cartridge.

</dd> <dt>

**SelectFont**
</dt> <dd>

Is an [**INVOC**](invoc.md) structure containing the printer's font selection command.

</dd> <dt>

**UnSelectFont**
</dt> <dd>

Is an INVOC structure containing the printer's font deselection command.

</dd> <dt>

**wReserved**
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

A .ufm (Unidrv Font Metrics) file's UNIDRVINFO structure is accessed by a pointer in the file's [**UNIFM\_HDR**](unifm-hdr.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**INVOC**](invoc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UNIDRVINFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





