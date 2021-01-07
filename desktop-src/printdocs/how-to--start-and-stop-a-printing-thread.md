---
description: This topic describes how to start and stop the print job processing thread.
ms.assetid: CA3A81D6-332F-4867-881F-AC6859A076CF
title: 'How To: Start and Stop a Printing Thread'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Start and Stop a Printing Thread

This topic describes how to start and stop the print job processing thread.

## Overview

To prevent printing activities from blocking the user interface response, create a separate thread to process the print job. The thread that is started when the program is started, is the thread that handles the window messages that result from user interaction, and is therefore the UI thread. The program must process these messages without delay for the user interface to respond to the user's mouse and keyboard input in a timely manner. For the program to be able to respond to these messages quickly, the amount of processing that can be performed during any one message is limited. When a user request requires extensive processing, a different thread must perform that processing to allow subsequent user interaction to be handled by the program.

Processing data in a separate thread requires the program to coordinate the operation of user interface thread and the processing thread. For example, while the processing thread is processing the data, the main thread must not alter that data. One way to manage this is through thread-safe synchronization objects such as semaphores, events, and mutexes.

At the same time, some user interaction must be prevented while the processing thread is running. In the sample program, the application data is protected and the user interaction is limited by having the print job processing be managed by the modal progress dialog box. A modal dialog box prevents the user from interacting with the program's main window, which prevents the user from altering the application program data while the data is printed.

The only action the user can perform while a print job is processing is to cancel the print job. This restriction is signaled to the user by the cursor shape. When the cursor is over the **Cancel** button, an arrow cursor is displayed, which indicates that the user can click this button. When the cursor is over any other part of the program's window area, a wait cursor is displayed, which indicates that the program is busy and cannot respond to user input.

## Creating the Printing Thread Procedure

We recommend including these features while print processing.

-   **Print processing is divided into steps**

    You can divide the print processing into discrete processing steps that you can interrupt if the user clicks the **Cancel** button. This is useful because print processing can include processor-intensive operations. Breaking this processing into steps can prevent the print processing from blocking or delaying other threads or processes. Breaking the processing into logical steps also makes it possible to cleanly terminate the print processing at any point, so that ending a print job before it has finished will not leave any orphaned resources.

    This is an example list of print steps.

    ```C++
    HRESULT PrintStep_1_StartJob (PPRINTTHREADINFO threadInfo);
    HRESULT PrintStep_2_DoOnePackage (PPRINTTHREADINFO threadInfo);
    HRESULT PrintStep_3_DoOneDoc (PPRINTTHREADINFO threadInfo);
    HRESULT PrintStep_4_DoOnePage (PPRINTTHREADINFO threadInfo);
    HRESULT PrintStep_5_ClosePackage (PPRINTTHREADINFO threadInfo);
    HRESULT PrintStep_6_CloseJob (PPRINTTHREADINFO threadInfo);
    ```

    

-   **Check for a cancel event between steps**

    When the user clicks the **Cancel** button, the user interface thread signals the cancel event. The processing thread must check the cancel event periodically to know when a user clicked the **Cancel** button. The [**WaitForSingleObject**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject) statements perform this check and they also give other programs a chance to run so that the print job processing doesn't block or delay other threads or processes.

    The following code example illustrates one of the tests to see whether the cancel event has occurred.

    ```C++
    waitStatus = WaitForSingleObject (
                    threadInfo->quitEvent, 
                    stepDelay);
    if (WAIT_OBJECT_0 == waitStatus)
    {
        hr = E_ABORT;
    }
    ```

    

-   **Send status updates to user interface thread**

    As each print processing step, the print processing thread sends update messages to the print progress dialog box so that it can update the progress bar. Note that the print progress dialog box is running in the UI thread.

    The following code example illustrates one of the update message calls.

    ```C++
    // Update print status
    PostMessage (
        threadInfo->parentWindow, 
        USER_PRINT_STATUS_UPDATE, 
        0L, 
        0L);
    ```

    

## Starting the Printing Thread

The print processing thread runs until the PrintThreadProc function returns. The following steps start the printing thread.

