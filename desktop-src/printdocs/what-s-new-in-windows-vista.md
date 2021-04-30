---
description: Lists the printing application programming interfaces (APIs) introduced in Windows Vista.
ms.assetid: 7a4eb5d7-b37d-4090-aea4-7274daa1e15c
title: What's New for Printing in Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# What's New for Printing in Windows Vista

Lists the printing application programming interfaces (APIs) introduced in Windows Vista.

The following functions and enumerations are used to manage print tickets.



| Function                                                               | Description                                                                                                                                   | Header    | Library     |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------|
| [**PTConvertPrintTicketToDevMode**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertprinttickettodevmode) | Converts a print ticket to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure.                                                                            | Prntvpt.h | Prntvpt.lib |
| [**PTConvertDevModeToPrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertdevmodetoprintticket) | Converts a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) to a print ticket.                                                                                      | Prntvpt.h | Prntvpt.lib |
| [**PTReleaseMemory**](/windows/desktop/api/prntvpt/nf-prntvpt-ptreleasememory)                             | Releases buffers created by certain print ticket management functions.                                                                        | Prntvpt.h | Prntvpt.lib |
| [**PTMergeAndValidatePrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptmergeandvalidateprintticket) | Validates and merges two print tickets into a viable print ticket.                                                                            | Prntvpt.h | Prntvpt.lib |
| [**PTGetPrintCapabilities**](/windows/desktop/api/prntvpt/nf-prntvpt-ptgetprintcapabilities)               | Gets an account of the printer's capabilities.                                                                                                | Prntvpt.h | Prntvpt.lib |
| [**PTOpenProvider**](/windows/desktop/api/prntvpt/nf-prntvpt-ptopenprovider)                               | Opens a print ticket provider.                                                                                                                | Prntvpt.h | Prntvpt.lib |
| [**PTOpenProviderEx**](/windows/desktop/api/prntvpt/nf-prntvpt-ptopenproviderex)                           | Opens a print ticket provider, even if it does not support the preferred version of the [Print Schema](./print-schema.md). | Prntvpt.h | Prntvpt.lib |
| [**PTCloseProvider**](/windows/desktop/api/prntvpt/nf-prntvpt-ptcloseprovider)                             | Closes a print ticket provider.                                                                                                               | Prntvpt.h | Prntvpt.lib |
| [**PTQuerySchemaVersionSupport**](/windows/desktop/api/prntvpt/nf-prntvpt-ptqueryschemaversionsupport)     | Gets the latest version of the [Print Schema](./print-schema.md) that a specified printer supports.                        | Prntvpt.h | Prntvpt.lib |



 



| Enumeration                                        | Description                                                                                                                                                                               | Header    |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [**EDefaultDevmodeType**](/windows/win32/api/prntvpt/ne-prntvpt-edefaultdevmodetype) | Enables callers to specify which [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) is used as the source of default values when a print ticket does not specify all the settings that might be in a **DEVMODE**. | Prntvpt.h |
| [**EPrintTicketScope**](/windows/desktop/api/prntvpt/ne-prntvpt-eprintticketscope)     | Specifies the scope of a print ticket.                                                                                                                                                    | Prntvpt.h |



 

The following functions are used to install printer drivers.



| Function                                                                   | Description                                                                                                                                                                 | Header     | Library      |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------|
| [**CorePrinterDriverInstalled**](coreprinterdriverinstalled.md)           | Reports whether a core printer driver with a specified GUID, date, and version is installed.                                                                                | Winspool.h | Winspool.lib |
| [**DeletePrinterDriverPackage**](deleteprinterdriverpackage.md)           | Deletes a printer driver package from the driver store.                                                                                                                     | Winspool.h | Winspool.lib |
| [**GetCorePrinterDrivers**](getcoreprinterdrivers.md)                     | Gets the GUID, version, and date of the specified core printer drivers and the path to their packages.                                                                      | Winspool.h | Winspool.lib |
| [**GetPrinterDriverPackagePath**](getprinterdriverpackagepath.md)         | Gets the path to the specified printer driver package on a print server.                                                                                                    | Winspool.h | Winspool.lib |
| [**InstallPrinterDriverFromPackage**](installprinterdriverfrompackage.md) | Installs a printer driver from a driver package in the print server's driver store.                                                                                         | Winspool.h | Winspool.lib |
| [**UploadPrinterDriverPackage**](uploadprinterdriverpackage.md)           | Uploads a printer driver to the driver store of a print server so that it can be installed with [**InstallPrinterDriverFromPackage**](installprinterdriverfrompackage.md). | Winspool.h | Winspool.lib |



 

