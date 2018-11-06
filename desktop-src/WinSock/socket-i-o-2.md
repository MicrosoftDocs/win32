---
Description: Using blocking I/O, nonblocking I/O with asynchronous notification of network events, and overlapped I/O with completion indication in Windows Sockets 2 (Winsock).
ms.assetid: 07f34177-72bc-4b2a-b655-57e53d1742b0
title: Socket I/O
ms.topic: article
ms.date: 05/31/2018
---

# Socket I/O

There are three primary ways of doing I/O in Windows Sockets 2:

-   Blocking I/O.
-   Nonblocking I/O along with asynchronous notification of network events.
-   Overlapped I/O with completion indication.

We describe each method in the following sections. Blocking I/O is the default behavior, nonblocking mode can be used on any socket that is placed into nonblocking mode, and overlapped I/O can only occur on sockets that are created with the overlapped attribute. It is also interesting to note that the two calls for sending: [**WSPSend**](https://msdn.microsoft.com/en-us/library/ms742292(v=VS.85).aspx) and [**WSPSendTo**](https://msdn.microsoft.com/en-us/library/ms742291(v=VS.85).aspx) and the two calls for receiving: [**WSPRecv**](https://msdn.microsoft.com/en-us/library/ms742288(v=VS.85).aspx) and [**WSPRecvFrom**](https://msdn.microsoft.com/en-us/library/ms742287(v=VS.85).aspx) each implement all three methods of I/O. Service providers determine how to perform the I/O operation based on socket modes, attributes, and the input parameter values.

 

 



