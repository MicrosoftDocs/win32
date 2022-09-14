---
description: The following functions are used to manage print tickets.
ms.assetid: 9e942a1d-660b-4691-9282-ffb49e0b9848
title: Print Ticket API Functions
ms.topic: article
ms.date: 05/31/2018
---

# Print Ticket API Functions

The following functions are used to manage print tickets.

## In this section



| Function                                                                                  | Description                                                                                                                                            |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConvertDevModeToPrintTicketThunk2**](convertdevmodetoprintticketthunk2.md)<br/> | Converts a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure to a print ticket.<br/>                                                                          |
| [**ConvertPrintTicketToDevModeThunk2**](convertprinttickettodevmodethunk2.md)<br/> | Converts a print ticket to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure.<br/>                                                                          |
| [**MergeAndValidatePrintTicketThunk2**](mergeandvalidateprintticketthunk2.md)<br/> | Merges two print tickets and returns a valid, viable print ticket.<br/>                                                                          |
| [**PTCloseProvider**](/windows/desktop/api/prntvpt/nf-prntvpt-ptcloseprovider)<br/>                                     | Closes a print ticket provider handle.<br/>                                                                                                      |
| [**PTConvertDevModeToPrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertdevmodetoprintticket)<br/>         | Converts a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure to a print ticket inside an [**IStream**](/windows/desktop/Stg/istream-compound-file-implementation).<br/>        |
| [**PTConvertPrintTicketToDevMode**](/windows/desktop/api/prntvpt/nf-prntvpt-ptconvertprinttickettodevmode)<br/>         | Converts a print ticket into a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure.<br/>                                                                        |
| [**PTGetPrintCapabilities**](/windows/desktop/api/prntvpt/nf-prntvpt-ptgetprintcapabilities)<br/>                       | Retrieves the printer's capabilities formatted in compliance with the XML [Print Schema](./printschema.md).<br/>                   |
| [**PTGetPrintDeviceCapabilities**](/windows/win32/api/prntvpt/nf-prntvpt-ptgetprintdevicecapabilities)<br/>    | Retrieves the device printer's capabilities formatted in compliance with the XML [Print Schema](./printschema.md).<br/>            |
| [**PTGetPrintDeviceResources**](/windows/win32/api/prntvpt/nf-prntvpt-ptgetprintdeviceresources)<br/>          | It retrieves the print devices resources for a printer formatted in compliance with the XML [Print Schema](./printschema.md).<br/> |
| [**PTMergeAndValidatePrintTicket**](/windows/desktop/api/prntvpt/nf-prntvpt-ptmergeandvalidateprintticket)<br/>         | Merges two print tickets and returns a valid, viable print ticket.<br/>                                                                          |
| [**PTOpenProvider**](/windows/desktop/api/prntvpt/nf-prntvpt-ptopenprovider)<br/>                                       | Opens an instance of a print ticket provider.<br/>                                                                                               |
| [**PTOpenProviderEx**](/windows/desktop/api/prntvpt/nf-prntvpt-ptopenproviderex)<br/>                                   | Opens an instance of a print ticket provider.<br/>                                                                                               |
| [**PTQuerySchemaVersionSupport**](/windows/desktop/api/prntvpt/nf-prntvpt-ptqueryschemaversionsupport)<br/>             | Retrieves the highest (latest) version of the [Print Schema](./printschema.md) that the specified printer supports.<br/>           |
| [**PTReleaseMemory**](/windows/desktop/api/prntvpt/nf-prntvpt-ptreleasememory)<br/>                                     | Releases buffers associated with print tickets and print capabilities.<br/>                                                                      |
| [**UnbindPTProviderThunk**](unbindptproviderthunk.md)<br/>                         | Closes a handle to a print ticket provider.<br/>                                                                                                 |



 

 

