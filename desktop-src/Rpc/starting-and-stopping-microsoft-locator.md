---
title: Starting and Stopping Microsoft Locator
description: The RPC run-time libraries automatically start Microsoft Locator when necessary. You can manually stop and start the Locator if, for example, you need to clear the database while debugging a distributed application.
ms.assetid: 06b50a9f-b640-45b2-86e2-2bcea6c16c5c
ms.topic: article
ms.date: 05/31/2018
---

# Starting and Stopping Microsoft Locator

The RPC run-time libraries automatically start Microsoft Locator when necessary. You can manually stop and start the Locator if, for example, you need to clear the database while debugging a distributed application.

**To stop and start Microsoft Locator**

1.  From Control Panel, click the Services icon.

    The **Services** dialog box appears.

2.  In the **Service** dialog box, select **Microsoft Locator** and then click **Start** or **Stop**.

You can also start and stop Microsoft Locator from the command line by typing:

**net \[start/stop\] rpclocator**

Only an administrator can start Microsoft Locator once it is stopped. If stopped, it will be restarted as necessary by the RPC run-time libraries.

 

 




