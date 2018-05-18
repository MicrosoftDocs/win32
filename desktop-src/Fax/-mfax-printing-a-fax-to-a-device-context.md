---
Description: 'This topic describes how to print a fax to a device context in the Microsoft Win32 environment.'
ms.assetid: 'd6e0afbd-6e64-487c-97fc-1e5cd5092d14'
title: Printing a Fax to a Device Context
---

# Printing a Fax to a Device Context

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

A fax client application does not require a connection to a fax server to print a fax to a printer device context (DC). Instead of calling the [**FaxSendDocument**](-mfax-faxsenddocument.md) or [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) functions, an application can provide transmission information directly to the Windows Graphics Device Interface (GDI) functions the Fax Service Client API provides. This enables the client application to transmit an active document by printing it directly to a printer DC. The fax client GDI functions include the [**FaxStartPrintJob**](-mfax-faxstartprintjob.md) and [**FaxPrintCoverPage**](-mfax-faxprintcoverpage.md) functions.

Since the fax GDI functions use the fax printer driver, you must specify the name of a connected fax printer when you call the [**FaxStartPrintJob**](-mfax-faxstartprintjob.md) function. The printer can be a local printer, for example, "printername", or a remote printer, such as "\\\\machinename\\printername". If you pass a **NULL** *PrinterName* parameter to **FaxStartPrintJob**, it specifies the local fax printer.

The [**FaxStartPrintJob**](-mfax-faxstartprintjob.md) function returns a handle to a printer DC. Note that a fax client application should not call the [CreateDC](http://msdn.microsoft.com/library/en-us/gdi/devcons_5g83.asp) Win32 GDI function to create the fax printer DC; nor should it call the [StartDoc](http://msdn.microsoft.com/library/en-us/gdi/prntspol_95sz.asp) printing function to start printing a fax document. Instead, the application should call the **FaxStartPrintJob** function.

## To print a fax to a printer device context

1.  Call the [**FaxStartPrintJob**](-mfax-faxstartprintjob.md) function to retrieve the handle to a fax printer DC. The function returns the handle in a [**FAX\_CONTEXT\_INFO**](-mfax-fax-context-info-str.md) structure.
2.  Call the [**FaxPrintCoverPage**](-mfax-faxprintcoverpage.md) function, if a cover page is required, passing a pointer to the [**FAX\_CONTEXT\_INFO**](-mfax-fax-context-info-str.md) structure returned by the [**FaxStartPrintJob**](-mfax-faxstartprintjob.md) function.
3.  Print the fax document to the printer DC in the normal manner, passing the handle to the DC returned by the [**FaxStartPrintJob**](-mfax-faxstartprintjob.md) function. The procedure can include calls to the [StartPage](http://msdn.microsoft.com/library/en-us/gdi/prntspol_2isl.asp) and [EndPage](http://msdn.microsoft.com/library/en-us/gdi/prntspol_3b1h.asp) Win32 GDI functions.
4.  Call the [EndDoc](http://msdn.microsoft.com/library/en-us/gdi/prntspol_0qhv.asp) function or the [AbortDoc](http://msdn.microsoft.com/library/en-us/gdi/prntspol_86xv.asp) function, passing the handle to the DC returned by [**FaxStartPrintJob**](-mfax-faxstartprintjob.md). This closes the document and ends the fax print job.
5.  Call the [DeleteDC](http://msdn.microsoft.com/library/en-us/gdi/devcons_2p2b.asp) function to deallocate the handle to the DC.

## Related topics

<dl> <dt>

[Printing and Print Spooler Reference](http://msdn.microsoft.com/library/en-us/gdi/prntspol_95id.asp)
</dt> </dl>

 

 



