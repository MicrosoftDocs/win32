---
Description: This section describes the methods defined for the IPrintOemUI2 COM interface.
ms.assetid: 9b7afb56-7abb-4f20-b69d-12a28d7e3617
title: IPrintOemUI2 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintOemUI2 interface

This section describes the methods defined for the **IPrintOemUI2** COM interface.

## Members

The **IPrintOemUI2** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintOemUI2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemUI2** interface has these methods.



| Method                                                        | Description                                                                                                                                                                                                                                                                                                                                                                    |
|:--------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DocumentEvent**](iprintoemui2-documentevent.md)           | The `IPrintOemUI2::DocumentEvent` method allows a UI plug-in to replace the core driver UI module's default implementation of the [**DrvDocumentEvent**](drvdocumentevent.md) DDI.<br/>                                                                                                                                                                                 |
| [**HideStandardUI**](iprintoemui2-hidestandardui.md)         | The `IPrintOemUI2::HideStandardUI` method allows a user interface plug-in to specify whether the standard property sheets should be displayed or hidden. Beginning with Microsoft Windows XP, this method can be implemented by a Pscript5 user interface plug-in. Beginning with Windows Vista, this method can be implemented by a Unidrv user interface plug-in.<br/> |
| [**QueryJobAttributes**](iprintoemui2-queryjobattributes.md) | The `IPrintOemUI2::QueryJobAttributes` method allows a UI plug-in to postprocess the core driver's results after a call to the [**DrvQueryJobAttributes**](drvqueryjobattributes.md) DDI. The plug-in can choose to overwrite the values that the core driver placed in the *lpAttributeInfo* output buffer.<br/>                                                       |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI2%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




