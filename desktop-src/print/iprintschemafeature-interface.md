---
Description: Exposes a Print Schema Feature element.
ms.assetid: AAC2A60B-9E70-4809-969A-68783A91B093
title: IPrintSchemaFeature interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintSchemaFeature interface

Exposes a Print Schema Feature element.

## Members

The **IPrintSchemaFeature** interface inherits from [**IPrintSchemaDisplayableElement**](iprintschemadisplayableelement-interface.md). **IPrintSchemaFeature** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IPrintSchemaFeature** interface has these methods.



| Method                                             | Description                                     |
|:---------------------------------------------------|:------------------------------------------------|
| [**GetOption**](iprintschemafeature-getoption.md) | Gets the option with the given name.<br/> |



 

### Properties

The **IPrintSchemaFeature** interface has these properties.



| Property                                                                    | Access type           | Description                                                                                                                                                     |
|:----------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DisplayUI**](iprintschemafeature-displayui.md)<br/>               | Read-only<br/>  | Gets the setting that indicates whether or not to show the print UI.<br/>                                                                                 |
| [**SelectedOption**](iprintschemafeature-selectedoption.md)<br/>     | Read-only<br/>  | Gets an [**IPrintSchemaOption**](iprintschemaoption-interface.md) representing the selected option.<br/>                                                 |
| [**SelectedOption**](iprintschemafeature-put-selectedoption.md)<br/> | Write-only<br/> | Changes the selected option of the Print Schema Feature element to the specified [**IPrintSchemaOption**](iprintschemaoption-interface.md) element.<br/> |
| [**SelectionType**](iprintschemafeature-selectiontype.md)<br/>       | Read-only<br/>  | Gets the selection type of the Feature.<br/>                                                                                                              |



 

## Remarks

You must ensure that each Feature or Option in a PrintTicket or PrintCapabilities XML document has a *name* attribute specified. This attribute is used to build the [**IPrintSchemaOption**](iprintschemaoption-interface.md) and **IPrintSchemaFeature** objects. If the *name* attribute is omitted, the feature or option will not be displayed in the object model, or the Microsoft-provided print preferences experience.

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

[**IPrintSchemaCapabilities::GetFeature**](iprintschemacapabilities-getfeature.md)
</dt> <dt>

[**IPrintSchemaTicket::GetFeature**](iprintschematicket-getfeature.md)
</dt> <dt>

[**IPrintSchemaTicket::GetFeatureByKeyName**](iprintschematicket-getfeaturebykeyname.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaFeature%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





