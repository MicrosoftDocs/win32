---
description: The following tables describe the media types used for BDA digital television filters.
ms.assetid: 875df611-a6ae-4a73-b00b-799249a39ff3
title: BDA Media Types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BDA Media Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tables describe the media types used for BDA digital television filters.

## Antenna

This media type is used for the pin connection between the Network Provider filter and the tuner filter.



| Label | Value |
|-------------|----------------------------------|
| Major type  | KSDATAFORMAT\_TYPE\_BDA\_ANTENNA |
| Subtype     | MEDIASUBTYPE\_None               |
| Format type | FORMAT\_None                     |



 

## Intermediate Frequency (IF) Signal

This media type represents the IF signal that is sent from the tuner to the demodulator.



| Label | Value |
|-------------|-------------------------------------|
| Major type  | KSDATAFORMAT\_TYPE\_BDA\_IF\_SIGNAL |
| Subtype     | MEDIASUBTYPE\_None                  |
| Format type | FORMAT\_None                        |



 

 

 



