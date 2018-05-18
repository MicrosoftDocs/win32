---
title: IrDA and accept
description: After an IrDA server application puts its server socket into listen mode, the IrDA server application calls the Windows Sockets accept function and blocks until an incoming connection is received.
ms.assetid: '9d39d89a-a209-4b8d-8869-a7c45caf7356'
keywords: ["IrDA and accept"]
---

# IrDA and accept

After an IrDA server application puts its server socket into listen mode, the IrDA server application calls the Windows Sockets [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function and blocks until an incoming connection is received.

The following sample demonstrates using the [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function for an IrDA application:

``` syntax
SOCKET NewSock;

while(1)
{
   sizeofSockAddr = sizeof(SOCKADDR_IRDA);

   if ((NewSock = accept(ServSock, (struct sockaddr *) &PeerSockAddr, &sizeofSockAddr)) 
        == INVALID_SOCKET)
   {
      // call WSAGetLastError
      // exit
   }

   // NewSock is a connected socket
   // create a new thread and pass it NewSock, return to accept() on main
   // or use NewSock here until done, then close it
}
```

An unusual characteristic of the [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function with IrDA is that it returns a new socket. The reason is that the server application may wish to continue accepting new inbound connections. To support that, the server typically creates a new thread to handle the new connection, then blocks again on another **accept** function call. There is no requirement that a simple server support multiple connections, and it is free to ignore the old listening socket until it is finished with the newly created socket. The [**SOCKADDR\_IRDA**](https://msdn.microsoft.com/library/windows/desktop/ms740502) structure passed to the **accept** function is filled in with the peer's addresses, and can usually be ignored.

 

 




