---
title: Synchronous Operations
description: When RasDial is invoked as a synchronous operation, the function does not return until the connection has been established or an error occurs.
ms.assetid: f165b4a7-00fb-4888-8225-8fd106e113f2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Synchronous Operations

When [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) is invoked as a synchronous operation, the function does not return until the connection has been established or an error occurs. Synchronous mode provides a simple way for a RAS client to establish a connection. The client can simply call **RasDial**, wait for the function to return, and then call the [**RasGetConnectStatus**](/windows/win32/Ras/nf-ras-rasgetconnectstatusa?branch=master) function to determine whether the connection operation was successful. Once the connection has been established, the client application can terminate without breaking the connection. If an error occurs, the client application must [shut down the connection operation](disconnecting.md) before terminating.

The disadvantage of synchronous mode is that the client does not receive progress notifications as the connection operation proceeds. As a workaround for this lack of progress notifications, a synchronous mode client can use a separate thread that calls [**RasGetConnectStatus**](/windows/win32/Ras/nf-ras-rasgetconnectstatusa?branch=master) to poll for and display the current state. However, for RAS clients that want to receive progress information, the preferred technique is to invoke [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) asynchronously.

 

 




