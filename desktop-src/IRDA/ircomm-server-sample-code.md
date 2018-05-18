---
title: IrCOMM Server Sample Code
description: The following code sample demonstrates the steps necessary to build an IrDA server that listens for incoming IrCOMM connections. For more information on IrDA and Windows Sockets programming elements, see IrDA Programming with Windows Sockets.
ms.assetid: '9dcb0955-d42d-4cf0-ae23-e6307adb262a'
keywords: ["Infrared Data Association IrDA , samples", "IrCOMM code IrDA", "IrCOMM IrDA , server sample code"]
---

# IrCOMM Server Sample Code

The following code sample demonstrates the steps necessary to build an IrDA server that listens for incoming IrCOMM connections. For more information on IrDA and Windows Sockets programming elements, see [IrDA Programming with Windows Sockets](irda-programming-with-windows-sockets.md).


```C++
#include <windows.h>
#include <af_irda.h>

#pragma comment(lib, "ws2_32.lib")

#define IAS_SET_ATTRIB_MAX_LEN 32

void main()
{

    // buffer for IAS set
    BYTE          IASSetBuff[sizeof(IAS_SET) - 3 + IAS_SET_ATTRIB_MAX_LEN];
    int           IASSetLen = sizeof(IASSetBuff);
    PIAS_SET      pIASSet   = (PIAS_SET) &amp;IASSetBuff;

    // for the setsockopt call to enable 9 wire IrCOMM
    int           Enable9WireMode  = 1;

    // server sockaddr with IrCOMM name
    SOCKADDR_IRDA ServSockAddr = { AF_IRDA, 0, 0, 0, 0, "IrDA:IrCOMM" };
    SOCKADDR_IRDA PeerSockAddr;
    int           sizeofSockAddr;

    SOCKET        ServSock;
    SOCKET        NewSock;

    if ((ServSock = socket(AF_IRDA, SOCK_STREAM, 0)) == INVALID_SOCKET)
    {
        // WSAGetLastError
    }
        
    // add IrCOMM IAS attributes for 3 wire cooked and 9 wire raw, see IrCOMM spec
    memcpy(&amp;pIASSet->irdaClassName[0],  "IrDA:IrCOMM", 12);
    memcpy(&amp;pIASSet->irdaAttribName[0], "Parameters",  11);
        
    pIASSet->irdaAttribType                       = IAS_ATTRIB_OCTETSEQ;
    pIASSet->irdaAttribute.irdaAttribOctetSeq.Len = 6;

    memcpy(&amp;pIASSet->irdaAttribute.irdaAttribOctetSeq.OctetSeq[0],
           "\000\001\006\001\001\001", 6);

    if (setsockopt(ServSock, SOL_IRLMP, IRLMP_IAS_SET, (const char *) pIASSet, IASSetLen) 
        == SOCKET_ERROR)
    {
        // WSAGetLastError
    }

    // enable 9wire mode before bind()
    if (setsockopt(ServSock, SOL_IRLMP, IRLMP_9WIRE_MODE, (const char *) &amp;Enable9WireMode,
                   sizeof(int))  == SOCKET_ERROR)
    {
        // WSAGetLastError
    }

    if (bind(ServSock, (const struct sockaddr *) &amp;ServSockAddr, sizeof(SOCKADDR_IRDA))
        == SOCKET_ERROR)
    {
        // WSAGetLastError
    }

    // nothing special for IrCOMM from now on...
    if (listen(ServSock, SOMAXCONN) == SOCKET_ERROR)
    {
        // WSAGetLastError
    }
}
```



 

 




