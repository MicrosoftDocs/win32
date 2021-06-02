---
description: Differences between local I/O and network I/O on Windows.
ms.assetid: 8a8f20bd-fa41-4f1a-b9bf-5f09683cd46c
title: Differences in Local and Network I/O
ms.topic: article
ms.date: 05/31/2018
---

# Differences in Local and Network I/O

There are some notable differences between local I/O and network I/O on Windows:

-   Network I/O support depends on the redirector and the network protocol.
-   Network I/O performance depends on how many network I/O operations are taking place and the speed of the network connection. Your application must be able to handle network I/O operations with servers that may be much faster or slower than your local machine, as well as transient changes in network capacity. In these cases, your application may need to allow more time for the operation to complete.
-   The functions you use to perform local file I/O may behave differently over the network. For example, a network I/O operation that takes a long time to complete may time out. In some situations, file handles may be left open indefinitely because of this. Another example is that functions may return error codes for your application to process that are specific to network I/O.

 

 



