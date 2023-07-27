---
description: Mapping DirectX Video Acceleration to IAMVideoAccelerator
ms.assetid: 5afb1021-85b9-42ae-ae85-f4e114194e70
title: Mapping DirectX Video Acceleration to IAMVideoAccelerator
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mapping DirectX Video Acceleration to IAMVideoAccelerator

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following section is primarily relevant for software decoder developers. It provides detailed information on how to use the [**IAMVideoAccelerator**](/previous-versions/windows/desktop/api/videoacc/nn-videoacc-iamvideoaccelerator) Interface when communicating through the [Overlay Mixer](overlay-mixer-filter.md) or Video Mixing Renderer filter with a DirectX VA-enabled hardware device. This section covers the following topics:

-   [Restricted Mode Profile and Configuration Establishment](restricted-mode-profile-and-configuration-establishment.md)
-   [DirectX Video Acceleration IAMVideoAccelerator Operational Specification](directx-video-acceleration-iamvideoaccelerator-operational-specification.md)
-   [Operational Correspondence with Motion Compensation Device Driver](operational-correspondence-with-motion-compensation-device-driver.md)

 

 



