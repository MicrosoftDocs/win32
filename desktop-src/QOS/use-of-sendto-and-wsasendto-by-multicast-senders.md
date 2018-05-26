---
title: Use of Sendto and WSASendTo by Multicast Senders
description: Use of Sendto and WSASendTo by multicast senders.
ms.assetid: af118e70-6c57-433e-b4ab-11050b39fca2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Use of Sendto and WSASendTo by Multicast Senders

Senders that join multicast sessions using the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function are required to call the [**sendto**](https://msdn.microsoft.com/library/windows/desktop/ms740148) or [**WSASendTo**](https://msdn.microsoft.com/library/windows/desktop/ms741693) function with the correct multicast session address to send data to the multicast session (even though the multicast session address is already provided with the **WSAJoinLeaf** function call). If the sending application calls the sendto or **WSASendTo** function specifying a multicast session address other than the address specified with the **WSAJoinLeaf** function call, the data will not receive QOS provisioning. This requirement is due to the fact that the sender's RSVP service generates the RSVP session based on the multicast session address specified in the call to the **WSAJoinLeaf** function.

Also note that QOS-enabled applications should only call the sendto or [**WSASendTo**](https://msdn.microsoft.com/library/windows/desktop/ms741693) function when acting as a multicast sender. Unicast (UDP or TCP) sender applications must specify their destination address using **WSAConnect**, and it is sufficient for that application to use the send or **WSASend** function calls, rather than the sendto or **WSASendTo** functions.

 

 




