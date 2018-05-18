---
Description: 'This section describes the methods defined for the IPrintOemDriverUni COM interface.'
ms.assetid: 'efd13e9e-ba25-4d1c-894c-a275374f5266'
title: IPrintOemDriverUni interface
---

# IPrintOemDriverUni interface

This section describes the methods defined for the IPrintOemDriverUni COM interface.

## Members

The **IPrintOemDriverUni** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintOemDriverUni** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemDriverUni** interface has these methods.



| Method                                                                                          | Description                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPrintOemDriverUni::DrvGetDriverSetting**](iprintoemdriveruni-drvgetdriversetting.md)       | The `IPrintOemDriverUni::DrvGetDriverSetting` method is provided by the Unidrv driver so that rendering plug-ins can obtain the current status of printer features and other internal information.<br/>                                                                |
| [**IPrintOemDriverUni::DrvGetGPDData**](iprintoemdriveruni-drvgetgpddata.md)                   | The `IPrintOemDriverUni::DrvGetGPDData` method is provided by the Unidrv driver so that rendering plug-ins can obtain data defined in a printer's [*GPD*](wdkgloss.g#wdkgloss-generic-printer-description--gpd-) file.<br/> |
| [**IPrintOemDriverUni::DrvGetStandardVariable**](iprintoemdriveruni-drvgetstandardvariable.md) | The `IPrintOemDriverUni::DrvGetStandardVariable` method is provided by the Unidrv driver so that rendering plug-ins can obtain the current value of Unidrv's [standard variables](print.standard_variables).<br/>                                                      |
| [**IPrintOemDriverUni::DrvUniTextOut**](iprintoemdriveruni-drvunitextout.md)                   | The `IPrintOemDriverUni::DrvUniTextOut` method is provided by the Unidrv driver so that a rendering plug-in using a device-managed drawing surface can easily output text strings.<br/>                                                                                |
| [**IPrintOemDriverUni::DrvWriteAbortBuf**](iprintoemdriveruni-drvwriteabortbuf.md)             | The `IPrintOemDriverUni::DrvWriteAbortBuf` method is provided by the Unidrv driver to allow an OEM [rendering plug-in](print.rendering_plug_ins) to send printer clean-up code after a user terminates a print job.<br/>                                               |
| [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md)             | The `IPrintOemDriverUni::DrvWriteSpoolBuf` method is provided by the Unidrv driver so that a [rendering plug-in](print.rendering_plug_ins) can send printer data to the spooler.<br/>                                                                                  |
| [**IPrintOemDriverUni::DrvXMoveTo**](iprintoemdriveruni-drvxmoveto.md)                         | The `IPrintOemDriverUni::DrvXMoveTo` method is provided by the Unidrv driver so that a [rendering plug-in](print.rendering_plug_ins) can notify the driver of cursor x-position changes.<br/>                                                                          |
| [**IPrintOemDriverUni::DrvYMoveTo**](iprintoemdriveruni-drvymoveto.md)                         | The `IPrintOemDriverUni::DrvYMoveTo` method is provided by the Unidrv driver so that a [rendering plug-in](print.rendering_plug_ins) can notify the driver of cursor y-position changes.<br/>                                                                          |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUni%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




