---
description: This topic describes how to display the print job progress to the user and give them the option to cancel a print job that is currently in progress.
ms.assetid: 2b7a0ab7-bf7e-473d-ab43-8b79478d4453
title: 'How To: Display the Print Job Progress'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Display the Print Job Progress

This topic describes how to display the print job progress to the user and give them the option to cancel a print job that is currently in progress.

## Overview

A print progress dialog procedure typically performs the following functions.

-   Display print job progress to the user.
-   Start the print processing thread.
-   Display a **Cancel** button so the user can stop a print job before it finishes.

Strictly speaking, the only thing that the print progress dialog box procedure must do is display the print job progress to the user. However, because the other two functions in the preceding list are closely related, they have also been included in this module.

## Displaying Print Job Progress

A print progress dialog box procedure handles the following window messages.

-   **WM\_INITDIALOG**

    Initializes the controls that the dialog box uses.

-   **WM\_SETCURSOR**

    Sets the cursor to a pointer when the user is able to cancel a print job, and to the wait cursor when the print job is at a point where it cannot be cancelled.

-   **USER\_PRINT\_START\_PRINTING**

    Sets the progress bar parameters for the print job, and creates the printing thread to start processing the print job.

    This is an application-specific window message.

-   **WM\_COMMAND - IDCANCEL**

    Sets the cancel event to tell the print processing thread to cancel the print job.

-   **USER\_PRINT\_STATUS\_UPDATE**

    Updates the progress bar and status text to show the current state of the print job.

    This is an application-specific window message.

-   **USER\_PRINT\_CLOSING**

    Sets the closing status text in the progress dialog box to indicate that the print job is closing.

    This is an application-specific window message.

-   **USER\_PRINT\_COMPLETE**

    Displays the "Print job complete" message to the user, and releases handles and events that were used in this print job.

    This is an application-specific window message.

 

 



