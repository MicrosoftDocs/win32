---
description: Notifying CBasePin of Filter State Changes
ms.assetid: 521ba95b-1f2d-4ad0-ab9b-4f1e3343a2d3
title: Notifying CBasePin of Filter State Changes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Notifying CBasePin of Filter State Changes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CBasePin** class is notified whenever the state of the owning filter changes. For each state transition, the filter calls a corresponding method on the pin, as shown in the following table.



| New Filter State | CBasePin Method                                 |
|------------------|-------------------------------------------------|
| Stopped          | [**CBasePin::Inactive**](cbasepin-inactive.md) |
| Paused           | [**CBasePin::Active**](cbasepin-active.md)     |
| Running          | [**CBasePin::Run**](cbasepin-run.md)           |



 

The derived class should override these methods to respond to the state change. Depending on the filter, the pin might start a worker thread that delivers samples, commit or decommit its memory allocator, and so forth.

 

 



