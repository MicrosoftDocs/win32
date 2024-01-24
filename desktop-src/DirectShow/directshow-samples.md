---
title: DirectShow sample apps
description: DirectShow sample apps
ms.assetid: 4166d5ca-5e02-49f6-bcb1-d448f8175a0c
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DirectShow sample apps

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can find the DirectShow sample apps in the [Windows-classic-samples](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/multimedia/directshow) repository on GitHub.

The table below lists all of the DirectShow samples provided in that repo. For instructions on how to build the samples, refer to the documentation provided in the Windows SDK. If a topic exists describing a sample, then the first column of this table links to it.

| Sample | Area | Description | Additional Dependencies | 
|--------|------|-------------|-------------------------|
| <a href="directshow-base-classes.md">DirectShow Base Classes</a> | Base class library | C++ classes and utility functions designed for implementing DirectShow filters. | 
| <a href="amcap-sample.md">AmCap Sample</a> | Capture | Video capture application. | strmbase.lib | 
| <a href="dvapp-sample.md">DVApp Sample</a> | Capture | Digital Video (DV) capture application. | 
| <a href="playcap-sample.md">PlayCap Sample</a> | Capture | Simple capture application. | 
| <a href="dmo-demo-sample.md">DMO Demo Sample</a> | DMO | Streams audio data from a WAV file through an audio effect DMO. | DirectX SDK | 
| DVD Sample | DVD | Demonstrates basic DVD playback and navigation, plus advanced features such as parental level management, bookmarks, karaoke, and command synchronization. | 
| <a href="inftee-filter-sample.md">InfTee Filter Sample</a> | Filters, miscellaneous | Sample implementation of the <a href="infinite-pin-tee-filter.md">Infinite Pin Tee</a> filter. | strmbase.lib | 
| <a href="metronome-filter-sample.md">Metronome Filter Sample</a> | Filters, miscellaneous | Shows how to implement a reference clock. | strmbase.lib | 
| <a href="psi-parser-filter-sample.md">PSI Parser Filter Sample</a> | Filters, miscellaneous | Receives Program Specific Information (PSI) tables from an MPEG-2 transport stream and extracts program information. | strmbase.lib | 
| <a href="dump-filter-sample.md">Dump Filter Sample</a> | Filters, renderer | Writes media samples receives to a text file. | strmbase.lib | 
| SampVid Filter | Filters, renderer | Video renderer filter. | strmbase.lib | 
| <a href="scope-filter-sample.md">Scope Filter Sample</a> | Filters, renderer | Displays sound data as wave forms. | strmbase.lib | 
| <a href="async-filter-sample.md">Async Filter Sample</a> | Filters, source | File reader filter that supports progressive download. | strmbase.lib | 
| <a href="ball-filter-sample.md">Ball Filter Sample</a> | Filters, source | Video source filter that produces an image of a bouncing ball. | strmbase.lib | 
| <a href="push-source-filters-sample.md">Push Source Filters Sample</a> | Filters, source | Source filters that provide the following data as a video stream: A single bitmap, a set of bitmaps, a copy of the current desktop image. | strmbase.lib | 
| <a href="synth-filter-sample.md">Synth Filter Sample</a> | Filters, source | Source filter that generates audio waveforms. This sample demonstrates dynamic graph building. | strmbase.lib | 
| <a href="ezrgb24-filter-sample.md">EZRGB24 Filter Sample</a> | Filters, transform | Image processing filter. | strmbase.lib | 
| <a href="gargle-filter-sample.md">Gargle Filter Sample</a> | Filters, transform | Audio effect filter. | strmbase.lib | 
| <a href="wavdest-filter-sample.md">WavDest Filter Sample</a> | Filters, transform | Writes an audio stream to a WAV file. | strmbase.lib | 
| <a href="dmoenum-sample.md">DMOEnum Sample</a> | Miscellaneous | Shows how to enumerate <a href="directx-media-objects.md">DirectX Media Objects</a> (DMOs). | 
| <a href="mapper-sample.md">Mapper Sample</a> | Miscellaneous | Shows how to use the <a href="filter-mapper.md">Filter Mapper</a> to find filters in the registry. | 
| SysEnum Sample | Miscellaneous | Demonstrates using the <a href="system-device-enumerator.md">System Device Enumerator</a> to enumerate devices and filters. | 
| <a href="cutscene-sample.md">CutScene Sample</a> | Playback | Plays a video file in full-screen mode. | 
| DDrawXCL Sample | Playback | Plays video in DirectDraw exclusive full-screen mode, using the <a href="/windows/desktop/api/Strmif/nn-strmif-iddrawexclmodevideo"><strong>IDDrawExclModeVideo</strong></a> interface on the <a href="overlay-mixer-filter.md">Overlay Mixer</a> filter. | 
| DShowPlayer Sample | Playback | Video playback application. | 
| EVRPlayer Sample | Playback | Demonstrates how to use the DirectShow EVR filter. **Note:** Requires Windows Vista or later.<br> This sample is available in the Windows SDK for Windows Server 2008 or later.<br> | strmbase.lib | 
| Texture3D9 Sample | Playback | Draws video on a Microsoft DirectX 9.0 texture surface. | strmbase.lib, DirectX SDK | 
| <a href="ticker-sample.md">Ticker Sample</a> | VMR-9 | Uses the VMR-9 to blend video and text. | 
| VMR9Allocator Sample | VMR-9 | Implements a custom allocator-presenter for the VMR-9. | strmbase.lib | 
| VMR9Compositor Sample | VMR-9 | Implements a custom mixer for the VMR-9. | 
| <a href="vmrplayer-sample.md">VMRPlayer Sample</a> | VMR-9 | Uses the VMR-9 to blend one or two running videos and a static image. | 
| Watermark Sample | VMR-9 | Blends a static bitmap onto a video during playback, using the VMR-9. | 
| <a href="windowless-sample.md">Windowless Sample</a> | VMR-9 | Demonstrates windowless mode in the VMR-9. | 

## Additional dependencies

Some of the samples link to the DirectShow base class library. To build those samples, first build the base class library. For more information, see [DirectShow base classes](directshow-base-classes.md). The base class library is required for all of the sample filters.

A few of the samples also require the DirectX SDK, in addition to the Windows SDK. To build those samples, you must install the DirectX SDK, and set the `%DXSDK\_DIR%` environment variable equal to your DirectX SDK installation path.

Many of the DirectShow samples use a set of common headers and source files located in the directrory `\[SDK Root\]Samples\Multimedia\DirectShow\Common`. If you copy a sample folder to another directory, then make sure to copy the `Common` folder as well.

## Related topics

* [Setting up the build environment](setting-up-the-build-environment.md)
