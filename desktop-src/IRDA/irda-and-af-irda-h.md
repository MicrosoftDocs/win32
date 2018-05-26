---
title: IrDA and Af\_irda.h
description: The Af\_irda.h header file must be included by Windows Sockets applications to support IrDA.
ms.assetid: d1d27829-48e2-4f3b-baac-d396fecd61e5
keywords:
- IrDA and Af_irda,h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IrDA and Af\_irda.h

The Af\_irda.h header file must be included by Windows Sockets applications to support IrDA. Several incompatible versions of Af\_irda.h have been distributed, including those shipped with Windows CE and Windows 95 Ir3.0 DDKs and SDKs. A common Af\_irda.h header file that supports all three platforms is available with the Windows IrDA DDK. This file may continue to evolve as Windows programmatic elements and platforms continue to merge.

To compile for a target platform, one of the following must be defined:

``` syntax
_WIN32_WINNT
_WIN32_WCE
_WIN32_WINDOWS
```

 

 




