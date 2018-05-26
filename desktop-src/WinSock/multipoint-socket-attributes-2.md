---
Description: Multipoint socket attributes in Windows Sockets (Winsock).
ms.assetid: f6e779c6-dd9d-470e-aad9-715b69ad8c5f
title: Multipoint Socket Attributes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multipoint Socket Attributes

In some instances sockets joined to a multipoint session may have some behavioral differences from point-to-point sockets. For example, a d\_leaf socket in a rooted data plane scheme can only send information to the d\_root participant. This creates a need for the client to be able to indicate the intended use of a socket coincident with its creation. This is done through four multipoint attribute flags that can be set through the *dwFlags* parameter in [**WSPSocket**](/windows/win32/Ws2spi/nc-ws2spi-lpwspsocket?branch=master):

-   WSA\_FLAG\_MULTIPOINT\_C\_ROOT, for the creation of a socket acting as a c\_root, and only allowed if a rooted control plane is indicated in the corresponding [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) entry.
-   WSA\_FLAG\_MULTIPOINT\_C\_LEAF, for the creation of a socket acting as a c\_leaf, and only allowed if XP1\_SUPPORT\_MULTIPOINT is indicated in the corresponding [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) entry.
-   WSA\_FLAG\_MULTIPOINT\_D\_ROOT, for the creation of a socket acting as a d\_root, and only allowed if a rooted data plane is indicated in the corresponding [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) entry.
-   WSA\_FLAG\_MULTIPOINT\_D\_LEAF, for the creation of a socket acting as a d\_leaf, and only allowed if XP1\_SUPPORT\_MULTIPOINT is indicated in the corresponding [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) entry.

When creating a multipoint socket, exactly one of the two control plane flags, and one of the two data plane flags must be set in [**WSPSocket**](/windows/win32/Ws2spi/nc-ws2spi-lpwspsocket?branch=master)'s *dwFlags* parameter. Thus, the four possibilities for creating multipoint sockets are: "c\_root/d\_root", "c\_root/d\_leaf", "c\_leaf/d\_root", or "c\_leaf /d\_leaf".

 

 



