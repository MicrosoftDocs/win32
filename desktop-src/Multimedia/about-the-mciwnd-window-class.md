---
title: About the MCIWnd Window Class
description: About the MCIWnd Window Class
ms.assetid: 7dde7346-5853-4c8f-8788-bf74d01ece83
keywords:
- MCIWnd window class,about
- MCIWndCreate function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the MCIWnd Window Class

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The MCIWnd Window class is easy to use. By using a single function, [**MCIWndCreate**](/windows/desktop/api/Vfw/nf-vfw-mciwndcreatea) your application can create a control that plays any device that uses the media control interface (MCI). These devices include CD audio, waveform-audio, MIDI, and video devices.

Automating playback is also quick and easy. Using only one function and two macros, an application can create an MCIWnd window with the appropriate media device, play the device, and close both the device and the window when the content has finished playing.

> [!Note]  
> Some devices play content that is stored in files. Other devices, such as CD audio devices, play content that is stored in another medium. For purposes of clarity, this overview refers to both circumstances as "playing the device."

 

 

 




