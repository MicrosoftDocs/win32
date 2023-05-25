---
description: System Device Enumerator
ms.assetid: ea98be7f-580d-4986-bd6b-d254a2c075e8
title: System Device Enumerator
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# System Device Enumerator

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The System Device Enumerator enumerates filters and hardware devices installed on the system. Applications can use this component to locate filters and devices in a given category. Create this object by calling **CoCreateInstance**.



| Label | Value |
|------------------|------------------------------------------|
| Class Identifier | CLSID\_SystemDeviceEnum                  |
| Interfaces       | [**ICreateDevEnum**](/windows/desktop/api/Strmif/nn-strmif-icreatedevenum) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Enumerating Devices and Filters](enumerating-devices-and-filters.md)
</dt> <dt>

[Filter Categories](filter-categories.md)
</dt> </dl>

 

 



