---
description: After you determine how to organize your filter through a CAPTUREFILTER structure, you must allocate and fill in the structure, which is then passed to the Network Monitor driver through a configuration BLOB.
ms.assetid: c2709da6-4d70-4abe-bab5-941053217e57
title: Implementing the Capture Filter Code
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Capture Filter Code

After you determine how to organize your filter through a [**CAPTUREFILTER**](capturefilter.md) structure, you must allocate and fill in the structure, which is then passed to the Network Monitor driver through a configuration BLOB.

Direct NPP users add the capture filter to the configuration BLOB that is passed to **Connect**, [**Configure**](configure.md), or both. For a list of COM interfaces that you can use to communicate with the NPP, see [NPP Interfaces](npp-interfaces.md).

 

 



