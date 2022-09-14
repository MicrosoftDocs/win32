---
description: Because the Winsock DLL itself is no longer supplied by each individual stack vendor, it is not possible for a stack vendor to offer extended functionality by adding entry points to the Winsock DLL.
ms.assetid: 5c71532a-c565-4f65-ab36-ca0e23190718
title: Function Extension Mechanism in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Function Extension Mechanism in the SPI

Because the Winsock DLL itself is no longer supplied by each individual stack vendor, it is not possible for a stack vendor to offer extended functionality by adding entry points to the Winsock DLL. To overcome this limitation, Winsock takes advantage of the new [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function to accommodate service providers who wish to offer provider-specific functionality extensions. This mechanism presupposes that an application is aware of a particular extension and understands both the semantics and syntax involved. Such information would typically be supplied by the service provider vendor.

To invoke an extension function, the application must first ask for a pointer to the desired function. This is done through the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function using the SIO\_GET\_EXTENSION\_FUNCTION\_POINTER command code. The input buffer to the **WSAIoctl** function contains an identifier for the desired extension function and the output buffer will contain the function pointer itself. The application can then invoke the extension function directly without passing through the Ws2\_32.dll.

The identifiers assigned to extension functions are globally unique identifiers (GUIDs) that are allocated by service provider vendors. Vendors who create extension functions are urged to publish full details about the function including the syntax of the function prototype. This facilitates common and/or popular extension functions to be offered by multiple service providers. An application can obtain the function pointer and use the function without needing to know anything about the particular service provider that implements the function.

 

 



