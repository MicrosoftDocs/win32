---
title: Audio Format
description: Audio Format
ms.assetid: a65dbd3f-1539-4f02-8573-c527c4e3c58d
keywords:
- WM_CAP_GET_AUDIOFORMAT message
- capGetAudioFormat macro
- capGetAudioFormatSize macro
- WM_CAP_SET_AUDIOFORMAT message
- capSetAudioFormat macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Format

You can retrieve the current capture format for audio data or the size of the audio format structure by sending the [**WM\_CAP\_GET\_AUDIOFORMAT**](wm-cap-get-audioformat.md) message (or the [**capGetAudioFormat**](/windows/win32/Vfw/nf-vfw-capgetaudioformat?branch=master) and [**capGetAudioFormatSize**](/windows/win32/Vfw/nf-vfw-capgetaudioformatsize?branch=master) macros) to a capture window. The default audio capture format is mono, 8-bit, 11 kHz PCM (Pulse Code Modulation). When you retrieve the format by using WM\_CAP\_GET\_AUDIOFORMAT, always use the [**WAVEFORMATEX**](/windows/win32/Mmreg/?branch=master) structure.

You can set the capture format for audio data by sending the [**WM\_CAP\_SET\_AUDIOFORMAT**](wm-cap-set-audioformat.md) message (or the [**capSetAudioFormat**](/windows/win32/Vfw/nf-vfw-capsetaudioformat?branch=master) macro) to a capture window. When setting the audio format, you can pass a pointer to a [**WAVEFORMAT**](/windows/win32/mmeapi/ns-mmeapi-twaveformatex?branch=master), **WAVEFORMATEX**, or [**PCMWAVEFORMAT**](pcmwaveformat.md) structure, depending on the specified audio format.

 

 




