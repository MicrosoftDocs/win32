---
description: Device Transport State
ms.assetid: 15edded0-207c-41e8-81fe-deb6335045eb
title: Device Transport State
ms.topic: article
ms.date: 05/31/2018
---

# Device Transport State

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

 

 



