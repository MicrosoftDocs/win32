---
Description: This section describes the methods that are defined for the IPrintCoreHelperUni COM interface.
ms.assetid: e581d190-8185-45c1-80c7-ff8eb305360e
title: IPrintCoreHelperUni interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintCoreHelperUni interface

This section describes the methods that are defined for the `IPrintCoreHelperUni` COM interface.

## Members

The **IPrintCoreHelperUni** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintCoreHelperUni** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintCoreHelperUni** interface has these methods.



| Method                                                                                 | Description                                                                                                                                                                        |
|:---------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDefaultGDLSnapshot**](iprintcorehelperuni-createdefaultgdlsnapshot.md)       | The `IPrintCoreHelperUni::CreateDefaultGDLSnapshot` method gets a GDL snapshot based on the driver default configuration.<br/>                                               |
| [**CreateGDLSnapshot**](iprintcorehelperuni-creategdlsnapshot.md)                     | The `IPrintCoreHelperUni::CreateGDLSnapshot` method creates a GDL snapshot of the driver configuration file based on the current configuration. <br/>                        |
| [**CreateInstanceOfMSXMLObject**](iprintcorehelperuni-createinstanceofmsxmlobject.md) | The `IPrintCoreHelperUni::CreateInstanceOfMSXMLObject` method creates an instance of an MSXML object. <br/>                                                                  |
| [**EnumConstrainedOptions**](iprintcorehelperuni-enumconstrainedoptions.md)           | The `IPrintCoreHelperUni::EnumConstrainedOptions` method provides a list of all of the options that are constrained in a particular feature, based on current settings.<br/> |
| [**EnumFeatures**](iprintcorehelperuni-enumfeatures.md)                               | The `IPrintCoreHelperUni::EnumFeatures` method gets a list of all available features, including synthesized and core driver-implement features.<br/>                         |
| [**EnumOptions**](iprintcorehelperuni-enumoptions.md)                                 | The `IPrintCoreHelperUni::EnumOptions` method gets a list of available options for the given feature. <br/>                                                                  |
| [**GetFontSubstitution**](iprintcorehelperuni-getfontsubstitution.md)                 | The `IPrintCoreHelperUni::GetFontSubstitution` method indicates which device font, if any, is used as a substitution font for a specified TrueType font.<br/>                |
| [**GetOption**](iprintcorehelperuni-getoption.md)                                     | The `IPrintCoreHelperUni::GetOption` method gets a specified option for a given feature.<br/>                                                                                |
| [**SetFontSubstitution**](iprintcorehelperuni-setfontsubstitution.md)                 | The `IPrintCoreHelperUni::SetFontSubstitution` method specifies the device font to print in place of a given TrueType font. <br/>                                            |
| [**SetOptions**](iprintcorehelperuni-setoptions.md)                                   | The `IPrintCoreHelperUni::SetOptions` method sets multiple feature-option pairs at the same time.<br/>                                                                       |
| [**WhyConstrained**](iprintcorehelperuni-whyconstrained.md)                           | The `IPrintCoreHelperUni::WhyConstrained` method provides a list of options that constrain the specified feature-option pair in the current configuration. <br/>             |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperUni%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




