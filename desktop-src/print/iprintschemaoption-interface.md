---
Description: Exposes a Print Schema Option object.
ms.assetid: B520875A-7882-43D5-A890-0F82654EFD6C
title: IPrintSchemaOption interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintSchemaOption interface

Exposes a Print Schema Option object.

## Members

The **IPrintSchemaOption** interface inherits from [**IPrintSchemaDisplayableElement**](iprintschemadisplayableelement-interface.md). **IPrintSchemaOption** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IPrintSchemaOption** interface has these methods.



| Method                                                          | Description                                                                                                                   |
|:----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**GetPropertyValue**](iprintschemaoption-getpropertyvalue.md) | Gets the XML node for the "value" child element of a "Property" or a "ScoredProperty" element with the given name.<br/> |



 

### Properties

The **IPrintSchemaOption** interface has these properties.



| Property                                                         | Access type          | Description                                                        |
|:-----------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------|
| [**Constrained**](iprintschemaoption-constrained.md)<br/> | Read-only<br/> | Gets the constraint setting type for the schema option.<br/> |
| [**Selected**](iprintschemaoption-selected.md)<br/>       | Read-only<br/> | Indicates whether this option is selected.<br/>              |



 

## Remarks

You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a *name* attribute specified. This attribute is used to build the **IPrintSchemaOption** and [**IPrintSchemaFeature**](iprintschemafeature-interface.md) objects. If the *name* attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintSchemaDisplayableElement**](iprintschemadisplayableelement-interface.md)
</dt> <dt>

[**IPrintSchemaFeature::GetOption**](iprintschemafeature-getoption.md)
</dt> <dt>

[**IPrintSchemaFeature::SelectedOption**](iprintschemafeature-selectedoption.md)
</dt> <dt>

[**IPrintSchemaOptionCollection**](iprintschemaoptioncollection.md)
</dt> <dt>

[**IPrintSchemaPageMediaSizeOption**](iprintschemapagemediasizeoption-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaOption%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





