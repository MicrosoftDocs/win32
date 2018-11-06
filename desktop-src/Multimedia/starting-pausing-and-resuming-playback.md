---
title: Starting, Pausing, and Resuming Playback
description: Starting, Pausing, and Resuming Playback
ms.assetid: 4af92781-5461-4195-82f5-a9213a9bdbd7
keywords:
- MCIWndPlay macro
- MCIWndPause macro
- MCIWndResume macro
ms.topic: article
ms.date: 05/31/2018
---

# Starting, Pausing, and Resuming Playback

[**MCIWndPlay**](/windows/desktop/api/Vfw/nf-vfw-mciwndplay) is the most general playback macro. This macro lets you play a file or device from the current playback position. Playback continues through the end of the content unless it is interrupted.

You can temporarily interrupt a device that is playing by using the [**MCIWndPause**](/windows/desktop/api/Vfw/nf-vfw-mciwndpause) macro. To resume playback from the paused position, use the [**MCIWndResume**](/windows/desktop/api/Vfw/nf-vfw-mciwndresume) macro. Some devices do not support the pause and resume commands. These devices usually map **MCIWndPause** to the [**MCIWndStop**](/windows/desktop/api/Vfw/nf-vfw-mciwndstop) macro, which stops playback or recording. You can restart a device that does not support pause or resume by using **MCIWndPlay**, which starts playback from the current playback position.

 

 




