---
description: Windows Installer performs the following actions during reinstallation of an application when the package contains isolated components. Typically, Component\_Shared is a DLL that is shared by Component\_Application and other client executables.
ms.assetid: 65909b47-dc09-4e9a-920a-9cb3f55b2e67
title: Reinstallation of Isolated Components
ms.topic: article
ms.date: 05/31/2018
---

# Reinstallation of Isolated Components

Windows Installer performs the following actions during reinstallation of an application when the package contains isolated components. Typically, Component\_Shared is a DLL that is shared by Component\_Application and other client executables.

## Reinstallation

-   Reinstall of the files of Component\_Shared into the same folder as Component\_Application only if Component\_Application is also being reinstalled.
-   Do not increment the client list of Component\_Shared and do not increment the SharedDLL count.
-   Recreate the zero-byte file with the short file name of the key file of Component\_Application. This file must be located in the same folder as Component\_Application and have the extension .LOCAL.
-   Reinstall all of the resources of Component\_Application as usual.

If the SharedDLL refcount for Component\_Shared is more than 1, or if other products remain on the client list of Component\_Shared:

-   Reinstall no files to the shared location of Component\_Shared.

If the SharedDLL refcount for Component\_Shared equals 1, or if there are no other remaining clients of Component\_Shared:

-   Reinstall of the files of Component\_Shared into the shared location using the [File Versioning Rules](file-versioning-rules.md).
-   Process all reinstall actions for Component\_Shared.
-   If Component\_Shared is a COM component, register the full COM path such that the installer syntaxes \[$Component\] and \[\#FileKey\] point to the shared location of Component\_Shared.

 

 



