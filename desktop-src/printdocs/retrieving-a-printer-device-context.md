---
description: This topic describes how to retrieve a printer device context.
ms.assetid: b3eb9c48-f4c4-42f1-b189-1fa42670008e
title: 'How To: Retrieve a Printer Device Context'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Retrieve a Printer Device Context

This topic describes how to retrieve a printer device context. You can retrieve a printer device context by calling the [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) function directly, or it can be returned by a **Print** common dialog box.

When you display a **Print** common dialog box a user will be able to select the printer, the pages of the document, and the number of document copies they want to print. The **Print** common dialog box returns these selections in a data structure.

This topic describes how to obtain a printer device context by using the following methods.

-   [Call CreateDC](#call-createdc)
-   [Display a Print Common Dialog Box](#display-a-print-common-dialog-box)
    -   [Using the PrintDlgEx Function](#using-the-printdlgex-function)
    -   [Using the PrintDlg Function](#using-the-printdlg-function)

## Call CreateDC

If you know the device to which you want to print, you can call [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) and pass that information directly to the function. **CreateDC** returns a device context into which you can render the content to print.

The simplest call to retrieve a device context is shown in the code example that follows. The code in this example retrieves a device context to the default display device.


```C++
    hDC = CreateDC(TEXT("DISPLAY"),NULL,NULL,NULL);
```



To render to a specific printer, you must specify "WINSPOOL" as the device and pass the correct name of the printer to [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca). You can also pass a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure in the call to **CreateDC** if you want to provide device-specific initialization data for the device driver when you create the device context.

The following example shows a call to [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) in which the "WINSPOOL" driver is selected and the printer name is specified by name.


```C++
    printerDC = CreateDC( L"WINSPOOL", printerName, NULL, NULL);
```



You can obtain the exact printer name string to pass to [**CreateDC**](/windows/desktop/api/wingdi/nf-wingdi-createdca) by calling the [**EnumPrinters**](enumprinters.md) function. The following code example shows how to call **EnumPrinters** and get the names of the local and locally connected printers. Because the size of the required buffer cannot be known in advance, the **EnumPrinters** is called two times. The first call returns the size of the required buffer. That information is used to allocate a buffer of the required size, and the second call to **EnumPrinters** returns the data that you want.


```C++
    fnReturn = EnumPrinters(
                PRINTER_ENUM_LOCAL | PRINTER_ENUM_CONNECTIONS,
                NULL,
                1L,                // printer info level
                (LPBYTE)NULL,
                0L,
                &dwNeeded,
                &dwReturned);
    
    if (dwNeeded > 0)
    {
        pInfo = (PRINTER_INFO_1 *)HeapAlloc(
                    GetProcessHeap(), 0L, dwNeeded);
    }

    if (NULL != pInfo)
    {
        dwReturned = 0;
        fnReturn = EnumPrinters(
                PRINTER_ENUM_LOCAL | PRINTER_ENUM_CONNECTIONS,
                NULL,
                1L,                // printer info level
                (LPBYTE)pInfo,
                dwNeeded,
                &dwNeeded,
                &dwReturned);
    }

    if (fnReturn)
    {
        // Review the information from all the printers
        //  returned by EnumPrinters.
        for (i=0; i < dwReturned; i++)
        {
            // pThisInfo[i]->pName contains the printer
            //  name to use in the CreateDC function call.
            //
            // When this desired printer is found in the list of
            //  returned printer, set the printerName value to 
            //  use in the call to CreateDC.

            // printerName = pThisInfo[i]->pName
        }
    }
```



## Display a Print Common Dialog Box

You can choose from two **Print** common dialog boxes to display to a user; the newer dialog box, which you can display by calling the [**PrintDlgEx**](/previous-versions/windows/desktop/legacy/ms646942(v=vs.85)) function, and the older style dialog box, which you can display by calling the [**PrintDlg**](/previous-versions/windows/desktop/legacy/ms646940(v=vs.85)) function. The following sections describe how to call each dialog box from an application.

### Using the PrintDlgEx Function

Call the [**PrintDlgEx**](/previous-versions/windows/desktop/legacy/ms646942(v=vs.85)) function to display the **Print** property sheet. By using the property sheet, the user can specify information about the print job. For example, the user can select a range of pages to print, the number of copies, and so on. The **PrintDlgEx** can also retrieve a handle to a device context for the selected printer. You can use the handle to render output on the printer.

For sample code that illustrates the use of [**PrintDlgEx**](/previous-versions/windows/desktop/legacy/ms646942(v=vs.85)) to retrieve a printer device context, see "Using the Print Property Sheet" in [Using Common Dialog Boxes](../dlgbox/using-common-dialog-boxes.md).

### Using the PrintDlg Function

If your application must run on a system that does not support the [**PrintDlgEx**](/previous-versions/windows/desktop/legacy/ms646942(v=vs.85)) function, such as on a system that is running a version of Windows earlier than Windows 2000, or does not need the extra functionality that the **PrintDlgEx** function provides, use the [**PrintDlg**](/previous-versions/windows/desktop/legacy/ms646940(v=vs.85)) function. The following steps describe how to display the older style **Print** common dialog box.

1.  Initialize the [**PRINTDLG**](/windows/win32/api/commdlg/ns-commdlg-printdlga) data structure.
2.  Call [**PrintDlg**](/previous-versions/windows/desktop/legacy/ms646940(v=vs.85)) to display the **Print** common dialog box to the user.
3.  If the [**PrintDlg**](/previous-versions/windows/desktop/legacy/ms646940(v=vs.85)) call returns **TRUE**, lock the returned [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure memory. If the **PrintDlg** call returns **FALSE**, the user pressed the **Cancel** button in the **Print** common dialog box so there is nothing more to process.
4.  Allocate a local memory buffer that is large enough to contain a copy of the [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure.
5.  Copy the returned [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure to the locally allocated one.
6.  Save other information that is returned in the [**PRINTDLG**](/windows/win32/api/commdlg/ns-commdlg-printdlga) structure and that you will need to process the print job.
7.  Free the [**PRINTDLG**](/windows/win32/api/commdlg/ns-commdlg-printdlga) and the memory buffers it references.

The following example code illustrates how to use the [**PrintDlg**](/previous-versions/windows/desktop/legacy/ms646940(v=vs.85)) function to get the device context and the name of selected printer.


```C++
// Display the printer dialog box so the user can select the 
//  printer and the number of copies to print.
BOOL            printDlgReturn = FALSE;
HDC                printerDC = NULL;
PRINTDLG        printDlgInfo = {0};
LPWSTR            localPrinterName = NULL;
PDEVMODE        returnedDevmode = NULL;
PDEVMODE        localDevmode = NULL;
int                localNumberOfCopies = 0;

// Initialize the print dialog box's data structure.
printDlgInfo.lStructSize = sizeof( printDlgInfo );
printDlgInfo.Flags = 
    // Return a printer device context.
    PD_RETURNDC 
    // Don't allow separate print to file.
    // Remove these flags if you want to support this feature.
    | PD_HIDEPRINTTOFILE        
    | PD_DISABLEPRINTTOFILE 
    // Don't allow selecting individual document pages to print.
    // Remove this flag if you want to support this feature.
    | PD_NOSELECTION;

// Display the printer dialog and retrieve the printer DC.
printDlgReturn = PrintDlg(&printDlgInfo);

// Check the return value.
if (TRUE == printDlgReturn)
{
    // The user clicked OK so the printer dialog box data 
    //  structure was returned with the user's selections.
    //  Copy the relevant data from the data structure and 
    //  save them to a local data structure.

    //
    // Get the HDC of the selected printer
    printerDC = printDlgInfo.hDC;
    
    // In this example, the DEVMODE structure returned by 
    //    the printer dialog box is copied to a local memory
    //    block and a pointer to the printer name that is 
    //    stored in the copied DEVMODE structure is saved.

    //
    //  Lock the handle to get a pointer to the DEVMODE structure.
    returnedDevmode = (PDEVMODE)GlobalLock(printDlgInfo.hDevMode);

    localDevmode = (LPDEVMODE)HeapAlloc(
                        GetProcessHeap(), 
                        HEAP_ZERO_MEMORY | HEAP_GENERATE_EXCEPTIONS, 
                        returnedDevmode->dmSize);

    if (NULL != localDevmode) 
    {
        memcpy(
            (LPVOID)localDevmode,
            (LPVOID)returnedDevmode, 
            returnedDevmode->dmSize);

        // Save the printer name from the DEVMODE structure.
        //  This is done here just to illustrate how to access
        //  the name field. The printer name can also be accessed
        //  by referring to the dmDeviceName in the local 
        //  copy of the DEVMODE structure.
        localPrinterName = localDevmode->dmDeviceName;

        // Save the number of copies as entered by the user
        localNumberOfCopies = printDlgInfo.nCopies;    
    }
    else
    {
        // Unable to allocate a new structure so leave
        //  the pointer as NULL to indicate that it's empty.
    }

    // Free the DEVMODE structure returned by the print 
    //  dialog box.
    if (NULL != printDlgInfo.hDevMode) 
    {
        GlobalFree(printDlgInfo.hDevMode);
    }
}
else
{
    // The user cancelled out of the print dialog box.
}
```



For more information about the [**PrintDlg**](/previous-versions/windows/desktop/legacy/ms646940(v=vs.85)) function, see "Displaying the Print Dialog Box" in [Using Common Dialog Boxes](../dlgbox/using-common-dialog-boxes.md).

 

 
