---
Description: This topic describes how to collect print job information from the user.
ms.assetid: 98ae97e2-25c1-455c-8283-45bb07fb8251
title: 'How To: Collect Print Job Information from the User'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Collect Print Job Information from the User

This topic describes how to collect print job information from the user.

## Overview

Collect print job information from the user by calling the [**PrintDlg**](https://msdn.microsoft.com/library/ms646940(v=VS.85).aspx) function. This function displays the **Print** common dialog box to the user, and returns the print job information in a [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) data structure.

The **Print** common dialog box is displayed when the user starts a print job. The **Print** common dialog box is a modal dialog box, which means that the user cannot interact with the main window until the common dialog box is closed.

## Collecting Print Job Information

1.  Initialize the [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) structure element.

    Before a program can display the **Print** common dialog box , it must allocate and initialize a [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) structure. It then passes this structure to the [**PrintDlg**](https://msdn.microsoft.com/library/ms646940(v=VS.85).aspx) function, which displays the dialog and returns the print job data in the same structure. The following code example shows how the sample program performs this step.

    ```C++
    // Initialize the print dialog box's data structure.
    pd.lStructSize = sizeof( pd );
    pd.Flags = 
        // Return a printer device context
        PD_RETURNDC 
        // Don't allow separate print to file.
        | PD_HIDEPRINTTOFILE        
        | PD_DISABLEPRINTTOFILE 
        // Don't allow selecting individual document pages to print.
        | PD_NOSELECTION;
    ```

    

2.  Display the **Print** common dialog box.

    Call [**PrintDlg**](https://msdn.microsoft.com/library/ms646940(v=VS.85).aspx) with the initialized [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) structure to display the **Print** common dialog box and collect the user data, as shown in the following code example.

    ```C++
    // Display the printer dialog and retrieve the printer DC
    pdReturn = PrintDlg(&pd);
    ```

    

3.  Save the fields from the [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) structure and start the print job.

    The [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) structure contains the data that describes the selections that the user made in the print dialog box. Some members of the **PRINTDLG** structure are handles to global memory objects. The [Print Sample Program](http://go.microsoft.com/?linkid=9737083) copies the data from the global memory objects to memory blocks that the program manages and copies other fields from the **PRINTDLG** structure to fields in a data structure that the program defined.

    After you store the data from the [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) structure in the program's data structure, you can open the print progress dialog box. The print progress dialog box procedure handles the dialog box messages and starts the print processing thread.

    The following code example shows how to copy the data from the [**PRINTDLG**](https://msdn.microsoft.com/library/windows/desktop/ms646843) structure to the program's data structure and how to start the print job.

    ```C++
    // A printer was returned so copy the information from 
    //  the dialog box structure and save it to the application's
    //  data structure.
    //
    //  Lock the handles to get pointers to the memory they refer to.
    PDEVMODE    devmode = (PDEVMODE)GlobalLock(pd.hDevMode);
    LPDEVNAMES  devnames = (LPDEVNAMES)GlobalLock(pd.hDevNames);

    // Free any old devmode structures and allocate a new one and
    // copy the data to the application's data structure.
    if (NULL != threadInfo->devmode)
    {
        HeapFree(GetProcessHeap(), 0L, threadInfo->devmode);
    }

    threadInfo->devmode = (LPDEVMODE)HeapAlloc(
        GetProcessHeap(), 
        PRINT_SAMPLE_HEAP_FLAGS, 
        devmode->dmSize);

    if (NULL != threadInfo->devmode) 
    {
        memcpy(
            (LPVOID)threadInfo->devmode,
            devmode, 
            devmode->dmSize);
    }
    else
    {
        // Unable to allocate a new structure so leave
        // the pointer as NULL to indicate that it's empty.
    }

    // Save the printer name from the devmode structure
    //  This is to make it easier to use. It could be
    //  used directly from the devmode structure.
    threadInfo->printerName = threadInfo->devmode->dmDeviceName;

    // Set the number of copies as entered by the user
    threadInfo->copies = pd.nCopies;

    // Some implementations might support printing more than
    // one package in a print job. For this program, only
    // one package (XPS document) can be printed per print job.
    threadInfo->packages = 1;

    // free allocated buffers from PRINTDLG structure
    if (NULL != pd.hDevMode) GlobalFree(pd.hDevMode);
    if (NULL != pd.hDevNames) GlobalFree(pd.hDevNames);

    // Display the print progress dialog box
    DialogBox(
        threadInfo->applicationInstance, 
        MAKEINTRESOURCE(IDD_PRINT_DLG), 
        hWnd, 
        PrintDlgProc);
    ```

    

4.  If the user clicks the **Cancel** button in the **Print** common dialog box, no further processing is performed.

 

 



