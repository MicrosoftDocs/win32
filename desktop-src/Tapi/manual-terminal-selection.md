---
description: If the rules of Default selection do not meet the needs of the application, the application has the option of selecting the terminal manually.
ms.assetid: 12d7781e-a27d-4cbe-b7c4-6c0dfef11074
title: Manual Terminal Selection
ms.topic: article
ms.date: 05/31/2018
---

# Manual Terminal Selection

If the rules of Default selection do not meet the needs of the application, the application has the option of selecting the terminal as it always has: that is, it can use [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream) to enumerate the streams present on the call and select the terminal on the appropriate streams (or, in case of multitrack terminals, create tracks for the streams and select created tracks on the streams).

 

 
