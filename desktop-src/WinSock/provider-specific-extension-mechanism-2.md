---
description: The WSAIoctl function enables service providers to offer provider-specific feature extensions.
ms.assetid: 8b0d86ad-2f8b-4f5e-a8a6-839cb8dba4d8
title: Provider-Specific Extension Mechanism
ms.topic: article
ms.date: 05/31/2018
---

# Provider-Specific Extension Mechanism

The [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function enables service providers to offer provider-specific feature extensions. This mechanism assumes, of course, that an application is aware of a particular extension and understands both the semantics and syntax involved. Such information would typically be supplied by the service provider vendor.

To invoke an extension function, the application must first ask for a pointer to the desired function. This is done through the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function using the SIO\_GET\_EXTENSION\_FUNCTION\_POINTER command code. The input buffer to **WSAIoctl** contains an identifier for the desired extension function while the output buffer contains the function pointer itself. The application can then invoke the extension function directly without passing through the Ws2\_32.dll.

The identifiers assigned to extension functions are globally unique identifiers (GUIDs) that are allocated by service provider vendors. Vendors who create extension functions are urged to publish full details about the function including the syntax of the function prototype. This makes it possible for common and popular extension functions to be offered by more than one service provider vendor. An application can obtain the function pointer and use the function without needing to know anything about the particular service provider that implements the function.

On Windows Vista and later, new Winsock system extensions are exported directly from the Winsock DLL, so the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function is not needed to load these extensions. The new extension functions available on Windows Vista and later include the [**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll) and [**WSASendMsg**](/windows/desktop/api/winsock2/nf-winsock2-wsasendmsg) functions that are exported from *Ws2\_32.dll*.

 

 
