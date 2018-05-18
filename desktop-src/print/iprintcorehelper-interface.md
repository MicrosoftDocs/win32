---
Description: 'This section describes the methods that are defined for the IPrintCoreHelper COM interface.'
ms.assetid: 'db13410f-e4cb-4077-bb4b-7963e97b435c'
title: IPrintCoreHelper interface
---

# IPrintCoreHelper interface

This section describes the methods that are defined for the **IPrintCoreHelper** COM interface.

## Members

The **IPrintCoreHelper** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintCoreHelper** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintCoreHelper** interface has these methods.



| Method                                                                              | Description                                                                                                                                                                       |
|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateInstanceOfMSXMLObject**](iprintcorehelper-createinstanceofmsxmlobject.md) | The **IPrintCoreHelper::CreateInstanceOfMSXMLObject** method creates an instance of an MSXML 6.0 object by using the correct MSXML DLL. <br/>                               |
| [**EnumConstrainedOptions**](iprintcorehelper-enumconstrainedoptions.md)           | The **IPrintCoreHelper::EnumConstrainedOptions** method provides a list of all of the options that are constrained in a particular feature, based on current settings.<br/> |
| [**EnumFeatures**](iprintcorehelper-enumfeatures.md)                               | The **IPrintCoreHelper::EnumFeatures** method gets a list of all available features, including synthesized and core driver-implement features.<br/>                         |
| [**EnumOptions**](iprintcorehelper-enumoptions.md)                                 | The **IPrintCoreHelper::EnumOptions** method gets a list of available options for the given feature. <br/>                                                                  |
| [**GetFontSubstitution**](iprintcorehelper-getfontsubstitution.md)                 | The **IPrintCoreHelper::GetFontSubstitution** method indicates which device font, if any, is used as a substitution font for a specified TrueType font.<br/>                |
| [**GetOption**](iprintcorehelper-getoption.md)                                     | The **IPrintCoreHelper::GetOption** method gets a specified option for a given feature.<br/>                                                                                |
| [**SetFontSubstitution**](iprintcorehelper-setfontsubstitution.md)                 | The **IPrintCoreHelper::SetFontSubstitution** method specifies the device font to print in place of a given TrueType font. <br/>                                            |
| [**SetOptions**](iprintcorehelper-setoptions.md)                                   | The **IPrintCoreHelper::SetOptions** method sets multiple feature-option pairs at the same time.<br/>                                                                       |
| [**WhyConstrained**](iprintcorehelper-whyconstrained.md)                           | The **IPrintCoreHelper::WhyConstrained** method provides a list of options that are constraining the specified feature-option pair in the current configuration.<br/>       |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelper%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




