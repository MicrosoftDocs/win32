---
Description: The GetPrintTicket method gets the print ticket object for the fixed page.
ms.assetid: 4a30efd9-8fef-4fef-8293-b7df5b954977
title: IFixedPage::GetPrintTicket method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IFixedPage::GetPrintTicket method

The **GetPrintTicket** method gets the print ticket object for the fixed page.

## Syntax


```C++
HRESULT GetPrintTicket(
  [out] IPartPrintTicket **ppPrintTicket
);
```



## Parameters

<dl> <dt>

*ppPrintTicket* \[out\]
</dt> <dd>

Pointer to a location into which the method writes a pointer to the [IPartPrintTicket](ipartprintticket.md) interface of a print ticket object. This object contains the print ticket for the fixed page.

</dd> </dl>

## Return value

**GetPrintTicket** returns an **HRESULT** value. If a print ticket is not in the fixed page, **GetPrintTicket** might return E\_ELEMENT\_NOT\_FOUND.

## Remarks

After calling this method to get the page-level print ticket, a print driver filter can obtain the *effective* print ticket for the fixed page by merging the page-level print ticket with the document-level print ticket and the job-level print ticket. The filter can get the document-level and job-level print tickets by calling the [**IFixedDocument::GetPrintTicket**](ifixeddocument-getprintticket.md) and [**IFixedDocumentSequence::GetPrintTicket**](ifixeddocumentsequence-getprintticket.md) methods. For more information about merging print tickets, see [Print Ticket Merging](https://www.bing.com/search?q=Print+Ticket+Merging).

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



## See also

<dl> <dt>

[**IFixedPage**](ifixedpage.md)
</dt> <dt>

[**IFixedDocument::GetPrintTicket**](ifixeddocument-getprintticket.md)
</dt> <dt>

[**IFixedDocumentSequence::GetPrintTicket**](ifixeddocumentsequence-getprintticket.md)
</dt> <dt>

[IPartPrintTicket](ipartprintticket.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IFixedPage::GetPrintTicket%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