The following functions, enumerations, and structures are used for printing and to manage printers and printer connections.



| Function                                               | Description                                                                                                                                              | Header     | Library      |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------|
| [**AddPrinterConnection2**](addprinterconnection2.md) | Adds a connection to the specified printer for the current user.                                                                                         | Winspool.h | Winspool.lib |
| [**OpenPrinter2**](openprinter2.md)                   | Retrieves a handle to the specified printer or print server or other types of handles in the print subsystem, while setting some of the printer options. | Winspool.h | Winspool.lib |



 



| Enumeration                                            | Description                                                                                       | Header     |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------|
| [**PRINTER\_OPTION\_FLAGS**](printer-option-flags.md) | Specifies the caching of a handle for a printer opened with [**OpenPrinter2**](openprinter2.md). | Winspool.h |



 



| Structure                                                         | Description                                                                            | Header     |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------|
| [**CORE\_PRINTER\_DRIVER**](core-printer-driver.md)              | Represents a printer driver on which other printer drivers are dependent.              | Winspool.h |
| [**DRIVER\_INFO\_8**](driver-info-8.md)                          | Represents a printer driver.                                                           | Winspool.h |
| [**FORM\_INFO\_2**](form-info-2.md)                              | Represents information about a localizable print form.                                 | Winspool.h |
| [**JOB\_INFO\_4**](job-info-4.md)                                | Represents a full set of values associated with a job and supports 64 bit spool files. | Winspool.h |
| [**PRINTER\_CONNECTION\_INFO\_1**](printer-connection-info-1.md) | Represents information about a connection to a printer.                                | Winspool.h |
| [**PRINTER\_OPTIONS**](printer-options.md)                       | Represents printer options.                                                            | Winspool.h |
| [**PRINTPROCESSOR\_CAPS\_2**](printprocessor-caps-2.md)          | Represents printer capability information.                                             | Winspool.h |



 

The following functions, enumerations, and interfaces are used to implement a new asynchronous printing notification system.



| Function                                                                             | Description                                                                                                                                                                                       | Header     | Library      |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------|
| [**CreatePrintAsyncNotifyChannel**](/windows/desktop/api/prnasnot/nf-prnasnot-createprintasyncnotifychannel)               | Creates a communication channel between the spooler-hosted printing component, such as a print driver or port monitor, and an application that needs to receive notifications from the component. | Prnasnot.h | Winspool.lib |
| [**RegisterForPrintAsyncNotifications**](/windows/desktop/api/prnasnot/nf-prnasnot-registerforprintasyncnotifications)     | Registers an application to receive notifications from spooler-hosted components such as printer drivers, print processors, and port monitors.                                                    | Prnasnot.h | Winspool.lib |
| [**UnRegisterForPrintAsyncNotifications**](/windows/desktop/api/prnasnot/nf-prnasnot-unregisterforprintasyncnotifications) | Enables an application that has registered to receive notifications from spooler-hosted printing components to end its subscription to the notifications.                                         | Prnasnot.h | Winspool.lib |



 



| Enumeration                                                                    | Description                                                                                                                                                                                                          | Header     |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| [**PrintAsyncNotifyConversationStyle**](/windows/desktop/api/prnasnot/ne-prnasnot-printasyncnotifyconversationstyle) | Specifies whether communication between applications and Print Spooler-hosted components, such as printer drivers, print processors, and port monitors, is bidirectional or unidirectional.                          | Prnasnot.h |
| [**PrintAsyncNotifyError**](/windows/desktop/api/prnasnot/ne-prnasnot-printasyncnotifyerror)                         | Specifies an error in an asynchronous notification transaction.                                                                                                                                                      | Prnasnot.h |
| [**PrintAsyncNotifyUserFilter**](/windows/desktop/api/prnasnot/ne-prnasnot-printasyncnotifyuserfilter)               | Specifies whether notifications will go only to listening applications that are associated with the same user as the Print Spooler-hosted sender or whether they will go to a broader set of listening applications. | Prnasnot.h |



 



