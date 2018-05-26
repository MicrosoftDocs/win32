---
Description: This section describes the methods that are defined for the IPrintOemPrintTicketProvider COM interface.
ms.assetid: a32b5ec9-b4f2-4f33-879d-252806bd34ed
title: IPrintOemPrintTicketProvider interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemPrintTicketProvider interface

This section describes the methods that are defined for the **IPrintOemPrintTicketProvider** COM interface.

## Members

The **IPrintOemPrintTicketProvider** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintOemPrintTicketProvider** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemPrintTicketProvider** interface has these methods.



| Method                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetSupportedVersions**](iprintoemprintticketprovider-getsupportedversions.md)                                                         | The `IPrintOemPrintTicketProvider::GetSupportedVersions` method retrieves major versions of the print schemas that are supported by the plug-in provider.<br/>                                                                                                                                         |
| [**IPrintOemPrintTicketProvider::BindPrinter**](iprintoemprintticketprovider-bindprinter.md)                                             | The `IPrintOemPrintTicketProvider::BindPrinter` method enables the core driver to associate a set of private namespace uniform resource identifiers (URIs) with a device. This method also allows the plug-in to cache information (such as the printer handle) that can be used at a later time.<br/> |
| [**IPrintOemPrintTicketProvider::CompletePrintCapabilities**](iprintoemprintticketprovider-completeprintcapabilities.md)                 | The `IPrintOemPrintTicketProvider::CompletePrintCapabilities` method fills in the remaining entries of the specified print capabilities document. <br/>                                                                                                                                                |
| [**IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket**](iprintoemprintticketprovider-convertdevmodetoprintticket.md)             | The `IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket` method converts a [**DEVMODEW**](display.devmodew) structure into a print ticket. <br/>                                                                                                                                                |
| [**IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode**](iprintoemprintticketprovider-convertprinttickettodevmode.md)             | The `IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode` method converts a print ticket to a [**DEVMODEW**](display.devmodew) structure. <br/>                                                                                                                                                  |
| [**IPrintOemPrintTicketProvider::ExpandIntentOptions**](iprintoemprintticketprovider-expandintentoptions.md)                             | The `IPrintOemPrintTicketProvider::ExpandIntentOptions` method enables the plug-in to expand printer options (such as photo printing) into individual feature settings in the print ticket. <br/>                                                                                                      |
| [**IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface**](iprintoemprintticketprovider-publishprinttickethelperinterface.md) | The `IPrintOemPrintTicketProvider::PublishPrintTicketHelperInterface` method publishes the print ticket helper interface for either Unidrv or Pscript5 user interface (UI) plug-ins.<br/>                                                                                                              |
| [**IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace**](iprintoemprintticketprovider-querydevicedefaultnamespace.md)             | The `IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace` method queries the device for its default namespace uniform resource identifier (URI).<br/>                                                                                                                                            |
| [**IPrintOemPrintTicketProvider::ValidatePrintTicket**](iprintoemprintticketprovider-validateprintticket.md)                             | The `IPrintOemPrintTicketProvider::ValidatePrintTicket` method validates a print ticket.<br/>                                                                                                                                                                                                          |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPrintTicketProvider%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




