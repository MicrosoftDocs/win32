---
Description: 'The IPrintOemDriverPS::DrvWriteSpoolBuf method is provided by the Pscript5 driver so that rendering plug-ins can send printer data to the spooler.'
ms.assetid: '91eb36b3-ea05-4a5e-8bba-47c262a4fa4a'
title: 'IPrintOemDriverPS::DrvWriteSpoolBuf method'
---

# IPrintOemDriverPS::DrvWriteSpoolBuf method

The `IPrintOemDriverPS::DrvWriteSpoolBuf` method is provided by the Pscript5 driver so that [rendering plug-ins](print.rendering_plug_ins) can send printer data to the spooler.

## Syntax


```C++
HRESULT DrvWriteSpoolBuf(
        PDEVOBJ pdevobj,
        PVOID   pBuffer,
        DWORD   cbSize,
  [out] DWORD   *pdwResult
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Caller-supplied pointer to a buffer containing data to be sent to the print spooler.

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied value representing the size, in bytes, of the buffer pointed to by *pBuffer*.

</dd> <dt>

*pdwResult* \[out\]
</dt> <dd>

Receives a method-supplied value representing the number of bytes sent to the spooler.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

Rendering plug-ins are described in [Customizing Microsoft's Printer Drivers](print.customizing_microsoft_s_printer_drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverPS::DrvWriteSpoolBuf%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




