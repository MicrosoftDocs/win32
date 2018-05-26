---
title: Window Callback Services
description: Window Callback Services
ms.assetid: 227602e5-7ea1-4afd-ac88-cfeabe746d1f
keywords:
- multimedia audio,window callback services
- audio,window callback services
- audio mixers,window callback services
- mixers,window callback services
- window callback services
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Window Callback Services

The mixer services provide window callback services so that your application can process messages from mixer drivers. To use these services, specify the CALLBACK\_WINDOW flag in the *fdwOpen* parameter and a window handle in the *dwCallback* parameter of the [**mixerOpen**](mixeropen.md) function. Driver messages are sent to the window procedure function for the window identified by the handle in *dwCallback*. The messages are specific to the audio device type.

 

 




