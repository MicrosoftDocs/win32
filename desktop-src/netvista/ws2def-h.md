---
Description: This section contains kernel mode network driver reference topics for the Ws2def.h header.
ms.assetid: 6D8CD301-12D7-4B37-83FC-5FE3D1714D64
title: Ws2def.h (Reference)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ws2def.h (Reference)

This section contains kernel mode network driver reference topics for the Ws2def.h header. This header is included in the Windows SDK as it is also shared with user mode networking applications.

The Ws2def.h header contains definitions for the Winsock2 specification. It is included in Winsock2.h. User mode applications should include Winsock2.h rather than including Ws2def.h directly. Ws2def.h cannot be included by a module that also includes Winsock.h.

> \[!Important\]
>
> This section's header topics contain pages for network driver reference: structures, enumerations, functions, and callbacks.
>
> For more information about definitions, macros, OIDs, status indications, and other data structures that are not part of network driver reference for this header, see [Ws2def.h](https://docs.microsoft.com/windows-hardware/drivers/network/ws2def-h).

 

## In this section



| Topic                                                           | Description                                                                                                                           |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**CMSGHDR**](/windows/desktop/api/ws2def/ns-ws2def-_wsacmsghdr)<br/>                           | The CMSGHDR structure defines the header for a control data object that is associated with a datagram.<br/>                     |
| [**SOCKADDR**](/windows/desktop/api/ws2def/ns-ws2def-sockaddr)<br/>                         | The SOCKADDR structure is a generic structure that specifies a transport address.<br/>                                          |
| [**SOCKADDR\_IN**](/windows/desktop/api/ws2def/ns-ws2def-sockaddr_in)<br/>                  | The SOCKADDR\_IN structure specifies a transport address and port for the [**AF\_INET**](https://www.bing.com/search?q=**AF\_INET**) address family.<br/> |
| [**SOCKADDR\_STORAGE**](/windows/desktop/api/ws2def/ns-ws2def-sockaddr_storage)<br/>        | The SOCKADDR\_STORAGE structure is a generic structure that specifies a transport address.<br/>                                 |
| [**SOCKET\_ADDRESS\_LIST**](/windows/desktop/api/ws2def/ns-ws2def-_socket_address_list)<br/> | The SOCKET\_ADDRESS\_LIST structure defines a variable-sized list of transport addresses.<br/>                                  |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Ws2def.h%20%28Reference%29%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




