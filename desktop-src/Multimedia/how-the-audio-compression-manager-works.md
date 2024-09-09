---
title: How the Audio Compression Manager Works
description: How the Audio Compression Manager Works
ms.assetid: 7f1c3f21-262f-42a1-b9f7-069fb13b9d8f
keywords:
- multimedia audio,audio compression manager (ACM)
- audio,audio compression manager (ACM)
- audio compression manager (ACM),about
- ACM (audio compression manager),about
- audio compression manager (ACM),codec drivers
- ACM (audio compression manager),codec drivers
- audio compression manager (ACM),format converter drivers
- ACM (audio compression manager),format converter drivers
- audio compression manager (ACM),filter drivers
- ACM (audio compression manager),filter drivers
- audio compression manager (ACM),compressor drivers
- ACM (audio compression manager),compressor drivers
- audio compression manager (ACM),decompressor drivers
- ACM (audio compression manager),decompressor drivers
- codec drivers
- format converter drivers
- filter drivers
- compressor drivers
- decompressor drivers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How the Audio Compression Manager Works

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The ACM uses existing driver interface hooks to override the default mapping algorithm for waveform-audio devices. This allows the ACM to intercept device-open calls. After a call has been intercepted, the ACM can perform a variety of tasks to process the audio data, such as inserting an external compressor or decompressor into the sequence.

The ACM manages the following types of drivers:

-   Compressor and decompressor (codec) drivers
-   Format converter drivers
-   Filter drivers

Compressors and decompressors change one format type to another. For example, a compressor or decompressor can change a PCM (Pulse Code Modulation) file to an ADPCM (Adaptive Differential Pulse Code Modulation) file. Format converters change the format, but not the data type. For example, a converter can change 44-kHz, 16-bit data to 44-kHz, 8-bit data. Filters do not change the data format at all, but they change the waveform-audio data in some manner. For example, a filter could combine a data stream and an echo of itself. A single ACM driver, or a filter tag or format tag within a driver, might also support combinations of the preceding types.

For waveform-audio output, the ACM passes each buffer of data to the converter as it arrives. The converter decompresses the data and returns the decompressed data to the ACM in a "shadow" buffer. The ACM then passes the decompressed shadow buffer to the waveform-audio driver. The ACM allocates the shadow buffers whenever it receives a prepare message.

For waveform-audio input, the ACM passes empty shadow buffers to the driver. It uses a background task to receive a notification after the driver has filled the shadow buffer. The ACM then passes the buffers to the driver for compression. After compression is finished, the driver passes the data to the application.

 

 




