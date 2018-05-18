---
Description: 'The default destination may be changed by simply calling WSPConnect again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous WSPConnect.'
ms.assetid: 'b5f5ab97-03bd-4f5c-8808-d14ad5a56a5a'
title: Reconnecting and Disconnecting
---

# Reconnecting and Disconnecting

The default destination may be changed by simply calling [**WSPConnect**](wspconnect-2.md) again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous **WSPConnect**.

If the address supplied for the socket is all zeros, the socket will be disconnected — the default remote address will be indeterminate, so [**WSPSend**](wspsend-2.md) and [**WSPRecv**](wsprecv-2.md) calls will return the error code WSAENOTCONN, although [**WSPSendTo**](wspsendto-2.md) and [**WSPRecvFrom**](wsprecvfrom-2.md) may still be used.

 

 



