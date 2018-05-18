---
Description: 'The IPrintTicketProvider::ConvertPrintTicketToDevMode method converts a print ticket to a DEVMODEW structure.'
ms.assetid: '59457b51-5ab5-4e20-a608-a71c799eeeb9'
title: 'IPrintTicketProvider::ConvertPrintTicketToDevMode method'
---

# IPrintTicketProvider::ConvertPrintTicketToDevMode method

The `IPrintTicketProvider::ConvertPrintTicketToDevMode` method converts a print ticket to a [**DEVMODEW**](display.devmodew) structure.

## Syntax


```C++
HRESULT ConvertPrintTicketToDevMode(
  [in]  IXMLDOMDocument2 *pPrintTicket,
  [in]  ULONG            cbDevmodeIn,
  [in]  PDEVMODE         pDevmodeIn,
  [out] ULONG            *pcbDevmodeOut,
  [out] PDEVMODE         *ppDevmodeOut
);
```



## Parameters

<dl> <dt>

*pPrintTicket* \[in\]
</dt> <dd>

A pointer to the input print ticket. `IPrintTicketProvider::ConvertPrintTicketToDevMode` converts the settings in the input print ticket into fields in the [**DEVMODEW**](display.devmodew) structure.

</dd> <dt>

*cbDevmodeIn* \[in\]
</dt> <dd>

The size, in bytes, of the input DEVMODEW structure. This size includes both the public and private sections of the DEVMODEW structure.

</dd> <dt>

*pDevmodeIn* \[in\]
</dt> <dd>

A pointer to the input DEVMODEW structure, which contains default settings. The DEVMODEW structure can be the print queue default DEVMODEW structure, or it can be the user default DEVMODEW structure. Because this parameter can represent the user default DEVMODEW structure, the OEM plug-in provider must validate the data in that structure. A user default DEVMODEW structure might not be valid for a specific driver, for example, when the print queue's driver changes or is upgraded.

</dd> <dt>

*pcbDevmodeOut* \[out\]
</dt> <dd>

A pointer to a variable that contains the size, in bytes, of the output [**DEVMODEW**](display.devmodew) structure.

</dd> <dt>

*ppDevmodeOut* \[out\]
</dt> <dd>

A pointer to a variable that contains the address of the output DEVMODEW structure. When `IPrintTicketProvider::ConvertPrintTicketToDevMode` successfully returns, the members of the output DEVMODEW structure will be reset to reflect the settings in the print ticket. For more information, see the following Remarks section.

</dd> </dl>

## Return value

`IPrintTicketProvider::ConvertPrintTicketToDevMode` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

The core driver calls the `IPrintTicketProvider::ConvertPrintTicketToDevMode` method before it performs its part of the conversion of a print ticket to a [**DEVMODEW**](display.devmodew) structure. In the call to this method, the core driver passes an input print ticket that is fully populated and a DEVMODEW structure that is set to default values. In the conversion, the plug-in must undo any changes that it made to the print ticket during the previous conversion from a DEVMODEW structure to a print ticket. If, during this previous conversion, the plug-in moved a feature from a private namespace to the public namespace, the plug-in must restore the feature to the private namespace in a format that is suitable for the core driver, that is, to the format in which the core driver had previously placed the feature in the print ticket that was provided to the plug-in in the [**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](iprintoemprintticketprovider-convertdevmodetoprintticket.md) method. This restoration is necessary so that the core driver can recognize a feature in the print ticket and reflect its settings in the private portion of the core driver's DEVMODEW structure while the core driver performs its part of the print ticket-to-DEVMODEW conversion.

Before the system converts a print ticket back to a [**DEVMODEW**](display.devmodew) structure, it first loads the default DEVMODEW. The system then calls the provider's [**IPrintTicketProvider::BindPrinter**](iprintticketprovider-bindprinter.md) method. This method should then read all of the settings that it supported from the print ticket, and place those settings into the DEVMODEW structure. Note that not all of the features necessarily will be represented, and that often Option instances that are present might not contain all of the Scored Property instances that the provider would normally populate. If the provider makes any changes to the settings that were populated by the system during conversion from print ticket to DEVMODEW, the provider should perform the reverse of that change in this method. After the provider returns, the system then overwrites any public DEVMODEW settings that are represented in the print ticket but that are not explicitly disabled by the provider.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prdrvcom.h (include Prdrvcom.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintTicketProvider**](iprintticketprovider-interface.md)
</dt> <dt>

[**IPrintTicketProvider::ConvertDevModeToPrintTicket**](iprintticketprovider-convertdevmodetoprintticket.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintTicketProvider::ConvertPrintTicketToDevMode%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





