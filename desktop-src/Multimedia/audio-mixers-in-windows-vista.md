---
title: Audio Mixers in Windows Vista
description: Audio Mixers in Windows Vista
ms.assetid: 541cb5f3-b5ca-436f-88dd-6ef8459c6157
keywords:
- multimedia audio,Windows Vista audio mixers
- audio,Windows Vista audio mixers
- audio mixers,Windows Vista
- mixers,Windows Vista
- Windows Vista audio mixers
ms.topic: article
ms.date: 05/31/2018
---

# Audio Mixers in Windows Vista

Starting in Windows Vista, some mixer controls are implemented in software rather than hardware. For example, the volume controls are implemented using the Windows audio session API (WASAPI). These controls do not directly affect hardware settings. In addition, they are associated with a process-specific audio session, so changes affect the calling application but do not affect other applications.

Each audio endpoint device has a standard mixer layout, implemented in software.

-   Each audio rendering endpoint contains one destination line that contains the following:
    -   Volume control
    -   Mute control
    -   Source line: Waveform-audio output.
    -   Source line: Audio CD.
-   Each audio capture endpoint contains one destination line that contains the following:
    -   Volume control
    -   Mute control
    -   Source line: Waveform-audio input. The component type depends on the input device— for example, a microphone.

Each source line contains a volume control and a mute control. The following diagram shows the components of render endpoints and capture endpoints.

![default mixer layouts](images/mixer1.gif)

All of the controls for an endpoint manipulate the same underlying software control. Therefore, if you change the settings on one control, you will receive a control change notification on the other controls. (See [**MM\_MIXM\_CONTROL\_CHANGE**](mm-mixm-control-change.md).)

This standard layout is provided for compatibility with existing applications that use the audio mixer functions. New applications should avoid using these functions.

 

 




