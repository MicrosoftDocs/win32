---
description: The Windows Installer can advertise the availability of an application to users or other applications without actually installing the application.
ms.assetid: 67170daa-448a-4a20-b38a-2dd36c95440f
title: Advertisement
ms.topic: article
ms.date: 05/31/2018
---

# Advertisement

The Windows Installer can advertise the availability of an application to users or other applications without actually installing the application. If an application is advertised, only the interfaces required for loading and launching the application are presented to the user or other applications. If a user or application activates an advertised interface the installer then proceeds to install the necessary components as described in [Installation-On-Demand](installation-on-demand.md).

The two types of advertising are assigning and publishing. An application appears installed to a user when that application is assigned to the user. The **Start** menu contains the appropriate shortcuts, icons are displayed, files are associated with the application, and registry entries reflect the application's installation. When the user tries to open an assigned application it is installed upon demand.

The installer supports the advertisement of applications and features according to the operating system. The installer registers COM class information for assigned applications beginning with Windows XP. This enables the installer to install the application upon the creation of an instance of an advertised class. For more information, see [Platform Support of Advertisement](platform-support-of-advertisement.md).

You can publish an application from the server beginning with Windows Server 2003. The published application is then installed through its file association or Multipurpose Internet Mail Extension (MIME) type. Publishing does not populate the user interface with any of the application's icons. The client operating system can install a published application beginning with Windows XP.

 

 



