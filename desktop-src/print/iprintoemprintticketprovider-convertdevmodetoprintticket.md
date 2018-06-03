---
Description: The IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method converts a DEVMODEW structure into a print ticket.
ms.assetid: b2e029b7-32c0-4cef-8388-9d30aa5610d3
title: IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method

The `IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket` method converts a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure into a print ticket.

## Syntax


```C++
HRESULT ConvertDevModeToPrintTicket(
  [in]      ULONG            cbDevmode,
  [in]      PDEVMODE         pDevmode,
  [in]      ULONG            cbDrvPrivateSize,
  [in]      PVOID            pPrivateDevmode,
  [in, out] IXMLDOMDocument2 *pPrintTicket
);
```



## Parameters

<dl> <dt>

*cbDevmode* \[in\]
</dt> <dd>

The size, in bytes, of the input [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure. The size includes both the public and private portions of this structure.

</dd> <dt>

*pDevmode* \[in\]
</dt> <dd>

A pointer to the input DEVMODEW structure.

</dd> <dt>

*cbDrvPrivateSize* \[in\]
</dt> <dd>

The size, in bytes, of the plug-in's private DEVMODEW structure.

</dd> <dt>

*pPrivateDevmode* \[in\]
</dt> <dd>

A pointer to the plug-in's private [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure.

</dd> <dt>

*pPrintTicket* \[in, out\]
</dt> <dd>

A pointer to the partially-completed print ticket. When `IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket` returns, all of the entries in the print ticket should be filled in.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

The core driver calls the `IPrintTicketProvider::ConvertDevModeToPrintTicket` method with an input print ticket that is populated with public and Unidrv-private or Pscript5-private features. The plug-in is free to set [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) settings in the public part or in the plug-in's private part, based on settings in the input print ticket. In addition to setting new DEVMODEW items, the plug-in can modify existing settings in the public portion of the DEVMODEW structure.

The DEVMODEW structure fields that correlate with the part of the DEVMODEW structure of interest to the client will already have been populated before `IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket` is called, including the public portion of the DEVMODEW structure and excluding the privately-defined values in the public portion of the DEVMODEW structure.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPrintTicketProvider**](iprintoemprintticketprovider-interface.md)
</dt> <dt>

[**IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode**](iprintoemprintticketprovider-convertprinttickettodevmode.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





