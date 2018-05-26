---
Description: The IPrintOemPrintTicketProviderValidatePrintTicket method validates a print ticket.
ms.assetid: 359f1a4b-8bcc-4c4a-97d7-6515993765e3
title: IPrintOemPrintTicketProviderValidatePrintTicket method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemPrintTicketProvider::ValidatePrintTicket method

The `IPrintOemPrintTicketProvider::ValidatePrintTicket` method validates a print ticket.

## Syntax


```C++
HRESULT ValidatePrintTicket(
  [in, out] IXMLDOMDocument2 *pPrintTicket
);
```



## Parameters

<dl> <dt>

*pPrintTicket* \[in, out\]
</dt> <dd>

A pointer to an input print ticket. When `IPrintOemPrintTicketProvider::ValidatePrintTicket` successfully returns, *pPrintTicket* points to a validated print ticket.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::ValidatePrintTicket` should return S\_NO\_CONFLICT or S\_CONFLICT\_RESOLVED if the operation succeeds. Otherwise, this method should return a standard COM error code. Note that Unidrv and Pscript do not consider S\_OK to mean successful completion for this method.

## Remarks

If necessary, the `IPrintOemPrintTicketProvider::ValidatePrintTicket` method should perform any conflict resolution, by inspecting the settings made in the public and Unidrv-private parts of the print ticket, to ensure that the resulting print ticket is valid, and that all of the constraints are resolved. If any required nodes are not present in the original print ticket, `IPrintOemPrintTicketProvider::ValidatePrintTicket` can add them to the returned print ticket.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPrintTicketProvider**](iprintoemprintticketprovider-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::ValidatePrintTicket%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





