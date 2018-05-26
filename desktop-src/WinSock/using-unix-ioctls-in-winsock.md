---
Description: The SIOCGIFCONF command provided by most UNIX implementations is supported in the form of WSAIoctl and WSPIoctl functions with the command SIO\_GET\_INTERFACE\_LIST. This command returns the list of configured interfaces and their parameters.
ms.assetid: c5028dae-052a-444c-837c-cd8d6d901b6c
title: Using UNIX Ioctls in Winsock
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using UNIX Ioctls in Winsock

The **SIOCGIFCONF** command provided by most UNIX implementations is supported in the form of [**WSAIoctl**](/windows/win32/Winsock2/nf-winsock2-wsaioctl?branch=master) and [**WSPIoctl**](/windows/win32/Ws2spi/?branch=master) functions with the command **SIO\_GET\_INTERFACE\_LIST**. This command returns the list of configured interfaces and their parameters.

> [!Note]  
> Support of this command is mandatory for Windows Sockets 2-compliant TCP/IP service providers.

 

The parameter *lpvOutBuffer* points to the buffer in which [**WSAIoctl**](/windows/win32/Winsock2/nf-winsock2-wsaioctl?branch=master) and [**WSPIoctl**](/windows/win32/Ws2spi/?branch=master) store the information about interfaces. The number of interfaces (number of structures returned in *lpvOutBuffer*) can be determined based on the actual length of the output buffer returned in *lpcbBytesReturned*.

 

 



