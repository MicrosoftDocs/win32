---
description: When complex drawing applications perform lengthy graphics operations, they consume valuable system resources.
ms.assetid: 3beef852-27fe-4ee2-b38b-3dc50e5d2fcf
title: Cancellation of Drawing Operations
ms.topic: article
ms.date: 05/31/2018
---

# Cancellation of Drawing Operations

When complex drawing applications perform lengthy graphics operations, they consume valuable system resources. By taking advantage of the system's multitasking features, an application can use threads and the [**CancelDC**](/windows/desktop/api/Wingdi/nf-wingdi-canceldc) function to manage these operations. For example, if the graphics operation performed by thread A is consuming needed resources, thread B can call the CancelDC function to halt that operation.

 

 



