---
description: 'Several options are available for receiving completion indications, thus providing applications with appropriate levels of flexibility. These include: waiting (or blocking) on event objects, polling event objects, and socket I/O completion routines.'
ms.assetid: 071cf198-6b4c-445e-9bd9-044f57f994a3
title: Receiving Completion Indications
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Completion Indications

Several options are available for receiving completion indications, thus providing applications with appropriate levels of flexibility. These include: waiting (or blocking) on event objects, polling event objects, and socket I/O completion routines.

## Blocking and Waiting for Completion Indication

Applications can block while waiting for one or more event objects to become set using the [**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents) function. In Windows implementations, the process or thread truly blocks. Since Windows Sockets 2 event objects are implemented as Windows events, the native Windows function, [**WaitForMultipleObjects**](/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjects) can also be used for this purpose. This is especially useful if the thread needs to wait on both socket and nonsocket events.

## Polling for Completion Indication

Applications that prefer not to block can use the [**WSAGetOverlappedResult**](/windows/desktop/api/Winsock2/nf-winsock2-wsagetoverlappedresult) function to poll for the completion status associated with any particular event object. This function indicates whether or not the overlapped operation has completed, and if completed, arranges for the [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) function to retrieve the error status of the overlapped operation.

## Using Socket I/O Completion Routines

The functions used to initiate overlapped I/O ( [**WSASend**](/windows/desktop/api/Winsock2/nf-winsock2-wsasend), [**WSASendTo**](/windows/desktop/api/Winsock2/nf-winsock2-wsasendto), [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv), [**WSARecvFrom**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecvfrom)) all take *lpCompletionRoutine* as an optional input parameter. This is a pointer to an application-specific function that is called after a successfully initiated overlapped I/O operation completes (successfully or otherwise). The completion routine follows the same rules as stipulated for Windows file I/O completion routines. That is, the completion routine is not invoked until the thread is in an alertable wait state, such as when the function [**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents) is invoked with the `fAlertable` flag set. An application that uses the completion routine option for a particular overlapped I/O request may not use the wait option of [**WSAGetOverlappedResult**](/windows/desktop/api/Winsock2/nf-winsock2-wsagetoverlappedresult) for that same overlapped I/O request.

The transports allow an application to invoke send and receive operations from within the context of the socket I/O completion routine and guarantee that, for a given socket, I/O completion routines will not be nested. This permits time-sensitive data transmissions to occur entirely within a preemptive context.

## Summary of Overlapped Completion Indication Mechanisms

The particular overlapped I/O completion indication to be used for a given overlapped operation is determined by whether the application supplies a pointer to a completion function, whether a [**WSAOVERLAPPED**](/windows/desktop/api/Winsock2/ns-winsock2-wsaoverlapped) structure is referenced, and by the value of the **hEvent** member within the **WSAOVERLAPPED** structure (if supplied). The following table summarizes the completion semantics for an overlapped socket and shows the various combinations of *lpOverlapped*, **hEvent**, and *lpCompletionRoutine*:

| *lpOverlapped* | hEvent         | *lpCompletionRoutine* | Completion indication                                                                                                                                                                                                    |
|----------------|----------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NULL           | Not applicable | Ignored               | Operation completes synchronously. It behaves as if it were a nonoverlapped socket.                                                                                                                                      |
| !NULL          | NULL           | NULL                  | Operation completes overlapped, but there is no Windows Sockets 2-supported completion mechanism. The completion port mechanism (if supported) can be used in this case. Otherwise, there is no completion notification. |
| !NULL          | !NULL          | NULL                  | Operation completes overlapped, notification by signaling event object.                                                                                                                                                  |
| !NULL          | Ignored        | !NULL                 | Operation completes overlapped, notification by scheduling completion routine.                                                                                                                                           |



 

 

 
