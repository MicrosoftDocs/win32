---
Description: This section describes the methods that are defined for the IPrintOemUIMXDC COM interface.
ms.assetid: 4a70c0a7-9de7-48ed-a678-64832f078018
title: IPrintOemUIMXDC interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintOemUIMXDC interface

This section describes the methods that are defined for the IPrintOemUIMXDC COM interface.

## Members

The **IPrintOemUIMXDC** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintOemUIMXDC** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemUIMXDC** interface has these methods.



| Method                                                                   | Description                                                                                                                                                                                                                          |
|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdjustDPI**](iprintoemuimxdc-adjustdpi.md)                           | The `IPrintOemUIMXDC::AdjustDPI` method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of image resolution.<br/>                                                              |
| [**AdjustImageableArea**](iprintoemuimxdc-adjustimageablearea.md)       | The `IPrintOemUIMXDC::AdjustImageableArea` method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of the printable area, including orientation and direction of rotation.<br/> |
| [**AdjustImageCompression**](iprintoemuimxdc-adjustimagecompression.md) | The `IPrintOemUIMXDC::AdjustImageCompression` method allows an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of compression level for JPEG or PNG images.<br/>                          |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUIMXDC%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




