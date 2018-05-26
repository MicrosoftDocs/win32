---
title: Multiple-session IrLAP Support with IrLMP and TinyTP
description: The IrLMP and TinyTP layers add multiple-session support to IrLAP.
ms.assetid: b19ddeb2-b1a6-40bf-aacb-06701d25090d
keywords:
- IrLAP IrDA
- IrLAP IrDA
- TinyTP IrDA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multiple-session IrLAP Support with IrLMP and TinyTP

The IrLMP and TinyTP layers add multiple-session support to IrLAP. In theory, such support enables multiple applications to have multiple concurrent active connections. This operation is fully supported, but often only one application can be active at a given time. IrLMP and TinyTP still provide significant value, because they enable multiple applications to be listening for incoming connections without interfering with each other. A single application might also choose to open a control connection and a data connection at the same time. Such operation is made possible by the IrLMP and TinyTP layers.

IrLMP and TinyTP also add per-connection flow control to the flow control provided by the single IrLAP connection. This feature enables applications to offer data to the IrDA stack in large blocks, and enables the IrDA stack to send the data at optimal speeds. Applications do not need to account for lost data or flow control.

Windows Sockets exposes the TinyTP service interface to application programs.

 

 




