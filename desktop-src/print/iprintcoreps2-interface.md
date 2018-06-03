---
Description: This section describes the methods defined for the IPrintCorePS2 COM Interface. Method prototypes are defined in prcomoem.h.
ms.assetid: bf7e15df-49ba-4850-acf6-dab5dc137f48
title: IPrintCorePS2 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintCorePS2 interface

This section describes the methods defined for the [IPrintCorePS2 COM Interface](https://www.bing.com/search?q=IPrintCorePS2 COM Interface). Method prototypes are defined in prcomoem.h.

## Members

The **IPrintCorePS2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintCorePS2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintCorePS2** interface has these methods.



| Method                                                           | Description                                                                                                                                                                              |
|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrvWriteSpoolBuf**](iprintcoreps2-drvwritespoolbuf.md)       | The `IPrintCorePS2::DrvWriteSpoolBuf` method is provided by the Pscript5 driver so that a [rendering plug-in](https://www.bing.com/search?q=rendering plug-in) can send printer data to the spooler.<br/> |
| [**EnumFeatures**](iprintcoreps2-enumfeatures.md)               | The `IPrintCorePS2::EnumFeatures` method enumerates a printer's available features.<br/>                                                                                           |
| [**EnumOptions**](iprintcoreps2-enumoptions.md)                 | The `IPrintCorePS2::EnumOptions` method enumerates the available options of a specific feature.<br/>                                                                               |
| [**GetFeatureAttribute**](iprintcoreps2-getfeatureattribute.md) | The `IPrintCorePS2::GetFeatureAttribute` method retrieves the feature attribute list or the value of a specific feature attribute.<br/>                                            |
| [**GetGlobalAttribute**](iprintcoreps2-getglobalattribute.md)   | The `IPrintCorePS2::GetGlobalAttribute` method retrieves the global attribute list or the value of a specific global attribute.<br/>                                               |
| [**GetOptionAttribute**](iprintcoreps2-getoptionattribute.md)   | The `IPrintCorePS2::GetOptionAttribute` method retrieves the option attribute list or the value of a specific option attribute.<br/>                                               |
| [**GetOptions**](iprintcoreps2-getoptions.md)                   | The `IPrintCorePS2::GetOptions` method retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.<br/>                               |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCorePS2%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




