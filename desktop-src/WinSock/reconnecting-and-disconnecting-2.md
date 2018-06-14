---
Description: The default destination may be changed by simply calling WSPConnect again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous WSPConnect.
ms.assetid: b5f5ab97-03bd-4f5c-8808-d14ad5a56a5a
title: Reconnecting and Disconnecting
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reconnecting and Disconnecting

The default destination may be changed by simply calling [**WSPConnect**](https://msdn.microsoft.com/en-us/library/ms742272(v=VS.85).aspx) again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous **WSPConnect**.

If the address supplied for the socket is all zeros, the socket will be disconnected — the default remote address will be indeterminate, so [**WSPSend**](https://msdn.microsoft.com/en-us/library/ms742292(v=VS.85).aspx) and [**WSPRecv**](https://msdn.microsoft.com/en-us/library/ms742288(v=VS.85).aspx) calls will return the error code WSAENOTCONN, although [**WSPSendTo**](https://msdn.microsoft.com/en-us/library/ms742291(v=VS.85).aspx) and [**WSPRecvFrom**](https://msdn.microsoft.com/en-us/library/ms742287(v=VS.85).aspx) may still be used.

 

 



