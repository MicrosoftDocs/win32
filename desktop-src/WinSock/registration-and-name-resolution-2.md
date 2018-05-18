---
Description: 'Windows Sockets 2 is a set of functions that standardizes the way applications access and use the various network naming services.'
ms.assetid: 'e245475c-26cc-491f-b335-b1b6a816dc3c'
title: Registration and Name Resolution
---

# Registration and Name Resolution

Windows Sockets 2 is a set of functions that standardizes the way applications access and use the various network naming services. When using these functions, applications need not distinguish the widely differing protocols associated with name services such as DNS, NIS, X.500, SAP, etc. To maintain full backward compatibility with Windows Sockets 1.1, the existing **getXbyY** and asynchronous **WSAAsyncGetXbyY** database-lookup functions continue to be supported, but are implemented in the Windows Sockets service provider interface in terms of the new name resolution capabilities. For more information, see the [**getservbyname**](getservbyname-2.md) and [**getservbyport**](getservbyport-2.md) functions. Also, see [Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-spi-2.md).

This section describes registration and name resolution capabilities available to Winsock developers. The following list describes the topics in this section:

-   [Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
-   [Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)

## Related topics

<dl> <dt>

[About Winsock](about-winsock.md)
</dt> <dt>

[Using Winsock](using-winsock.md)
</dt> </dl>

 

 



