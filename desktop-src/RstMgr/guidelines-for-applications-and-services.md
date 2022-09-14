---
title: Guidelines for Applications and Services
description: To reduce the number of system restarts when installing and servicing applications on Windows Vista or Windows Server 2008, you should observe the following guidelines to enable your application or service to be shut down cleanly and restarted.
ms.assetid: d0b9344f-05c6-4054-90b9-86942df50b3d
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Applications and Services

To reduce the number of system restarts when installing and servicing applications on Windows Vista or Windows Server 2008, you should observe the following guidelines to enable your application or service to be shut down cleanly and restarted.

-   Your applications and services should be prepared to be shut down and restarted by the system when this is necessary to install an update. Typically, when an update is installed, an application or service needs to be shut down because it currently holds an affected file in use. All applications or services that can hold a file in use during an update should be prepared to shut down cleanly.
-   Your applications should save user data and state information that are needed after a restart and should adhere to the guidelines that are described in the section [Guidelines for Applications](guidelines-for-applications.md).
-   Your services should adhere to the guidelines that are described in the section [Guidelines for Services](guidelines-for-services.md).
-   Restart Manager does not shut down [critical system services](critical-system-services.md); therefore, these services should limit the number of DLLs they depend on.

 

 




