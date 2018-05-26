---
title: Determining and Changing the Current Position
description: Determining and Changing the Current Position
ms.assetid: 20f78dcd-3259-43c2-8da3-8cfc299252e6
keywords:
- MCIWndGetStart macro
- MCIWndGetEnd macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining and Changing the Current Position

When a file or device is associated with an MCIWnd window, the playback position is initially set at the start of the content, regardless of the media type. During playback, the playback position moves linearly through the content and, if playback is uninterrupted, eventually reaches the end of the content. If an interruption occurs, the current playback position is the location at which playback was stopped or paused.

You can retrieve the locations for the beginning and end of the content by using the [**MCIWndGetStart**](/windows/win32/Vfw/nf-vfw-mciwndgetstart?branch=master) and [**MCIWndGetEnd**](/windows/win32/Vfw/nf-vfw-mciwndgetend?branch=master) macros. You can determine the length of the content by subtracting the value returned by **MCIWndGetStart** from the value returned by **MCIWndGetEnd**, or by using the [**MCIWndGetLength**](/windows/win32/Vfw/nf-vfw-mciwndgetlength?branch=master) macro. You can retrieve the current playback position by using the [**MCIWndGetPosition**](/windows/win32/Vfw/nf-vfw-mciwndgetposition?branch=master) macro, or you can retrieve the playback position as a null-terminated string by using the [**MCIWndGetPositionString**](/windows/win32/Vfw/nf-vfw-mciwndgetpositionstring?branch=master) macro.

To change the current playback position, use the [**MCIWndHome**](/windows/win32/Vfw/nf-vfw-mciwndhome?branch=master), [**MCIWndEnd**](/windows/win32/Vfw/nf-vfw-mciwndend?branch=master), and [**MCIWndSeek**](/windows/win32/Vfw/nf-vfw-mciwndseek?branch=master) macros. You can move the playback position to the start of the content by using **MCIWndHome** or to the end of the content by using **MCIWndEnd**. Use **MCIWndSeek** to move the playback position to any location in the content.

You can also step through the content by using the [**MCIWndStep**](/windows/win32/Vfw/nf-vfw-mciwndstep?branch=master) macro. Beginning from the current playback position, this macro moves the playback position forward or backward by a specified increment.

> [!Note]  
> The units used to specify position vary among the different media types and devices. For example, the playback position for AVI files used by the MCIAVI device is measured in frames; the playback position for CD audio, waveform-audio, and MIDI files is measured in milliseconds.

 

Devices for other media types and third-party devices might use other units. For information about determining these units, see [Playback Enhancements](playback-enhancements.md).

 

 




