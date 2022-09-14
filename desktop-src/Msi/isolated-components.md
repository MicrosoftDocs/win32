---
description: Authors of installation packages can specify that the installer copy the shared files (commonly shared DLLs) of an application into that application's folder rather than to a shared location.
ms.assetid: 'eb5f7088-30e0-4644-813a-c93e6f56ccbf'
title: Isolated Components
ms.topic: article
ms.date: 05/31/2018
---

# Isolated Components

Authors of installation packages can specify that the installer copy the shared files (commonly shared DLLs) of an application into that application's folder rather than to a shared location. This private set of files (DLLs) are then used only by the application. Isolating the application together with its shared components in this manner has the following advantages:

-   The application always uses the versions of the shared files with which it was deployed.
-   Installing the application does not overwrite other versions of the shared files by other applications.
-   Subsequent installations of other applications using different versions of the shared files cannot overwrite the files used by this application.

Because the current implementation of COM keeps a single full path in the registry for each CLSID/Context pair, it forces all applications to use the same version of a shared DLL. To enable an application to keep a private copy of a COM server, the system loader in Windows 2000 checks for the presence of a .LOCAL file in the application's folder. If the system loader detects a .LOCAL file, it alters its search logic to prefer DLLs located in the same folder as the application.

When Windows Installer runs the [IsolateComponents action](isolatecomponents-action.md) they copy the files of the component (commonly a shared DLL) specified in the Component\_Shared column of the [IsolatedComponent table](isolatedcomponent-table.md) into the same folder as the component (commonly an .exe file) specified in the Component\_Application column. The installer creates a file in this directory, zero bytes in length, having the short file name of the key file for Component\_Application (typically the name is the same as the application's .exe) appended with .LOCAL. The installer uses the registration for the component in its shared location and does not write any registration information for the copy of the component in the private location.

For more information, see:

-   [Installation of Isolated Components](installation-of-isolated-components.md)
-   [Reinstallation of Isolated Components](reinstallation-of-isolated-components.md)
-   [Removal of Isolated Components](removal-of-isolated-components.md)
-   [Using Isolated Components](using-isolated-components.md)

 

 



