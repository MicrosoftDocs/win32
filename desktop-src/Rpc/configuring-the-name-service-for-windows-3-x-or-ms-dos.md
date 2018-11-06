---
title: Configuring the Name Service for Windows 3.x or MS-DOS
description: Remote Procedure Call (RPC) and configuring the name service for Windows 3.x or MS-DOS.
ms.assetid: 7b22a12e-43d0-4e32-a191-d63a56559143
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Name Service for Windows 3.x or MS-DOS

When you run Setup.exe to install the 16-bit RPC run-time library, it prompts you to select a name service provider:

-   If you choose **Install Default Name Service Provider**, the default NSP, Microsoft Locator, is installed.
-   If you choose **Install Custom Name Service Provider**, complete the **Define Network Address** dialog box to install the DCE Cell Directory Service as your NSP. The DCE Cell Directory Service is the NSP used with DCE servers.

The network address is the name of the host computer that runs the NSI daemon (nsid). This computer acts as a gateway to the DCE Cell Directory Service, passing NSI function calls between computers that run Microsoft operating systems and DCE computers. The network address can be 80 characters or less—for example, 11.1.9.169 is a valid address.

 

 




