---
Description: 'The IPrintOemPS::DisablePDEV method allows a rendering plug-in for Pscript5 to delete the private PDEV structure that was allocated by its IPrintOemPS::EnablePDEV method.'
ms.assetid: '131a3113-1d65-44e7-8752-bf4cdc20129d'
title: 'IPrintOemPS::DisablePDEV method'
---

# IPrintOemPS::DisablePDEV method

The `IPrintOemPS::DisablePDEV` method allows a rendering plug-in for Pscript5 to delete the private PDEV structure that was allocated by its [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md) method.

## Syntax


```C++
STDMETHOD DisablePDEV(
   PDEVOBJ pdevobj
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemPS::DisablePDEV` method performs the same types of operations as the [**DrvDisablePDEV**](display.drvdisablepdev) function that is exported by a printer graphics DLL. Its purpose is to allow a rendering plug-in to delete the private PDEV structure that is pointed to by the DEVOBJ structure's **pdevOEM** member. This PDEV structure is one that was allocated by the plug-in's [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md) method.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS::DisablePDEV%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




