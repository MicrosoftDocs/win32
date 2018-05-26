---
title: IrDA and getsockopt Using IRLMP\_ENUMDEVICES
description: The Windows Sockets getsockopt function is used to run a discovery.
ms.assetid: 56efd580-e8da-4787-b24e-794f5c402336
keywords:
- IrDA and getsockopt using IRLMP_ENUMDEVICES
- Infrared Data Association IrDA , tasks, initiating a discovery
- Infrared Data Association IrDA , tasks, running a lazy discovery
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IrDA and getsockopt Using IRLMP\_ENUMDEVICES

The Windows Sockets [**getsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms738544) function is used to run a discovery. Before a connection can be initiated, a device address must be obtained by performing a discovery operation. An extension to the Winsock **getsockopt** call returns a list of all currently visible IrDA devices. A device address returned from this list is copied into a [**SOCKADDR\_IRDA**](https://msdn.microsoft.com/library/windows/desktop/ms740502) structure to be used by the [**connect**](https://msdn.microsoft.com/library/windows/desktop/ms737625) function call.

**To initiate a discovery**

-   Performing a [**getsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms738544) function call with the IRLMP\_ENUMDEVICES option causes a single discovery to be run on each idle adapter. The list of discovered devices and cached devices (on active adapters) will be returned immediately. The following code demonstrates this:
    ```C++
    #include <windows.h>
    #include <af_irda.h>

    #pragma comment(lib, "ws2_32.lib")

    #define DEVICE_LIST_LEN    10

    void main()
    {
        SOCKADDR_IRDA     DestSockAddr = { AF_IRDA, 0, 0, 0, 0, "SampleIrDAService" };
         
        unsigned char    DevListBuff[sizeof(DEVICELIST) -
                 sizeof(IRDA_DEVICE_INFO) +
                 (sizeof(IRDA_DEVICE_INFO) * DEVICE_LIST_LEN)];
        int        DevListLen    = sizeof(DevListBuff);
        PDEVICELIST    pDevList    = (PDEVICELIST) &amp;DevListBuff;
      int i;
      
        pDevList->numDevice = 0;

        // Sock is not in connected state
        if (getsockopt(Sock, SOL_IRLMP, IRLMP_ENUMDEVICES,
                       (char *) pDevList, &amp;DevListLen) == SOCKET_ERROR)
        {
        // WSAGetLastError 
        }

        if (pDevList->numDevice == 0)
        {
            // no devices discovered or cached
            // not a bad idea to run a couple of times
        }
        else
        {
            // one per discovered device
            for (i = 0; i < (int) pDevList->numDevice; i++)
            {
            // typedef struct _IRDA_DEVICE_INFO
            // {
                    //    u_char    irdaDeviceID[4];
                    //    char    irdaDeviceName[22];
                    //    u_char    irdaDeviceHints1;
                    //     u_char    irdaDeviceHints2;
                    //    u_char    irdaCharSet;
            // } _IRDA_DEVICE_INFO;

                // pDevList->Device[i]. see _IRDA_DEVICE_INFO for fields
                // display the device names and let the user select one
            }
        }

        // assume the user selected the first device [0]
        memcpy(&amp;DestSockAddr.irdaDeviceID[0], &amp;pDevList->Device[0].irdaDeviceID[0], 4);

        if (connect(Sock, (const struct sockaddr *) &amp;DestSockAddr,
                    sizeof(SOCKADDR_IRDA)) == SOCKET_ERROR)
        {
            // WSAGetLastError
        }
    }
    ```

    

**To run a lazy discovery**

-   It is also possible to run a lazy discovery — the application will not be notified until the discovered device list changes from the last discovery run by the stack.

 

 




