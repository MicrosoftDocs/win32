---
Description: 'The IPrintOemUni3::DownloadPattern method downloads a pattern to a printer.'
ms.assetid: '7604a6df-c73a-4114-916f-1e777a323731'
title: 'IPrintOemUni3::DownloadPattern method'
---

# IPrintOemUni3::DownloadPattern method

The `IPrintOemUni3::DownloadPattern` method downloads a pattern to a printer.

## Syntax


```C++
HRESULT DownloadPattern(
   PDEVOBJ pdevobj,
   SURFOBJ *psoPattern,
   LONG    lPatternID
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

A pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*psoPattern* 
</dt> <dd>

A pointer to the [**SURFOBJ**](display.surfobj) structure that contains the pattern to download.

</dd> <dt>

*lPatternID* 
</dt> <dd>

The ID of the pattern to download.

</dd> </dl>

## Return value

If successful, this method should return S\_OK. Otherwise, this method should return an appropriate value in the returned HRESULT.

## Remarks

This method is available in Windows Vista and later.

You should implement this method if you want your rendering plug-in, rather than Unidrv, to download a pattern. If implemented, this method is called by **DrvRealizeBrush** for raster-mode print jobs. This method is not called for vector-mode print jobs.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni3**](iprintoemuni3-interface.md)
</dt> <dt>

[**DrvRealizeBrush**](display.drvrealizebrush)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni3::DownloadPattern%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





