---
title: Mapping Waveform-Audio Devices
description: Mapping Waveform-Audio Devices
ms.assetid: e23919c9-c5fa-4406-920c-1fdbeea4821d
keywords:
- multimedia audio,mapping waveform-audio devices
- audio,mapping waveform-audio devices
- audio compression manager (ACM),mapping waveform-audio devices
- ACM (audio compression manager),mapping waveform-audio devices
- mapping waveform-audio devices
- multimedia audio,mapper
- audio,mapper
- audio compression manager (ACM),mapper
- ACM (audio compression manager),mapper
- mapper
- waveform audio,mapping devices
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mapping Waveform-Audio Devices

\[The feature associated with this page, [﻿Audio Compression Manager](/windows/win32/multimedia/audio-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

Windows provides a set of standard functions for audio devices. These functions issue calls to device drivers that manage hardware devices. The system uses a module called a "mapper" to manage installed devices. The mapper uses special hooks in the driver interface to intercept calls and to act as an intermediary between the system and the drivers installed in the system. The mapper is responsible for matching an application's requests for access to a device with the available devices and for finding a device that meets the current application's audio requirements. The system provides mappers for standard driver types: waveform-audio, MIDI (Musical Instrument Digital Interface), and auxiliary devices.

The ACM is an extension of the basic multimedia system and is installed as a mapper. This means the ACM uses the driver-interface mapper hooks for waveform-audio devices. Using these hooks allows the ACM to decode or encode waveform-audio data before passing it to or from a waveform-audio device driver. The difference between the ACM and the standard system mapper is that the ACM can search for a waveform-audio device that supports a specified format or find a combination of a waveform-audio device and an ACM compressor or decompressor that supports a specified format.

When an application requests that the system open a waveform-audio device for input or output, the request specifies the format and device. When the specified device is the mapper, the mapper must find a device that supports the specified format. The mapper implemented in the ACM searches for an installed waveform-audio device that supports the specified format. If the ACM cannot find such a device, it searches for a waveform-audio device and a compressor or decompressor that together support the format. Specifically, the ACM searches for a compressor or decompressor that converts the specified format into a format that is supported by an installed waveform-audio device. After the ACM finds a device that supports the converted format, it can honor requests to play or record the format originally requested, even though no installed waveform-audio device directly supports that format.

In addition to format conversion, the ACM also offers services to support compression, decompression, filtering, format selection, and filter selection. It provides a standard API that it supports by calling its own drivers.

 

 




