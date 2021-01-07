---
description: This section describes how to print from a native Windows program.
ms.assetid: D0AE8FF8-D02D-43D3-80CA-E13EAA894F87
title: 'How To: Print from a Windows Program'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Print from a Windows Program

This section describes how to print from a native Windows program.

## Overview

Printing is usually an integral part of a native Windows program. Therefore, it is not a feature that you can add easily after you have written the program. That being said, if the program is designed to use XPS documents it will not need much, if any, additional code to render the document content for printing. The XPS documents of the application can be sent directly to a printer that has an XPSDrv printer driver.

Use the [XPS Document API](/previous-versions/windows/desktop/dd316976(v=vs.85)) to create the document content and the [XPS Print API](xps-printing.md) to send the document content to the printer. The XPS Print API processes the document content for the destination printer. If the selected printer has an XPSDrv printer driver, the document will be sent to the printer without any additional conversion. If the selected printer has a GDI-based printer driver, the program can also send the content to the printer, and the XPS Print API converts the document content so that it will be compatible with the GDI-based printer driver. In either case, the processing that the application performs is the same.

## Printing tasks

The following topics describe the basic steps of printing program content.

1.  **Collect print job information from user.**

    Typically, a user initiates a print job when they select the print option from a menu and the program displays a print dialog box to collect the details of the print job. The user typically selects the printer, the number of copies, and printer configuration details such as two-sided printing and stapling.

    For information about how to do this, see [How To: Collect Print Job Information from the User](preparing-to-print.md).

2.  **Create progress indicator.**

    A progress indicator provides the user with feedback about how the print job is progressing. The progress indicator can be a progress bar that is part of a dialog box that includes the **Cancel** button for the job, or it can be a progress bar in the status bar at the bottom of the main window.

    For information about the progress indicator works, see [How To: Display the Print Job Progress](cancel-dialog-box.md).

    For more ideas about how to display the progress of the print job, see the information in the [Windows Application UI Development](/windows/desktop/windows-application-ui-development) guidelines.

3.  **Start the printing thread.**

    After the program has collected the print job information from the user, it can start the printing thread to perform the actual processing of the document for printing.

    For information about the printing thread, see [How To: Start and Stop a Printing Thread](how-to--start-and-stop-a-printing-thread.md).

4.  **Render print job data.**

    The printing thread renders the document data for printing. You should break down this processing into discrete processing steps so that the user can interrupt the processing and cancel the job as well as to not allow the processing thread to block other threads and processes.

    For information about how the renders the print job data, see [How To: Render Print Job Data](how-to--render-the-print-job-data.md).

5.  **Monitor print job progress.**

    As each processing step is performed, update the progress bar to inform the use. Compute the processing steps to complete the requested job and then updates the progress bar as those steps are performed.

6.  **Close print job and terminate printing thread.**

    After the program has sent the print job to the printer, or if the user has cancelled the print job, you must close the print job and release the resources used by the print job.

## Related topics

<dl> <dt>

[How To: Collect Print Job Information from the User](preparing-to-print.md)
</dt> </dl>

 

 
