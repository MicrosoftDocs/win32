---
description: Windows Installer performs the following actions during the removal of an application when the package contains isolated components. Typically, Component\_Shared is a DLL that is shared by Component\_Application and other client executables.
ms.assetid: 26343a01-9a06-43d5-bbe3-959faf51739d
title: Removal of Isolated Components
ms.topic: article
ms.date: 05/31/2018
---

# Removal of Isolated Components

Windows Installer performs the following actions during the removal of an application when the package contains isolated components. Typically, Component\_Shared is a DLL that is shared by Component\_Application and other client executables.

## Uninstall

-   Remove the files of Component\_Shared from the folder containing Component\_Application only if Component\_Application is also being removed.
-   If the msidbComponentAttributesSharedDllRefCount bit is set in the [Component table](component-table.md) decrement the SharedDLL refcount.
-   Remove the .LOCAL zero-byte file from the folder containing Component\_Application.
-   Remove Component\_Application from the client list of Component\_Shared.
-   Remove all of the resources of Component\_Application as usual.

If there are other products remaining on the client list of Component\_Shared:

-   Remove no files from the shared location of Component\_Shared.

If the SharedDLL refcount for Component\_Shared is 0 after being decremented, or if there are no other remaining clients of Component\_Shared:

-   Remove the files of Component\_Shared from the shared location.
-   Process all uninstall actions with respect to this component.

 

 



