---
description: A process can monitor a set of events that occur in a communications resource. For example, an application can use event monitoring to determine when the CTS (clear-to-send) and DSR (data-set-ready) signals change state.
ms.assetid: 5d2a7bf3-a972-474b-b8ca-da3351f1e59c
title: Communications Events
ms.topic: article
ms.date: 05/31/2018
---

# Communications Events

A process can monitor a set of events that occur in a communications resource. For example, an application can use event monitoring to determine when the CTS (clear-to-send) and DSR (data-set-ready) signals change state.

A process can monitor events on a given communications resource by using the [**SetCommMask**](/windows/desktop/api/Winbase/nf-winbase-setcommmask) function to create an event mask. To determine the current event mask for a communications resource, a process can use the [**GetCommMask**](/windows/desktop/api/Winbase/nf-winbase-getcommmask) function. The following values specify events that can be monitored.



| Value           | Meaning                                                                                                                                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EV\_BREAK**   | A break was detected on input.                                                                                                                                                                                                                    |
| **EV\_CTS**     | The CTS (clear-to-send) signal changed state.                                                                                                                                                                                                     |
| **EV\_DSR**     | The DSR (data-set-ready) signal changed state.                                                                                                                                                                                                    |
| **EV\_ERR**     | A line-status error occurred. Line-status errors are **CE\_FRAME**, **CE\_OVERRUN**, and **CE\_RXPARITY**.                                                                                                                                        |
| **EV\_RING**    | A ring indicator was detected.                                                                                                                                                                                                                    |
| **EV\_RLSD**    | The RLSD (receive-line-signal-detect) signal changed state.                                                                                                                                                                                       |
| **EV\_RXCHAR**  | A character was received and placed in the input buffer.                                                                                                                                                                                          |
| **EV\_RXFLAG**  | The event character was received and placed in the input buffer. The event character is specified in the device's [**DCB**](/windows/desktop/api/Winbase/ns-winbase-dcb) structure, which is applied to a serial port by using the [**SetCommState**](/windows/desktop/api/Winbase/nf-winbase-setcommstate) function. |
| **EV\_TXEMPTY** | The last character in the output buffer was sent.                                                                                                                                                                                                 |



 

After a set of events is specified, a process uses the [**WaitCommEvent**](/windows/desktop/api/Winbase/nf-winbase-waitcommevent) function to wait for one of the events to occur. **WaitCommEvent** can be used synchronously or as an overlapped operation. For additional information about executing a function as an overlapped operation, see [Synchronization](/windows/desktop/Sync/synchronization).

When one of the events specified in the event mask occurs, the process completes the wait operation and sets an event mask variable to indicate the type of event detected. If the [**SetCommMask**](/windows/desktop/api/Winbase/nf-winbase-setcommmask) is called for a communications resource while a wait is pending for that resource, [**WaitCommEvent**](/windows/desktop/api/Winbase/nf-winbase-waitcommevent) returns an error.

The [**WaitCommEvent**](/windows/desktop/api/Winbase/nf-winbase-waitcommevent) function detects events that have occurred since the last call to [**SetCommMask**](/windows/desktop/api/Winbase/nf-winbase-setcommmask) or **WaitCommEvent**. For example, if you specify the **EV\_RXCHAR** event as a wait-satisfying event, a call to **WaitCommEvent** will be satisfied if there are characters in the driver's input buffer that have arrived since the last call to **WaitCommEvent** or **SetCommMask**. Thus, given the following pseudocode, any characters received between T1 and T2 will satisfy the next call to **WaitCommEvent**.


```C++
while (!bFinished) 
{ 
    WaitCommEvent(args)
 
T1: // Read bytes 
    // Process bytes 

T2: 
}
```



When monitoring an event that occurs when a signal (CTS, DSR, and so on) changes state, [**WaitCommEvent**](/windows/desktop/api/Winbase/nf-winbase-waitcommevent) reports the change, but not the current state. To query the current state of the CTS (clear-to-send), DSR (data-set-ready), RLSD (receive-line-signal-detect), and ring indicator signals, a process can use the [**GetCommModemStatus**](/windows/desktop/api/Winbase/nf-winbase-getcommmodemstatus) function.

 

 
