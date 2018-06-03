---
Description: The IPrintOemUni::OutputCharStr method enables a rendering plug-in to control the printing of font glyphs.
ms.assetid: 73518253-d65a-40ab-8735-44e92fbbed57
title: IPrintOemUni::OutputCharStr method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::OutputCharStr method

The `IPrintOemUni::OutputCharStr` method enables a rendering plug-in to control the printing of font glyphs.

## Syntax


```C++
HRESULT OutputCharStr(
   PDEVOBJ     pdevobj,
   PUNIFONTOBJ pUFObj,
   DWORD       dwType,
   DWORD       dwCount,
   PVOID       pGlyph
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pUFObj* 
</dt> <dd>

Caller-supplied pointer to a [**UNIFONTOBJ**](unifontobj.md) structure.

</dd> <dt>

*dwType* 
</dt> <dd>

Caller-supplied value indicating the type of glyph specifier array pointed to by *pGlyph*. Valid values are as follows:



| Value                        | Definition                                                                  |
|------------------------------|-----------------------------------------------------------------------------|
| TYPE\_GLYPHHANDLE<br/> | The *pGlyph* array elements are glyph handles of type HGLYPH.<br/>    |
| TYPE\_GLYPHID<br/>     | The *pGlyph* array elements are glyph identifiers of type DWORD.<br/> |



 

</dd> <dt>

*dwCount* 
</dt> <dd>

Caller-supplied value representing the number of glyph specifiers in the array pointed to by *pGlyph*.

</dd> <dt>

*pGlyph* 
</dt> <dd>

Caller-supplied pointer to an array of glyph specifiers, where the array element type is indicated by *dwType*.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::OutputCharStr` method is used for supporting printers that do not recognize the [*PCL*](https://www.bing.com/search?q=*PCL*), CAPSL, or PPDS-formatted character output commands supported by Unidrv. Its purpose is to allow a rendering plug-in to control the printing of a font's glyphs, and to provide glyph substitutions if necessary.

If a rendering plug-in implements the `IPrintOemUni::OutputCharStr` method, Unidrv calls the method each time a string of characters is ready to be spooled.

The method receives an array of glyph specifiers. The value received for *dwType* indicates the identifier type.

If the specified font is a device font, the array contains glyph handles. The handles need to be translated to character codes or commands, and then sent to the print spooler to cause device glyphs to be printed.

If the specified font is a soft (TrueType) font, the array contains glyph identifiers. The identifiers represent previously downloaded glyphs that need to be printed.

If the specified font is a device font, the method must do the following:

1.  Allocate a [**GETINFO\_GLYPHSTRING**](getinfo-glyphstring.md) structure with *dwTypeIn* set to TYPE\_GLYPHHANDLE and *dwTypeOut* set to TYPE\_TRANSDATA.

2.  Call the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) function, passing the GETINFO\_GLYPHSTRING structure as input, to obtain glyph translations as [**TRANSDATA**](transdata.md) structure contents.

3.  Call [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md) to send TRANSDATA structure contents to the print spooler, in order to print the glyphs.

If the specified font is a soft font, the method can just call **IPrintOemDriverUni::DrvWriteSpoolBuf** to send commands to the print spooler that will cause the specified previously-downloaded glyphs to be printed.

The `IPrintOemUni::OutputCharStr` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "OutputCharStr" as input.

For additional information see [Customized Font Management](https://www.bing.com/search?q=Customized Font Management).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::OutputCharStr%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




