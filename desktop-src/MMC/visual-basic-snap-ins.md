---
title: Visual Basic Snap-ins
description: Describes how a VB snap-in can be deployed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d77ad61a-7297-4687-9b28-233cb9cf2c08
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Visual Basic Snap-ins

## To deploy a snap-in developed using Visual Basic

1.  Copy your snap-in's DLL to your target directory.
2.  If the Visual Basic runtime (msvbvm60.dll) is not installed on the computer, install it in the system folder.
3.  Copy mssnapr.dll to: Program Files\\Common Files\\Microsoft Shared\\SnapInDesigner.
4.  Register the DLLs with Regsvr32.
    > \[!Important\]  
    > The designer runtime (mssnapr.dll) must be registered before your snap-in's DLL. If it is not registered first, registration of your snap-in's DLL will fail.

     

Registering your snap-in's DLLs adds all the necessary entries to the MMC registry keys under the following key: **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\MMC**

 

 




