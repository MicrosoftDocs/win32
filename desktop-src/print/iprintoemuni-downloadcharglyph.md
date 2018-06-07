---
Description: The IPrintOemUni::DownloadCharGlyph method enables a rendering plug-in for Unidrv to send a character glyph for a specified soft font to the printer.
ms.assetid: 1ce7ebaa-759e-418a-af07-e530b1102567
title: IPrintOemUni::DownloadCharGlyph method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::DownloadCharGlyph method

The `IPrintOemUni::DownloadCharGlyph` method enables a rendering plug-in for Unidrv to send a character glyph for a specified soft font to the printer.

## Syntax


```C++
HRESULT DownloadCharGlyph(
        PDEVOBJ     pdevobj,
        PUNIFONTOBJ pUFObj,
        HGLYPH      hGlyph,
        PDWORD      pdwWidth,
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

*hGlyph* 
</dt> <dd>

Caller-supplied glyph handle.

</dd> <dt>

*pdwWidth* 
</dt> <dd>

Caller-supplied pointer to receive the method-supplied width of the character.

</dd> <dt>

*pdwResult* \[out\]
</dt> <dd>

Receives a method-supplied value representing the amount of printer memory, in bytes, required to store the character glyph. If the operation fails, the returned value should be zero.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::DownloadCharGlyph` method is used for supporting soft fonts on printers that do not accept [*PCL*](https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c) commands. Its purpose is to enable a rendering plug-in to send a character glyph to the printer.

If a rendering plug-in implements the `IPrintOemUni::DownloadCharGlyph` method, Unidrv calls the method immediately after sending the command string specified by the CmdSetCharCode command entry, which is contained in the printer's [*GPD*](https://msdn.microsoft.com/f67c673d-c6f0-49f0-850a-d8b00e99ddd4) file. (GPD files are described in [Microsoft Universal Printer Driver](https://www.bing.com/search?q=Microsoft+Universal+Printer+Driver).) The method should do the following:

-   Call the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) function to obtain the glyph image specified by *hGlyph*.

-   Call [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md) to send the glyph to the printer.

-   Call the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) function again to obtain the glyph's width, then store the width in the address pointed to by *pdwWidth*.

-   Return the amount of printer memory required to store the glyph by placing it in the location specified by *pdwResult*.

The `IPrintOemUni::DownloadCharGlyph` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "DownloadCharGlyph" as input.

If you implement the `IPrintOemUni::DownloadCharGlyph` method, you must also implement the [**IPrintOemUni::DownloadFontHeader**](iprintoemuni-downloadfontheader.md) method.

For additional information see [Customized Font Management](https://www.bing.com/search?q=Customized+Font+Management).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::DownloadCharGlyph%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




