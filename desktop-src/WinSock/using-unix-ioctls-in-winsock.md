---
Description: 'The SIOCGIFCONF command provided by most UNIX implementations is supported in the form of WSAIoctl and WSPIoctl functions with the command SIO\_GET\_INTERFACE\_LIST. This command returns the list of configured interfaces and their parameters.'
ms.assetid: 'c5028dae-052a-444c-837c-cd8d6d901b6c'
title: Using UNIX Ioctls in Winsock
---

# Using UNIX Ioctls in Winsock

The **SIOCGIFCONF** command provided by most UNIX implementations is supported in the form of [**WSAIoctl**](wsaioctl-2.md) and [**WSPIoctl**](wspioctl-2.md) functions with the command **SIO\_GET\_INTERFACE\_LIST**. This command returns the list of configured interfaces and their parameters.

> [!Note]  
> Support of this command is mandatory for Windows Sockets 2-compliant TCP/IP service providers.

 

The parameter *lpvOutBuffer* points to the buffer in which [**WSAIoctl**](wsaioctl-2.md) and [**WSPIoctl**](wspioctl-2.md) store the information about interfaces. The number of interfaces (number of structures returned in *lpvOutBuffer*) can be determined based on the actual length of the output buffer returned in *lpcbBytesReturned*.

 

 



