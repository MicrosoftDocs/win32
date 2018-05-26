---
title: Installing and Configuring DSML Services for Windows
description: DSML Services for Windows requires a server running Windows 2000 or Windows Server 2003, Standard Edition, that is configured to support IIS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 62ccfa25-3a0f-4277-957d-98fbcf66cd42
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Installing and Configuring DSML Services for Windows DSML
- DSML Services for Windows, installing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Installing and Configuring DSML Services for Windows

DSML Services for Windows requires a server running Windows 2000 or Windows Server 2003, Standard Edition, that is configured to support IIS. The IIS server must be part of an Active Directory forest if using DSML Services for Windows with an Active Directory server. If using DSML Services for Windows with Active Directory Application Mode (ADAM) instead of Active Directory, the IIS server does not need to be part of a forest. If the IIS and ADAM servers are not joined to a domain, then IIS and ADAM should be run on the same computer, because IIS will use local accounts for authentication.

Before installing DSML Services for Windows:

-   Read the [System Requirements](systreq.md).
-   Verify that your IIS server is running and that the security certificates are properly installed.

**To install DSML Services for Windows**

1.  [Install the DSML Services for Windows files](installing-dsml-services-for-windows.md) on the IIS server.
2.  [Configure DSML Services for Windows](configuring-dsml-services-for-windows.md).

    The DSML Services for Windows configuration application requires the .NET Framework runtime, which is included in the Windows Server 2003. To download the .NET Framework, go to [https://msdn.microsoft.com/netframework](http://go.microsoft.com/fwlink/p/?linkid=83942) and, in the left pane, click **Downloads**.

    Alternatively, DSML Services for Windows can be [configured manually](manually-configuring-dsml-services-for-windows.md) if it is not desirable to install the .NET Framework runtime on the IIS server.

 

 




