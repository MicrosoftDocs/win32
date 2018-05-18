---
title: Get Functions
description: The network management get functions retrieve information about a domain. You can also call these functions to retrieve information about local, global, workstation, and server user accounts.
ms.assetid: '9c97420d-bc8a-42c9-b7ea-3d2ebc0034b3'
---

# Get Functions

The network management get functions retrieve information about a domain. You can also call these functions to retrieve information about local, global, workstation, and server user accounts.

The network management get functions are listed following.



| Function                                                               | Description                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetGetAnyDCName**](netgetanydcname.md)                             | Returns the name of any domain controller for a domain that is directly trusted by a specified server.                                   |
| [**NetGetDCName**](netgetdcname.md)                                   | Returns the name of the primary domain controller (PDC) for the specified domain.                                                        |
| [**NetGetDisplayInformationIndex**](netgetdisplayinformationindex.md) | Returns the index of the first display information entry whose name begins with a specified string or alphabetically follows the string. |
| [**NetQueryDisplayInformation**](netquerydisplayinformation.md)       | Returns user, computer, or global group account information.                                                                             |



 

The information returned by the [**NetQueryDisplayInformation**](netquerydisplayinformation.md) function is available at the following levels:

-   [**NET\_DISPLAY\_GROUP**](net-display-group-str.md)
-   [**NET\_DISPLAY\_MACHINE**](net-display-machine-str.md)
-   [**NET\_DISPLAY\_USER**](net-display-user-str.md)

 

 




