---
title: Internet Connection Sharing
description: BITS can force a dial-up connection for home networks that use Microsoft Internet Connection Sharing if Connection Sharing is configured to dial out when computers on the network access the Internet.
ms.assetid: a0a05ddb-6ce4-4cf5-8953-cb7122702d17
ms.topic: article
ms.date: 05/31/2018
---

# Internet Connection Sharing

BITS can force a dial-up connection for home networks that use Microsoft Internet Connection Sharing if Connection Sharing is configured to dial out when computers on the network access the Internet. To prevent a forced dial-up connection, disable the **Establish a dial-up connection whenever a computer on my network attempts to access the Internet** option on the Connection Sharing host computer that shares its Internet connection.

Computers connected to the Connection Sharing host computer assume they have a network connection, so BITS will try to transfer files. If the dial-up option is disabled on the host computer and the host computer does not have an active connection, the transfers will fail with a transient error. BITS will retry the transfers periodically.

 

 




