---
Description: The IPartBase interface is a common base for document part interfaces.
ms.assetid: 7523990f-04de-4182-99d9-fba100bebb84
title: IPartBase interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPartBase interface

The **IPartBase** interface is a common base for document part interfaces.

## Members

The **IPartBase** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPartBase** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPartBase** interface has these methods.



| Method                                                                | Description                                                                                                                                                                                        |
|:----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPartBase::GetPartCompression**](ipartbase-getpartcompression.md) | The **GetPartCompression** method gets the compression of the part.<br/>                                                                                                                     |
| [**IPartBase::GetStream**](ipartbase-getstream.md)                   | The **GetStream** method gets the stream object that contains the part data. Each part has part-specific data that is associated with it (for example, a font, image, and page markup).<br/> |
| [**IPartBase::GetUri**](ipartbase-geturi.md)                         | The **GetUri** method gets the URI of the part.<br/>                                                                                                                                         |
| [**IPartBase::SetPartCompression**](ipartbase-setpartcompression.md) | The **SetPartCompression** method sets the compression of the part.<br/>                                                                                                                     |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPartBase%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




