---
title: Yield Callback Functions
description: Yield Callback Functions
ms.assetid: 8c9b43ea-fdba-41a2-ba2d-1eaa4516e14f
keywords:
- AVICap callback functions,yield
ms.topic: article
ms.date: 05/31/2018
---

# Yield Callback Functions

Applications can use yield callback functions during streaming capture. (A yield callback function typically consists of a message loop that calls [PeekMessage](https://msdn.microsoft.com/library/ms644943.aspx), [TranslateMessage](https://msdn.microsoft.com/library/ms644955.aspx), and [DispatchMessage](https://msdn.microsoft.com/library/ms644934.aspx).) The capture window calls the yield callback function at least once for every captured video frame, but the exact rate depends on the frame rate and the overhead of the capture driver and disk.

 

 




