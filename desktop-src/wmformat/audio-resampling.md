---
title: Audio Resampling
description: Audio Resampling
ms.assetid: ec6ad6b2-1d35-4ac4-9a1e-3fc9c053000c
keywords:
- Windows Media Format SDK,audio resampling
- Windows Media Format SDK,resampling audio
- Advanced Systems Format (ASF),audio resampling
- ASF (Advanced Systems Format),audio resampling
- Advanced Systems Format (ASF),resampling audio
- ASF (Advanced Systems Format),resampling audio
- audio resampling
- resampling audio,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Resampling

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Every compressed format of an audio codec has a specific sample rate and sample size. These do not need to match the settings of the input format or output format. If an input format has different settings than the compressed format described in the profile, the writer will resample the audio, during the encoding process, to match the compressed format. Only certain formats are accepted by the writer as input. When you enumerate the input formats for a compressed audio stream, all of the formats retrieved can be resampled to match the format in the profile.

When reading compressed audio, the reader will resample the content to match the output format. You must use one of the output formats enumerated by the reader, so you are guaranteed that the audio can be resampled to the output format settings.

Each resampling potentially affects the quality of the audio. When possible, you should use input and output formats with settings that match the compressed format.

## Related topics

<dl> <dt>

[**File Writing Features**](file-writing-features.md)
</dt> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> <dt>

[**Working with Outputs**](working-with-outputs.md)
</dt> </dl>

 

 




