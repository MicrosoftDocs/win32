---
Description: The IPrintOemUni3::SetBandSize method can be used with Unidrv-supported printers to specify the desired band size on the printed output.
ms.assetid: e75fdfa5-2b25-4d89-b3ef-40cb445f874f
title: IPrintOemUni3::SetBandSize method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni3::SetBandSize method

The `IPrintOemUni3::SetBandSize` method can be used with Unidrv-supported printers to specify the desired band size on the printed output.

## Syntax


```C++
HRESULT SetBandSize(
  [in] PDEVOBJ pdevobj,
  [in] INT     iFormat,
  [in] DWORD   dwPageWidthBytes,
  [in] DWORD   dwPageHeight,
  [in] DWORD   dwMaxHeight,
  [in] PDWORD  pdwRequiredHeight
);
```



## Parameters

<dl> <dt>

*pdevobj* \[in\]
</dt> <dd>

A caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*iFormat* \[in\]
</dt> <dd>

An integer value that specifies the format of the bitmap in terms of the number of bits of color information per pixel that are required. This parameter can be one of the following values.



| Value                                                                                                                                             | Meaning                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <span id="BMF_1BPP"></span><span id="bmf_1bpp"></span><dl> <dt>**BMF\_1BPP**</dt> </dl>    | Monochrome<br/>                           |
| <span id="BMF_4BPP"></span><span id="bmf_4bpp"></span><dl> <dt>**BMF\_4BPP**</dt> </dl>    | 4 bits per pixel<br/>                     |
| <span id="BMF_8BPP"></span><span id="bmf_8bpp"></span><dl> <dt>**BMF\_8BPP**</dt> </dl>    | 8 bits per pixel<br/>                     |
| <span id="BMF_16BPP"></span><span id="bmf_16bpp"></span><dl> <dt>**BMF\_16BPP**</dt> </dl> | 16 bits per pixel<br/>                    |
| <span id="BMF_24BPP"></span><span id="bmf_24bpp"></span><dl> <dt>**BMF\_24BPP**</dt> </dl> | 24 bits per pixel<br/>                    |
| <span id="BMF_32BPP"></span><span id="bmf_32bpp"></span><dl> <dt>**BMF\_32BPP**</dt> </dl> | 32 bits per pixel<br/>                    |
| <span id="BMF_4RLE"></span><span id="bmf_4rle"></span><dl> <dt>**BMF\_4RLE**</dt> </dl>    | 4 bits per pixel; run length encoded<br/> |
| <span id="BMF_8RLE"></span><span id="bmf_8rle"></span><dl> <dt>**BMF\_8RLE**</dt> </dl>    | 8 bits per pixel; run length encoded<br/> |



 

</dd> <dt>

*dwPageWidthBytes* \[in\]
</dt> <dd>

A Unidrv-supplied value that specifies the width of the printing area, in bytes.

</dd> <dt>

*dwPageHeight* \[in\]
</dt> <dd>

A Unidrv-supplied value that specifies the height of the printing area, in pixels.

</dd> <dt>

*dwMaxHeight* \[in\]
</dt> <dd>

A Unidrv-supplied value that specifies the maximum allowable height of the printing area, in pixels.

</dd> <dt>

*pdwRequiredHeight* \[in\]
</dt> <dd>

A caller-supplied pointer to a DWORD that contains the height of the printing area, in pixels, required by the rendering plug-in.

</dd> </dl>

## Return value

The method must return one of the following values:



| Return code                                                                               | Description                                        |
|-------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded. See Note.<br/>      |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed. See Note.<br/>         |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | Unidrv should compute the banding size.<br/> |



 

## Remarks

This method is available in Windows Vista and later.

This method is used by a rendering plug-in to specify band size using the plug-in's own calculations, rather than using Unidrv's band size calculations.

You can disable banding operations by Unidrv by setting the *dwPageHeight* value to \**pdwRequiredHeight*, but you should consider the performance effect of the height value that the rendering plug-in requests. For rendering, Unidrv needs at least the amount of memory that is calculated by multiplying *dwPageWidthBytes* by \**pdwRequiredHeight*. If the rendering plug-in supports the [**IPrintOemUni::DriverDMS**](iprintoemuni-driverdms.md) method and that method returns "S\_OK", `IPrintOemUni3::SetBandSize` is not called.

If this method is defined and the printer's generic printer description (GPD) file indicates that preanalysis is disabled (the GPD file includes "\***PreAnalysisOptions**: 0"), Unidrv calls this method to calculate band size. For information about the **PreAnalysisOptions** attribute, see [Preanalysis Infrastructure](https://www.bing.com/search?q=Preanalysis Infrastructure).

If the rendering plug-in supports [**IPrintOemUni::DriverDMS**](iprintoemuni-driverdms.md) and that method returns S\_OK, `IPrintOemUni3::SetBandSize` is not called.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni3::SetBandSize%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