1.  **Prepare the data and user interface elements for printing.**

    Before starting the print processing thread, you must initialize the data elements that describe the print job and the user interface elements. These elements include the cursor state, so that the wait cursor will be displayed appropriately. You must also configure the progress bar to reflect the size of the print job. These preparation steps are described in detail in [How To: Collect Print Job Information from the User](preparing-to-print.md).

    The following code example shows how to configure the progress bar to reflect the size of the print job that the user requested.

    ```C++
    // Compute the number of steps in this job.
    stepCount = (((
                // One copy of a document contains
                //  one step for each page +
                //  one step for the document
                ((threadInfo->documentContent)->pages + 1) * 
                // Each copy of the document includes
                //  two steps to open and close the document
                threadInfo->copies) + 2) * 
                // Each job includes one step to start the job
                threadInfo->packages) + 1;
    // Send the total number of steps to the progress bar control.
    SendMessage (
        dlgInfo->progressBarWindow, 
        PBM_SETRANGE32, 
        0L, 
        (stepCount));
    ```

    

2.  **Start the print processing thread.**

    Call [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread) to start the processing thread.

    The following code example starts the processing thread.

    ```C++
    // Start the printing thread
    threadInfo->printThreadHandle = CreateThread (
                    NULL, 
                    0L, 
                    (LPTHREAD_START_ROUTINE)PrintThreadProc,
                    (LPVOID)threadInfo, 
                    0L, 
                    &threadInfo->printThreadId);
    ```

    

3.  **Check whether print processing failed on start.**

    [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread) returns a handle to the created thread if the thread was created successfully. The PrintThreadProc function that was started in the new thread checks some conditions before it starts the actual print job processing. If it detects any errors in these checks, PrintThreadProc could return without processing any print job data. The UI thread can check whether the processing thread started successfully by waiting on the thread handle for a period of time that is longer than it takes to perform the initial tests but no longer than necessary. When the thread exits, the handle to the thread becomes signaled. The code checks the thread's state for a short period of time after it starts the processing thread. The [**WaitForSingleObject**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject) function returns when either the timeout occurs or the thread handle is signaled. If the **WaitForSingleObject** function returns a **WAIT\_OBJECT\_0** status, the thread exited early and so you should close the print progress dialog, as the following code example shows.

    ```C++
    // Make sure the printing thread started OK
    //  by waiting to see if it is still running after
    //  a short period of time. This time delay should be
    //  long enough to know that it's running but shorter
    //  than the shortest possible print job.
    waitStatus = WaitForSingleObject (
        threadInfo->printThreadHandle, 
        THREAD_START_WAIT);

    // If the object is signaled, that means that the
    //  thread terminated before the timeout period elapsed.
    if (WAIT_OBJECT_0 == waitStatus)
    {
        // The thread exited, so post close messages.
        PostMessage (hDlg, USER_PRINT_CLOSING, 0L, (LPARAM)E_FAIL);
        PostMessage (hDlg, USER_PRINT_COMPLETE, 0L, (LPARAM)E_FAIL);
    }
    ```

    

## Stopping the Printing Thread

When the user clicks the **Cancel** button in the print progress dialog box, the printing thread is notified so that it can stop processing the print job in an orderly manner. While the **Cancel** button and the **quitEvent** event are important aspects of this processing, you must design the entire processing sequence to be interrupted successfully. This means that the steps in the sequence must not leave any allocated resources that are not freed if a user cancels the sequence before it had completed.

The following code example shows how the sample program checks the **quitEvent** before it processes each page in the document being printed. If the **quitEvent** is signaled or an error was detected, print processing stops.


```C++
// While no errors and the user hasn't clicked cancel...
while (((waitStatus = WaitForSingleObject (
                        threadInfo->quitEvent, 
                        stepDelay)) == WAIT_TIMEOUT) &&
        SUCCEEDED(hr))
{
    // ...print one page
    hr = PrintStep_4_DoOnePage (threadInfo);

    // Update print status
    PostMessage (
        threadInfo->parentWindow, 
        USER_PRINT_STATUS_UPDATE, 
        0L, 
        0L);
    

    if (threadInfo->currentPage < (threadInfo->documentContent)->pages)
    {
        // More pages, so continue to the next one
        threadInfo->currentPage++;
    }
    else
    {
        // Last page printed so exit loop and close
        break;
    }
}
```



 

 
