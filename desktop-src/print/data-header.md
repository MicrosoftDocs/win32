---
Description: The DATA\_HEADER structure is used to specify a data section within a Unidrv font format file (.uff file).
ms.assetid: 8c7b6d2f-d2d9-49a5-8137-13d71dfd2611
title: DATA\_HEADER structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DATA\_HEADER structure

The DATA\_HEADER structure is used to specify a data section within a Unidrv font format file (.uff file).

## Syntax


```C++
typedef struct _DATA_HEADER {
  DWORD dwSignature;
  WORD  wSize;
  WORD  wDataID;
  DWORD dwDataSize;
  DWORD dwReserved;
} DATA_HEADER, *PDATA_HEADER;
```



## Members

<dl> <dt>

**dwSignature**
</dt> <dd>

Specifies the signature value identifying the type of data in the data section. Valid signature values are listed in the following table.



| Signature                 | Definition                                                                                                                                                                       |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DATA\_CTT\_SIG<br/> | This data section contains [*CTT*](https://www.bing.com/search?q=*CTT*)-formatted glyph set information.<br/> |
| DATA\_GTT\_SIG<br/> | This data section contains [*GTT*](https://www.bing.com/search?q=*GTT*)-formatted glyph set information.<br/>         |
| DATA\_IFI\_SIG<br/> | This data section contains IFI-formatted font metrics.<br/>                                                                                                                |
| DATA\_UFM\_SIG<br/> | This data section contains [*UFM*](https://www.bing.com/search?q=*UFM*)-formatted font metrics.<br/>                          |
| DATA\_VAR\_SIG<br/> | This data section contains data to be downloaded to the printer. See the following Remarks section.<br/>                                                                   |



 

</dd> <dt>

**wSize**
</dt> <dd>

Specifies the size, in bytes, of the DATA\_HEADER structure.

</dd> <dt>

**wDataID**
</dt> <dd>

If the data section contains font metrics data, this value must be a unique font identifier. For fonts that are permanently downloaded by the font installer, this value should be the downloaded font's identifier.

If the data section contains glyph data, this value must be a glyph set identifier.

If the data section contains variable data, this value must be zero.

</dd> <dt>

**dwDataSize**
</dt> <dd>

Specifies the size, in bytes, of all the information represented by this DATA\_HEADER structure. For example, if **dwSignature** is DATA\_UFM\_SIG, this value represents the size, in bytes, of the font's [**UNIFM\_HDR**](unifm-hdr.md) structure and all associated structures. The size value does not include any byte padding required to align the next DATA\_HEADER structure to a DWORD.

</dd> <dt>

**dwReserved**
</dt> <dd>

Not used. Must be set to zero.

</dd> </dl>

## Remarks

If **dwSignature** is DATA\_VAR\_SIG, the data section contains variable data that Unidrv sends to the printer the first time the font is selected. Typically, this data consists of a font header and corresponding font identifier, along with downloadable glyph information for all the glyphs supported by the font. [*PCL*](https://www.bing.com/search?q=*PCL*) soft font information includes printer control language commands for loading the font header and glyph definitions for all supported glyphs. Unidrv does not validate variable data. Data validation should be performed by the font installer.

Each DATA\_HEADER structure must be DWORD-aligned.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**UNIFM\_HDR**](unifm-hdr.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DATA_HEADER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





