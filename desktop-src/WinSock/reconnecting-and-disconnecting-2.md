---
description: The default destination may be changed by simply calling WSPConnect again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous WSPConnect.
ms.assetid: b5f5ab97-03bd-4f5c-8808-d14ad5a56a5a
title: Reconnecting and Disconnecting
ms.topic: article
ms.date: 05/31/2018
---

# Reconnecting and Disconnecting

The default destination may be changed by simply calling [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85)) again, even if the socket is already connected. Any datagrams queued for receipt are discarded if the new address is different from the address specified in a previous **WSPConnect**.

If the address supplied for the socket is all zeros, the socket will be disconnected — the default remote address will be indeterminate, so [**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85)) and [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) calls will return the error code WSAENOTCONN, although [**WSPSendTo**](/previous-versions/windows/desktop/legacy/ms742291(v=vs.85)) and [**WSPRecvFrom**](/previous-versions/windows/desktop/legacy/ms742287(v=vs.85)) may still be used.

 

 
