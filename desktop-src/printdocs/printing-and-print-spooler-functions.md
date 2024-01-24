---
description: The Print Spooler API contains the functions and data structures that applications use to manage the Windows print spooler and the printers and print jobs that it controls.
ms.assetid: d859f84d-af0e-4b8b-b7fa-d7b1fc35ed39
title: Print Spooler API Functions
ms.topic: article
ms.date: 05/31/2018
---

# Print Spooler API Functions

The Print Spooler API contains the functions and data structures that applications use to manage the Windows print spooler and the printers and print jobs that it controls.

The functions of the Print Spooler API are divided into the following groups:

-   [Print Job Functions](#print-job-functions)
-   [Printer User Interface Functions](#printer-user-interface-functions)
-   [Printer Functions](#printer-functions)
-   [Printer Change Notification Functions](#printer-change-notification-functions)
-   [Printer Form Functions](#printer-form-functions)
-   [Print Spooler Functions](#print-spooler-api-functions)

## Print Job Functions

These functions send print jobs to a printer and track and control the print jobs in the print spooler.



| Function                                                                      | Description                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddJob**](addjob.md)<br/>                                           | The [**AddJob**](/windows/desktop/printdocs/addjob) function adds a print job to the list of print jobs that can be scheduled by the print spooler. The function retrieves the name of the file you can use to store the job. <br/>                                      |
| [**ClosePrinter**](closeprinter.md)<br/>                               | The [**ClosePrinter**](/windows/desktop/printdocs/closeprinter) function closes the specified printer object. <br/>                                                                                                                                                      |
| [**DocumentEvent**](documentevent.md)<br/>                             | The [**DocumentEvent**](/windows/desktop/printdocs/documentevent) function is an event handler for events associated with printing a document. <br/>                                                                                                                     |
| [**DocumentProperties**](documentproperties.md)<br/>                   | The [**DocumentProperties**](/windows/desktop/printdocs/documentproperties) function retrieves or modifies printer initialization information or displays a printer-configuration property sheet for the specified printer. <br/>                                        |
| [**EndDocPrinter**](enddocprinter.md)<br/>                             | The [**EndDocPrinter**](/windows/desktop/printdocs/enddocprinter) function ends a print job for the specified printer. <br/>                                                                                                                                             |
| [**EndPagePrinter**](endpageprinter.md)<br/>                           | The [**EndPagePrinter**](/windows/desktop/printdocs/endpageprinter) function notifies the print spooler that the application is at the end of a page in a print job. <br/>                                                                                               |
| [**EnumJobs**](enumjobs.md)<br/>                                       | The [**EnumJobs**](/windows/desktop/printdocs/enumjobs) function retrieves information about a specified set of print jobs for a specified printer. <br/>                                                                                                                |
| [**GetJob**](getjob.md)<br/>                                           | The [**GetJob**](/windows/desktop/printdocs/getjob) function retrieves information about a specified print job. <br/>                                                                                                                                                    |
| [**OpenPrinter**](openprinter.md)<br/>                                 | The [**OpenPrinter**](/windows/desktop/printdocs/openprinter) function retrieves a handle to the specified printer or print server or other types of handles in the print subsystem. <br/>                                                                               |
| [**OpenPrinter2**](openprinter2.md)<br/>                               | Retrieves a handle to the specified printer, print server, or other types of handles in the print subsystem, while setting some of the printer options.<br/>                                                                                      |
| [**ReportJobProcessingProgress**](reportjobprocessingprogress.md)<br/> | Reports to the Print Spooler service whether an XPS print job is in the spooling or the rendering phase and what part of the processing is currently underway.<br/>                                                                               |
| [**ScheduleJob**](schedulejob.md)<br/>                                 | The [**ScheduleJob**](/windows/desktop/printdocs/schedulejob) function requests that the print spooler schedule a specified print job for printing. <br/>                                                                                                                |
| [**SetJob**](setjob.md)<br/>                                           | The [**SetJob**](/windows/desktop/printdocs/setjob) function pauses, resumes, cancels, or restarts a print job on a specified printer. You can also use the **SetJob** function to set print job parameters, such as the print job priority and the document name. <br/> |
| [**StartDocPrinter**](startdocprinter.md)<br/>                         | The [**StartDocPrinter**](/windows/desktop/printdocs/startdocprinter) function notifies the print spooler that a document is to be spooled for printing. <br/>                                                                                                           |
| [**StartPagePrinter**](startpageprinter.md)<br/>                       | The [**StartPagePrinter**](/windows/desktop/printdocs/startpageprinter) function notifies the spooler that a page is about to be printed on the specified printer. <br/>                                                                                                 |



 

## Printer User Interface Functions

These functions display a user interface that enables the user to select or configure a printer.



| Function                                                                    | Description                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdvancedDocumentProperties**](advanceddocumentproperties.md)<br/> | The [**AdvancedDocumentProperties**](/windows/desktop/printdocs/advanceddocumentproperties) function displays a printer-configuration dialog box for the specified printer, allowing the user to configure that printer. <br/>                                                                                                                                                      |
| [**ConfigurePort**](configureport.md)<br/>                           | The [**ConfigurePort**](/windows/desktop/printdocs/configureport) function displays the port-configuration dialog box for a port on the specified server. <br/>                                                                                                                                                                                                                     |
| [**ConnectToPrinterDlg**](connecttoprinterdlg.md)<br/>               | The [**ConnectToPrinterDlg**](/windows/desktop/printdocs/connecttoprinterdlg) function displays a dialog box that lets users browse and connect to printers on a network. If the user selects a printer, the function attempts to create a connection to it; if a suitable driver is not installed on the server, the user is given the option of creating a printer locally. <br/> |
| [**PrinterProperties**](printerproperties.md)<br/>                   | The [**PrinterProperties**](/windows/desktop/printdocs/printerproperties) function displays a printer-properties property sheet for the specified printer. <br/>                                                                                                                                                                                                                    |



 

## Printer Functions

These functions add and configure the printers that the print spooler uses.



| Function                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortPrinter**](abortprinter.md)<br/>                       | The [**AbortPrinter**](/windows/desktop/printdocs/abortprinter) function deletes a printer's spool file if the printer is configured for spooling. <br/>                                                                                                                                                                                                                                                                  |
| [**AddPrinter**](addprinter.md)<br/>                           | The [**AddPrinter**](/windows/desktop/printdocs/addprinter) function adds a printer to the list of supported printers for a specified server. <br/>                                                                                                                                                                                                                                                                       |
| [**AddPrinterConnection**](addprinterconnection.md)<br/>       | The **AddPrinterConnection** function adds a connection to the specified printer for the current user. <br/>                                                                                                                                                                                                                                                                                       |
| [**AddPrinterConnection2**](addprinterconnection2.md)<br/>     | Adds a connection to the specified printer for the current user and specifies connection details.<br/>                                                                                                                                                                                                                                                                                             |
| [**DeletePrinter**](deleteprinter.md)<br/>                     | The [**DeletePrinter**](/windows/desktop/printdocs/deleteprinter) function deletes the specified printer object. <br/>                                                                                                                                                                                                                                                                                                    |
| [**DeletePrinterConnection**](deleteprinterconnection.md)<br/> | The [**DeletePrinterConnection**](/windows/desktop/printdocs/deleteprinterconnection) function deletes a connection to a printer that was established by a call to [**AddPrinterConnection**](addprinterconnection.md) or [**ConnectToPrinterDlg**](connecttoprinterdlg.md). <br/>                                                                                                                                      |
| [**DeletePrinterData**](deleteprinterdata.md)<br/>             | The [**DeletePrinterData**](/windows/desktop/printdocs/deleteprinterdata) function deletes specified configuration data for a printer. A printer's configuration data consists of a set of named and typed values. The **DeletePrinterData** function deletes one of these values, specified by its value name. <br/>                                                                                                     |
| [**DeletePrinterDataEx**](deleteprinterdataex.md)<br/>         | The [**DeletePrinterDataEx**](/windows/desktop/printdocs/deleteprinterdataex) function deletes a specified value from the configuration data for a printer. A printer's configuration data consists of a set of named and typed values stored in a hierarchy of registry keys. The function deletes a specified value under a specified key. <br/>                                                                        |
| [**DeletePrinterKey**](deleteprinterkey.md)<br/>               | The [**DeletePrinterKey**](/windows/desktop/printdocs/deleteprinterkey) function deletes a specified key and all its subkeys for a specified printer. <br/>                                                                                                                                                                                                                                                               |
| [**EnumPrinterData**](enumprinterdata.md)<br/>                 | The [**EnumPrinterData**](/windows/desktop/printdocs/enumprinterdata) function enumerates configuration data for a specified printer. <br/>                                                                                                                                                                                                                                                                               |
| [**EnumPrinterDataEx**](enumprinterdataex.md)<br/>             | The [**EnumPrinterDataEx**](/windows/desktop/printdocs/enumprinterdataex) function enumerates all value names and data for a specified printer and key. <br/>                                                                                                                                                                                                                                                             |
| [**EnumPrinterKey**](enumprinterkey.md)<br/>                   | The [**EnumPrinterKey**](/windows/desktop/printdocs/enumprinterkey) function enumerates the subkeys of a specified key for a specified printer. <br/>                                                                                                                                                                                                                                                                     |
| [**EnumPrinters**](enumprinters.md)<br/>                       | The [**EnumPrinters**](/windows/desktop/printdocs/enumprinters) function enumerates available printers, print servers, domains, or print providers. <br/>                                                                                                                                                                                                                                                                 |
| [**FlushPrinter**](flushprinter.md)<br/>                       | The [**FlushPrinter**](/windows/desktop/printdocs/flushprinter) function sends a buffer to the printer in order to clear it from a transient state. <br/>                                                                                                                                                                                                                                                                 |
| [**GetDefaultPrinter**](getdefaultprinter.md)<br/>             | The [**GetDefaultPrinter**](/windows/desktop/printdocs/getdefaultprinter) function retrieves the printer name of the default printer for the current user on the local computer. <br/>                                                                                                                                                                                                                                    |
| [**GetPrinter**](getprinter.md)<br/>                           | The [**GetPrinter**](/windows/desktop/printdocs/getprinter) function retrieves information about a specified printer. <br/>                                                                                                                                                                                                                                                                                               |
| [**GetPrinterData**](getprinterdata.md)<br/>                   | The [**GetPrinterData**](/windows/desktop/printdocs/getprinterdata) function retrieves configuration data for the specified printer or print server. <br/>                                                                                                                                                                                                                                                                |
| [**GetPrinterDataEx**](getprinterdataex.md)<br/>               | The [**GetPrinterDataEx**](/windows/desktop/printdocs/getprinterdataex) function retrieves configuration data for the specified printer or print server. **GetPrinterDataEx** can retrieve values stored by the [**SetPrinterData**](setprinterdata.md) function. In addition, **GetPrinterDataEx** can retrieve values stored under a specified key by the [**SetPrinterDataEx**](setprinterdataex.md) function. <br/> |
| [**IsValidDevmode**](isvaliddevmode.md)<br/>                   | The [**IsValidDevmode**](isvaliddevmode.md) function verifies that the contents of a DEVMODE structure are valid. <br/>                                                                                                                                                                                                                                                                           |
| [**ReadPrinter**](readprinter.md)<br/>                         | The [**ReadPrinter**](/windows/desktop/printdocs/readprinter) function retrieves data from the specified printer. <br/>                                                                                                                                                                                                                                                                                                   |
| [**ResetPrinter**](resetprinter.md)<br/>                       | The [**ResetPrinter**](/windows/desktop/printdocs/resetprinter) function specifies the data type and device mode values to be used for printing documents submitted by the [**StartDocPrinter**](startdocprinter.md) function. These values can be overridden by using the [**SetJob**](setjob.md) function after document printing has started. <br/>                                                                  |
| [**SetDefaultPrinter**](setdefaultprinter.md)<br/>             | The [**SetDefaultPrinter**](/windows/desktop/printdocs/setdefaultprinter) function sets the printer name of the default printer for the current user on the local computer. <br/>                                                                                                                                                                                                                                         |
| [**SetPort**](setport.md)<br/>                                 | The [**SetPort**](/windows/desktop/printdocs/setport) function sets the status associated with a printer port. <br/>                                                                                                                                                                                                                                                                                                      |
| [**SetPrinter**](setprinter.md)<br/>                           | The [**SetPrinter**](/windows/desktop/printdocs/setprinter) function sets the data for a specified printer or sets the state of the specified printer by pausing printing, resuming printing, or clearing all print jobs. <br/>                                                                                                                                                                                           |
| [**SetPrinterData**](setprinterdata.md)<br/>                   | The [**SetPrinterData**](/windows/desktop/printdocs/setprinterdata) function sets the configuration data for a printer or print server. <br/>                                                                                                                                                                                                                                                                             |
| [**SetPrinterDataEx**](setprinterdataex.md)<br/>               | The [**SetPrinterDataEx**](/windows/desktop/printdocs/setprinterdataex) function sets the configuration data for a printer or print server. The function stores the configuration data under the printer's registry key. <br/>                                                                                                                                                                                            |
| [**WritePrinter**](writeprinter.md)<br/>                       | The [**WritePrinter**](writeprinter.md) function notifies the print spooler that data should be written to the specified printer. <br/>                                                                                                                                                                                                                                                           |



 

## Printer Change Notification Functions

These functions enable an application to be notified of changes to a printer's status.



| Function                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FindClosePrinterChangeNotification**](findcloseprinterchangenotification.md)<br/> | The [**FindClosePrinterChangeNotification**](/windows/desktop/printdocs/findcloseprinterchangenotification) function closes a change notification object created by calling the [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) function. The printer or print server associated with the change notification object will no longer be monitored by that object. <br/> |
| [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md)<br/> | The [**FindFirstPrinterChangeNotification**](/windows/desktop/printdocs/findfirstprinterchangenotification) function creates a change notification object and returns a handle to the object. You can then use this handle in a call to one of the wait functions to monitor changes to the printer or print server. <br/>                                                                              |
| [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md)<br/>   | The [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md) function retrieves information about the most recent change notification for a change notification object associated with a printer or print server. Call this function when a wait operation on the change notification object is satisfied. <br/>                                           |
| [**FreePrinterNotifyInfo**](freeprinternotifyinfo.md)<br/>                           | The [**FreePrinterNotifyInfo**](/windows/desktop/printdocs/freeprinternotifyinfo) function frees a system-allocated buffer created by the [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md) function. <br/>                                                                                                                                                                |



 

## Printer Form Functions

These functions manage the forms used by a printer.



| Function                                    | Description                                                                                                                                    |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddForm**](addform.md)<br/>       | The [**AddForm**](/windows/desktop/printdocs/addform) function adds a form to the list of available forms that can be selected for the specified printer. <br/> |
| [**DeleteForm**](deleteform.md)<br/> | The [**DeleteForm**](/windows/desktop/printdocs/deleteform) function removes a form name from the list of supported forms. <br/>                                |
| [**EnumForms**](enumforms.md)<br/>   | The [**EnumForms**](/windows/desktop/printdocs/enumforms) function enumerates the forms supported by the specified printer. <br/>                               |
| [**GetForm**](getform.md)<br/>       | The [**GetForm**](/windows/desktop/printdocs/getform) function retrieves information about a specified form. <br/>                                              |
| [**SetForm**](setform.md)<br/>       | The [**SetForm**](/windows/desktop/printdocs/setform) function sets the form information for the specified printer. <br/>                                       |



 

## Print Spooler Functions

These functions interact with the print spooler at a low level.



| Function                                                          | Description                                                                                                                                                                                            |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CloseSpoolFileHandle**](closespoolfilehandle.md)<br/>   | The [**CloseSpoolFileHandle**](/windows/desktop/printdocs/closespoolfilehandle) function closes a handle to a spool file associated with the print job currently submitted by the application. <br/>                    |
| [**CommitSpoolData**](commitspooldata.md)<br/>             | The [**CommitSpoolData**](/windows/desktop/printdocs/commitspooldata) function notifies the print spooler that a specified amount of data has been written to a specified spool file and is ready to be rendered. <br/> |
| [**GetPrintExecutionData**](getprintexecutiondata.md)<br/> | The [**GetPrintExecutionData**](getprintexecutiondata.md) retrieves the current print context.<br/>                                                                                             |
| [**GetSpoolFileHandle**](getspoolfilehandle.md)<br/>       | The [**GetSpoolFileHandle**](/windows/desktop/printdocs/getspoolfilehandle) function retrieves a handle for the spool file associated with the job currently submitted by the application. <br/>                        |



 

 

