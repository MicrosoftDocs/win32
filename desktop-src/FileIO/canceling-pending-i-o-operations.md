---
description: Allowing users to cancel I/O requests that are slow or blocked can enhance the usability and robustness of your application.
ms.assetid: adfe6d05-f30b-40a1-b3b0-58e2593e7b25
title: Canceling Pending I/O Operations
ms.topic: article
ms.date: 05/31/2018
---

# Canceling Pending I/O Operations

Allowing users to cancel I/O requests that are slow or blocked can enhance the usability and robustness of your application. For example, if a call to the [OpenFile](/windows/win32/api/WinBase/nf-winbase-openfile) function is blocked because the call is to a very slow device, canceling it enables the call to be made again, with new parameters, without terminating the application.

Windows Vista extends the cancellation capabilities and includes support for canceling synchronous operations.

>[!NOTE]
>Calling the [CancelIoEx](cancelioex-func.md) function does not guarantee that an I/O operation will be canceled; the driver which is handling the operation must support cancellation and the operation must be in a state that can be canceled.

## Cancellation Considerations

When programming cancellation calls, keep in mind the following considerations:

- There is no guarantee that underlying drivers correctly support cancellation.
- When canceling asynchronous I/O, when no overlapped structure is supplied to the [CancelIoEx](cancelioex-func.md) function, the function attempts to cancel all outstanding I/O on the file on all threads in the process. Each thread is processed individually, so after a thread has been processed it may start another I/O on the file before all the other threads have had their I/O for the file canceled, causing synchronization issues.
- When canceling asynchronous I/O, do not reuse overlapped structures with targeted cancellation. Once the I/O operation completes (either successfully or with a canceled status) then the overlapped structure is no longer in use by the system and can be reused.
- When canceling synchronous I/O, calling the [CancelSynchronousIo](cancelsynchronousio-func.md) function attempts to cancel any current synchronous call on the thread. You must take care to ensure the synchronization of the calls is correct; the wrong call in a series of calls could get canceled. For example, if the **CancelSynchronousIo** function is called for a synchronous operation, X, operation Y only starts after that operation X is completed (normally or with an error). If the thread that called operation X then starts another synchronous call to X, the cancel call could interrupt this new I/O request.
- When canceling synchronous I/O, be aware that a race condition can exist whenever a thread is shared between different parts of an application, for example, with a thread-pool thread.

## Operations That Cannot Be Canceled

Some functions cannot be canceled using the [CancelIo](cancelio.md), [CancelIoEx](cancelioex-func.md), or [CancelSynchronousIo](cancelsynchronousio-func.md) function. Some of these functions have been extended to allow cancellation (for example, the [CopyFileEx](/windows/desktop/api/WinBase/nf-winbase-copyfileexa) function) and you should use these instead. In addition to supporting cancellation, these functions also have built-in callbacks to support you when tracking the progress of the operation. The following functions do not support cancellation:

- [CopyFile](/windows/win32/api/WinBase/nf-winbase-copyfile)—use [CopyFileEx](/windows/win32/api/WinBase/nf-winbase-copyfileexa)
- [MoveFile](/windows/win32/api/WinBase/nf-winbase-movefile)—use [MoveFileWithProgress](/windows/win32/api/WinBase/nf-winbase-movefilewithprogressa)
- [MoveFileEx](/windows/win32/api/WinBase/nf-winbase-movefileexa)—use [MoveFileWithProgress](/windows/win32/api/WinBase/nf-winbase-movefilewithprogressa)
- [ReplaceFile](/windows/win32/api/WinBase/nf-winbase-replacefilea)

For more information, see [I/O Completion/Cancellation Guidelines](/previous-versions/windows/hardware/design/dn613954(v=vs.85)).

## Canceling Asynchronous I/O

You can cancel asynchronous I/O from any thread in the process that issued the I/O operation. You must specify the handle which the I/O was performed on and, optionally, the overlapped structure that was used to perform the I/O. You can determine if the cancel occurred by examining the status returned in the overlapped structure or in the completion callback. A status of **ERROR\_OPERATION\_ABORTED** indicates that the operation was canceled.

The following example shows a routine that takes a timeout and attempts a read operation, canceling it with the [CancelIoEx](cancelioex-func.md) function if the timeout expires.

