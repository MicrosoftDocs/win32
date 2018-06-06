---
Description: The IPrintOemUni::SendFontCmd method enables a rendering plug-in to modify a printer's font selection command and then send it to the printer.
ms.assetid: b90a94d1-c6f3-483c-b5fc-edfee27094ab
title: IPrintOemUni::SendFontCmd method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::SendFontCmd method

The `IPrintOemUni::SendFontCmd` method enables a rendering plug-in to modify a printer's font selection command and then send it to the printer.

## Syntax


```C++
HRESULT SendFontCmd(
   PDEVOBJ      pdevobj,
   PUNIFONTOBJ  pUFObj,
   PFINVOCATION pFInv
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

*pFInv* 
</dt> <dd>

Caller-supplied pointer to an [**FINVOCATION**](finvocation.md) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::SendFontCmd` method is used for selecting device fonts on printers that do not recognize the [*PCL*](wdkgloss.p#wdkgloss-pcl), CAPSL, or PPDS-formatted font commands supported by Unidrv. Its purpose is to allow a rendering plug-in to modify the font selection command that is specified in the font's .ufm (Unidrv Font Metrics) file. (To see how the command is stored, refer to the description of .ufm file's [**UNIDRVINFO**](unidrvinfo.md) structure.) If the command needs to be modified before being sent to the printer, you should implement the `IPrintOemUni::SendFontCmd` method.

The method receives the command string in the [**FINVOCATION**](finvocation.md) structure pointed to by *pFInv*. Typically, the string contains variables for which values must be supplied. For example, the following font selection command requires that *\#FontHeight* and *\#FontWidth* be replaced with numeric values:


```
\x1B(9U\x1B(s4148t0b0s#FontHeight1P\x1B)6J\x1B)s4148t0b0s#FontWidth1P
```



Current values for the font height and width can be obtained by calling [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) to read Unidrv's standard variables.

Whenever the `IPrintOemUni::SendFontCmd` method called, it must send the command string to the printer by calling [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md).

The `IPrintOemUni::SendFontCmd` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "SendFontCmd" as input.

For additional information see [Customized Font Management](https://www.bing.com/search?q=Customized+Font+Management).

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

[**FINVOCATION**](finvocation.md)
</dt> <dt>

[*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md)
</dt> <dt>

[**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md)
</dt> <dt>

[**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::SendFontCmd%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





