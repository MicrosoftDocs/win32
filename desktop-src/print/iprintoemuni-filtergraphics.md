---
Description: The IPrintOemUni::FilterGraphics method can be used with Unidrv-supported printers to modify scan line data and send it to the spooler.
ms.assetid: a1651745-08f0-44f2-bb9f-825d6497db42
title: IPrintOemUni::FilterGraphics method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::FilterGraphics method

The `IPrintOemUni::FilterGraphics` method can be used with Unidrv-supported printers to modify scan line data and send it to the spooler.

## Syntax


```C++
HRESULT FilterGraphics(
   PDEVOBJ pdevobj,
   PBYTE   pBuf,
   DWORD   dwLen
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pBuf* 
</dt> <dd>

Caller-supplied pointer to a buffer containing scan line data to be printed.

</dd> <dt>

*dwLen* 
</dt> <dd>

Caller-supplied value representing the length, in bytes, of the data pointed to by *pBuf*.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::FilterGraphics` method is used to modify scan line data before it is sent to the print spooler. The method is responsible for sending the data it receives to the spooler.

The `IPrintOemUni::FilterGraphics` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "FilterGraphics" as input.

If the `IPrintOemUni::FilterGraphics` method is implemented, Unidrv does not spool printer data. Instead, Unidrv calls this method each time a buffer of image data is ready to be spooled. Note that when this method is implemented, Unidrv also does not compress printer data, as it normally does. If you intend to make use of Unidrv compression, you should not implement this method. Also, you should modify **IPrintOemUni::GetImplementedMethod** so that it returns S\_FALSE when it is passed the string "FilterGraphics".

The method can perform final postprocessing of image data, such as removing adjacent dots or any other data stream filtering operation that Unidrv does not provide. It must then spool the data by calling the [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md) method.

`IPrintOemUni::FilterGraphics` method is called by Unidrv's [*DrvSendPage*](https://msdn.microsoft.com/d9c452e3-3850-4ca2-8114-b3866fbdeba6) function. If you want to implement `IPrintOemUni::FilterGraphics`, you must not completely override Unidrv's **DrvSendPage** or [**DrvNextBand**](https://msdn.microsoft.com/7c02d32b-6c95-4dd5-b9cf-2f64ba78f25a) functions.

Before Unidrv's **DrvSendPage** function calls the plug-in's `IPrintOemUni::FilterGraphics` implementation, **DrvSendPage**.

1.  If necessary, transposes the bitmap that is to be rendered.

2.  Transforms an output pass that consists of color data into a single contiguous array of data.

3.  Processes a group of scan lines and turn this data into commands for the printer.

4.  Sets X/Y position and passes the line of graphics data to the printer.

If the plug-in has implemented `IPrintOemUni::FilterGraphics,` Unidrv will call the plug-in with the scan line data instead of sending it to the printer.

The `IPrintOemUni::FilterGraphics` method allows a rendering plug-in to modify scan line data and send it to the spooler. If you implement this function, Unidrv will not spool your data. Instead, `IPrintOemUni::FilterGraphics` will be called every time a buffer of data is ready to be spooled and sent to the printer.

You can use `IPrintOemUni::FilterGraphics` to implement a special compression method or to perform bit manipulation on the data stream that is sent to the printer or both. In any situation, the driver's built-in compression code is not used. `IPrintOemUni::FilterGraphics` is presented with a block of data and is required to output this data by using the [**DrvWriteSpoolBuf**](drvwritespoolbuf.md) function. The core driver (Unidrv) will perform no further processing of the raster data after calling [**OEMFilterGraphics**](oemfiltergraphics.md).

When you implement the `IPrintOemUni::FilterGraphics` method in your plug-in, it will be used for sending the raster data directly to the printer. The number of scan lines in a block is specified through the \***PinsPerPhysPass** attribute that is associated with the [Resolution feature](https://www.bing.com/search?q=Resolution+feature) This attribute is optional, and if you do not specify it, it is set to 1 (like it is for most of the inkjet and page printers). Otherwise, \***PinsPerPhysPass** should be a multiple of 8. In `IPrintOemUni::FilterGraphics`, the *pBuf* parameter points to the buffer that contains the scan line raster data that you will manipulate if necessary (for example, for compression) and finally send out. The *dwLen* parameter is the length of the buffer that *pBuf* points to.

The following list describes several common scenarios for implementing `IPrintOemUni::FilterGraphics`:

1.  Special compression techniques

2.  Bit manipulation of the incoming raster data before sending it out to the printer

`IPrintOemUni::FilterGraphics` finally sends all of the data to the printer by using the [**DrvWriteSpoolBuf**](drvwritespoolbuf.md) function. The core driver (Unidrv) does not do any more processing on the data that `IPrintOemUni::FilterGraphics` sends out. If the plug-in is performing special compression or bit manipulation, the plug-in must allocate the buffers that are necessary for the special compression or bit manipulation. If the plug-in does not allocate its own buffers and if the compressed data is smaller than the source, the output will overwrite the source buffer.

The `IPrintOemUni::FilterGraphics` method gives you access to the scan line data itself and gives you the ability to post-process the raster data.

> [!Note]  
> The number of scan lines is equal to the height of the image. For example, a 1 bit per pixel (bpp) thickness of each scan line is equal to the width of 1 pixel, so the number of scan lines is equal to the height of the image.

 

For more information about customizing Unidrv's rendering operations, see [Unidrv-Specific Customized Rendering](https://www.bing.com/search?q=Unidrv-Specific+Customized+Rendering).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni**](iprintoemuni-interface.md)
</dt> <dt>

[**DrvNextBand**](https://msdn.microsoft.com/7c02d32b-6c95-4dd5-b9cf-2f64ba78f25a)
</dt> <dt>

[*DrvSendPage*](https://msdn.microsoft.com/d9c452e3-3850-4ca2-8114-b3866fbdeba6)
</dt> <dt>

[**DrvWriteSpoolBuf**](drvwritespoolbuf.md)
</dt> <dt>

[**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md)
</dt> <dt>

[**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md)
</dt> <dt>

[**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md)
</dt> <dt>

[**OEMFilterGraphics**](oemfiltergraphics.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::FilterGraphics%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





