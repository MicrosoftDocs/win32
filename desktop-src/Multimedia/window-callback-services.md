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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Window Callback Services

\[The feature associated with this page, [Audio Mixers](/windows/win32/multimedia/audio-mixers), is a legacy feature. It has been superseded by [Volume Controls](/windows/win32/coreaudio/volume-controls). **Volume Controls** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Volume Controls** instead of **Audio Mixers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The mixer services provide window callback services so that your application can process messages from mixer drivers. To use these services, specify the CALLBACK\_WINDOW flag in the *fdwOpen* parameter and a window handle in the *dwCallback* parameter of the [**mixerOpen**](/windows/win32/api/mmeapi/nf-mmeapi-mixeropen) function. Driver messages are sent to the window procedure function for the window identified by the handle in *dwCallback*. The messages are specific to the audio device type.

 

 