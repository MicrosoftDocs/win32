---
description: Device Transport State
ms.assetid: 15edded0-207c-41e8-81fe-deb6335045eb
title: Device Transport State
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Transport State

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To retrieve the current state of the device, such as play, pause, or stop, call the [**IAMExtTransport::get\_Mode**](/windows/desktop/api/Strmif/nf-strmif-iamexttransport-get_mode) method. The method retrieves a constant that indicates the device state:



| Value                    | Device State |
|--------------------------|--------------|
| ED\_MODE\_PLAY           | Play         |
| ED\_MODE\_STOP           | Stop         |
| ED\_MODE\_FREEZE         | Pause        |
| ED\_MODE\_FF             | Fast-forward |
| ED\_MODE\_REW            | Rewind       |
| ED\_MODE\_RECORD         | Record       |
| ED\_MODE\_RECORD\_FREEZE | Record-pause |



 

The following code checks the device state:


```C++
LONG State;
hr = MyDevCap.pTransport->get_Mode(&State);
if (SUCCEEDED(hr))
{
    switch (State)
    {
        case ED_MODE_PLAY:
        // ... 
    }
}
```



## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 



