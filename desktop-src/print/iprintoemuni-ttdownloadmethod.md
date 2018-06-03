---
Description: The IPrintOemUni::TTDownloadMethod method enables a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType soft font.
ms.assetid: bf8c2baf-eaca-4d0e-a6d6-dba67b2f85db
title: IPrintOemUni::TTDownloadMethod method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::TTDownloadMethod method

The `IPrintOemUni::TTDownloadMethod` method enables a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType soft font.

## Syntax


```C++
HRESULT TTDownloadMethod(
        PDEVOBJ     pdevobj,
        PUNIFONTOBJ pUFObj,
  [out] DWORD       *pdwResult
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

*pdwResult* \[out\]
</dt> <dd>

Receives one of the following method-supplied constant values:



| Value                            | Definition                                                                                                                 |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| TTDOWNLOAD\_BITMAP<br/>    | Unidrv should download the specified font as bitmaps.<br/>                                                           |
| TTDOWNLOAD\_DONTCARE<br/>  | Unidrv can select the font format.<br/>                                                                              |
| TTDOWNLOAD\_GRAPHICS<br/>  | Unidrv should print TrueType fonts as graphics, instead of downloading the font.<br/>                                |
| TTDOWNLOAD\_TTOUTLINE<br/> | Unidrv should download the specified font as outlines. For more information, see the following Remarks section.<br/> |



 

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::TTDownloadMethod` method's purpose is to allow a rendering plug-in to specify a printer's preferred format for a specified TrueType soft font.

If a rendering plug-in implements the `IPrintOemUni::TTDownloadMethod` method, Unidrv calls the method each time it is ready to send a TrueType font to the print spooler. Unidrv specifies the font type and the `IPrintOemUni::TTDownloadMethod` method should specify the printer's preferred format in the location pointed to by *pdwResult*.

The method should not return TTDOWNLOAD\_TTOUTLINE unless the printer can rasterize TrueType fonts. The rendering plug-in is responsible for reading and parsing TrueType font files. Pointers to TrueType font files can be obtained by calling [**FONTOBJ\_pvTrueTypeFontFile**](https://www.bing.com/search?q=**FONTOBJ\_pvTrueTypeFontFile**).

The `IPrintOemUni::TTDownloadMethod` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "TTDownLoadMethod" as input.

For additional information see [Customized Font Management](https://www.bing.com/search?q=Customized Font Management).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni**](iprintoemuni-interface.md)
</dt> <dt>

[**DEVOBJ**](devobj.md)
</dt> <dt>

[**UNIFONTOBJ**](unifontobj.md)
</dt> <dt>

[**FONTOBJ\_pvTrueTypeFontFile**](https://www.bing.com/search?q=**FONTOBJ\_pvTrueTypeFontFile**)
</dt> <dt>

[**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::TTDownloadMethod%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





