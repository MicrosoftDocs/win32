---
title: Yield Callback Functions
description: Yield Callback Functions
ms.assetid: '8c9b43ea-fdba-41a2-ba2d-1eaa4516e14f'
keywords: ["AVICap callback functions,yield"]
---

# Yield Callback Functions

Applications can use yield callback functions during streaming capture. (A yield callback function typically consists of a message loop that calls [PeekMessage](http://go.microsoft.com/fwlink/p/?linkid=16992), [TranslateMessage](http://go.microsoft.com/fwlink/p/?linkid=16993), and [DispatchMessage](http://go.microsoft.com/fwlink/p/?linkid=16994).) The capture window calls the yield callback function at least once for every captured video frame, but the exact rate depends on the frame rate and the overhead of the capture driver and disk.

 

 




