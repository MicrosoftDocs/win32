---
Description: The IPrintTicketProvider::ConvertDevModeToPrintTicket method converts a DEVMODEW structure into a print ticket.
ms.assetid: 853258c4-24fe-4ca4-92bc-bc84366476ac
title: IPrintTicketProvider::ConvertDevModeToPrintTicket method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintTicketProvider::ConvertDevModeToPrintTicket method

The `IPrintTicketProvider::ConvertDevModeToPrintTicket` method converts a [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure into a print ticket.

## Syntax


```C++
HRESULT ConvertDevModeToPrintTicket(
  [in] ULONG            cbDevmode,
  [in] PDEVMODE         pDevmode,
  [in] IXMLDOMDocument2 *pPrintTicket
);
```



## Parameters

<dl> <dt>

*cbDevmode* \[in\]
</dt> <dd>

The size, in bytes, of the input [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure. The size includes both the public and private portions of this structure.

</dd> <dt>

*pDevmode* \[in\]
</dt> <dd>

A pointer to the input DEVMODEW structure, including its public and private portions.

</dd> <dt>

*pPrintTicket* \[in\]
</dt> <dd>

A pointer to the partially-completed print ticket. When `IPrintTicketProvider::ConvertDevModeToPrintTicket` returns, all entries in the print ticket should be filled in.

</dd> </dl>

## Return value

`IPrintTicketProvider::ConvertDevModeToPrintTicket` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

When the print system converts the contents of a [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure into a print ticket, it converts all of the public DEVMODEW fields except those that the plug-in provider has indicated should be disabled. For these DEVMODEW fields that are disabled and not converted, the plug-in provider is responsible for populating the corresponding print ticket values. If the DEVMODEW snapshot was disabled during a call to [**IPrintTicketProvider::BindPrinter**](iprintticketprovider-bindprinter.md), the representation from the conversion must provide enough information to reconstruct the original DEVMODEW structure from the print ticket without loss of information.

The DEVMODEW snapshot allows support for subtle distinctions in options provided in the DEVMODEW structure for which the print ticket might not have representations. For example, DEVMODEW might support the LETTER paper size while the print ticket supports the LETTERSMALL paper size.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintTicketProvider**](iprintticketprovider-interface.md)
</dt> <dt>

[**IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode**](iprintoemprintticketprovider-convertprinttickettodevmode.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintTicketProvider::ConvertDevModeToPrintTicket%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





