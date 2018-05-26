---
Description: The IPrintOemUniDownloadFontHeader method allows a rendering plug-in for Unidrv to send a fonts header information to a printer.
ms.assetid: 3d660d04-2872-44e6-ab76-719f5262bdd8
title: IPrintOemUniDownloadFontHeader method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemUni::DownloadFontHeader method

The `IPrintOemUni::DownloadFontHeader` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to send a font's header information to a printer.

## Syntax


```C++
HRESULT DownloadFontHeader(
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

Receives a method-supplied value representing the amount of printer memory, in bytes, required to store the font header information. If the operation fails, the returned value should be zero.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::DownloadFontHeader` method is used for supporting soft fonts on printers that do not accept [*PCL*](wdkgloss.p#wdkgloss-pcl) commands. Its purpose is to allow a rendering plug-in to obtain font header information from Unidrv and to send the information to the printer.

Information that might be required for constructing a non-[*PCL*](wdkgloss.p#wdkgloss-pcl) font header can be obtained by:

-   Referencing the [**UNIFONTOBJ**](unifontobj.md) structure that is received as an input argument.

-   Calling the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function to get the font's [**FONTOBJ**](display.fontobj) structure.

The method should send the header information to the spooler by calling [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md).

The `IPrintOemUni::DownloadFontHeader` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "DownloadFontHeader" as input.

If you implement the `IPrintOemUni::DownloadFontHeader` method, you must also implement the [**IPrintOemUni::DownloadCharGlyph**](iprintoemuni-downloadcharglyph.md) method.

For additional information see [Customized Font Management](print.customized_font_management).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::DownloadFontHeader%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




