---
title: Starting, Pausing, and Resuming Playback
description: Starting, Pausing, and Resuming Playback
ms.assetid: '4af92781-5461-4195-82f5-a9213a9bdbd7'
keywords: ["MCIWndPlay macro", "MCIWndPause macro", "MCIWndResume macro"]
---

# Starting, Pausing, and Resuming Playback

[**MCIWndPlay**](mciwndplay.md) is the most general playback macro. This macro lets you play a file or device from the current playback position. Playback continues through the end of the content unless it is interrupted.

You can temporarily interrupt a device that is playing by using the [**MCIWndPause**](mciwndpause.md) macro. To resume playback from the paused position, use the [**MCIWndResume**](mciwndresume.md) macro. Some devices do not support the pause and resume commands. These devices usually map **MCIWndPause** to the [**MCIWndStop**](mciwndstop.md) macro, which stops playback or recording. You can restart a device that does not support pause or resume by using **MCIWndPlay**, which starts playback from the current playback position.

 

 




