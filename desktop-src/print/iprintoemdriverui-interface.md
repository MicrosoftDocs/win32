---
Description: 'This section describes the methods defined for the IPrintOemDriverUI COM Interface.'
ms.assetid: '2a885dd5-d328-4aae-8771-613ff93b35ac'
title: IPrintOemDriverUI interface
---

# IPrintOemDriverUI interface

This section describes the methods defined for the IPrintOemDriverUI COM Interface.

## Members

The **IPrintOemDriverUI** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintOemDriverUI** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemDriverUI** interface has these methods.



| Method                                                                                              | Description                                                                                                                                                                                                                         |
|:----------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPrintOemDriverUI::DrvGetDriverSetting**](iprintoemdriverui-drvgetdriversetting.md)             | The `IPrintOemDriverUI::DrvGetDriverSetting` method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can obtain the current status of printer features and other internal information.<br/> |
| [**IPrintOemDriverUI::DrvUpdateUISetting**](iprintoemdriverui-drvupdateuisetting.md)               | The `IPrintOemDriverUI::DrvUpdateUISetting` method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can notify the driver of a modified user interface option.<br/>                         |
| [**IPrintOemDriverUI::DrvUpgradeRegistrySetting**](iprintoemdriverui-drvupgraderegistrysetting.md) | The `IPrintOemDriverUI::DrvUpdateRegistrySetting` method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can update device settings stored in the registry.<br/>                           |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUI%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




