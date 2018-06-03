---
title: Deploying Snap-ins
description: Provides instructions for deploying a snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cb2a0da4-041a-449c-8dcd-46db54291b25
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- deploying snap-ins MMC
- snap-in deployment MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Deploying Snap-ins

After you have coded and tested your snap-in, you are ready to deliver it to your end users. This means that you need to:

1.  Gather the files required for your snap-in (create a package).
2.  Save the files to some medium for distribution (deploy the snap-in).
3.  Provide some way for end users to install the snap-in on their local systems.

There are three primary setup technologies you can use to distribute your snap-ins to end users:

-   Microsoft Windows Installer

    Prepares and deploys packages for computers running Windows. It includes the ability to create installer- based setups on any 32-bit Windows operating system.

-   Microsoft Visual Basic Package and Deployment Wizard

    Prepares packages and deploys packages for application programs using the Visual Basic programming system. It includes the creation of installer programs to copy application programs including the Visual Basic programming system—in this case snap-ins—onto the users' computers.

-   Proprietary or third-party installation package

    You may choose to use a third-party installation program or write your own scripts to package, deploy, and install snap-ins.

The following sections provide details about using these methods with snap-ins as well as special concerns about distributing saved console files.

-   [Using Windows Installer](using-windows-installer.md)
-   [Using the Package and Deployment Wizard](using-the-package-and-deployment-wizard.md)
-   [Using a Proprietary or Third-Party Installation Package](using-a-proprietary-or-third-party-installation-package.md)

 

 




