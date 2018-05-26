---
title: Windows Support for IrCOMM (IrLPT) Printers
description: IrLPT printing is directly supported in Windows.
ms.assetid: b5c1c53f-9205-411e-a18f-da8aeddfa302
keywords:
- IrCOMM IrDA , printers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Support for IrCOMM (IrLPT) Printers

IrLPT printing is directly supported in Windows. When IrDA is installed, an IrDA local port will appear in the local printer ports list of the **Add Printer** dialog box. Associating a printer with this port, then printing to that printer causes the system to print using IrLPT. The print monitor itself will access the IrLPT protocol through Windows Sockets. It is possible for another application to print through this same interface, but such configurations are not expected to be common.

 

 




