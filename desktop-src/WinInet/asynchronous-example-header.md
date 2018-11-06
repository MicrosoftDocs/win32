---
title: Asynchronous Example Header
description: The following is the header file for the asynchronous example application.
ms.assetid: e35b395a-4092-478f-b3e0-b40303b8f591
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Example Header

The following is the header file for the [asynchronous example application](asynchronous-example-application.md).


```C++
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <wininet.h>
#include <stdio.h>

#ifdef DBG
#define ASYNC_ASSERT(x) \
    do                  \
    {                   \
        if (x)          \
        {               \
            break;      \
        }               \
        DebugBreak();   \
    }                   \
    while (FALSE, FALSE)
#else
#define ASYNC_ASSERT(x)
#endif

#define BUFFER_LEN  4096
#define ERR_MSG_LEN 512

#define METHOD_NONE 0
#define METHOD_GET  1
#define METHOD_POST 2

#define REQ_STATE_SEND_REQ             0
#define REQ_STATE_SEND_REQ_WITH_BODY   1
#define REQ_STATE_POST_GET_DATA        2
#define REQ_STATE_POST_SEND_DATA       3
#define REQ_STATE_POST_COMPLETE        4
#define REQ_STATE_RESPONSE_RECV_DATA   5
#define REQ_STATE_RESPONSE_WRITE_DATA  6
#define REQ_STATE_COMPLETE             7

#define DEFAULT_TIMEOUT 2 * 60 * 1000 // Two minutes

#define DEFAULT_HOSTNAME L"www.microsoft.com"
#define DEFAULT_RESOURCE L"/"

#define DEFAULT_OUTPUT_FILE_NAME L"response.htm"
#define SPIN_COUNT 4000

#pragma comment(lib, "wininet.lib")

//
// Structure to store configuration in that was gathered from
// passed in arguments
//

typedef struct _CONFIGURATION
{
    DWORD Method;                 // Method, GET or POST
    LPWSTR HostName;              // Host to connect to
    LPWSTR ResourceOnServer;      // Resource to get from the server
    LPWSTR InputFileName;         // File containing data to post
    LPWSTR OutputFileName;        // File to write the data received from the server
    BOOL UseProxy;                // Flag to indicate the use of a proxy
    LPWSTR ProxyName;             // Name of the proxy to use
    BOOL IsSecureConnection;      // Flag to indicate the use of SSL
    DWORD UserTimeout;            // Timeout for the async operations
} CONFIGURATION, *PCONFIGURATION;

//
// Structure used for storing the context for the asynchronous calls
//

typedef struct _REQUEST_CONTEXT {
    HINTERNET RequestHandle;
    HINTERNET ConnectHandle;
    HANDLE CompletionEvent;
    HANDLE CleanUpEvent;
    LPSTR OutputBuffer;
    DWORD DownloadedBytes;
    DWORD WrittenBytes;
    DWORD ReadBytes;
    HANDLE UploadFile;
    DWORD FileSize;
    HANDLE DownloadFile;
    DWORD Method;
    DWORD State;
    
    CRITICAL_SECTION CriticalSection;
    BOOL CritSecInitialized;


    //
    // Synchronized by CriticalSection
    //

    DWORD HandleUsageCount; // Request object is in use(not safe to close handle)
    BOOL Closing;           // Request is closing(don't use handle)

} REQUEST_CONTEXT, *PREQUEST_CONTEXT;



// WinInet Callback function
VOID CALLBACK 
CallBack(
    __in HINTERNET hInternet,
    __in DWORD_PTR dwContext,
    __in DWORD dwInternetStatus,
    __in_bcount(dwStatusInformationLength) LPVOID lpvStatusInformation,
    __in DWORD dwStatusInformationLength
    );


//
// IO related functions
//

VOID ProcessRequest(
    __inout PREQUEST_CONTEXT ReqContext,
    __in DWORD Error
    );

DWORD SendRequest(
    __in PREQUEST_CONTEXT ReqContext
    );

DWORD SendRequestWithBody(
    __in PREQUEST_CONTEXT ReqContext
    );

DWORD GetDataToPost(
    __inout PREQUEST_CONTEXT ReqContext
    );

DWORD PostDataToServer(
    __inout PREQUEST_CONTEXT ReqContext,
    __out PBOOL Eof
    );

DWORD CompleteRequest(
    __inout PREQUEST_CONTEXT ReqContext
    );

DWORD RecvResponseData(
    __inout PREQUEST_CONTEXT ReqContext
    );

DWORD WriteResponseData(
    __in PREQUEST_CONTEXT ReqContext,
    __out PBOOL Eof
    );


//
// Initialization functions
//

DWORD AllocateAndInitializeRequestContext(
    __in HINTERNET SessionHandle,
    __in PCONFIGURATION Configuration,
    __deref_out PREQUEST_CONTEXT *ReqContext
    );

DWORD CreateWininetHandles(
    __inout PREQUEST_CONTEXT ReqContext,
    __in HINTERNET SessionHandle,
    __in LPWSTR HostName,
    __in LPWSTR Resource,
    __in BOOL IsSecureConnection
    );


//
// Cleanup functions
//

VOID CleanUpRequestContext(
    __inout_opt PREQUEST_CONTEXT ReqContext
    );

    
VOID CleanUpSessionHandle(
    __in HINTERNET SessionHandle
    );

//
// Cancellation support functions
//


VOID CloseRequestHandle(
    __inout PREQUEST_CONTEXT ReqContext
);

BOOL AcquireRequestHandle(
    __inout PREQUEST_CONTEXT ReqContext
);

VOID ReleaseRequestHandle(
    __inout PREQUEST_CONTEXT ReqContext
);


//
// Utility functions
//

VOID WaitForRequestCompletion(
    __in PREQUEST_CONTEXT ReqContext,
    __in DWORD Timeout
);

DWORD OpenFiles(
    __inout PREQUEST_CONTEXT ReqContext,
    __in DWORD Method,
    __in LPWSTR InputFileName,
    __in LPWSTR OutputFileName    
    );

DWORD ParseArguments(
    __in int argc,
    __in_ecount(argc) LPWSTR *argv,
    __inout PCONFIGURATION Configuration
    );


VOID ShowUsage(
    VOID
    );

VOID  LogInetError(
    __in DWORD Err,
    __in LPCWSTR Str
    );

VOID LogSysError(
    __in DWORD Err,
    __in LPCWSTR Str
    );
```



 

 




