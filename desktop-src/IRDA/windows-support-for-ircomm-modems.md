---
title: Windows Support for IrCOMM Modems
description: IrCOMM modem support is delivered through a kernel-mode driver that communicates with the existing IrDA stack through its TDI interface.
ms.assetid: 4bec50e4-2232-4cfb-9ec3-14ff179e54e1
keywords:
- IrCOMM IrDA , modems
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Support for IrCOMM Modems

IrCOMM modem support is delivered through a kernel-mode driver that communicates with the existing IrDA stack through its [*TDI*](https://www.bing.com/search?q=*TDI*) interface. The driver supports the IrDA 9-wire specification, thereby allowing control-line information to be sent over the link. Applications can access the driver through Telephony API (TAPI) and Unimodem.

This support is limited to computer-originated infrared links to a cell phone. Windows does not support phones originating the infrared link.

 

 




