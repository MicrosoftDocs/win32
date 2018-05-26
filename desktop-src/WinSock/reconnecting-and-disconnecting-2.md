---
Description: The default destination may be changed by simply calling WSPConnect again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous WSPConnect.
ms.assetid: b5f5ab97-03bd-4f5c-8808-d14ad5a56a5a
title: Reconnecting and Disconnecting
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reconnecting and Disconnecting

The default destination may be changed by simply calling [**WSPConnect**](/windows/win32/Ws2spi/?branch=master) again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous **WSPConnect**.

If the address supplied for the socket is all zeros, the socket will be disconnected — the default remote address will be indeterminate, so [**WSPSend**](/windows/win32/Ws2spi/?branch=master) and [**WSPRecv**](/windows/win32/Ws2spi/?branch=master) calls will return the error code WSAENOTCONN, although [**WSPSendTo**](/windows/win32/Ws2spi/?branch=master) and [**WSPRecvFrom**](/windows/win32/Ws2spi/?branch=master) may still be used.

 

 



