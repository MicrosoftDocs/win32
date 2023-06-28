---
title: Starting, Pausing, and Resuming Playback
description: Starting, Pausing, and Resuming Playback
ms.assetid: 4af92781-5461-4195-82f5-a9213a9bdbd7
keywords:
- MCIWndPlay macro
- MCIWndPause macro
- MCIWndResume macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Starting, Pausing, and Resuming Playback

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

[**MCIWndPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndplay) is the most general playback macro. This macro lets you play a file or device from the current playback position. Playback continues through the end of the content unless it is interrupted.

You can temporarily interrupt a device that is playing by using the [**MCIWndPause**](/windows/desktop/api/Vfw/nf-vfw-mciwndpause) macro. To resume playback from the paused position, use the [**MCIWndResume**](/windows/desktop/api/Vfw/nf-vfw-mciwndresume) macro. Some devices do not support the pause and resume commands. These devices usually map **MCIWndPause** to the [**MCIWndStop**](/windows/desktop/api/Vfw/nf-vfw-mciwndstop) macro, which stops playback or recording. You can restart a device that does not support pause or resume by using **MCIWndPlay**, which starts playback from the current playback position.

 

 




