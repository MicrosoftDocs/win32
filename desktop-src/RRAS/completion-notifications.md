---
title: Completion Notifications
description: The Remote Access Connection Manager continues progress notifications until the connection operation has been completed.
ms.assetid: 2c3b0d03-1cb7-4fa4-a7fa-bcfe623b791f
ms.topic: article
ms.date: 05/31/2018
---

# Completion Notifications

The Remote Access Connection Manager continues progress notifications until the connection operation has been completed. This occurs in the following situations:

-   The handler receives a RASCS\_Connected, or RASCS\_Disconnected notification. The RAS client application can exit without breaking any established connection.
-   An error occurs. The handler receives a notification indicating the error and the connection state when the error occurred. The RAS client application can exit.

The RAS client application should not assume the connection operation is complete after calling [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa). It should wait for one of the preceding conditions before exiting.

 

 




