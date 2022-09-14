---
description: Windows Installer developers can author tools that enable end users to use configurable merge modules.
ms.assetid: 5857b788-f1dd-41d0-b0ee-0872494e3c2c
title: Adding Module Configuration Capability to a Merge Tool
ms.topic: article
ms.date: 05/31/2018
---

# Adding Module Configuration Capability to a Merge Tool

To enable end users to use configurable merge modules, you can author merge and configuration tools to do the following:

-   Merge tools should call the functions in Mergemod.dll version 2.0 to merge the module. Earlier versions of Mergemod.dll cannot be used to configure merge modules.
-   Client configuration applications should interact with the merge module user to collect the user selections for configurable items.
-   Merge tools should expose configuration information authored into the merge module to the client application so that the client can use this information to query the user.
-   When a merge tool encounters a configurable item during a merge, it should call the client configuration tool for customization information obtained from the user. The merge tool should make the specified changes to the merge module.
-   Configuration applications should enable the user to provide choices for configurable items, but all the possible choices do not need to be revealed to the user. The merge tool can use default values for configurable items that the user does not select.
-   If a user does not provide customization information, merge tools should use the default configuration values that are specified in the merge module.
-   After a user gives the configuration tool specific selections, the merge tool calls Mergemod.dll to perform the merge.

 

 



