---
description: AutoRun is a feature of the Windows operating system.
title: Creating an AutoRun-enabled CD-ROM Application
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 5c583c1d-a4eb-4291-a839-c1ca7c51342c
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Creating an AutoRun-enabled CD-ROM Application

AutoRun is a feature of the Windows operating system. It automates the procedures for installing and configuring products designed for Windows-based platforms that are distributed on CD-ROMs. When users insert an AutoRun-enabled compact disc into their CD-ROM drive, AutoRun automatically runs an application on the CD-ROM that installs, configures, or runs the selected product.

AutoRun can be used to install and run CD-ROM applications. Although AutoRun is most commonly used for Windows applications, it can also be used to install, configure, or run MS-DOS-based applications in a Windows Microsoft MS-DOS session. You can configure each MS-DOS-based application with its own unique icon, Config.sys file, and Autoexec.bat file. Windows creates the correct configuration files for the MS-DOS-based application. The startup application then starts the MS-DOS-based application in a window.

> [!Note]  
> For AutoRun to work, the CD-ROM drive must have 32 or 64-bit device drivers that detect when a user inserts a compact disc and notify the system.

 

The following sections discuss how to implement an AutoRun-enabled CD-ROM application.

-   [Creating an AutoRun-Enabled Application](autoplay-works.md)
-   [Autorun.inf Entries](autorun-cmds.md)
-   [Enabling and Disabling AutoRun](autoplay-reg.md)

 

 



