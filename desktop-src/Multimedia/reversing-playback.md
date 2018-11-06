---
title: Reversing Playback
description: Reversing Playback
ms.assetid: cb7c1293-42d7-4c74-b9e6-cc8899ca7c54
keywords:
- MCIWndPlayReverse macro
ms.topic: article
ms.date: 05/31/2018
---

# Reversing Playback

Some devices support playback in the reverse direction. You can play the content of such a device in the reverse direction by using the [**MCIWndPlayReverse**](/windows/desktop/api/Vfw/nf-vfw-mciwndplayreverse) macro. This macro defines the playback scope from the current playback position to the beginning of the content. The digital-video device, MCIAVI.DRV, can play backward. Devices that cannot play backward, such as CD audio, can issue an error message when **MCIWndPlayReverse** is invoked.

 

 




