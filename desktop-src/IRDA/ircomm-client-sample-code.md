---
title: IrCOMM Client Sample Code
description: The following sample code demonstrates the steps necessary to build an IrDA client that connects using 9-wire IrCOMM. For more information on IrDA and Windows Sockets programming elements, see IrDA Programming with Windows Sockets.
ms.assetid: a2b095b7-05c5-41af-bcb1-4146521723f8
keywords:
- Infrared Data Association IrDA , samples, IrCOMM client code
- samples IrDA , client code
- code IrDA , client
- IrCOMM IrDA , client sample code
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IrCOMM Client Sample Code

The following sample code demonstrates the steps necessary to build an IrDA client that connects using 9-wire IrCOMM. For more information on IrDA and Windows Sockets programming elements, see [IrDA Programming with Windows Sockets](irda-programming-with-windows-sockets.md).


```C++
#include <windows.h>
#include <af_irda.h>

#pragma comment(lib, "ws2_32.lib")

#define IAS_QUERY_ATTRIB_MAX_LEN 32
#define DEVICE_LIST_LEN 5

void main()
{
    // discovery buffer
    BYTE          DevListBuff[sizeof(DEVICELIST) - sizeof(IRDA_DEVICE_INFO) + 
                              (sizeof(IRDA_DEVICE_INFO) * DEVICE_LIST_LEN)];
    int           DevListLen = sizeof(DevListBuff);
    PDEVICELIST   pDevList   = (PDEVICELIST) &amp;DevListBuff;
    int           DevNum;



    // buffer for IAS query
  BYTE        IASQueryBuff[sizeof(IAS_QUERY) - 3 + IAS_QUERY_ATTRIB_MAX_LEN];
  int         IASQueryLen = sizeof(IASQueryBuff);
  PIAS_QUERY  pIASQuery   = (PIAS_QUERY) &amp;IASQueryBuff;
        
    // for searching through peers IAS response
    BOOL          Found = FALSE;
    UCHAR        *pPI, *pPL, *pPV;
        
    // for the setsockopt call to enable 9 wire IrCOMM
    int           Enable9WireMode  = 1;

    SOCKADDR_IRDA DstAddrIR = { AF_IRDA, 0, 0, 0, 0, "IrDA:IrCOMM" };

    if ((pConn->Sock = socket(AF_IRDA, SOCK_STREAM, 0)) == INVALID_SOCKET)
    {
        // WSAGetLastError
    }

    // search for the peer device
    pDevList->numDevice = 0;
    if (getsockopt(pConn->Sock, SOL_IRLMP, IRLMP_ENUMDEVICES, (CHAR *) pDevList, &amp;DevListLen)
        == SOCKET_ERROR)
    {
        // WSAGetLastError
    }

    // if (pDevList->numDevice == 0)
    {
        // no devices found, tell the user
    }

    // assume first device, we should have a common dialog here
    memcpy(&amp;DstAddrIR.irdaDeviceID[0], &amp;pDevList->Device[0].irdaDeviceID[0], 4);

    // query the peer to check for 9wire IrCOMM support
    memcpy(&amp;pIASQuery->irdaDeviceID[0], &amp;pDevList->Device[0].irdaDeviceID[0], 4);

    // IrCOMM IAS attributes
    memcpy(&amp;pIASQuery->irdaClassName[0],  "IrDA:IrCOMM", 12);
    memcpy(&amp;pIASQuery->irdaAttribName[0], "Parameters",  11);

    if (getsockopt(pConn->Sock, SOL_IRLMP, IRLMP_IAS_QUERY,  (char *) pIASQuery, 
                   &amp;IASQueryLen) == SOCKET_ERROR)
    {
        // WSAGetLastError
    }

    if (pIASQuery->irdaAttribType != IAS_ATTRIB_OCTETSEQ)
    {
        // peer's IAS database entry for IrCOMM is bad
        // error
    }

    if (pIASQuery->irdaAttribute.irdaAttribOctetSeq.Len < 3)
    {
        // peer's IAS database entry for IrCOMM is bad
        // error
    }

    // search for the PI value 0x00 and check 9 wire, see IrCOMM spec.
    pPI = pIASQuery->irdaAttribute.irdaAttribOctetSeq.OctetSeq;
    pPL = pPI + 1;
    pPV = pPI + 2;

    while (1)
    {
        if (*pPI == 0 &amp;&amp; (*pPV & 0x04))
        {
            Found = TRUE;
            break;
        }
            
        if (pPL + *pPL >= pIASQuery->irdaAttribute.irdaAttribOctetSeq.OctetSeq + 
                          pIASQuery->irdaAttribute.irdaAttribOctetSeq.Len)
        {
            break;
        }
            
         pPI = pPL + *pPL;
         pPL = pPI + 1;
         pPV = pPI + 2;
    }

    if (! Found)
    {
        // peer doesn't support 9 wire mode
        // error
    }

    // enable 9wire mode before connect()
    if (setsockopt(ServSock, SOL_IRLMP, IRLMP_9WIRE_MODE, (const char *) &amp;Enable9WireMode,
                   sizeof(int))  == SOCKET_ERROR)
    {
        // WSAGetLastError
    }

    // nothing special for IrCOMM from now on...
    if (connect(pConn->Sock, (const struct sockaddr *) &amp;DstAddrIR, sizeof(SOCKADDR_IRDA)) 
        == SOCKET_ERROR)
    {
        // WSAGetLastError
    }
}
```



 

 




