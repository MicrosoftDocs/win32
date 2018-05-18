---
Description: 'The IPrintOemPrintTicketProvider::CompletePrintCapabilities method fills in the remaining entries of the specified print capabilities document.'
ms.assetid: '067eca3b-f487-405a-9799-bd62376f9e24'
title: 'IPrintOemPrintTicketProvider::CompletePrintCapabilities method'
---

# IPrintOemPrintTicketProvider::CompletePrintCapabilities method

The `IPrintOemPrintTicketProvider::CompletePrintCapabilities` method fills in the remaining entries of the specified print capabilities document.

## Syntax


```C++
HRESULT CompletePrintCapabilities(
  [in]      IXMLDOMDocument2 *pPrintTicket,
  [in, out] IXMLDOMDocument2 *pCapabilities
);
```



## Parameters

<dl> <dt>

*pPrintTicket* \[in\]
</dt> <dd>

A pointer to an input print ticket. Any configuration-dependent data in the print capabilities (that is, data that would be represented by a \***Switch** / \***Case** construct in a GPD file) must be based on the settings in the print ticket. If the application does not provide a print ticket, this parameter can be **NULL**. In such situations, the provider should assume default settings for feature and parameter constructs.

</dd> <dt>

*pCapabilities* \[in, out\]
</dt> <dd>

A pointer to a partially-complete print capabilities document. When `IPrintOemPrintTicketProvider::CompletePrintCapabilities` returns, the buffer that is pointed to by *pCapablities* should contain a completed print capabilities document.

</dd> </dl>

## Return value

`IPrintOemPrintTicketProvider::CompletePrintCapabilities` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

A Unidrv or Pscript5 plug-in should fill in only those capabilities that it explicitly supports, over and above the features and options that the driver supports. The plug-in should at least fill in the capabilities that it supports, as listed in its private DEVMODEW structure. If the plug-in provider changes the representation of features provided by the core driver in the print ticket, the provider must make equivalent changes to the representation here.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider::CompletePrintCapabilities%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




