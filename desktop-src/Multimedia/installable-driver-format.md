---
title: Installable Driver Format
description: Installable Driver Format
ms.assetid: 4573567e-237d-47f9-9510-31d01326205f
keywords:
- installable drivers,formats
- installable drivers,DriverProc function
- installable drivers,messages
- driver messages
- driver formats
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installable Driver Format

Every installable driver exports a [DriverProc](driverproc.md) function. This common entry-point function receives *driver messages* from the system that direct the driver to carry out actions or provide information. The system sends driver messages to the **DriverProc** function when an application or DLL opens or closes the driver or requests that a message be sent to the driver. The **DriverProc** function either processes the message or passes the message to the default message handler, the [DefDriverProc](defdriverproc.md) function. In either case, **DriverProc** must return a value indicating whether the requested action was successful.

 

 




