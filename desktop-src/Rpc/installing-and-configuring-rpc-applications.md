---
title: Installing and Configuring RPC Applications
description: When the Microsoft Windows operating system is installed on a server or client, setup automatically installs the RPC run-time files.
ms.assetid: cfcada3d-cf7c-42a9-9ed4-0b1bba7a98cf
keywords:
- Remote Procedure Call RPC , tasks, installing and configuring applications
ms.topic: article
ms.date: 05/31/2018
---

# Installing and Configuring RPC Applications

When the Microsoft Windows operating system is installed on a server or client, setup automatically installs the RPC run-time files. No further RPC installation is required. You must ensure, however, that the version of Windows you install supports all the features used in your distributed application.

When you use an RPC application on a Windows 3.x or Microsoft MS-DOS operating system, you must copy the RPC run-time executable files to the Windows 3.x or MS-DOS computers that will be using the application. The directory \\mstools\\rpc\_rt16 on the Platform Software Development Kit (SDK) CD contains a disk image of these files along with a setup program to install the files. Use this disk image to create an install disk for distribution with your RPC application. You can also use 16-bit client applications targeted toward MS-DOS or Windows on a 32-bit/64-bit Windows operating system. However, your application's installation program must install the executable files contained in this disk image.

When you build an RPC application for a Macintosh client, you must link the necessary files to the application at build time. No additional RPC installation is needed.

For more details about redistributable files and licensing agreements, see \\LICENSE\\Redist.txt and \\LICENSE\\License.txt on the Platform SDK CD.

This section contains information about setting up RPC applications on a variety of hardware and software platforms. It presents the discussion in the following sections:

-   [Configuring the Name Service Provider](configuring-the-name-service-provider.md)
-   [Registry Information](registry-information.md)
-   [Using RPC with Winsock Proxy](using-rpc-with-winsock-proxy.md)
-   [SPX/IPX Installation](spx-ipx-installation.md)
-   [Configuring the Security Server](configuring-the-security-server.md)

 

 