```C++
#include <windows.h>

BOOL DoCancelableRead(HANDLE hFile,
                 LPVOID lpBuffer,
                 DWORD nNumberOfBytesToRead,
                 LPDWORD lpNumberOfBytesRead,
                 LPOVERLAPPED lpOverlapped,
                 DWORD dwTimeout,
                 LPBOOL pbCancelCalled)
//
// Parameters:
//
//      hFile - An open handle to a readable file or device.
//
//      lpBuffer - A pointer to the buffer to store the data being read.
//
//      nNumberOfBytesToRead - The number of bytes to read from the file or 
//          device. Must be less than or equal to the actual size of
//          the buffer referenced by lpBuffer.
//
//      lpNumberOfBytesRead - A pointer to a DWORD to receive the number 
//          of bytes read after all I/O is complete or canceled.
//
//      lpOverlapped - A pointer to a preconfigured OVERLAPPED structure that
//          has a valid hEvent.
//          If the caller does not properly initialize this structure, this
//          routine will fail.
//
//      dwTimeout - The desired time-out, in milliseconds, for the I/O read.
//          After this time expires, the I/O is canceled.
// 
//      pbCancelCalled - A pointer to a Boolean to notify the caller if this
//          routine attempted to perform an I/O cancel.
//
// Return Value:
//
//      TRUE on success, FALSE on failure.
//
{
    BOOL result;
    DWORD waitTimer;
    BOOL bIoComplete = FALSE;
    const DWORD PollInterval = 100; // milliseconds

    // Initialize "out" parameters
    *pbCancelCalled = FALSE;
    *lpNumberOfBytesRead = 0;

    // Perform the I/O, in this case a read operation.
    result = ReadFile(hFile,
                  lpBuffer,
                  nNumberOfBytesToRead,
                  lpNumberOfBytesRead,
                  lpOverlapped );

    if (result == FALSE) 
    {
        if (GetLastError() != ERROR_IO_PENDING) 
        {
            // The function call failed. ToDo: Error logging and recovery.
            return FALSE; 
        }
    } 
    else 
    {
        // The I/O completed, done.
        return TRUE;
    }
        
    // The I/O is pending, so wait and see if the call times out.
    // If so, cancel the I/O using the CancelIoEx function.

    for (waitTimer = 0; waitTimer < dwTimeout; waitTimer += PollInterval)
    {
        result = GetOverlappedResult( hFile, lpOverlapped, lpNumberOfBytesRead, FALSE );
        if (result == FALSE)
        {
            if (GetLastError() != ERROR_IO_PENDING)
            {
                // The function call failed. ToDo: Error logging and recovery.
                return FALSE;
            }
            Sleep(PollInterval);
        }
        else
        {
            bIoComplete = TRUE;
            break;
        }
    }

    if (bIoComplete == FALSE) 
    {
        result = CancelIoEx( hFile, lpOverlapped );
        
        *pbCancelCalled = TRUE;

        if (result == TRUE || GetLastError() != ERROR_NOT_FOUND) 
        {
            // Wait for the I/O subsystem to acknowledge our cancellation.
            // Depending on the timing of the calls, the I/O might complete with a
            // cancellation status, or it might complete normally (if the ReadFile was
            // in the process of completing at the time CancelIoEx was called, or if
            // the device does not support cancellation).
            // This call specifies TRUE for the bWait parameter, which will block
            // until the I/O either completes or is canceled, thus resuming execution, 
            // provided the underlying device driver and associated hardware are functioning 
            // properly. If there is a problem with the driver it is better to stop 
            // responding here than to try to continue while masking the problem.

            result = GetOverlappedResult( hFile, lpOverlapped, lpNumberOfBytesRead, TRUE );

            // ToDo: check result and log errors. 
        }
    }

    return result;
}
```

## Canceling Synchronous I/O

You can cancel synchronous I/O from any thread in the process that issued the I/O operation. You must specify the handle to the thread which is currently performing the I/O operation.

The following example shows two routines:

- The **SynchronousIoWorker** function is a worker thread that implements some synchronous file I/O, starting with a call to the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function. If the routine is successful, the routine can be followed by additional operations, which are not included here. The global variable *gCompletionStatus* can be used to determine whether all operations succeeded or whether an operation failed or was canceled. The global variable *dwOperationInProgress* indicates whether file I/O is still in progress.

    >[!NOTE]
    >In this example, the UI thread could also check for the existence of the worker thread.

    Additional manual checks, which are not included here, are required in the **SynchronousIoWorker** function is to ensure that if the cancellation was requested during the brief periods between file I/O calls, the rest of the operations will be canceled.

