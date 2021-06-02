---
description: A raw socket is a type of socket that allows access to the underlying transport provider. The use of raw sockets when porting applications to Winsock is not recommended for several reasons.
ms.assetid: b78c75b7-255c-4e85-9a88-0efb3b5f0e51
title: Raw Sockets
ms.topic: article
ms.date: 05/31/2018
---

# Raw Sockets

A raw socket is a type of socket that allows access to the underlying transport provider. The use of raw sockets when porting applications to Winsock is not recommended for several reasons.

The Windows Sockets specification does not mandate that a Winsock service provider support raw sockets, that is, sockets of type **SOCK\_RAW**. However, service providers are encouraged to supply raw socket support. A Windows Sockets-compliant application that wishes to use raw sockets should attempt to open the socket with the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) call, and if it fails either attempt to use another socket type or indicate the failure to the user.

On Windows 7, Windows Server 2008 R2, Windows Vista, and Windows XP with Service Pack 2 (SP2), the ability to send traffic over raw sockets has been restricted in several ways. For more information, see [TCP/IP Raw Sockets](tcp-ip-raw-sockets-2.md).

## Related topics

<dl> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket)
</dt> <dt>

[TCP/IP Raw Sockets](tcp-ip-raw-sockets-2.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> </dl>

 

 



