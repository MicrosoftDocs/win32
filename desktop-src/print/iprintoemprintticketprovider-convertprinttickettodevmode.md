---
Description: The IPrintOemPrintTicketProviderConvertPrintTicketToDevMode method converts a print ticket to a DEVMODEW structure.
ms.assetid: 1243f679-76c3-4d2e-8d57-b9d652b21a05
title: IPrintOemPrintTicketProviderConvertPrintTicketToDevMode method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode method

The `IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode` method converts a print ticket to a [**DEVMODEW**](display.devmodew) structure.

## Syntax


```C++
HRESULT ConvertPrintTicketToDevMode(
  [in]      IXMLDOMDocument2 *pPrintTicket,
  [in]      ULONG            cbDevmode,
  [in, out] PDEVMODE         pDevmode,
  [in]      ULONG            cbDrvPrivateSize,
  [in]      PVOID            pPrivateDevmode
);
```



## Parameters

<dl> <dt>

*pPrintTicket* \[in\]
</dt> <dd>

A pointer to the input print ticket.

</dd> <dt>

*cbDevmode* \[in\]
</dt> <dd>

The size, in bytes, of the input [**DEVMODEW**](display.devmodew) structure. This size includes both the public and private sections of the DEVMODEW structure.

</dd> <dt>

*pDevmode* \[in, out\]
</dt> <dd>

A pointer to the input DEVMODEW structure. When `IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode` returns, the plug-in's private DEVMODEW structure will contain information that was obtained from the print ticket.

</dd> <dt>

*cbDrvPrivateSize* \[in\]
</dt> <dd>

The size, in bytes, of the plug-in's private DEVMODEW structure.

</dd> <dt>

*pPrivateDevmode* \[in\]
</dt> <dd>

A pointer to the plug-in's private [**DEVMODEW**](display.devmodew) structure.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

The core driver calls the `IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode` method before it performs its part of the conversion of a print ticket to a [**DEVMODEW**](display.devmodew) structure. In the call to this method, the core driver passes an input print ticket that is fully populated and a DEVMODEW structure that is set to default values. In the conversion, the plug-in must undo any changes that it made to the print ticket during the previous conversion from a DEVMODEW structure to a print ticket. If, during this previous conversion, the plug-in moved a feature from a private namespace to the public namespace, the plug-in must restore the feature to the private namespace in a format that is suitable for the core driver, that is, the format in which the core driver had previously placed the feature in the print ticket that was provided to the plug-in in the [**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](iprintoemprintticketprovider-convertdevmodetoprintticket.md) method. This restoration is necessary so that the core driver can recognize the feature in the print ticket and reflect its settings in private portion of the core driver's DEVMODEW structure while the core driver performs its part of the print ticket-to-DEVMODEW conversion .

Before the system converts a print ticket back to a [**DEVMODEW**](display.devmodew) structure, it first loads the default DEVMODEW structure. The system then calls the provider's [**IPrintOemPrintTicketProvider::BindPrinter**](iprintoemprintticketprovider-bindprinter.md) method. This method should then read all of the settings that it supported from the print ticket and populate those settings in the DEVMODEW structure. Note that not all of the features necessarily will be represented, and that often Option instances that are present might not contain all of the Scored Property instances that the provider would normally populate. If the provider makes any changes to the settings that are populated by the system during conversion from print ticket to DEVMODEW, the provider should perform the reverse of that change in the `IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode` method. After the provider returns, the system then overwrites any public DEVMODEW settings that are represented in the print ticket but that are not explicitly disabled by the provider.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPrintTicketProvider**](iprintoemprintticketprovider-interface.md)
</dt> <dt>

[**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](iprintoemprintticketprovider-convertdevmodetoprintticket.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