- The **MainUIThreadMessageHandler** function simulates the message handler within a UI thread's window procedure. The user requests a set of synchronous file operations by clicking a control, which generates a user-defined window message, (in the section marked by **WM\_MYSYNCOPS**). This creates a new thread using the **CreateFileThread** function, which then starts the **SynchronousIoWorker** function is. The UI thread continues to process messages while the worker thread performs the requested I/O. If the user decides to cancel the unfinished operations (typically by clicking a cancel button), the routine (in the section marked by **WM\_MYCANCEL**) calls the [CancelSynchronousIo](cancelsynchronousio-func.md) function using the thread handle returned by the **CreateFileThread** function. The **CancelSynchronousIo** function returns immediately after the cancellation attempt. Finally, the user or application may later request some other operation that depends on whether the file operations have completed. In this case, the routine (in the section marked by **WM\_PROCESSDATA**) first verifies that the operations have completed and then executes the clean-up operations.

    >[!NOTE]
    >In this example, since the cancellation could have occurred anywhere in the sequence of operations, it may be necessary for the caller to ensure that the state is consistent, or at least understood, before proceeding.

```C++
// User-defined codes for the message-pump, which is outside the scope 
// of this sample. Windows messaging and message pumps are well-documented
// elsewhere.
#define WM_MYSYNCOPS    1
#define WM_MYCANCEL     2
#define WM_PROCESSDATA  3

VOID SynchronousIoWorker( VOID *pv )
{
    LPCSTR lpFileName = (LPCSTR)pv;
    HANDLE hFile;
    g_dwOperationInProgress = TRUE;    
    g_CompletionStatus = ERROR_SUCCESS;
     
    hFile = CreateFileA(lpFileName,
                        GENERIC_READ,
                        0,
                        NULL,
                        OPEN_EXISTING,
                        0,
                        NULL);


    if (hFile != INVALID_HANDLE_VALUE) 
    {
        BOOL result = TRUE;
        // TODO: CreateFile succeeded. 
        // Insert your code to make more synchronous calls with hFile.
        // The result variable is assumed to act as the error flag here,
        // but can be whatever your code needs.
        
        if (result == FALSE) 
        {
            // An operation failed or was canceled. If it was canceled,
            // GetLastError() returns ERROR_OPERATION_ABORTED.

            g_CompletionStatus = GetLastError();            
        }
             
        CloseHandle(hFile);
    } 
    else 
    {
        // CreateFile failed or was canceled. If it was canceled,
        // GetLastError() returns ERROR_OPERATION_ABORTED.
        g_CompletionStatus = GetLastError();
    }

    g_dwOperationInProgress = FALSE;
}  

LRESULT
CALLBACK
MainUIThreadMessageHandler(HWND hwnd,
                           UINT uMsg,
                           WPARAM wParam,
                           LPARAM lParam)
{
    UNREFERENCED_PARAMETER(hwnd);
    UNREFERENCED_PARAMETER(wParam);
    UNREFERENCED_PARAMETER(lParam);
    HANDLE syncThread = INVALID_HANDLE_VALUE;

    //  Insert your initializations here.

    switch (uMsg) 
    {
        // User requested an operation on a file.  Insert your code to 
        // retrieve filename from parameters.
        case WM_MYSYNCOPS:    
            syncThread = CreateThread(
                          NULL,
                          0,
                          (LPTHREAD_START_ROUTINE)SynchronousIoWorker,
                          &g_lpFileName,
                          0,
                          NULL);

            if (syncThread == INVALID_HANDLE_VALUE) 
            {
                // Insert your code to handle the failure.
            }
        break;
    
        // User clicked a cancel button.
        case WM_MYCANCEL:
            if (syncThread != INVALID_HANDLE_VALUE) 
            {
                CancelSynchronousIo(syncThread);
            }
        break;

        // User requested other operations.
        case WM_PROCESSDATA:
            if (!g_dwOperationInProgress) 
            {
                if (g_CompletionStatus == ERROR_OPERATION_ABORTED) 
                {
                    // Insert your cleanup code here.
                } 
                else
                {
                    // Insert code to handle other cases.
                }
            }
        break;
    } 

    return TRUE;
} 
```

## Related topics

[Synchronous and Asynchronous I/O](synchronous-and-asynchronous-i-o.md)
