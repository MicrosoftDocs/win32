---
title: Asynchronous Example Application
description: The following example demonstrated sending a request asynchronously.
ms.assetid: 1dd32e17-88bb-4729-80f6-f4f1184788d5
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Example Application

The following example demonstrated sending a request asynchronously.


```C++
 /*++
 Copyright (C) Microsoft.  All Rights Reserved.

--*/

#include "async.h"

#pragma warning(disable:4127) // Conditional expression is constant


int __cdecl 
wmain(
    __in int argc,
    __in_ecount(argc) LPWSTR *argv
    )
{
    DWORD Error;
    DWORD OpenType = INTERNET_OPEN_TYPE_PRECONFIG; // Use pre-configured options as default

    CONFIGURATION Configuration = {0};

    PREQUEST_CONTEXT ReqContext = NULL;
    HINTERNET SessionHandle = NULL;

    // Callback function
    INTERNET_STATUS_CALLBACK CallbackPointer;


    // Parse the command line arguments
    Error = ParseArguments(argc, argv, &Configuration);
    if(Error != ERROR_SUCCESS)
    {
        ShowUsage();
        goto Exit; 
    }

    if(Configuration.UseProxy)
    {
        OpenType = INTERNET_OPEN_TYPE_PROXY;
    }
    
    // Create Session handle and specify async Mode
    SessionHandle = InternetOpen(L"WinInet HTTP Async Sample",  // User Agent
                                 OpenType,                      // Preconfig or Proxy
                                 Configuration.ProxyName,       // Proxy name
                                 NULL,                          // Proxy bypass, do not bypass any address
                                 INTERNET_FLAG_ASYNC);          // 0 for Synchronous
    
    if (SessionHandle == NULL)
    {
        LogInetError(GetLastError(), L"InternetOpen");
        goto Exit;
    }


    // Set the status callback for the handle to the Callback function
    CallbackPointer = InternetSetStatusCallback(SessionHandle, 
                                                (INTERNET_STATUS_CALLBACK)CallBack);

    if (CallbackPointer == INTERNET_INVALID_STATUS_CALLBACK)
    {
        fprintf(stderr, "InternetSetStatusCallback failed with INTERNET_INVALID_STATUS_CALLBACK\n");
        goto Exit;
    }


    
    // Initialize the ReqContext to be used in the asynchronous calls
    Error = AllocateAndInitializeRequestContext(SessionHandle,
                                                &Configuration,
                                                &ReqContext);
    if (Error != ERROR_SUCCESS)
    {
        fprintf(stderr, "AllocateAndInitializeRequestContext failed with error %d\n", Error);
        goto Exit;
    }

    //
    // Send out request and receive response
    //
    
    ProcessRequest(ReqContext, ERROR_SUCCESS);


    //
    // Wait for request completion or timeout
    //

    WaitForRequestCompletion(ReqContext, Configuration.UserTimeout);
    

Exit:

    // Clean up the allocated resources
    CleanUpRequestContext(ReqContext);

    CleanUpSessionHandle(SessionHandle);

    return (Error != ERROR_SUCCESS) ? 1 : 0;
}

VOID CALLBACK 
CallBack(
    __in HINTERNET hInternet,
    __in DWORD_PTR dwContext,
    __in DWORD dwInternetStatus,
    __in_bcount(dwStatusInformationLength) LPVOID lpvStatusInformation,
    __in DWORD dwStatusInformationLength
    )
/*++

Routine Description:
    Callback routine for asynchronous WinInet operations

Arguments:
     hInternet - The handle for which the callback function is called.
     dwContext - Pointer to the application defined context.
     dwInternetStatus - Status code indicating why the callback is called.
     lpvStatusInformation - Pointer to a buffer holding callback specific data.
     dwStatusInformationLength - Specifies size of lpvStatusInformation buffer.

Return Value:
    None.

--*/
{
    InternetCookieHistory cookieHistory;
    PREQUEST_CONTEXT ReqContext = (PREQUEST_CONTEXT)dwContext;
 
    UNREFERENCED_PARAMETER(dwStatusInformationLength);

    fprintf(stderr, "Callback Received for Handle %p \t", hInternet);
    
    switch(dwInternetStatus)
    {
        case INTERNET_STATUS_COOKIE_SENT:
            fprintf(stderr, "Status: Cookie found and will be sent with request\n");
            break;
            
        case INTERNET_STATUS_COOKIE_RECEIVED:
            fprintf(stderr, "Status: Cookie Received\n");
            break;
            
        case INTERNET_STATUS_COOKIE_HISTORY:

            fprintf(stderr, "Status: Cookie History\n");

            ASYNC_ASSERT(lpvStatusInformation);
            ASYNC_ASSERT(dwStatusInformationLength == sizeof(InternetCookieHistory));

            cookieHistory = *((InternetCookieHistory*)lpvStatusInformation);
            
            if(cookieHistory.fAccepted)
            {
                fprintf(stderr, "Cookie Accepted\n");
            }
            if(cookieHistory.fLeashed)
            {
                fprintf(stderr, "Cookie Leashed\n");
            }        
            if(cookieHistory.fDowngraded)
            {
                fprintf(stderr, "Cookie Downgraded\n");
            }        
            if(cookieHistory.fRejected)
            {
                fprintf(stderr, "Cookie Rejected\n");
            }

 
            break;
            
        case INTERNET_STATUS_CLOSING_CONNECTION:
            fprintf(stderr, "Status: Closing Connection\n");
            break;
            
        case INTERNET_STATUS_CONNECTED_TO_SERVER:
            fprintf(stderr, "Status: Connected to Server\n");
            break;
            
        case INTERNET_STATUS_CONNECTING_TO_SERVER:
            fprintf(stderr, "Status: Connecting to Server\n");
            break;
            
        case INTERNET_STATUS_CONNECTION_CLOSED:
            fprintf(stderr, "Status: Connection Closed\n");
            break;
            
        case INTERNET_STATUS_HANDLE_CLOSING:
            fprintf(stderr, "Status: Handle Closing\n");

            //
            // Signal the cleanup routine that it is
            // safe to cleanup the request context
            //
            
            ASYNC_ASSERT(ReqContext);
            SetEvent(ReqContext->CleanUpEvent);
            
            break;
            
        case INTERNET_STATUS_HANDLE_CREATED:
            ASYNC_ASSERT(lpvStatusInformation);
            fprintf(stderr,
                    "Handle %x created\n", 
                    ((LPINTERNET_ASYNC_RESULT)lpvStatusInformation)->dwResult);

            break;
            
        case INTERNET_STATUS_INTERMEDIATE_RESPONSE:
            fprintf(stderr, "Status: Intermediate response\n");
            break;
            
        case INTERNET_STATUS_RECEIVING_RESPONSE:
            fprintf(stderr, "Status: Receiving Response\n");    
            break;
            
        case INTERNET_STATUS_RESPONSE_RECEIVED:
            ASYNC_ASSERT(lpvStatusInformation);
            ASYNC_ASSERT(dwStatusInformationLength == sizeof(DWORD));
            
            fprintf(stderr, "Status: Response Received (%d Bytes)\n", *((LPDWORD)lpvStatusInformation));
            
            break;
            
        case INTERNET_STATUS_REDIRECT:
            fprintf(stderr, "Status: Redirect\n");
            break;

        case INTERNET_STATUS_REQUEST_COMPLETE:
            fprintf(stderr, "Status: Request complete\n");

            ASYNC_ASSERT(lpvStatusInformation);
            
            ProcessRequest(ReqContext, ((LPINTERNET_ASYNC_RESULT)lpvStatusInformation)->dwError);

            break;
            
        case INTERNET_STATUS_REQUEST_SENT:
            ASYNC_ASSERT(lpvStatusInformation);
            ASYNC_ASSERT(dwStatusInformationLength == sizeof(DWORD));

            fprintf(stderr,"Status: Request sent (%d Bytes)\n", *((LPDWORD)lpvStatusInformation));
            break;
            
        case INTERNET_STATUS_DETECTING_PROXY:
            fprintf(stderr, "Status: Detecting Proxy\n");
            break;            
            
        case INTERNET_STATUS_RESOLVING_NAME:
            fprintf(stderr, "Status: Resolving Name\n");
            break;
            
        case INTERNET_STATUS_NAME_RESOLVED:
            fprintf(stderr, "Status: Name Resolved\n");
            break;
            
        case INTERNET_STATUS_SENDING_REQUEST:
            fprintf(stderr, "Status: Sending request\n");
            break;
            
        case INTERNET_STATUS_STATE_CHANGE:
            fprintf(stderr, "Status: State Change\n");
            break;
            
        case INTERNET_STATUS_P3P_HEADER:
            fprintf(stderr, "Status: Received P3P header\n");
            break;
            
        default:
            fprintf(stderr, "Status: Unknown (%d)\n", dwInternetStatus);
            break;
    }

    return;
}


VOID
ProcessRequest(
    __inout PREQUEST_CONTEXT ReqContext,
    __in DWORD Error
    )
/*++

Routine Description:
    Process the request context - Sending the request and
    receiving the response

Arguments:
    ReqContext - Pointer to request context structure
    Error - error returned from last asynchronous call

Return Value:
    None.

--*/
{
    BOOL Eof = FALSE;
    
    ASYNC_ASSERT(ReqContext);

    
    while(Error == ERROR_SUCCESS && ReqContext->State != REQ_STATE_COMPLETE)
    {
        
        switch(ReqContext->State)
        {
            case REQ_STATE_SEND_REQ:

                ReqContext->State = REQ_STATE_RESPONSE_RECV_DATA;
                Error = SendRequest(ReqContext);
                
                break;

            case REQ_STATE_SEND_REQ_WITH_BODY: 
                
                ReqContext->State = REQ_STATE_POST_GET_DATA;
                Error = SendRequestWithBody(ReqContext);                

                break;
                
            case REQ_STATE_POST_GET_DATA:
                
                ReqContext->State = REQ_STATE_POST_SEND_DATA;
                Error = GetDataToPost(ReqContext);
                
                break;
                
            case REQ_STATE_POST_SEND_DATA:
                
                ReqContext->State = REQ_STATE_POST_GET_DATA;
                Error = PostDataToServer(ReqContext, &Eof);
                
                if(Eof)
                {
                    ASYNC_ASSERT(Error == ERROR_SUCCESS);
                    ReqContext->State = REQ_STATE_POST_COMPLETE;  
                }
                
                break;
                
            case REQ_STATE_POST_COMPLETE:     
                
                ReqContext->State = REQ_STATE_RESPONSE_RECV_DATA;
                Error = CompleteRequest(ReqContext);
                
                break;                
                
            case REQ_STATE_RESPONSE_RECV_DATA: 
                
                ReqContext->State = REQ_STATE_RESPONSE_WRITE_DATA;
                Error = RecvResponseData(ReqContext);
                
                break;
                
            case REQ_STATE_RESPONSE_WRITE_DATA:

                ReqContext->State = REQ_STATE_RESPONSE_RECV_DATA;
                Error = WriteResponseData(ReqContext, &Eof);

                if(Eof)
                {
                    ASYNC_ASSERT(Error == ERROR_SUCCESS);
                    ReqContext->State = REQ_STATE_COMPLETE;
                }
                
                break;
                
            default:
                
                ASYNC_ASSERT(FALSE);
                
                break;
        }
    }

    if(Error != ERROR_IO_PENDING)
    {
        //
        // Everything has been procesed or has failed. 
        // In either case, the signal processing has
        // completed
        //
        
        SetEvent(ReqContext->CompletionEvent);
    }

    return;
}

DWORD
SendRequest(
    __in PREQUEST_CONTEXT ReqContext
    )
/*++

Routine Description:
    Send the request using HttpSendRequest

Arguments:
    ReqContext - Pointer to request context structure

Return Value:
    Error code for the operation.

--*/
{
    BOOL Success;
    DWORD Error = ERROR_SUCCESS;
    

    ASYNC_ASSERT(ReqContext->Method == METHOD_GET);

    Success = AcquireRequestHandle(ReqContext);
    if(!Success)
    {
        Error = ERROR_OPERATION_ABORTED;
        goto Exit;
    }
    
    Success = HttpSendRequest(ReqContext->RequestHandle,
                              NULL,                   // do not provide additional Headers
                              0,                      // dwHeadersLength 
                              NULL,                   // Do not send any data 
                              0);                     // dwOptionalLength 

    ReleaseRequestHandle(ReqContext);

    if (!Success)
    {
        Error = GetLastError();

        if(Error != ERROR_IO_PENDING)
        {
            LogInetError(Error, L"HttpSendRequest");
        }
        goto Exit;
    }

Exit:

    return Error;
}


DWORD
SendRequestWithBody(
    __in PREQUEST_CONTEXT ReqContext
    )
/*++

Routine Description:
    Send the request with entity-body using HttpSendRequestEx

Arguments:
    ReqContext - Pointer to request context structure

Return Value:
    Error code for the operation.

--*/
{
    BOOL Success;
    INTERNET_BUFFERS BuffersIn;    
    DWORD Error = ERROR_SUCCESS;
    
    //
    // HttpSendRequest can also be used also to post data to a server, 
    // to do so, the data should be provided using the lpOptional
    // parameter and it's size on dwOptionalLength.
    // Here we decided to depict the use of HttpSendRequestEx function.
    //
    

    ASYNC_ASSERT(ReqContext->Method == METHOD_POST);
    
    //Prepare the Buffers to be passed to HttpSendRequestEx
    ZeroMemory(&BuffersIn, sizeof(INTERNET_BUFFERS));
    BuffersIn.dwStructSize = sizeof(INTERNET_BUFFERS);
    BuffersIn.lpvBuffer = NULL;
    BuffersIn.dwBufferLength = 0;
    BuffersIn.dwBufferTotal = ReqContext->FileSize; // content-length of data to post


    Success = AcquireRequestHandle(ReqContext);
    if(!Success)
    {
        Error = ERROR_OPERATION_ABORTED;
        goto Exit;
    }
    
    Success = HttpSendRequestEx(ReqContext->RequestHandle,
                                &BuffersIn,
                                NULL,                 // Do not use output buffers
                                0,                    // dwFlags reserved
                                (DWORD_PTR)ReqContext);

    ReleaseRequestHandle(ReqContext);

    if (!Success)
    {
        Error = GetLastError();

        if(Error != ERROR_IO_PENDING)
        {
            LogInetError(Error, L"HttpSendRequestEx");
        }
        
        goto Exit;
    }
    
Exit:    

    return Error;
}

DWORD 
GetDataToPost(
    __inout PREQUEST_CONTEXT ReqContext
    )
/*++

Routine Description:
    Reads data from a file

Arguments:
    ReqContext - Pointer to request context structure

Return Value:
    Error code for the operation.

--*/
{
    DWORD Error = ERROR_SUCCESS;
    BOOL Success;


    //
    //
    // ReadFile is done inline here assuming that it will return quickly
    // I.E. the file is on disk
    //
    // If you plan to do blocking/intensive operations they should be
    // queued to another thread and not block the callback thread
    //
    //

    Success = ReadFile(ReqContext->UploadFile,
                       ReqContext->OutputBuffer,
                       BUFFER_LEN,
                       &ReqContext->ReadBytes,
                       NULL);
    if(!Success)
    {
        Error = GetLastError();
        LogSysError(Error, L"ReadFile");
        goto Exit;
    }

    
Exit:    
 
    return Error;
}

DWORD 
PostDataToServer(
    __inout PREQUEST_CONTEXT ReqContext,
    __out PBOOL Eof
    )
/*++

Routine Description:
    Post data in the http request

Arguments:
    ReqContext - Pointer to request context structure
    Eof - Done posting data to server

Return Value:
    Error code for the operation.

--*/
{
    DWORD Error = ERROR_SUCCESS;
    BOOL Success;

    *Eof = FALSE;

    if(ReqContext->ReadBytes == 0)
    {
        *Eof = TRUE;
        goto Exit;
    }

        
    Success = AcquireRequestHandle(ReqContext);
    if(!Success)
    {
        Error = ERROR_OPERATION_ABORTED;
        goto Exit;
    }


    //
    // The lpdwNumberOfBytesWritten parameter will be
    // populated on async completion, so it must exist
    // until INTERNET_STATUS_REQUEST_COMPLETE.
    // The same is true of lpBuffer parameter.
    //

    Success = InternetWriteFile(ReqContext->RequestHandle,
                                ReqContext->OutputBuffer,
                                ReqContext->ReadBytes,
                                &ReqContext->WrittenBytes);
    

    ReleaseRequestHandle(ReqContext);
    
    if(!Success)
    {
        Error = GetLastError();
        
        if(Error == ERROR_IO_PENDING)
        {
            fprintf(stderr, "Waiting for InternetWriteFile to complete\n");                
        }
        else
        {
            LogInetError(Error, L"InternetWriteFile");
        }
        
        goto Exit;
        
    }
 
    

Exit:
    
 
    return Error;
}


DWORD 
CompleteRequest(
    __inout PREQUEST_CONTEXT ReqContext
    )
/*++

Routine Description:
    Perform completion of asynchronous post.

Arguments:
    ReqContext - Pointer to request context structure

Return Value:
    Error Code for the operation.

--*/
{

    DWORD Error = ERROR_SUCCESS;
    BOOL Success;

    fprintf(stderr, "Finished posting file\n");
    
    Success = AcquireRequestHandle(ReqContext);
    if(!Success)
    {
        Error = ERROR_OPERATION_ABORTED;
        goto Exit;
    }   

    Success = HttpEndRequest(ReqContext->RequestHandle, NULL, 0, 0);

    ReleaseRequestHandle(ReqContext);
    
    if(!Success)
    {
        Error = GetLastError();
        if(Error == ERROR_IO_PENDING)
        {
            fprintf(stderr, "Waiting for HttpEndRequest to complete \n");
        }
        else
        {
            LogInetError(Error, L"HttpEndRequest");
            goto Exit;
        }
    }

Exit:
    
    return Error;
}



DWORD
RecvResponseData(
    __inout PREQUEST_CONTEXT ReqContext
    )
/*++

Routine Description:
     Receive response

Arguments:
     ReqContext - Pointer to request context structure

Return Value:
     Error Code for the operation.

--*/
{
    DWORD Error = ERROR_SUCCESS;
    BOOL Success;

 

            
    Success = AcquireRequestHandle(ReqContext);
    if(!Success)
    {
        Error = ERROR_OPERATION_ABORTED;
        goto Exit;
    } 

    //
    // The lpdwNumberOfBytesRead parameter will be
    // populated on async completion, so it must exist
    // until INTERNET_STATUS_REQUEST_COMPLETE.
    // The same is true of lpBuffer parameter.
    //
    // InternetReadFile will block until the buffer
    // is completely filled or the response is exhausted.
    //

    
    Success = InternetReadFile(ReqContext->RequestHandle,
                               ReqContext->OutputBuffer,
                               BUFFER_LEN,
                               &ReqContext->DownloadedBytes);
                               
    ReleaseRequestHandle(ReqContext);
    
    if(!Success)
    {
        Error = GetLastError();
        if(Error == ERROR_IO_PENDING)
        {
            fprintf(stderr, "Waiting for InternetReadFile to complete\n");
        }
        else
        {
            LogInetError(Error, L"InternetReadFile");
        }
        
        goto Exit;
    }

    
Exit:

    return Error;
}


DWORD
WriteResponseData(
    __in PREQUEST_CONTEXT ReqContext,
    __out PBOOL Eof
    )
/*++

Routine Description:
     Write response to a file

Arguments:
     ReqContext - Pointer to request context structure
     Eof - Done with response

Return Value:
     Error Code for the operation.

--*/
{
    DWORD Error = ERROR_SUCCESS;
    DWORD BytesWritten = 0;
    
    BOOL Success;

     *Eof = FALSE;

    //
    // Finished receiving response
    //
    
    if (ReqContext->DownloadedBytes == 0)
    {
        *Eof = TRUE;
        goto Exit;
        
    }    
    
    //
    //
    // WriteFile is done inline here assuming that it will return quickly
    // I.E. the file is on disk
    //
    // If you plan to do blocking/intensive operations they should be
    // queued to another thread and not block the callback thread
    //
    //
    
    Success = WriteFile(ReqContext->DownloadFile,
                        ReqContext->OutputBuffer,
                        ReqContext->DownloadedBytes,
                        &BytesWritten,
                        NULL);
    
    if (!Success)
    {
        Error = GetLastError();

        LogSysError(Error, L"WriteFile");
        goto Exit;;
    }

    
Exit:

    return Error;
}





VOID
CloseRequestHandle(
    __inout PREQUEST_CONTEXT ReqContext
)
/*++

Routine Description:
    Safely  close the request handle by synchronizing
    with all threads using the handle.

    When this function returns no more calls can be made with the
    handle.
    
Arguments:
    ReqContext - Pointer to Request context structure
Return Value:
    None.

--*/
{
    BOOL Close = FALSE;
    
    EnterCriticalSection(&ReqContext->CriticalSection);

    //
    // Current implementation only supports the main thread
    // kicking off the request handle close
    //
    // To support multiple threads the lifetime 
    // of the request context must be carefully controlled
    // (most likely guarded by refcount/critsec)
    // so that they are not trying to abort a request
    // where the context has already been freed.
    //
    
    ASYNC_ASSERT(ReqContext->Closing == FALSE);
    ReqContext->Closing = TRUE;
    
    if(ReqContext->HandleUsageCount == 0)
    {
        Close = TRUE;
    }

    LeaveCriticalSection(&ReqContext->CriticalSection);



    if(Close)
    {
        //
        // At this point there must be the guarantee that all calls
        // to wininet with this handle have returned with some value
        // including ERROR_IO_PENDING, and none will be made after
        // InternetCloseHandle.
        //        
        (VOID)InternetCloseHandle(ReqContext->RequestHandle);
    }

    return;
}

BOOL
AcquireRequestHandle(
    __inout PREQUEST_CONTEXT ReqContext
)
/*++

Routine Description:
    Acquire use of the request handle to make a wininet call
Arguments:
    ReqContext - Pointer to Request context structure
Return Value:
    TRUE - Success
    FALSE - Failure
--*/
{
    BOOL Success = TRUE;

    EnterCriticalSection(&ReqContext->CriticalSection);

    if(ReqContext->Closing == TRUE)
    {
        Success = FALSE;        
    }
    else
    {
        ReqContext->HandleUsageCount++;
    }

    LeaveCriticalSection(&ReqContext->CriticalSection);
    
    return Success;
}


VOID
ReleaseRequestHandle(
    __inout PREQUEST_CONTEXT ReqContext
)
/*++

Routine Description:
    release use of the request handle
Arguments:
    ReqContext - Pointer to Request context structure
Return Value:
    None.

--*/
{
    BOOL Close = FALSE;

    EnterCriticalSection(&ReqContext->CriticalSection);

    ASYNC_ASSERT(ReqContext->HandleUsageCount > 0);
    
    ReqContext->HandleUsageCount--;
    
    if(ReqContext->Closing == TRUE && ReqContext->HandleUsageCount == 0)
    {
        Close = TRUE;

    }

    LeaveCriticalSection(&ReqContext->CriticalSection);


    if(Close)
    {
        //
        // At this point there must be the guarantee that all calls
        // to wininet with this handle have returned with some value
        // including ERROR_IO_PENDING, and none will be made after
        // InternetCloseHandle.
        //        
        (VOID)InternetCloseHandle(ReqContext->RequestHandle);
    }
    
    return;
}


DWORD 
AllocateAndInitializeRequestContext(
    __in HINTERNET SessionHandle,
    __in PCONFIGURATION Configuration,
    __deref_out PREQUEST_CONTEXT *ReqContext
    )
/*++

Routine Description:
    Allocate the request context and initialize it values

Arguments:
    ReqContext - Pointer to Request context structure
    Configuration - Pointer to configuration structure
    SessionHandle - Wininet session handle to use when creating
                    connect handle
    
Return Value:
    Error Code for the operation.

--*/
{
    DWORD Error = ERROR_SUCCESS;
    BOOL Success;
    PREQUEST_CONTEXT LocalReqContext;

    *ReqContext = NULL;

    LocalReqContext = (PREQUEST_CONTEXT) malloc(sizeof(REQUEST_CONTEXT));

    if(LocalReqContext == NULL)
    {
        Error = ERROR_NOT_ENOUGH_MEMORY;
        goto Exit;
    }
    
    LocalReqContext->RequestHandle = NULL;
    LocalReqContext->ConnectHandle = NULL;
    LocalReqContext->DownloadedBytes = 0;
    LocalReqContext->WrittenBytes = 0;
    LocalReqContext->ReadBytes = 0;    
    LocalReqContext->UploadFile = INVALID_HANDLE_VALUE;
    LocalReqContext->DownloadFile = INVALID_HANDLE_VALUE;
    LocalReqContext->FileSize = 0;
    LocalReqContext->HandleUsageCount = 0;
    LocalReqContext->Closing = FALSE;
    LocalReqContext->Method = Configuration->Method;
    LocalReqContext->CompletionEvent = NULL;    
    LocalReqContext->CleanUpEvent = NULL;
    LocalReqContext->OutputBuffer = NULL;
    LocalReqContext->State = 
        (LocalReqContext->Method == METHOD_GET) ?  REQ_STATE_SEND_REQ : REQ_STATE_SEND_REQ_WITH_BODY;
    LocalReqContext->CritSecInitialized = FALSE;    
    
       
    // initialize critical section

    Success = InitializeCriticalSectionAndSpinCount(&LocalReqContext->CriticalSection, SPIN_COUNT);
    
    if(!Success)
    {
        Error = GetLastError();
        LogSysError(Error, L"InitializeCriticalSectionAndSpinCount");
        goto Exit;
    }

    LocalReqContext->CritSecInitialized = TRUE;

    LocalReqContext->OutputBuffer = (LPSTR) malloc(BUFFER_LEN);
    
    if(LocalReqContext->OutputBuffer == NULL)
    {
        Error = ERROR_NOT_ENOUGH_MEMORY;
        goto Exit;
    }
        
    // create events
    LocalReqContext->CompletionEvent = CreateEvent(NULL,  // Sec attrib
                                                   FALSE, // Auto reset
                                                   FALSE, // Initial state unsignalled
                                                   NULL); // Name
    if(LocalReqContext->CompletionEvent == NULL)
    {
        Error = GetLastError();
        LogSysError(Error, L"CreateEvent CompletionEvent");
        goto Exit;
    }

    // create events
    LocalReqContext->CleanUpEvent = CreateEvent(NULL,  // Sec attrib
                                                FALSE, // Auto reset
                                                FALSE, // Initial state unsignalled
                                                NULL); // Name
    if(LocalReqContext->CleanUpEvent == NULL)
    {
        Error = GetLastError();
        LogSysError(Error, L"CreateEvent CleanUpEvent");
        goto Exit;
    }    
    
    // Open the file to dump the response entity body and
    // if required the file with the data to post
    Error = OpenFiles(LocalReqContext,
                      Configuration->Method, 
                      Configuration->InputFileName, 
                      Configuration->OutputFileName);
    
    if(Error != ERROR_SUCCESS)
    {
            fprintf(stderr, "OpenFiles failed with %d\n", Error);
            goto Exit;
    }

    // Verify if we've opened a file to post and get its size
    if (LocalReqContext->UploadFile != INVALID_HANDLE_VALUE)
    {
        LocalReqContext->FileSize = GetFileSize(LocalReqContext->UploadFile, NULL);
        if(LocalReqContext->FileSize == INVALID_FILE_SIZE)
        {
            Error = GetLastError();
            LogSysError(Error, L"GetFileSize");
            goto Exit;
        }
    }


    Error = CreateWininetHandles(LocalReqContext, 
                                 SessionHandle,
                                 Configuration->HostName,
                                 Configuration->ResourceOnServer,
                                 Configuration->IsSecureConnection);
    
    if(Error != ERROR_SUCCESS)
    {
        fprintf(stderr, "CreateWininetHandles failed with %d\n", Error);
        goto Exit;        
    }
    

    *ReqContext = LocalReqContext;
    
Exit:  
    
    if(Error != ERROR_SUCCESS)
    {
        CleanUpRequestContext(LocalReqContext);
    }
    
    return Error;
}


DWORD 
CreateWininetHandles(
    __inout PREQUEST_CONTEXT ReqContext,
    __in HINTERNET SessionHandle,
    __in LPWSTR HostName,
    __in LPWSTR Resource,
    __in BOOL IsSecureConnection
    )
/*++

Routine Description:
    Create connect and request handles

Arguments:
    ReqContext - Pointer to Request context structure
    SessionHandle - Wininet session handle used to create
                    connect handle
    HostName - Hostname to connect
    Resource - Resource to get/post
    IsSecureConnection - SSL?

Return Value:
    Error Code for the operation.

--*/
{
    DWORD Error = ERROR_SUCCESS;
    INTERNET_PORT ServerPort = INTERNET_DEFAULT_HTTP_PORT;
    DWORD RequestFlags = 0;
    LPWSTR Verb;


    //
    // Set the correct server port if using SSL
    // Also set the flag for HttpOpenRequest 
    //
    
    if(IsSecureConnection)
    {
        ServerPort = INTERNET_DEFAULT_HTTPS_PORT;
        RequestFlags = INTERNET_FLAG_SECURE;
    }    

    // Create Connection handle and provide context for async operations
    ReqContext->ConnectHandle = InternetConnect(SessionHandle,
                                                HostName,                  // Name of the server to connect to
                                                ServerPort,                // HTTP (80) or HTTPS (443)
                                                NULL,                      // Do not provide a user name for the server
                                                NULL,                      // Do not provide a password for the server
                                                INTERNET_SERVICE_HTTP,
                                                0,                         // Do not provide any special flag
                                                (DWORD_PTR)ReqContext);    // Provide the context to be
                                                                           // used during the callbacks
    //                                                                        
    // For HTTP InternetConnect returns synchronously because it does not
    // actually make the connection.
    //
    // For FTP InternetConnect connects the control channel, and therefore
    // can be completed asynchronously.  This sample would have to be
    // changed, so that the InternetConnect's asynchronous completion
    // is handled correctly to support FTP.
    //
    
    if (ReqContext->ConnectHandle == NULL)
    {
        Error = GetLastError();
        LogInetError(Error, L"InternetConnect");
        goto Exit;
    }


    // Set the Verb depending on the operation to perform
    if(ReqContext->Method == METHOD_GET)
    {
        Verb = L"GET";
    }
    else
    {
        ASYNC_ASSERT(ReqContext->Method == METHOD_POST);
        
        Verb = L"POST";
    }

    //
    // We're overriding WinInet's default behavior.
    // Setting these flags, we make sure we get the response from the server and not the cache.
    // Also ask WinInet not to store the response in the cache.
    //
    // These flags are NOT performant and are only used to show case WinInet's Async I/O.
    // A real WinInet application would not want to use this flags.
    //
    
    RequestFlags |= INTERNET_FLAG_RELOAD | INTERNET_FLAG_NO_CACHE_WRITE;

    // Create a Request handle
    ReqContext->RequestHandle = HttpOpenRequest(ReqContext->ConnectHandle,
                                                Verb,                     // GET or POST
                                                Resource,                 // root "/" by default
                                                NULL,                     // Use default HTTP/1.1 as the version
                                                NULL,                     // Do not provide any referrer
                                                NULL,                     // Do not provide Accept types
                                                RequestFlags,
                                                (DWORD_PTR)ReqContext);
    
    if (ReqContext->RequestHandle == NULL)
    {
        Error = GetLastError();
        LogInetError(Error, L"HttpOpenRequest");
        
        goto Exit;
    }
    
    
Exit:
    
    return Error;
}

VOID
WaitForRequestCompletion(
    __in PREQUEST_CONTEXT ReqContext,
    __in DWORD Timeout
)
/*++

Routine Description:
    Wait for the request to complete or timeout to occur

Arguments:
    ReqContext - Pointer to request context structure

Return Value:
    None.

--*/
{
    DWORD SyncResult;

    //
    // The preferred method of doing timeouts is to
    // use the timeout options through InternetSetOption,
    // but this overall timeout is being used to show 
    // the correct way to abort and close a request.
    //
    
    SyncResult = WaitForSingleObject(ReqContext->CompletionEvent,
                                     Timeout);              // Wait until we receive the completion
    
    switch(SyncResult)
    {
        case WAIT_OBJECT_0:
            
            printf("Done!\n");
            break;
            
        case WAIT_TIMEOUT:

            fprintf(stderr,
                    "Timeout while waiting for completion event (request will be cancelled)\n");
            break;
            
        case WAIT_FAILED:
            
            fprintf(stderr,
                    "Wait failed with Error %d while waiting for completion event (request will be cancelled)\n", 
                    GetLastError());
            break;
            
        default:
            // Not expecting any other error codes
            ASYNC_ASSERT(FALSE);
            break;
            
 
    }

    return;
}
    
VOID 
CleanUpRequestContext(
    __inout_opt PREQUEST_CONTEXT ReqContext
    )
/*++

Routine Description:
    Used to cleanup the request context before exiting.

Arguments:
    ReqContext - Pointer to request context structure

Return Value:
    None.

--*/
{
    if(ReqContext == NULL)
    {
        goto Exit;
    }

    if(ReqContext->RequestHandle) 
    {
        CloseRequestHandle(ReqContext);
        
        //
        // Wait for the closing of the handle to complete
        // (waiting for all async operations to complete)
        //
        // This is the only safe way to get rid of the context
        //
        
        (VOID)WaitForSingleObject(ReqContext->CleanUpEvent, INFINITE);           
    }
    
    if(ReqContext->ConnectHandle)
    {
        //
        // Remove the callback from the ConnectHandle since
        // we don't want the closing notification
        // The callback was inherited from the session handle
        //
        (VOID)InternetSetStatusCallback(ReqContext->ConnectHandle, 
                                        NULL);

        (VOID)InternetCloseHandle(ReqContext->ConnectHandle);
    }    

    if(ReqContext->UploadFile != INVALID_HANDLE_VALUE) 
    {
        CloseHandle(ReqContext->UploadFile);
    }
    
    if(ReqContext->DownloadFile != INVALID_HANDLE_VALUE) 
    {
        CloseHandle(ReqContext->DownloadFile);
    }

    if(ReqContext->CompletionEvent) 
    {
        CloseHandle(ReqContext->CompletionEvent);
    }

    if(ReqContext->CleanUpEvent) 
    {
        CloseHandle(ReqContext->CleanUpEvent);
    }
    
    if(ReqContext->CritSecInitialized)
    {
        DeleteCriticalSection(&ReqContext->CriticalSection);
    }
    
    if(ReqContext->OutputBuffer)
    {
        free(ReqContext->OutputBuffer);
    }
    

    
    free(ReqContext);
    
    
Exit:
    
    return;
}



VOID 
CleanUpSessionHandle(
    __in HINTERNET SessionHandle
    )
/*++

Routine Description:
    Used to cleanup session before exiting.

Arguments:
    SessionHandle - Wininet session handle

Return Value:
    None.

--*/
{

    if(SessionHandle) 
    {
        //
        // Remove the callback from the SessionHandle since
        // we don't want the closing notification
        //
        (VOID)InternetSetStatusCallback(SessionHandle, 
                                        NULL);
        //
        // Call InternetCloseHandle and do not wait for the closing notification 
        // in the callback function
        //
        (VOID)InternetCloseHandle(SessionHandle);

    }

    return;
}


DWORD 
OpenFiles(
    __inout PREQUEST_CONTEXT ReqContext,
    __in DWORD Method,
    __in LPWSTR InputFileName,
    __in LPWSTR OutputFileName    
    )
/*++

Routine Description:
    This routine opens files, one to post data from, and
    one to write response into

Arguments:
    ReqContext - Pointer to request context structure
    Method - GET or POST - do we need to open the input file
    InputFileName - Input file name
    OutputFileName - output file name

Return Value:
    Error Code for the operation.

--*/
{
    DWORD Error = ERROR_SUCCESS;
    
    if (Method == METHOD_POST)
    {
        // Open input file
        ReqContext->UploadFile = CreateFile(InputFileName,
                                            GENERIC_READ,
                                            FILE_SHARE_READ, 
                                            NULL,                   // handle cannot be inherited
                                            OPEN_ALWAYS,            // if file exists, open it
                                            FILE_ATTRIBUTE_NORMAL,
                                            NULL);                  // No template file

        if (ReqContext->UploadFile == INVALID_HANDLE_VALUE)
        {
            Error = GetLastError();
            LogSysError(Error, L"CreateFile for input file");
            goto Exit;
        }
    }

    // Open output file
    ReqContext->DownloadFile = CreateFile(OutputFileName,
                                          GENERIC_WRITE,
                                          0,                        // Open exclusively
                                          NULL,                     // handle cannot be inherited
                                          CREATE_ALWAYS,            // if file exists, delete it
                                          FILE_ATTRIBUTE_NORMAL,
                                          NULL);                    // No template file
    
    if (ReqContext->DownloadFile == INVALID_HANDLE_VALUE)
    {
            Error = GetLastError();
            LogSysError(Error, L"CreateFile for output file");
            goto Exit;
    }
    
Exit:
    return Error;
}


DWORD 
ParseArguments(
    __in int argc,
    __in_ecount(argc) LPWSTR *argv,
    __inout PCONFIGURATION Configuration
    )
/*++

Routine Description:
     This routine is used to Parse command line arguments. Flags are
     case sensitive.

Arguments:
     argc - Number of arguments
     argv - Pointer to the argument vector
     Configuration - pointer to configuration struct to write configuration

Return Value:
    Error Code for the operation.

--*/
{ 
    int i;
    DWORD Error = ERROR_SUCCESS;

    for (i = 1; i < argc; ++i)
    {        
        if (wcsncmp(argv[i], L"-", 1))
        {
            printf("Invalid switch %ws\n", argv[i]);
            i++;
            continue;
        }
        
        switch(argv[i][1])
        {            
            case L'p':
                
                Configuration->UseProxy = 1;
                if (i < argc - 1)
                {
                    Configuration->ProxyName = argv[++i];
                }
                break;
                
            case L'h':
                
                if (i < argc - 1)
                {
                    Configuration->HostName = argv[++i];
                }
                
                break;
                
            case L'o':
                
                if (i < argc - 1)
                {
                    Configuration->ResourceOnServer = argv[++i];
                }
                
                break;
                
            case L'r':
            
                if (i < argc - 1)
                {
                    Configuration->InputFileName = argv[++i];
                }
                
                break;

            case L'w':
                
                if (i < argc - 1)
                {
                    Configuration->OutputFileName = argv[++i];
                }
                
                break;
            
            case L'm':
                
                if (i < argc - 1)
                {
                    if (!_wcsnicmp(argv[i + 1], L"get", 3))
                    {
                        Configuration->Method = METHOD_GET;
                    }
                    else if (!_wcsnicmp(argv[i + 1], L"post", 4))
                    {
                        Configuration->Method = METHOD_POST;
                    }
                }
                ++i;
                break;

            case L's':
                Configuration->IsSecureConnection = TRUE;
                break;

            case L't':
                if (i < argc - 1)
                {
                    Configuration->UserTimeout = _wtoi(argv[++i]);
                }
                break;      

            default:
                Error = ERROR_INVALID_PARAMETER;
                break;
        }
    }

    if(Error == ERROR_SUCCESS)
    {
        if(Configuration->UseProxy && Configuration->ProxyName == NULL)
        {
            printf("No proxy server name provided!\n\n");
            Error = ERROR_INVALID_PARAMETER;
            goto Exit;
        }

        if(Configuration->HostName == NULL)
        {
            printf("Defaulting hostname to: %ws\n", DEFAULT_HOSTNAME);
            Configuration->HostName = DEFAULT_HOSTNAME;
        }

        if(Configuration->Method == METHOD_NONE)
        {
            printf("Defaulting method to: GET\n");
            Configuration->Method = METHOD_GET;
        }

        if(Configuration->ResourceOnServer == NULL)
        {
            printf("Defaulting resource to: %ws\n", DEFAULT_RESOURCE);
            Configuration->ResourceOnServer = DEFAULT_RESOURCE; 
        }

        if(Configuration->UserTimeout == 0)
        {
            printf("Defaulting timeout to: %d\n", DEFAULT_TIMEOUT);
            Configuration->UserTimeout = DEFAULT_TIMEOUT;         
        }

        if(Configuration->InputFileName == NULL && Configuration->Method == METHOD_POST)
        {
            printf("Error: File to post not specified\n");
            Error = ERROR_INVALID_PARAMETER;
            goto Exit;
        }
        
        if(Configuration->OutputFileName == NULL)
        {
            printf("Defaulting output file to: %ws\n", DEFAULT_OUTPUT_FILE_NAME);
            
            Configuration->OutputFileName = DEFAULT_OUTPUT_FILE_NAME;
        }

    }

Exit:    
    return Error;
}


VOID
ShowUsage(
    VOID
    )
/*++

Routine Description:
      Shows the usage of the application.

Arguments:
      None.

Return Value:
      None.

--*/
{
    printf("Usage: async [-m {GET|POST}] [-h <hostname>] [-o <resourcename>] [-s] ");
    printf("[-p <proxyname>] [-w <output filename>] [-r <file to post>] [-t <userTimeout>]\n");
    printf("Option Semantics: \n");
    printf("-m : Specify method (Default: \"GET\")\n");
    printf("-h : Specify hostname (Default: \"%ws\"\n", DEFAULT_HOSTNAME);
    printf("-o : Specify resource name on the server (Default: \"%ws\")\n", DEFAULT_RESOURCE);
    printf("-s : Use secure connection - https\n");
    printf("-p : Specify proxy\n");
    printf("-w : Specify file to write output to (Default: \"%ws\")\n", DEFAULT_OUTPUT_FILE_NAME);
    printf("-r : Specify file to post data from\n");
    printf("-t : Specify time to wait in ms for operation completion (Default: %d)\n", DEFAULT_TIMEOUT);
    
    return;
}

VOID 
LogInetError(
    __in DWORD Err,
    __in LPCWSTR Str
    )
/*++

Routine Description:
     This routine is used to log WinInet errors in human readable form.

Arguments:
     Err - Error number obtained from GetLastError()
     Str - String pointer holding caller-context information 

Return Value:
    None.

--*/
{
    DWORD Result;
    PWSTR MsgBuffer = NULL;
    
    Result = FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER |
                           FORMAT_MESSAGE_FROM_HMODULE,
                           GetModuleHandle(L"wininet.dll"),
                           Err,
                           MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
                           (LPWSTR)&MsgBuffer,
                           ERR_MSG_LEN,
                           NULL);
    
    if (Result)
    {
        fprintf(stderr, "%ws: %ws\n", Str, MsgBuffer);
        LocalFree(MsgBuffer);
    }
    else
    {
        fprintf(stderr,
                "Error %d while formatting message for %d in %ws\n",
                GetLastError(),
                Err,
                Str);
    }

    return;
}

VOID
LogSysError(
    __in DWORD Err,
    __in LPCWSTR Str
    )
/*++

Routine Description:
     This routine is used to log System Errors in human readable form.

Arguments:
     Err - Error number obtained from GetLastError()
     Str - String pointer holding caller-context information 

Return Value:
    None.

--*/
{
    DWORD Result;
    PWSTR MsgBuffer = NULL;

    Result = FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER |
                           FORMAT_MESSAGE_FROM_SYSTEM,
                           NULL,
                           Err,
                           MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
                           (LPWSTR)&MsgBuffer,
                           ERR_MSG_LEN,
                           NULL);
    
    if (Result)
    {
        fprintf(stderr,
                "%ws: %ws\n",
                Str,
                MsgBuffer);
       LocalFree(MsgBuffer);
    }
    else
    {
        fprintf(stderr,
                "Error %d while formatting message for %d in %ws\n",
                GetLastError(),
                Err,
                Str);    
    }

    return;
}
```



 

 




