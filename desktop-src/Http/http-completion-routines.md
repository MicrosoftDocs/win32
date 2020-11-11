---
title: HTTP Completion Routines
description: Applications have several options for receiving completion indications and providing some flexibility for developers.
ms.assetid: c48a64d2-b6c8-4694-8600-f84751954bad
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Completion Routines

Applications have several options for receiving completion indications and providing some flexibility for developers. The options are to block while waiting for an API call to complete or to use completion routines for asynchronous operations. The advantage of using asynchronous operations is an increase in responsiveness of the application.

## Blocked I/O

Applications can block while waiting for the API call to complete by setting the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure to **NULL**. This truly blocks all operations on the thread. For example, in calls to [**HttpWaitForDisconnect**](/windows/desktop/api/Http/nf-http-httpwaitfordisconnect), the call blocks until the connection is broken.

## Asynchronous I/O

Applications that prefer not to block can use the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure to obtain the completion results. The application supplies a pointer to an **OVERLAPPED** structure, which is used with an event object or a completion port. With an I/O completion port, an HTTP handle is used as a file handle would be in an asynchronous file I/O operation. The following table summarizes the completion options available to the applications.



| Overlapped structure | Event object   | Completion port | Completion                                                                                                   |
|----------------------|----------------|-----------------|--------------------------------------------------------------------------------------------------------------|
| **NULL**             | Not Applicable | Ignored         | Operation completes synchronously.                                                                           |
| Non-**NULL**         | Non-**NULL**   | **NULL**        | Operation completes asynchronously. Overlapped notification is performed by signaling an event object.       |
| Non-**NULL**         | Ignored        | Non-**NULL**    | Operation completes asynchronously. Overlapped notification is performed by scheduling a completion routine. |



 

## Returning the Number of Bytes Read

Some of the functions that use the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure for asynchronous completion return a *pBytesReceived* (or *pBytesSent* or *pBytesRead*) parameter that indicates the number of bytes transferred synchronously. For asynchronous calls, this parameter should be set to **NULL**. For synchronous calls, the *pBytesReceived* parameter is optional and can be either **NULL** or non-**NULL**.

If the event object is used for asynchronous completion, the [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) function is called to determine the number of bytes read. If the completion port is used (the *hFile* parameter is associated with an I/O completion port), the application calls the [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function to determine the number of bytes read. If the asynchronous operations have not completed, applications can call the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function to obtain extended error information.

The following table summarizes the completion behavior for synchronous and asynchronous completion in functions such as [**HttpReceiveHttpRequest**](/windows/desktop/api/Http/nf-http-httpreceivehttprequest) that use the *pBytesReceived* parameter.



| pBytesReceived\* | pOverlapped  | Description                                                                             |
|------------------|--------------|-----------------------------------------------------------------------------------------|
| **NULL**         | **NULL**     | The application does not receive information on the number of bytes returned.           |
| **NULL**         | Non-**NULL** | Asynchronous operation, *pBytesReceived* is meaningless.                                |
| Non-**NULL**     | **NULL**     | Synchronous operation, number of bytes returned in *pBytesReceived*.                    |
| Non-**NULL**     | Non-**NULL** | Asynchronous operation, *pBytesReceived* is ignored even though it is not **NULL**.\*\* |



 

> [!Note]  
> \*This parameter can also be *pBytesSent* or *pBytesRead*.

 

> [!Note]  
> \*\*It is recommended that applications pass a **NULL** in *pBytesReceived* for asynchronous operations and obtain the number of bytes received from either [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) or [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus).

 

## Return Codes

The HTTP Server API returns three classes of codes for asynchronous function calls.

-   NO\_ERROR
-   ERROR\_IO\_PENDING
-   Any other [system error code](/windows/desktop/Debug/system-error-codes).

When ERROR\_IO\_PENDING or NO\_ERROR are returned from the asynchronous function call, users should expect the event or completion routine to be signaled. Calling the [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) function for the event or the [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function for the completion port returns the completion status. In addition, if NO\_ERROR is returned, applications can perform post-processing on the same thread that made the API call.

If the HTTP Server API returns anything other than ERROR\_IO\_PENDING or NO\_ERROR, from the asynchronous function call, the completion routine is not signaled, and the error is directly returned by the API.

 

 