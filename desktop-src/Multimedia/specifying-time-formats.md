---
title: Specifying Time Formats
description: Specifying Time Formats
ms.assetid: 11d28d63-ed3e-4137-b9d8-1681bf0e33ff
keywords:
- MCIWndGetTimeFormat macro
- MCIWndSetTimeFormat macro
- MCIWndUseTime macro
- MCIWndUseFrames macro
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Time Formats

Multimedia data types typically can use time to identify significant positions within their content. Common time formats are milliseconds, tracks, and frames; other less common time formats, such as SMPTE (Society of Motion Picture and Television Engineers) 24, also exist. Time is the format and reference system for waveform-audio, MIDI, and CD audio data. Video supports time even though it is recorded as a sequence of frames (stream) that is typically played at a specific speed. Several macros are available for designating time format.

You can retrieve the current time format for a file or device by using the [**MCIWndGetTimeFormat**](/windows/desktop/api/Vfw/nf-vfw-mciwndgettimeformat) macro. You can change the current time format to any other time format supported by a device by using the [**MCIWndSetTimeFormat**](/windows/desktop/api/Vfw/nf-vfw-mciwndsettimeformat) macro. Or you can the set the time format to milliseconds or frames by using the [**MCIWndUseTime**](/windows/desktop/api/Vfw/nf-vfw-mciwndusetime) or [**MCIWndUseFrames**](/windows/desktop/api/Vfw/nf-vfw-mciwnduseframes) macros.

> [!Note]  
> Noncontinuous formats, such as tracks and SMPTE, can cause the toolbar to behave erratically. For these time formats, you might want to turn off the toolbar by specifying the MCIWNDF\_NOPLAYBAR window style when creating an MCIWnd window.

 

 

 




