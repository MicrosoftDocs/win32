---
Description: When complex drawing applications perform lengthy graphics operations, they consume valuable system resources.
ms.assetid: 3beef852-27fe-4ee2-b38b-3dc50e5d2fcf
title: Cancellation of Drawing Operations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cancellation of Drawing Operations

When complex drawing applications perform lengthy graphics operations, they consume valuable system resources. By taking advantage of the system's multitasking features, an application can use threads and the [**CancelDC**](/windows/win32/Wingdi/nf-wingdi-canceldc?branch=master) function to manage these operations. For example, if the graphics operation performed by thread A is consuming needed resources, thread B can call the CancelDC function to halt that operation.

 

 



