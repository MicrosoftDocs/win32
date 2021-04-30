---
description: The SIOCGIFCONF command provided by most UNIX implementations is supported in the form of WSAIoctl and WSPIoctl functions with the command SIO\_GET\_INTERFACE\_LIST. This command returns the list of configured interfaces and their parameters.
ms.assetid: c5028dae-052a-444c-837c-cd8d6d901b6c
title: Using UNIX Ioctls in Winsock
ms.topic: article
ms.date: 05/31/2018
---

# Using UNIX Ioctls in Winsock

The **SIOCGIFCONF** command provided by most UNIX implementations is supported in the form of [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) and [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) functions with the command **SIO\_GET\_INTERFACE\_LIST**. This command returns the list of configured interfaces and their parameters.

> [!Note]  
> Support of this command is mandatory for Windows Sockets 2-compliant TCP/IP service providers.

 

The parameter *lpvOutBuffer* points to the buffer in which [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) and [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) store the information about interfaces. The number of interfaces (number of structures returned in *lpvOutBuffer*) can be determined based on the actual length of the output buffer returned in *lpcbBytesReturned*.

 

 
