---
description: To remove an application that has been installed in the advertised state, simply uninstall it using MsiInstallProduct or MsiConfigureProduct. You can also remove an advertised application from the command line. See Command Line Options.
ms.assetid: 979928fc-d95b-4c4e-88bd-aa16fbced736
title: Removing an Advertised Application
ms.topic: article
ms.date: 05/31/2018
---

# Removing an Advertised Application

To remove an application that has been installed in the advertised state, simply uninstall it using [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta) or [**MsiConfigureProduct**](/windows/desktop/api/Msi/nf-msi-msiconfigureproducta). You can also remove an advertised application from the command line. See [Command Line Options](command-line-options.md).

Note that you may be unable to remove an advertised application if you have authored the package in such a way that running an installation is conditional upon the statement **NOT Installed**. An advertised application is not installed on the user's computer and the installer does not set the [**Installed**](installed.md) Property. The package must be authored so that advertised applications can be uninstalled.

 

 



