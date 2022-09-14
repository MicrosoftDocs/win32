---
description: Signal Format
ms.assetid: 8684972c-3233-49bf-8c34-ca644aca432a
title: Signal Format
ms.topic: article
ms.date: 05/31/2018
---

# Signal Format

A DV camcorder's signal format can be NTSC or PAL, standard or long-play.

**MSDV Driver**

To get the input signal format from the MSDV driver, call the [**IAMExtTransport::GetTransportBasicParameters**](/windows/desktop/api/Strmif/nf-strmif-iamexttransport-gettransportbasicparameters) method and pass in the ED\_TRANSBASIC\_INPUT\_SIGNAL flag. The method returns a defined constant, indicating the format.

The following code checks the signal format, and uses this value to calculates the average time per frame. The variable Mode receives the signal-format constant.


```C++
LONG Mode, AvgTimePerFrame;
hr = MyDevCap.pTransport->GetTransportBasicParameters(
        ED_TRANSBASIC_INPUT_SIGNAL, &Mode, NULL);
if (SUCCEEDED(hr))
{
    switch (Mode)
    {
    case ED_TRANSBASIC_SIGNAL_525_60_SD: // NTSC SD
        AvgTimePerFrame = 33;  // 33 msec (29.97 FPS)
        break;
    case ED_TRANSBASIC_SIGNAL_525_60_SDL: // NTSC SDL
        AvgTimePerFrame = 33;  
        break;
    case ED_TRANSBASIC_SIGNAL_625_50_SD: // PAL SD
        AvgTimePerFrame = 40;  // 40 msec (25 FPS)
        break;
    case ED_TRANSBASIC_SIGNAL_625_50_SDL: // PAL SDL
        AvgTimePerFrame = 40;  
        break;
    default: 
        // Unknown type
        AvgTimePerFrame = 33; // Default
        break;
    }
}
```



To get the output signal format, call the same method with the ED\_TRANSBASIC\_OUTPUT\_SIGNAL flag.

**UVC Driver**

To get the input or output signal format from the UVC driver, call [**IAMStreamConfig::GetFormat**](/windows/desktop/api/Strmif/nf-strmif-iamstreamconfig-getformat) on the pin and examine the video format block. (For UVC devices, the code shown in the previous example usually returns ED\_TRANSBASIC\_SIGNAL\_UNKNOWN, so it is not reliable.)

## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 



