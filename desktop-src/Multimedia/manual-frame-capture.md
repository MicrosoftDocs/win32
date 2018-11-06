---
title: Manual Frame Capture
description: Manual Frame Capture
ms.assetid: 7c5576ff-2694-4f44-a386-03bbc6f9c2ed
keywords:
- WM_CAP_SINGLE_FRAME_OPEN message
- WM_CAP_SINGLE_FRAME message
- WM_CAP_SINGLE_FRAME_CLOSE message
- capCaptureSingleFrameOpen macro
- capCaptureSingleFrame macro
- capCaptureSingleFrameClose macro
ms.topic: article
ms.date: 05/31/2018
---

# Manual Frame Capture

If you want to individually specify the frames to capture in a video stream, you can control the sequence by using the [**WM\_CAP\_SINGLE\_FRAME\_OPEN**](wm-cap-single-frame-open.md), [**WM\_CAP\_SINGLE\_FRAME**](wm-cap-single-frame.md), and [**WM\_CAP\_SINGLE\_FRAME\_CLOSE**](wm-cap-single-frame-close.md) messages (or the [**capCaptureSingleFrameOpen**](/windows/desktop/api/Vfw/nf-vfw-capcapturesingleframeopen), [**capCaptureSingleFrame**](/windows/desktop/api/Vfw/nf-vfw-capcapturesingleframe), and [**capCaptureSingleFrameClose**](/windows/desktop/api/Vfw/nf-vfw-capcapturesingleframeclose) macros). Typically, these messages are used to create animation by appending individual frames to the capture file. WM\_CAP\_SINGLE\_FRAME\_OPEN opens a file for a manually driven capture operation. WM\_CAP\_SINGLE\_FRAME captures an individual frame and appends it to the capture file. WM\_CAP\_SINGLE\_FRAME\_CLOSE closes the file used for manual frame capture.

> [!Note]  
> This capture method does not support simultaneous audio capture with video capture.

 

 

 




