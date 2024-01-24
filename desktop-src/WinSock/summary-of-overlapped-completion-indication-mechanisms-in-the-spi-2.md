---
description: Summary of overlapped completion indication mechanisms in the Windows Sockets (Winsock) SPI.
ms.assetid: 2306b884-7d3a-4002-928e-54537571e5f8
title: Summary of Overlapped Completion Indication Mechanisms in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Summary of Overlapped Completion Indication Mechanisms in the SPI

The following table summarizes the completion semantics for an overlapped socket, showing the various combination of *lpOverlapped*, **hEvent**, and *lpCompletionRoutine*.



| *lpOverlapped* | **hEvent**     | *lpCompletionRoutine* | Completion indication                                                                                                                                                                                                        |
|----------------|----------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NULL           | Not applicable | Ignored               | Operation completes synchronously, that is, it behaves as if it were a nonoverlapped socket.                                                                                                                                 |
| not NULL       | NULL           | NULL                  | Operation completes overlapped, but there is no Windows Sockets 2-supported completion mechanism. The completion port mechanism (if supported) may be used in this case, otherwise there will be no completion notification. |
| not NULL       | not NULL       | NULL                  | Operation completes overlapped, notification by signaling event object.                                                                                                                                                      |
| not NULL       | Ignored        | not NULL              | Operation completes overlapped, notification by scheduling completion routine.                                                                                                                                               |



 

 

 



