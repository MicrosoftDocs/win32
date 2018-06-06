---
Description: The IPrintOemUni::Compression method can be used with Unidrv-supported printers to provide a customized bitmap compression method.
ms.assetid: 02524493-3842-462e-86f6-2ab35998c65e
title: IPrintOemUni::Compression method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::Compression method

The `IPrintOemUni::Compression` method can be used with Unidrv-supported printers to provide a customized bitmap compression method.

## Syntax


```C++
HRESULT Compression(
        PDEVOBJ pdevobj,
        PBYTE   pInBuf,
        PBYTE   pOutBuf,
        DWORD   dwInLen,
        DWORD   dwOutLen,
  [out] INT     *piResult
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pInBuf* 
</dt> <dd>

Caller-supplied pointer to input scan line data.

</dd> <dt>

*pOutBuf* 
</dt> <dd>

Caller-supplied pointer to an output buffer to receive compressed scan line data.

</dd> <dt>

*dwInLen* 
</dt> <dd>

Caller-supplied length of the input data.

</dd> <dt>

*dwOutLen* 
</dt> <dd>

Caller-supplied length of the output buffer.

</dd> <dt>

*piResult* \[out\]
</dt> <dd>

Receives a method-supplied result value. If the operation succeeds, this value should be the number of compressed bytes, which must not be larger than the value received for *dwOutLen*. If an error occurs, or if the method cannot compress, the result value should be -1.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::Compression` method is used by rendering plug-ins to compress scan line data before it is sent to the print spooler. The method's purpose is to provide support for printer-specific compression methods that are not supported by Unidrv.

If the `IPrintOemUni::Compression` method is defined, and if the printer's [*GPD*](https://msdn.microsoft.com/f67c673d-c6f0-49f0-850a-d8b00e99ddd4) file contains a CmdEnableOEMComp command entry, Unidrv calls the method each time a scan line is ready to be sent to the print spooler. (For information about the CmdEnableOEMComp command, see [Raster Data Compression Commands](https://www.bing.com/search?q=Raster+Data+Compression+Commands).)

The *pInBuf* and *dwInLen* parameter values describe a buffer containing a scan line of image data to be compressed. The *pOutBuf* and *dwOutLen* parameter values describe the buffer into which the `IPrintOemUni::Compression` method should place the compressed data.

Before Unidrv sends a scan line to the print spooler, it tries every enabled compression method to determine which one creates the smallest data stream. After it determines the best compression algorithm (by compressing the data using each method), it spools the printer command that enables the printer to accept the best compressed format, then sends the compressed data to the printer.

Therefore, the `IPrintOemUni::Compression` method is called for every scan line, whether the compressed data returned by the method is actually used or not. When the method is called, *dwOutLen* contains the length returned by the best compression method Unidrv has tried up to then. (If no other methods have been tried, *dwOutLen* contains the uncompressed length.) If the algorithm cannot produce a compressed scan line that is equal to or shorter than *dwOutLen* bytes, it should return -1 in the location specified by *piResult*.

If, after Unidrv tries all enabled compression methods, the compressed data returned by `IPrintOemUni::Compression` has the smallest length, Unidrv sends the buffer to the print spooler, preceded by the command specified by the CmdEnableOEMComp command entry.

If possible, the method's compression algorithm should use the received *dwOutLen* value to determine whether it can stop the algorithm before completion, to save time if another compression method has already created a better result.

The `IPrintOemUni::Compression` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "Compression" as input.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::Compression%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




