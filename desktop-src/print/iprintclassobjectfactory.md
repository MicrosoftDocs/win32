---
Description: TheIPrintClassObjectFactory interface creates print filter-related interfaces.
ms.assetid: 09691b81-6488-4972-8cbc-7873e6717287
title: IPrintClassObjectFactory interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintClassObjectFactory interface

The**IPrintClassObjectFactory** interface creates print filter-related interfaces.

## Members

The **IPrintClassObjectFactory** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintClassObjectFactory** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintClassObjectFactory** interface has these methods.



| Method                                                                                                | Description                                                                                                                                                     |
|:------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPrintClassObjectFactory::GetPrintClassObject**](iprintclassobjectfactory-getprintclassobject.md) | The **GetPrintClassObject** method creates a print filter-related object for a specified printer by using the IID of the interface object to create.<br/> |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintClassObjectFactory%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




