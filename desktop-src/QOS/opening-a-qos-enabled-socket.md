---
title: Opening a QOS-enabled Socket
description: The services and service quality guarantees provided by the RSVP SP require a QOS-enabled socket.
ms.assetid: 'a1ab2f67-2e66-4e20-831e-f6e970352329'
---

# Opening a QOS-enabled Socket

The services and service quality guarantees provided by the RSVP SP require a QOS-enabled socket.

**Note**  RSVP is not supported as of Windows XP.

**To find a QOS-enabled protocol**

1.  Call the [**WSAEnumProtocols**](https://msdn.microsoft.com/library/windows/desktop/ms741574) function to enumerate the existing protocols.
2.  Loop through the enumerated protocols to find a protocol that supports quality of service. QOS support is indicated by the presence of the XP1\_QOS\_SUPPORTED flag in **dwServiceFlags1** in the [**WSAPROTOCOL\_INFO**](https://msdn.microsoft.com/library/windows/desktop/ms741675) structure.
3.  Call the [**WSASocket**](https://msdn.microsoft.com/library/windows/desktop/ms742212) function, and pass a pointer to the [**WSAPROTOCOL\_INFO**](https://msdn.microsoft.com/library/windows/desktop/ms741675) structure corresponding to the QOS-enabled protocol. Note that the RSVP SP requires an overlapped socket. Create the socket in overlapped mode by setting the WSA\_FLAG\_OVERLAPPED flag in the *dwFlags* parameter of the **WSASocket** function.

> [!Note]  
> Do not attempt to use the [**WSADuplicateSocket**](https://msdn.microsoft.com/library/windows/desktop/ms741565) function to create QOS-enabled sockets; the **WSADuplicateSocket** function cannot be used on a QOS-enabled socket. Attempting to do so will result in the return of a WSAEINVAL error.

 

 

 




