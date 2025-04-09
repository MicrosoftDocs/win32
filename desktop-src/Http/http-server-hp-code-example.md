---
title: High-performance HTTP Server code example
description: The code example in this topic builds into an app that demonstrates how to use the HTTP Server APIs asynchronously from multiple threads to achieve high performance and throughput when performing server-side tasks.
ms.topic: reference
ms.date: 05/28/2024
---


# High-performance HTTP Server code example

The code example in this topic builds into an app that demonstrates how to use the HTTP Server APIs asynchronously from multiple threads to achieve high performance and throughput when performing server-side tasks.

```cpp
#ifndef UNICODE
#define UNICODE
#endif

#ifndef _WIN32_WINNT
#define _WIN32_WINNT 0x0600
#endif

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <windows.h>
#include <winternl.h>
#include <stdio.h>
#include <conio.h>
#include <http.h>

#pragma comment(lib, "httpapi.lib")
#pragma comment(lib, "ntdll.lib")

//
// Macros
//

#define ALLOC_MEM(cb) HeapAlloc(GetProcessHeap(), 0, (cb))
#define FREE_MEM(ptr) HeapFree(GetProcessHeap(), 0, (ptr))

#define STRLEN_LIT(x) ((sizeof(x) / sizeof(x[0])) - 1)

#define LISTENER_THREAD_COUNT            MAXIMUM_WAIT_OBJECTS
#define MAX_COMPLETIONS_PER_DEQUEUE                         4
#define MAX_INLINE_COMPLETION_SPIN_TIME                   500

//
// Global definitions
//

BOOL g_StopListeners = FALSE;
HANDLE g_RequestQueue = NULL;
DWORD g_InitialReceivesPerThread = 4;
HANDLE g_CompletionPort = NULL;
ULONG g_ResponseSize = 512;
PBYTE g_ResponseData = NULL;
DWORD g_RequestReceived = 0;
DWORD g_ResponseSent = 0;

#define REQUEST_BUFFER_SIZE   4096

typedef enum _IO_CONTEXT_STATE
{
    IoStateIdle,
    IoStateReceive,
    IoStateSend,
} IO_CONTEXT_STATE, * PIO_CONTEXT_STATE;

typedef struct _IO_CONTEXT
{
    IO_CONTEXT_STATE State;
    OVERLAPPED Overlapped;
    LIST_ENTRY ListEntry;
    ULONG IoResult;
    HTTP_RESPONSE Response;
    HTTP_DATA_CHUNK DataChunk;
    PHTTP_REQUEST Request;
    ULONG RequestBufferSize;
    DWORD NumberOfBytesTransferred;
} IO_CONTEXT, * PIO_CONTEXT;

typedef struct _WORKER_STATS
{
    ULONGLONG InlineReceives;
    ULONGLONG AsyncReceives;
    ULONGLONG InlineSends;
    ULONGLONG AsyncSends;
    ULONGLONG RequestsReceived;
} WORKER_STATS, * PWORKER_STATS;

typedef struct _WORKER_BLOCK
{
    LIST_ENTRY CompletionList;
    WORKER_STATS Stats;
} WORKER_BLOCK, * PWORKER_BLOCK;

//
// Prototypes.
//

DWORD
WINAPI
HttpListenerThread(
    __in VOID* pThreadParams
);

DWORD
WINAPI
DisplayStatsThread(
    __in VOID* pThreadParams
);

ULONG
InitiateReceive(
    __inout PWORKER_BLOCK Worker,
    __in HTTP_REQUEST_ID RequestId,
    __in ULONG RequestBufferSize
);

ULONG
ProcessReceiveCompletion(
    __inout PIO_CONTEXT Context,
    __inout PWORKER_BLOCK Worker
);

ULONG
SendResponse(
    __inout PIO_CONTEXT Context,
    __inout PWORKER_BLOCK Worker
);

VOID
ProcessSendCompletion(
    __inout PIO_CONTEXT Context,
    __inout PWORKER_BLOCK Worker
);

ULONG
WaitForCompletions(
    __inout PWORKER_BLOCK Worker,
    __in ULONG Timeout
);

PIO_CONTEXT
AllocateIoContext();

VOID
FreeIoContext(
    __in PIO_CONTEXT Context
);

//
// Utility functions
//

VOID
InsertTailList(
    __inout PLIST_ENTRY ListHead,
    __inout PLIST_ENTRY Entry
);

BOOLEAN
IsListEmpty(
    __in const LIST_ENTRY* ListHead
);

VOID
InitializeListHead(
    __out PLIST_ENTRY ListHead
);

PLIST_ENTRY
RemoveHeadList(
    __inout PLIST_ENTRY ListHead
);

int __cdecl wmain(
    int argc,
    wchar_t* argv[]
)
{
    DWORD                  Result = ERROR_SUCCESS;
    DWORD                  WaitResult = 0;
    HTTPAPI_VERSION        HttpApiVersion = HTTPAPI_VERSION_2;
    DWORD                  Index = 0;
    ULONG                  ThreadCount = LISTENER_THREAD_COUNT;
    HANDLE                 ThreadHandles[LISTENER_THREAD_COUNT] = {};
    HTTP_URL_GROUP_ID      UrlGroupId = HTTP_NULL_ID;
    HTTP_SERVER_SESSION_ID SessionId = HTTP_NULL_ID;
    HTTP_BINDING_INFO      BindingInfo = {};

    if (argc < 2)
    {
        wprintf(L"%ws: <Url1> [Url2] ... \n", argv[0]);
        return -1;
    }

    //
    // Initialize HTTP Server APIs.
    //

    Result = HttpInitialize(
        HttpApiVersion,
        HTTP_INITIALIZE_SERVER,
        NULL);
    if (Result != ERROR_SUCCESS)
    {
        wprintf(L"HttpInitialize failed with %d\n", Result);
        return Result;
    }

    //
    // Create a request queue.
    //

    Result = HttpCreateRequestQueue(
        HttpApiVersion,
        NULL,
        NULL,
        0,
        &g_RequestQueue);
    if (Result != ERROR_SUCCESS)
    {
        wprintf(L"HttpCreateRequestQueue failed %d\n", Result);
        goto Exit;
    }

    //
    // Create the HTTP Server session.
    //

    Result = HttpCreateServerSession(HttpApiVersion, &SessionId, 0);
    if (Result != ERROR_SUCCESS)
    {
        wprintf(L"HttpCreateServerSession failed %d\n", Result);
        goto Exit;
    }

    //
    // Create a URL group.
    //

    Result = HttpCreateUrlGroup(SessionId, &UrlGroupId, 0);
    if (Result != ERROR_SUCCESS)
    {
        wprintf(L"HttpCreateUrlGroup failed %d\n", Result);
        goto Exit;
    }

    //
    // Add our URLs to the URL group.
    //
    // The URI is a fully-qualified URI, and must include the
    // terminating (/) character.
    //

    for (Index = 1; Index < (DWORD) argc; Index++)
    {
        wprintf(L"Listening for requests on the following url: %s\n", argv[Index]);

        Result = HttpAddUrlToUrlGroup(UrlGroupId, argv[Index], 0, 0);
        if (Result != ERROR_SUCCESS)
        {
            wprintf(L"HttpAddUrlToUrlGroup for %s failed %d\n", argv[Index], Result);
            goto Exit;
        }
    }

    //
    // Bind the URL group to the request queue.
    //

    ZeroMemory(&BindingInfo, sizeof(BindingInfo));
    BindingInfo.Flags.Present = 1;
    BindingInfo.RequestQueueHandle = g_RequestQueue;

    Result = HttpSetUrlGroupProperty(
        UrlGroupId,
        HttpServerBindingProperty,
        &BindingInfo,
        sizeof(BindingInfo));
    if (Result != ERROR_SUCCESS)
    {
        wprintf(L"HttpSetUrlGroupProperty failed %d\n", Result);
        goto Exit;
    }

    //
    // Initialize the response buffer.
    //

    g_ResponseData = (PBYTE) ALLOC_MEM(g_ResponseSize + 1);
    if (g_ResponseData == NULL)
    {
        printf("out of memory\n");
        Result = ERROR_OUTOFMEMORY;
        goto Exit;
    }

    for (Index = 0; Index < g_ResponseSize; Index++)
    {
        g_ResponseData[Index] = (Index % 10) + '0';
    }
    g_ResponseData[Index] = '\0';

    //
    // Create completion port to receive IO completions.
    //

    //
    // We don't want to potentially switch the threads thru
    // completion ports when processing the inline completions.
    //

    if (!SetFileCompletionNotificationModes(
            g_RequestQueue,
            FILE_SKIP_COMPLETION_PORT_ON_SUCCESS | FILE_SKIP_SET_EVENT_ON_HANDLE))
    {
        Result = GetLastError();
        printf("SetFileCompletionNotificationModes failed %d\n", Result);
        goto Exit;
    }

    g_CompletionPort = CreateIoCompletionPort(
        g_RequestQueue,
        NULL,
        0,
        ThreadCount);

    if (g_CompletionPort == NULL)
    {
        Result = GetLastError();
        printf("CreateIoCompletionPort failed %d\n", Result);
        goto Exit;
    }

    //
    // Launch stats display thread.
    //

    ThreadHandles[0] = CreateThread(
        NULL,
        0,
        DisplayStatsThread,
        NULL,
        0,
        NULL);

    if (ThreadHandles[0] == NULL)
    {
        Result = GetLastError();
        printf("CreateThread failed %d\n", Result);
        goto Exit;
    }

    //
    // Launch request/response I/O threads.
    //

    for (Index = 1; Index < ThreadCount; Index++)
    {
        ThreadHandles[Index] = CreateThread(
            NULL,
            0,
            HttpListenerThread,
            (PVOID)(SIZE_T)Index,
            0,
            NULL);

        if (ThreadHandles[Index] == NULL)
        {
            Result = GetLastError();
            printf("CreateThread failed %d\n", Result);
            goto Exit;
        }
    }

    //
    // Wait for user command to exit.
    //

    _getch();

    //
    // Signal I/O threads to stop processing the requests, and exit.
    //

    g_StopListeners = TRUE;

    //
    // Stop queuing requests, and cancel all outstanding requests.
    //

    Result = HttpShutdownRequestQueue(g_RequestQueue);
    if (Result != ERROR_SUCCESS)
    {
        wprintf(L"HttpShutdownRequestQueue failed with %lu \n", Result);
        goto Exit;
    }

    //
    // Wait for all I/O threads to exit.
    //

    WaitResult = WaitForMultipleObjects(LISTENER_THREAD_COUNT, ThreadHandles, TRUE, 15000);
    if (WaitResult == WAIT_FAILED)
    {
        Result = GetLastError();
        printf("WaitForMultipleObjects failed %d\n", Result);
        goto Exit;
    }

    if (WaitResult == WAIT_TIMEOUT)
    {
        printf("WaitForMultipleObjects timed out\n");
        goto Exit;
    }

Exit:

    //
    // Close the request queue handle.
    //

    if (g_RequestQueue)
    {
        HttpCloseRequestQueue(g_RequestQueue);
        g_RequestQueue = NULL;
    }

    //
    // Close the URL group.
    //

    if (UrlGroupId != HTTP_NULL_ID)
    {
        HttpCloseUrlGroup(UrlGroupId);
        UrlGroupId = HTTP_NULL_ID;
    }

    if (SessionId != HTTP_NULL_ID)
    {
        HttpCloseServerSession(SessionId);
        SessionId = HTTP_NULL_ID;
    }

    //
    // Call HttpTerminate.
    //

    HttpTerminate(HTTP_INITIALIZE_SERVER, NULL);

    //
    // Close the completion port handle.
    //

    if (g_CompletionPort)
    {
        CloseHandle(g_CompletionPort);
        g_CompletionPort = NULL;
    }

    //
    // Close the I/O threads' handles.
    //

    for (Index = 0; Index < ThreadCount; Index++)
    {
        if (ThreadHandles[Index] != NULL)
        {
            CloseHandle(ThreadHandles[Index]);
            ThreadHandles[Index] = NULL;
        }
    }

    return Result;
}

//
// Show some statistics.
//

DWORD
WINAPI
DisplayStatsThread(
    __in VOID* /*pThreadParams*/
)
{
    printf("Press any key to exit ...\r\n");

    printf("Requests Received,   Responses Sent\r\n");
    printf("%17u,%17u\r\n", g_RequestReceived, g_ResponseSent);

    while (!g_StopListeners)
    {
        Sleep(3000);
        printf("%17u,%17u\r\n", g_RequestReceived, g_ResponseSent);
        fflush(stdout);
    }

    return 0;
}


DWORD
WINAPI
HttpListenerThread(
    __in VOID* /*pThreadParams*/
)
{
    ULONG Result = ERROR_SUCCESS;
    ULONG Index = 0;
    WORKER_BLOCK Worker = { 0 };
    PIO_CONTEXT Context = NULL;
    ULONG TickCount = 0;
    ULONG CompletionCheckTimestamp = 0;

    InitializeListHead(&Worker.CompletionList);

    //
    // Posting initial receives.
    //

    for (Index = 0; Index < g_InitialReceivesPerThread; Index++)
    {
        Result = InitiateReceive(
            &Worker,
            HTTP_NULL_ID,
            REQUEST_BUFFER_SIZE);
        if (Result != ERROR_SUCCESS)
        {
            printf("InitiateReceive faield with %d\n", Result);
            goto Exit;
        }
    }

    while (!g_StopListeners)
    {
        CompletionCheckTimestamp = GetTickCount();

        //
        // Process the completions.
        //

        while (!IsListEmpty(&Worker.CompletionList))
        {
            if (g_StopListeners)
            {
                goto Exit;
            }

            Context = CONTAINING_RECORD(
                RemoveHeadList(&Worker.CompletionList),
                IO_CONTEXT,
                ListEntry);

            switch (Context->State)
            {
                case IoStateReceive:
                    ProcessReceiveCompletion(Context, &Worker);
                    break;

                case IoStateSend:
                    ProcessSendCompletion(Context, &Worker);
                    break;

                default:
                    printf("Invalid IoContext state %d\n", Context->State);
                    goto Exit;
            }

            //
            // To prevent inline completions from starving the
            // completion port, we check the completion port regularly.
            //

            TickCount = GetTickCount();
            if ((LONG)(TickCount - CompletionCheckTimestamp) > MAX_INLINE_COMPLETION_SPIN_TIME)
            {
                CompletionCheckTimestamp = TickCount;
                WaitForCompletions(&Worker, 0);
            }
        }

        //
        // Wait for completions.
        //

        Result = WaitForCompletions(&Worker, 5000);
        if (Result != ERROR_SUCCESS)
        {
            printf("WaitForCompletions faield with %d\n", Result);
            goto Exit;
        }
    }

Exit:

    //
    // Clean up any unprocessed I/O context.
    //

    while (!IsListEmpty(&Worker.CompletionList))
    {
        Context = CONTAINING_RECORD(
            RemoveHeadList(&Worker.CompletionList),
            IO_CONTEXT,
            ListEntry);

        FreeIoContext(Context);
    }

    return 0;
}


PIO_CONTEXT
AllocateIoContext(
    ULONG RequestBufferSize
)
{
    PSLIST_ENTRY Entry = NULL;
    PIO_CONTEXT Context = NULL;
    ULONG ContextSize = 0;

    //
    // The request buffer size should be at least big enough for an HTTP_REQUEST structure.
    //

    if (sizeof(HTTP_REQUEST) > RequestBufferSize)
    {
        RequestBufferSize = sizeof(HTTP_REQUEST);
    }

    ContextSize = sizeof(IO_CONTEXT) + RequestBufferSize;

    Context = (PIO_CONTEXT)ALLOC_MEM(ContextSize);
    if (Context == NULL)
    {
        return NULL;
    }

    RtlZeroMemory(Context, ContextSize);

    Context->State = IoStateIdle;
    Context->Request = (PHTTP_REQUEST)((PCHAR)Context + sizeof(IO_CONTEXT));
    Context->RequestBufferSize = RequestBufferSize;

    return Context;
}


VOID
FreeIoContext(
    __in PIO_CONTEXT Context
)
{
    FREE_MEM(Context);
}


ULONG
InitiateReceive(
    __inout PWORKER_BLOCK Worker,
    __in HTTP_REQUEST_ID RequestId,
    __in ULONG RequestBufferSize
)
{
    ULONG Result = ERROR_SUCCESS;
    PIO_CONTEXT Context = NULL;
    ULONG BytesTransferred = 0;

    for (;;)
    {
        Context = AllocateIoContext(RequestBufferSize);
        if (Context == NULL)
        {
            printf("out of memory\n");
            Result = ERROR_OUTOFMEMORY;
            goto Exit;
        }

        Context->State = IoStateReceive;

        Result = HttpReceiveHttpRequest(
            g_RequestQueue,
            RequestId,
            0,
            Context->Request,
            Context->RequestBufferSize,
            &BytesTransferred,
            &Context->Overlapped);

        //
        // Check return status.
        //

        switch (Result)
        {
            case ERROR_MORE_DATA:
            case ERROR_SUCCESS:

                //
                // The call might fail with ERROR_MORE_DATA if the buffer wasn't large enough for the request.
                // The buffer size required to read the remaining part of the request is returned in the BytesTransferred.
                //

                Worker->Stats.InlineReceives += 1;

                Context->NumberOfBytesTransferred = BytesTransferred;

                //
                // Completed inline, put the context to the processing queue.
                //

                Context->IoResult = Result;

                InsertTailList(&Worker->CompletionList, &Context->ListEntry);

                Result = ERROR_SUCCESS;

                goto Exit;

            case ERROR_IO_PENDING:
                Worker->Stats.AsyncReceives += 1;

                Result = ERROR_SUCCESS;

                goto Exit;

            case ERROR_CONNECTION_INVALID:

                //
                // The error means that the client closed the underlying connection.
                // In that case we issue a new HttpReceiveHttpRequest to keep requests flowing.
                //

                if (RequestId == HTTP_NULL_ID)
                {
                    printf("HttpReceiveHttpRequest returned an unexpected error for HTTP_NULL_ID %d\n", Result);
                    goto Exit;
                }

                //
                // Free the current I/O context.
                //

                FreeIoContext(Context);
                Context = NULL;

                RequestId = HTTP_NULL_ID;
                BytesTransferred = 0;

                //
                // Receive new request with the default buffer size.
                //

                RequestBufferSize = REQUEST_BUFFER_SIZE;

                break;

            default:

                //
                // Free async I/O context
                //

                FreeIoContext(Context);
                Context = NULL;

                //
                // Because of a race condition with cancelation routine, the call can fail with ERROR_INVALID_HANDLE.
                // That can be avoided if we synchronize HttpReceiveHttpRequest and HttpShutdownRequestQueue calls.
                //

                if (g_StopListeners &&
                    Result == ERROR_INVALID_HANDLE)
                {
                    Result = ERROR_SUCCESS;
                    goto Exit;
                }

                printf("HttpReceiveHttpRequest initiate failed %d\n", Result);
                goto Exit;
            }
    }

Exit:

    return Result;
}


ULONG
ProcessReceiveCompletion(
    __inout PIO_CONTEXT Context,
    __inout PWORKER_BLOCK Worker
)
{
    ULONG Result = ERROR_SUCCESS;
    HTTP_REQUEST_ID RequestId = HTTP_NULL_ID;
    ULONG RequestBufferSize = REQUEST_BUFFER_SIZE;

    Result = Context->IoResult;

    //
    // The call might fail with ERROR_MORE_DATA if the buffer wasn't
    // large enough for the request. The required buffer size is returned
    // in the OVERLAPPED_ENTRY::dwNumberOfBytesTransferred (stored in
    // Context->NumberOfBytesTransferred). In that case, HttpReceiveHttpRequest
    // should be called again with the same Context->Request->RequestId,
    // and with a big enough buffer.
    //

    if (Result == ERROR_MORE_DATA)
    {
        RequestId = Context->Request->RequestId;
        RequestBufferSize = Context->NumberOfBytesTransferred;

        FreeIoContext(Context);
        Context = NULL;

        goto InitReceive;
    }

    if (Result != ERROR_SUCCESS &&
        Result != ERROR_HANDLE_EOF)
    {
        printf("HttpReceiveHttpRequest completion failed %d\n", Result);
        goto Exit;
    }

    //
    // The code example is expecting only the GET verb. Cancel the request.
    //

    if (Context->Request->Verb != HttpVerbGET)
    {
        printf("Receved an unexpected http verb %d\n", Context->Request->Verb);

        Result = HttpCancelHttpRequest(
            g_RequestQueue,
            Context->Request->RequestId,
            NULL);
        if (Result != ERROR_SUCCESS)
        {
            printf("HttpCancelHttpRequest failed %d\n", Result);
            goto Exit;
        }

        FreeIoContext(Context);
        Context = NULL;

        //
        // Post the next receive
        //

        goto InitReceive;
    }

    //
    // The implementations must handle the scenario when the Context->Request->Flags
    // has HTTP_REQUEST_FLAG_MORE_ENTITY_BODY_EXISTS bit set. In that case, additional
    // calls to HttpReceiveRequestEntityBody or HttpReceiveHttpRequest should be made until
    // all data are received.
    //

    //
    // Update the receive statistics, and issue the send response.
    //

    Worker->Stats.RequestsReceived += 1;
    InterlockedIncrement(&g_RequestReceived);

    Result = SendResponse(
        Context,
        Worker);

    if (Result != ERROR_SUCCESS)
    {
        if (Result == ERROR_CONNECTION_INVALID)
        {
            //
            // The error means that the client closed the underlying connection.
            // In that case we issue a new HttpReceiveHttpRequest to keep requests flowing.
            //

            FreeIoContext(Context);
            Context = NULL;

            goto InitReceive;
        }

        printf("SendResponse failed %d\n", Result);
        goto Exit;
    }

    //
    // SendResponse's async I/O took the ownership of the context.
    //

    Context = NULL;

InitReceive:

    //
    // Post the next receive without waiting for SendResponse's
    // completion, as we want to keep the receive pip active.
    //

    Result = InitiateReceive(
        Worker,
        RequestId,
        RequestBufferSize);
    if (Result != ERROR_SUCCESS)
    {
        printf("InitiateReceive failed %d\n", Result);
        goto Exit;
    }

Exit:

    if (Context != NULL)
    {
        FreeIoContext(Context);
        Context = NULL;
    }

    return Result;
}


ULONG
SendResponse(
    __inout PIO_CONTEXT Context,
    __inout PWORKER_BLOCK Worker
)
{
    ULONG Result = ERROR_SUCCESS;

    //
    // Build response.
    //

    Context->Response.Headers.KnownHeaders[HttpHeaderContentType].pRawValue = "text/plain";
    Context->Response.Headers.KnownHeaders[HttpHeaderContentType].RawValueLength = STRLEN_LIT("text/plain");

    Context->Response.StatusCode = 200;
    Context->Response.pReason = "OK";
    Context->Response.ReasonLength = STRLEN_LIT("OK");

    Context->DataChunk.DataChunkType = HttpDataChunkFromMemory;
    Context->DataChunk.FromMemory.pBuffer = g_ResponseData;
    Context->DataChunk.FromMemory.BufferLength = g_ResponseSize;

    Context->Response.EntityChunkCount = 1;
    Context->Response.pEntityChunks = &Context->DataChunk;

    //
    // Send response.
    // Tiny responses might complete inline.
    //

    Context->State = IoStateSend;

    Result = HttpSendHttpResponse(
        g_RequestQueue,
        Context->Request->RequestId,
        0,
        &Context->Response,
        NULL,
        NULL,
        NULL,
        0,
        &Context->Overlapped,
        NULL);

    //
    // Update stats.
    //

    if (Result == ERROR_IO_PENDING)
    {
        Worker->Stats.AsyncSends += 1;
        Result = ERROR_SUCCESS;
    }
    else if (Result == ERROR_SUCCESS)
    {
        Worker->Stats.InlineSends += 1;

        //
        // Completed inline, put the context to the processing queue.
        //

        Context->IoResult = ERROR_SUCCESS;
        InsertTailList(&Worker->CompletionList, &Context->ListEntry);
    }
    else
    {
        printf("HttpSendHttpResponse failed in-line %d. Continuing...\n", Result);
    }

    return Result;
}


VOID
ProcessSendCompletion(
    __inout PIO_CONTEXT Context,
    __inout PWORKER_BLOCK Worker
)
{
    ULONG Result = Context->IoResult;

    if (Result != ERROR_SUCCESS)
    {
        printf("HttpSendHttpResponse failed %d. Continuing...\n", Result);
    }
    else
    {
        InterlockedIncrement(&g_ResponseSent);
    }

    Context->State = IoStateIdle;

    FreeIoContext(Context);
    Context = NULL;
}


ULONG
WaitForCompletions(
    __inout PWORKER_BLOCK Worker,
    __in ULONG Timeout
)
{
    ULONG Result = ERROR_SUCCESS;
    BOOL Success = FALSE;
    OVERLAPPED_ENTRY Entries[MAX_COMPLETIONS_PER_DEQUEUE] = {};
    ULONG EntryCount = 0;
    ULONG Index = 0;
    PIO_CONTEXT Context = NULL;
    ULONG MaxEntries = 0;
    ULONG IoStatus = ERROR_SUCCESS;

    MaxEntries = min(g_InitialReceivesPerThread, MAX_COMPLETIONS_PER_DEQUEUE);

    Success = GetQueuedCompletionStatusEx(
        g_CompletionPort,
        Entries,
        MaxEntries,
        &EntryCount,
        Timeout,
        FALSE);

    if (!Success)
    {
        Result = GetLastError();
        if (Result != WAIT_TIMEOUT)
        {
            printf("GetQueuedCompletionStatusEx failed %d\n", Result);
            goto Exit;
        }

        Result = ERROR_SUCCESS;

        goto Exit;
    }

    for (Index = 0; Index < EntryCount; Index++)
    {
        IoStatus = RtlNtStatusToDosError((NTSTATUS)Entries[Index].Internal);

        Context = CONTAINING_RECORD(
            Entries[Index].lpOverlapped,
            IO_CONTEXT,
            Overlapped);

        Context->IoResult = IoStatus;

        if (IoStatus == ERROR_SUCCESS ||
            IoStatus == ERROR_MORE_DATA)
        {
            Context->NumberOfBytesTransferred = Entries[Index].dwNumberOfBytesTransferred;
        }

        InsertTailList(&Worker->CompletionList, &Context->ListEntry);

        Context = NULL;
    }

Exit:

    return Result;
}

//
// Utility functions.
//

VOID
InsertTailList(
    __inout PLIST_ENTRY ListHead,
    __inout PLIST_ENTRY Entry
)
{
    PLIST_ENTRY Blink;

    Blink = ListHead->Blink;
    Entry->Flink = ListHead;
    Entry->Blink = Blink;
    Blink->Flink = Entry;
    ListHead->Blink = Entry;
    return;
}

BOOLEAN
IsListEmpty(
    __in const LIST_ENTRY* ListHead
)
{
    return (BOOLEAN)(ListHead->Flink == ListHead);
}

VOID
InitializeListHead(
    __out PLIST_ENTRY ListHead
)
{
    ListHead->Flink = ListHead->Blink = ListHead;
    return;
}

PLIST_ENTRY
RemoveHeadList(
    __inout PLIST_ENTRY ListHead
)
{
    PLIST_ENTRY Flink;
    PLIST_ENTRY Entry;

    Entry = ListHead->Flink;
    Flink = Entry->Flink;
    ListHead->Flink = Flink;
    Flink->Blink = ListHead;
    return Entry;
}
```
