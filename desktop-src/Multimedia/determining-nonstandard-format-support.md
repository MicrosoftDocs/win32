---
title: Determining Nonstandard Format Support
description: Determining Nonstandard Format Support
ms.assetid: a795aa7d-704b-4f03-9815-7a298907bd3d
keywords:
- waveform audio,nonstandard format support
- auxiliary audio,nonstandard format support
- waveform audio,standard format support
- auxiliary audio,standard format support
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Determining Nonstandard Format Support

\[The feature associated with this page, [Waveform Audio](/windows/win32/multimedia/waveform-audio), is a legacy feature. It has been superseded by [WASAPI](/windows/win32/coreaudio/wasapi) and [Audio Graphs](/windows/uwp/audio-video-camera/audio-graphs). **WASAPI** and **Audio Graphs** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **WASAPI** and **Audio Graphs** instead of **Waveform Audio**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To see whether a device supports a particular format (standard or nonstandard), you can call the [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen) function with the WAVE\_FORMAT\_QUERY flag. The following example uses this technique to determine whether a waveform-audio device supports a specified format.


```C++
// Determines whether the specified waveform-audio output device 
// supports a specified waveform-audio format. Returns 
// MMSYSERR_NOERROR if the format is supported, WAVEERR_BADFORMAT if 
// the format is not supported, and one of the other MMSYSERR_ error 
// codes if there are other errors encountered in opening the 
// specified waveform-audio device. 
 
MMRESULT IsFormatSupported(LPWAVEFORMATEX pwfx, UINT uDeviceID) 
{ 
    return (waveOutOpen( 
        NULL,                 // ptr can be NULL for query 
        uDeviceID,            // the device identifier 
        pwfx,                 // defines requested format 
        NULL,                 // no callback 
        NULL,                 // no instance data 
        WAVE_FORMAT_QUERY));  // query only, do not open device 
} 
```



This technique for determining nonstandard format support also applies to waveform-audio input devices. The only difference is that the [**waveInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveinopen) function is used in place of [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen) to query for format support.

To determine whether a particular waveform-audio data format is supported by any of the waveform-audio devices in a system, use the technique illustrated in the previous example, but specify the WAVE\_MAPPER constant for the *uDeviceID* parameter.

 

 