---
title: Windows Support for IrTran-P Cameras
description: A subset of IrTran-P V1 is supported in Windows, and consists of a user-space background image transfer service that accepts incoming IrTran-P images, then writes those files to disk.
ms.assetid: 0218f007-8bf1-4acb-a0cc-1f9a768fa2f5
keywords:
- IrCOMM IrDA , cameras
- IrTran-P cameras IrDA
- cameras IrDA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Support for IrTran-P Cameras

A subset of IrTran-P V1 is supported in Windows, and consists of a user-space background image transfer service that accepts incoming IrTran-P images, then writes those files to disk.

The service accesses the IrDA stack through Windows Sockets. Because the service will be continuously listening for incoming connections, it will not be feasible for another application to use the IrCOMM services exposed for the IrTran-P server, as the IrCOMM protocol itself prevents more than one IrCOMM application to be listening for incoming connections at one time.

Windows will only advertise that it supports the IrCOMM 9-wire mode. Cameras must support IrCOMM 9-wire mode to work with Windows. Cameras must also be able to initiate the IrDA connection. The IrTran-P file transfer service is a listen-only service, and does not attempt to connect to a camera.

 

 




