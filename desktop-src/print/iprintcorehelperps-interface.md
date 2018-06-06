---
Description: This section describes the methods that are defined for the IPrintCoreHelperPS COM interface.
ms.assetid: 2be594f1-1eb1-42e0-a345-ee7edf4d96dd
title: IPrintCoreHelperPS interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintCoreHelperPS interface

This section describes the methods that are defined for the **IPrintCoreHelperPS** COM interface.

## Members

The **IPrintCoreHelperPS** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintCoreHelperPS** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintCoreHelperPS** interface has these methods.



| Method                                                                                | Description                                                                                                                                                                         |
|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateInstanceOfMSXMLObject**](iprintcorehelperps-createinstanceofmsxmlobject.md) | The **IPrintCoreHelperPS::CreateInstanceOfMSXMLObject** method creates an instance of an MSXML object. <br/>                                                                  |
| [**EnumConstrainedOptions**](iprintcorehelperps-enumconstrainedoptions.md)           | The **IPrintCoreHelperPS::EnumConstrainedOptions** method provides a list of all of the options that are constrained in a particular feature, based on current settings.<br/> |
| [**EnumFeatures**](iprintcorehelperps-enumfeatures.md)                               | The **IPrintCoreHelperPS::EnumFeatures** method gets a list of all available features, including synthesized and core driver-implement features.<br/>                         |
| [**EnumOptions**](iprintcorehelperps-enumoptions.md)                                 | The **IPrintCoreHelperPS::EnumOptions** method gets a list of available options for the given feature. <br/>                                                                  |
| [**GetFeatureAttribute**](iprintcorehelperps-getfeatureattribute.md)                 | The **IPrintCoreHelperPS::GetFeatureAttribute** method retrieves the feature attribute list or the value of a specific feature attribute.<br/>                                |
| [**GetFontSubstitution**](iprintcorehelperps-getfontsubstitution.md)                 | The **IPrintCoreHelperPS::GetFontSubstitution** method indicates which device font, if any, is used as a substitution font for a specified TrueType font.<br/>                |
| [**GetGlobalAttribute**](iprintcorehelperps-getglobalattribute.md)                   | The **IPrintCoreHelperPS::GetGlobalAttribute** method retrieves the global attribute list or the value of a specific global attribute.<br/>                                   |
| [**GetOption**](iprintcorehelperps-getoption.md)                                     | The **IPrintCoreHelperPS::GetOption** method gets a specified option for a given feature.<br/>                                                                                |
| [**GetOptionAttribute**](iprintcorehelperps-getoptionattribute.md)                   | The **IPrintCoreHelperPS::GetOptionAttribute** method retrieves the option attribute list or the value of a specific option attribute.<br/>                                   |
| [**SetFontSubstitution**](iprintcorehelperps-setfontsubstitution.md)                 | The **IPrintCoreHelperPS::SetFontSubstitution** method specifies the device font to print in place of a given TrueType font. <br/>                                            |
| [**SetOptions**](iprintcorehelperps-setoptions.md)                                   | The **IPrintCoreHelperPS::SetOptions** method sets multiple feature-option pairs at the same time.<br/>                                                                       |
| [**WhyConstrained**](iprintcorehelperps-whyconstrained.md)                           | The **IPrintCoreHelperPS::WhyConstrained** method provides a list of options that constrain the specified feature-option pair in the current configuration.<br/>              |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperPS%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




