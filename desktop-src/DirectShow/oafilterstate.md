---
description: The OAFilterState data type defines the state of the filter graph. The value is a member of the FILTER\_STATE enumeration. This data type is defined for OLE Automation clients, such as Microsoft Visual Basic 6.0.
ms.assetid: c0e5d581-a15a-4dd2-b38c-72285cfc2617
title: OAFilterState (Control.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# OAFilterState

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `OAFilterState` data type defines the state of the filter graph. The value is a member of the [**FILTER\_STATE**](/windows/win32/api/strmif/ne-strmif-filter_state) enumeration. This data type is defined for OLE Automation clients, such as Microsoft Visual Basic 6.0.


```C++
typedef long OAFilterState;
```



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Control.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Data Types](directshow-data-types.md)
</dt> <dt>

[**IMediaControl::GetState**](/windows/desktop/api/Control/nf-control-imediacontrol-getstate)
</dt> </dl>

 

 




