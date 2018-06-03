---
title: COM Snap-ins
description: Describes how a COM snap-in can be deployed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71bda477-8aa5-4b51-85d0-f80e7dd9284f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# COM Snap-ins

## To deploy a snap-in developed with C++

1.  Copy your snap-in's DLL to your target directory.
2.  Use Regsvr32.exe to register the snap-in DLL.

Registering your snap-in's DLLs adds all the necessary entries to the registry. For more information, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

 

 




