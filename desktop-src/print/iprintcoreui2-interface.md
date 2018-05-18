---
Description: 'This section describes the methods defined for the IPrintCoreUI2 COM Interface.'
ms.assetid: 'e2d2e486-d69d-4a6d-aaab-a7b8806665b4'
title: IPrintCoreUI2 interface
---

# IPrintCoreUI2 interface

This section describes the methods defined for the [IPrintCoreUI2 COM Interface](print.iprintcoreui2_com_interface).

This interface inherits from the [IPrintOemDriverUI COM Interface](print.iprintoemdriverui_com_interface). The methods in this interface are provided by the Windows XP Pscript5 driver, for the sole use of its user interface plug-ins. Method prototypes appear in prcomoem.h.

## Members

The **IPrintCoreUI2** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintCoreUI2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintCoreUI2** interface has these methods.



| Method                                                                       | Description                                                                                                                                                                                                                         |
|:-----------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DrvGetDriverSetting**](iprintcoreui2-drvgetdriversetting.md)             | The `IPrintCoreUI2::DrvGetDriverSetting` method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can obtain the current status of printer features and other internal information.<br/> |
| [**DrvUpdateUISetting**](iprintcoreui2-drvupdateuisetting.md)               | The `IPrintCoreUI2::DrvUpdateUISetting` method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can notify the driver of a modified user interface option.<br/>                         |
| [**DrvUpgradeRegistrySetting**](iprintcoreui2-drvupgraderegistrysetting.md) | The `IPrintCoreUI2::DrvUpgradeRegistrySetting` method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can update device settings stored in the registry.<br/>                          |
| [**EnumConstrainedOptions**](iprintcoreui2-enumconstrainedoptions.md)       | The `IPrintCoreUI2::EnumConstrainedOptions` method determines which options of a feature are constrained.<br/>                                                                                                                |
| [**EnumFeatures**](iprintcoreui2-enumfeatures.md)                           | The `IPrintCoreUI2::EnumFeatures` method enumerates a printer's available features.<br/>                                                                                                                                      |
| [**EnumOptions**](iprintcoreui2-enumoptions.md)                             | The `IPrintCoreUI2::EnumOptions` method enumerates the available options of a specific feature.<br/>                                                                                                                          |
| [**GetFeatureAttribute**](iprintcoreui2-getfeatureattribute.md)             | The `IPrintCoreUI2::GetFeatureAttribute` method retrieves the feature attribute list or the value of a specific feature attribute.<br/>                                                                                       |
| [**GetGlobalAttribute**](iprintcoreui2-getglobalattribute.md)               | The `IPrintCoreUI2::GetGlobalAttribute` method retrieves the global attribute list or the value of a specific global attribute.<br/>                                                                                          |
| [**GetOptionAttribute**](iprintcoreui2-getoptionattribute.md)               | The `IPrintCoreUI2::GetOptionAttribute` method retrieves the option attribute list or the value of a specific option attribute.<br/>                                                                                          |
| [**GetOptions**](iprintcoreui2-getoptions.md)                               | The `IPrintCoreUI2::GetOptions` method retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.<br/>                                                                          |
| [**QuerySimulationSupport**](iprintcoreui2-querysimulationsupport.md)       | The `IPrintCoreUI2::QuerySimulationSupport` method retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports.<br/>                                                    |
| [**SetOptions**](iprintcoreui2-setoptions.md)                               | The `IPrintCoreUI2::SetOptions` method sets the driver's feature settings.<br/>                                                                                                                                               |
| [**WhyConstrained**](iprintcoreui2-whyconstrained.md)                       | The `IPrintCoreUI2::WhyConstrained` method determines why the specified feature/option selection is constrained.<br/>                                                                                                         |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