| Interface and method                                                                                                      | Description                                                                                                                                                   | Header     | Library      |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|--------------|
| [**IPrintAsyncNotifyCallback::ChannelClosed**](/windows/desktop/api/prnasnot/nf-prnasnot-iprintasyncnotifycallback-channelclosed)    | Used by one member of a communication channel to advise the other member that the channel is being closed.                                                    | Prnasnot.h | Winspool.lib |
| [**IPrintAsyncNotifyCallback::OnEventNotify**](/windows/desktop/api/prnasnot/nf-prnasnot-iprintasyncnotifycallback-oneventnotify)    | Called by the Print Spooler to alert a listener that a notification is available on a specified channel.                                                      | Prnasnot.h | Winspool.lib |
| [**IPrintAsyncNotifyChannel::CloseChannel**](/windows/desktop/api/prnasnot/nf-prnasnot-iprintasyncnotifychannel-closechannel)         | Closes a communication channel.                                                                                                                               | Prnasnot.h | Winspool.lib |
| [**IPrintAsyncNotifyChannel::SendNotification**](/windows/desktop/api/prnasnot/nf-prnasnot-iprintasyncnotifychannel-sendnotification) | Sends a notification from a Print Spooler-hosted component to one or more listening applications or sends a response from an application back to a component. | Prnasnot.h | Winspool.lib |
| [**IPrintAsyncNotifyDataObject::AcquireData**](/windows/desktop/api/prnasnot/nf-prnasnot-iprintasyncnotifydataobject-acquiredata)  | Points listening applications to the notification data as well as the data's size and type.                                                                   | Prnasnot.h | Winspool.lib |
| [**IPrintAsyncNotifyDataObject::ReleaseData**](/windows/desktop/api/prnasnot/nf-prnasnot-iprintasyncnotifydataobject-releasedata)  | Releases the memory used by the data encapsulated in the [**IPrintAsyncNotifyDataObject**](/windows/desktop/api/prnasnot/nn-prnasnot-iprintasyncnotifydataobject).                                  | Prnasnot.h | Winspool.lib |



 

The following enumeration and structures are used for invoking the Microsoft XPS Document Converter (MXDC) which writes XML Paper Specification (XPS) documents to a device or file.



| Enumeration                                | Description                                                            | Header |
|--------------------------------------------|------------------------------------------------------------------------|--------|
| [**MxdcS0PageEnums**](mxdcs0pageenums.md) | Specifies types of resources, such as fonts or images, on an XPS page. | Mxdc.h |



 



| Structure                                                          | Description                                                                                                                                    | Header |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [**MxdcEscapeHeader**](mxdcescapeheader.md)                       | Represents an instruction to the MXDC.                                                                                                         | Mxdc.h |
| [**MxdcGetFileNameData**](mxdcgetfilenamedata.md)                 | Represents the full path and name for an MXDC output file.                                                                                     | Mxdc.h |
| [**MxdcPrintTicketEscape**](mxdcprintticketescape.md)             | Represents a combination of [**MxdcEscapeHeader**](mxdcescapeheader.md) and [**MxdcPrintTicketPassthrough**](mxdcprintticketpassthrough.md). | Mxdc.h |
| [**MxdcPrintTicketPassthrough**](mxdcprintticketpassthrough.md)   | Represents a print ticket that will be associated with an XPS document.                                                                        | Mxdc.h |
| [**MxdcS0PageData**](mxdcs0pagedata.md)                           | Represents an XPS-formatted page to be passed to the MXDC output file without any processing.                                                  | Mxdc.h |
| [**MxdcS0PagePassthroughEscape**](mxdcs0pagepassthroughescape.md) | Represents a combination of [**MxdcEscapeHeader**](mxdcescapeheader.md) and [**MxdcS0PageData**](mxdcs0pagedata.md).                         | Mxdc.h |
| [**MxdcS0PageResourceEscape**](mxdcs0pageresourceescape.md)       | Represents a combination of [**MxdcEscapeHeader**](mxdcescapeheader.md) and [**MxdcS0PageResource**](mxdcs0pageresourceescape.md).           | Mxdc.h |
| [**MxdcS0PageResource**](mxdcs0pageresourceescape.md)             | Represents a resource, such as a font or image, that is included on an XPS page by the MXDC.                                                   | Mxdc.h |



 

 

 
