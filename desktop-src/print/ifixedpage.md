---
Description: A filter uses the IFixedPage interface to work with fixed pages in an XPS document.
ms.assetid: e9e309ed-42e5-40cc-a230-6ca001f9fb1b
title: IFixedPage interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IFixedPage interface

A filter uses the **IFixedPage** interface to work with fixed pages in an XPS document.

## Members

The **IFixedPage** interface inherits from [IPartBase](ipartbase.md). **IFixedPage** also has these types of members:

-   [Methods](#methods)

### Methods

The **IFixedPage** interface has these methods.



| Method                                                                  | Description                                                                                                                                        |
|:------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFixedPage::DeleteResource**](ifixedpage-deleteresource.md)         | The **DeleteResource** method deletes a resource that is associated with the page.<br/>                                                      |
| [**IFixedPage::GetPagePart**](ifixedpage-getpagepart.md)               | The **GetPagePart** method gets the images, thumbnails, fonts, and so on in a page by using the URI.<br/>                                    |
| [**IFixedPage::GetPrintTicket**](ifixedpage-getprintticket.md)         | The **GetPrintTicket** method gets the print ticket object for the fixed page.<br/>                                                          |
| [**IFixedPage::GetWriteStream**](ifixedpage-getwritestream.md)         | The **GetWriteStream** method retrieves the stream object to write page markup to read . You can use this stream to change page markup.<br/> |
| [**IFixedPage::GetXpsPartIterator**](ifixedpage-getxpspartiterator.md) | The **GetXpsPartIterator** method gets an iterator to enumerate all of the parts that are associated with the page. <br/>                    |
| [**IFixedPage::SetPagePart**](ifixedpage-setpagepart.md)               | The **SetPagePart** method associates a new part with the page.<br/>                                                                         |
| [**IFixedPage::SetPrintTicket**](ifixedpage-setprintticket.md)         | The **SetPrintTicket** method associates a print ticket with the page.<br/>                                                                  |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



## See also

<dl> <dt>

[IPartBase](ipartbase.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IFixedPage%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





