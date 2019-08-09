---
title: Get Functions
description: The network management get functions retrieve information about a domain. You can also call these functions to retrieve information about local, global, workstation, and server user accounts.
ms.assetid: 9c97420d-bc8a-42c9-b7ea-3d2ebc0034b3
ms.topic: article
ms.date: 05/31/2018
---

# Get Functions

The network management get functions retrieve information about a domain. You can also call these functions to retrieve information about local, global, workstation, and server user accounts.

The network management get functions are listed following.



| Function                                                               | Description                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetGetAnyDCName**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgetanydcname)                             | Returns the name of any domain controller for a domain that is directly trusted by a specified server.                                   |
| [**NetGetDCName**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgetdcname)                                   | Returns the name of the primary domain controller (PDC) for the specified domain.                                                        |
| [**NetGetDisplayInformationIndex**](/windows/desktop/api/Lmaccess/nf-lmaccess-netgetdisplayinformationindex) | Returns the index of the first display information entry whose name begins with a specified string or alphabetically follows the string. |
| [**NetQueryDisplayInformation**](/windows/desktop/api/Lmaccess/nf-lmaccess-netquerydisplayinformation)       | Returns user, computer, or global group account information.                                                                             |



 

The information returned by the [**NetQueryDisplayInformation**](/windows/desktop/api/Lmaccess/nf-lmaccess-netquerydisplayinformation) function is available at the following levels:

-   [**NET\_DISPLAY\_GROUP**](/windows/desktop/api/Lmaccess/ns-lmaccess-net_display_group)
-   [**NET\_DISPLAY\_MACHINE**](/windows/desktop/api/Lmaccess/ns-lmaccess-net_display_machine)
-   [**NET\_DISPLAY\_USER**](/windows/desktop/api/Lmaccess/ns-lmaccess-net_display_user)

 

 




