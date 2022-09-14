---
description: The code sample later in this topic shows how to send printer control data directly to printers that use GDI-based printer drivers.
ms.assetid: 321f2333-d88e-4042-b9b1-0d918b3209d4
title: 'How To: Send Data Directly to a GDI Printer'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Send Data Directly to a GDI Printer

The code sample later in this topic shows how to send printer control data directly to printers that use GDI-based printer drivers.

The following steps describe how to send data directly to a printer. These steps are also illustrated in the code example that follows.

1.  Call [**OpenPrinter**](openprinter.md) to get a handle to the printer.
2.  Initialize a [**DOCINFO**](/windows/desktop/api/wingdi/ns-wingdi-docinfoa) structure with the printer data.
3.  Call [**StartDocPrinter**](startdocprinter.md) to indicate that the application will be sending document data to the printer.
4.  Call [**StartPagePrinter**](startpageprinter.md) to indicate that the application will be sending a new page to the printer.
5.  Call [**WritePrinter**](writeprinter.md) to send the data.
6.  Call [**EndPagePrinter**](endpageprinter.md) to indicate that all data for the current page has been sent.
7.  Call [**EndDocPrinter**](enddocprinter.md) to indicate that all data for this document has been sent.
8.  Call [**ClosePrinter**](closeprinter.md) to release the resources.

Send printer control data directly to printers that use GDI-based printer drivers.


```C++
// 
// RawDataToPrinter - sends binary data directly to a printer 
//  
// szPrinterName: NULL-terminated string specifying printer name 
// lpData:        Pointer to raw data bytes 
// dwCount        Length of lpData in bytes 
//  
// Returns: TRUE for success, FALSE for failure. 
//  
BOOL RawDataToPrinter(LPTSTR szPrinterName, LPBYTE lpData, DWORD dwCount)
{
    BOOL     bStatus = FALSE;
    HANDLE     hPrinter = NULL;
    DOC_INFO_1 DocInfo;
    DWORD      dwJob = 0L;
    DWORD      dwBytesWritten = 0L;

    // Open a handle to the printer. 
    bStatus = OpenPrinter( szPrinterName, &hPrinter, NULL );
    if (bStatus) {
        // Fill in the structure with info about this "document." 
        DocInfo.pDocName = (LPTSTR)_T("My Document");
        DocInfo.pOutputFile = NULL;
        DocInfo.pDatatype = (LPTSTR)_T("RAW");

        // Inform the spooler the document is beginning. 
        dwJob = StartDocPrinter( hPrinter, 1, (LPBYTE)&DocInfo );
        if (dwJob > 0) {
            // Start a page. 
            bStatus = StartPagePrinter( hPrinter );
            if (bStatus) {
                // Send the data to the printer. 
                bStatus = WritePrinter( hPrinter, lpData, dwCount, &dwBytesWritten);
                EndPagePrinter (hPrinter);
            }
            // Inform the spooler that the document is ending. 
            EndDocPrinter( hPrinter );
        }
        // Close the printer handle. 
        ClosePrinter( hPrinter );
    }
    // Check to see if correct number of bytes were written. 
    if (!bStatus || (dwBytesWritten != dwCount)) {
        bStatus = FALSE;
    } else {
        bStatus = TRUE;
    }
    return bStatus;
}
```



## Related topics

<dl> <dt>

[**ClosePrinter**](closeprinter.md)
</dt> <dt>

[**EndDocPrinter**](enddocprinter.md)
</dt> <dt>

[**EndPagePrinter**](endpageprinter.md)
</dt> <dt>

[**OpenPrinter**](openprinter.md)
</dt> <dt>

[**StartDocPrinter**](startdocprinter.md)
</dt> <dt>

[**StartPagePrinter**](startpageprinter.md)
</dt> <dt>

[**WritePrinter**](writeprinter.md)
</dt> </dl>

 

 
