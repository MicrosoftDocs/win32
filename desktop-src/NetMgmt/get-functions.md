---
title: Get Functions
description: The network management get functions retrieve information about a domain. You can also call these functions to retrieve information about local, global, workstation, and server user accounts.
ms.assetid: 9c97420d-bc8a-42c9-b7ea-3d2ebc0034b3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Get Functions

The network management get functions retrieve information about a domain. You can also call these functions to retrieve information about local, global, workstation, and server user accounts.

The network management get functions are listed following.



| Function                                                               | Description                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetGetAnyDCName**](/windows/win32/Lmaccess/nf-lmaccess-netgetanydcname?branch=master)                             | Returns the name of any domain controller for a domain that is directly trusted by a specified server.                                   |
| [**NetGetDCName**](/windows/win32/Lmaccess/nf-lmaccess-netgetdcname?branch=master)                                   | Returns the name of the primary domain controller (PDC) for the specified domain.                                                        |
| [**NetGetDisplayInformationIndex**](/windows/win32/Lmaccess/nf-lmaccess-netgetdisplayinformationindex?branch=master) | Returns the index of the first display information entry whose name begins with a specified string or alphabetically follows the string. |
| [**NetQueryDisplayInformation**](/windows/win32/Lmaccess/nf-lmaccess-netquerydisplayinformation?branch=master)       | Returns user, computer, or global group account information.                                                                             |



 

The information returned by the [**NetQueryDisplayInformation**](/windows/win32/Lmaccess/nf-lmaccess-netquerydisplayinformation?branch=master) function is available at the following levels:

-   [**NET\_DISPLAY\_GROUP**](/windows/win32/Lmaccess/ns-lmaccess-_net_display_group?branch=master)
-   [**NET\_DISPLAY\_MACHINE**](/windows/win32/Lmaccess/ns-lmaccess-_net_display_machine?branch=master)
-   [**NET\_DISPLAY\_USER**](/windows/win32/Lmaccess/ns-lmaccess-_net_display_user?branch=master)

 

 




