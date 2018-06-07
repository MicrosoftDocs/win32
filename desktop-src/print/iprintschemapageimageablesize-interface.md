---
Description: Exposes the PageImageableSize property of PrintCapabilities. The properties of this interface map directly to those in the PageImageableSize property of PrintCapabilities.
ms.assetid: C8E9278D-D24A-4EEC-8F68-D77C76ECCC40
title: IPrintSchemaPageImageableSize interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintSchemaPageImageableSize interface

Exposes the PageImageableSize property of PrintCapabilities. The properties of this interface map directly to those in the PageImageableSize property of PrintCapabilities.

## Members

The **IPrintSchemaPageImageableSize** interface inherits from [**IPrintSchemaElement**](iprintschemaelement-interface.md). **IPrintSchemaPageImageableSize** also has these types of members:

-   [Properties](#properties)

### Properties

The **IPrintSchemaPageImageableSize** interface has these properties.



| Property                                                                                                      | Access type          | Description                                                                                                           |
|:--------------------------------------------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**ExtentHeightInMicrons**](iprintschemapageimageablesize-extentheightinmicrons.md)<br/>               | Read-only<br/> | Gets the vertical distance between the origin and the bounding limit of the canvas application media size.<br/> |
| [**ExtentWidthInMicrons**](iprintschemapageimageablesize-extentwidthinmicrons.md)<br/>                 | Read-only<br/> | Gets the horizontal distance between the origin and the bounding limit of the application media size.<br/>      |
| [**ImageableSizeHeightInMicrons**](iprintschemapageimageablesize-imageablesizeheightinmicrons.md)<br/> | Read-only<br/> | Gets the vertical dimension of the application media size relative to the page orientation.<br/>                |
| [**ImageableSizeWidthInMicrons**](iprintschemapageimageablesize-imageablesizewidthinmicrons.md)<br/>   | Read-only<br/> | Gets the horizontal dimension of the application media size relative to the page orientation.<br/>              |
| [**OriginHeightInMicrons**](iprintschemapageimageablesize-originheightinmicrons.md)<br/>               | Read-only<br/> | Gets the vertical origin of the imageable area relative to the application media size.<br/>                     |
| [**OriginWidthInMicrons**](iprintschemapageimageablesize-originwidthinmicrons.md)<br/>                 | Read-only<br/> | Gets the horizontal origin of the imageable area relative to the application media size.<br/>                   |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintSchemaPageImageableSize%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




