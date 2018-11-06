---
title: Capture Without Using Disk Storage
description: Capture Without Using Disk Storage
ms.assetid: 2e2f1b67-69be-424c-8a6f-d9db5eeb6088
keywords:
- WM_CAP_SEQUENCE_NOFILE message
- capCaptureSequenceNoFile macro
ms.topic: article
ms.date: 05/31/2018
---

# Capture Without Using Disk Storage

You can use capture services without writing the data to a disk file by using the [**WM\_CAP\_SEQUENCE\_NOFILE**](wm-cap-sequence-nofile.md) message (or the [**capCaptureSequenceNoFile**](/windows/desktop/api/Vfw/nf-vfw-capcapturesequencenofile) macro). This message is useful only in conjunction with callback functions that allow your application to use the video and audio data directly. For example, videoconferencing applications might use this message to obtain streaming video frames. The callback functions would transfer the captured images to the remote computer.

 

 




