---
description: The installer records errors and events in its own error log.
ms.assetid: 244e9afa-2052-469e-aa57-424e03ce5673
title: Normal Logging
ms.topic: article
ms.date: 05/31/2018
---

# Normal Logging

The installer records errors and events in its own error log. The type of logging that is performed by the installer is determined by the setting of the logging mode. Logging is enabled and the mode can be set by using the following methods:

-   The logging mode of an installation launched from the command line can be specified by using the /L option of the [Command Line Options](command-line-options.md). If the logging mode is not specified by using the /L command-line option, the default logging mode will be used.
-   The logging mode of an installation process can be specified programmatically by using the [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga) function or the [**EnableLog**](installer-enablelog.md) method. If the logging mode is not specified by using the **MsiEnableLog** function or the **EnableLog** method, the default logging mode will be used.
-   The default logging mode of a particular installation package can be specified by setting the [**MsiLogging**](msilogging.md) property in the [Property table](property-table.md) of the package. This property is available starting with Windows Installer 4.0.
-   If the [**MsiLogging**](msilogging.md) property is present in the [Property table](property-table.md), the default logging mode of the package can be modified by changing the value by using a [database transform](database-transforms.md). The default logging mode cannot be changed by using [Patch Packages](patch-packages.md) (a .msp file.)
-   If the [**MsiLogging**](msilogging.md) property has not been set, the default logging mode for all users of the computer can be specified by using the [Logging](logging.md) policy.
-   If the [**MsiLogging**](msilogging.md) property has been set, the default logging mode for all users of the computer can be specified by setting both the [DisableLoggingFromPackage](disableloggingfrompackage.md) policy and [Logging](logging.md) policy.
-   If the logging mode has not been specified by the /L option, [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga), [**EnableLog**](installer-enablelog.md), [**MsiLogging**](msilogging.md) property, or the [Logging](logging.md) policy, then the default logging mode for the package is the same mode that is obtained as setting the **MsiLogging** property to 'iwearmo'.

 

 



