---
description: Windows Installer performs the following actions during installation of an application when the package contains isolated components. Typically, Component\_Shared is a DLL that is shared by Component\_Application and other client executables.
ms.assetid: fbc5dd86-5d38-4ce8-ab38-03c84cc77e80
title: Installation of Isolated Components
ms.topic: article
ms.date: 05/31/2018
---

# Installation of Isolated Components

Windows Installer performs the following actions during installation of an application when the package contains isolated components. Typically, Component\_Shared is a DLL that is shared by Component\_Application and other client executables.

## Installation

-   Copy the files of Component\_Shared into the same folder as Component\_Application only if Component\_Application is also being installed.
-   Create a zero-byte file with the short file name of the key file of Component\_Application. Locate this file in the same folder as Component\_Application. Append the extension .LOCAL to this file name.
-   Increment the SharedDLL refcount if the msidbComponentAttributesSharedDllRefCount bit is set in the Attributes column of the [Component table](component-table.md).
-   Register Component\_Application as a client of Component\_Shared and register a key path pointing to the shared location of Component\_Shared.
-   Install all of the resources of Component\_Application as usual.

If Component\_Shared or its key file is already installed on the computer do not copy files to the shared location of Component\_Shared.

If Component\_Shared or its key file is not yet installed on the computer:

-   Copy the files of Component\_Shared to the shared location.
-   Process all install actions for Component\_Shared.
-   If Component\_Shared is a COM component, register the full COM path such that the syntax \[$Component\] and \[\#FileKey\] point to the shared location of Component\_Shared.

 

 



