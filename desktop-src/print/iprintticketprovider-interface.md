---
Description: This section describes the methods that are defined for the IPrintOemPrintTicketProvider COM interface.
ms.assetid: 4eb3c193-377b-4e51-a97b-50c6fdaa1b08
title: IPrintTicketProvider interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintTicketProvider interface

This section describes the methods that are defined for the [**IPrintOemPrintTicketProvider**](iprintoemprintticketprovider-interface.md) COM interface.

## Members

The **IPrintTicketProvider** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintTicketProvider** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintTicketProvider** interface has these methods.



| Method                                                                                  | Description                                                                                                                                                                                                                                                         |
|:----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BindPrinter**](iprintticketprovider-bindprinter.md)                                 | The `IPrintTicketProvider::BindPrinter` method binds a printer or print queue to a specific version of the print ticket schema, which enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device.<br/> |
| [**ConvertDevModeToPrintTicket**](iprintticketprovider-convertdevmodetoprintticket.md) | The `IPrintTicketProvider::ConvertDevModeToPrintTicket` method converts a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure into a print ticket. <br/>                                                                                                               |
| [**ConvertPrintTicketToDevMode**](iprintticketprovider-convertprinttickettodevmode.md) | The `IPrintTicketProvider::ConvertPrintTicketToDevMode` method converts a print ticket to a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure. <br/>                                                                                                                 |
| [**GetPrintCapabilities**](iprintticketprovider-getprintcapabilities.md)               | The `IPrintTicketProvider::GetPrintCapabilities` method queries the provider for a complete print capabilities document that describes the printer's features and parameters.<br/>                                                                            |
| [**GetSupportedVersions**](iprintticketprovider-getsupportedversions.md)               | The `IPrintTicketProvider::GetSupportedVersions` method retrieves major version numbers of the print schemas that are supported by the plug-in provider.<br/>                                                                                                 |
| [**QueryDeviceNamespace**](iprintticketprovider-querydevicenamespace.md)               | The `IPrintTicketProvider::QueryDeviceNamespace` method queries the device for its default namespace uniform resource identifier (URI).<br/>                                                                                                                  |
| [**ValidatePrintTicket**](iprintticketprovider-validateprintticket.md)                 | The `IPrintTicketProvider::ValidatePrintTicket` method validates a print ticket.<br/>                                                                                                                                                                         |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintTicketProvider%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




