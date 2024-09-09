---
description: Decoder Volume Control
ms.assetid: 94d68722-a0c2-47a7-a0a0-ae315f8f31ed
title: Decoder Volume Control
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Decoder Volume Control

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Applications control audio volume through the [**IBasicAudio**](/windows/desktop/api/Control/nn-control-ibasicaudio) interface. An **IBasicAudio** interface handler is provided for KSProxy. For a decoder to handle the volume commands from KSProxy, it must add several registry keys in its setup script and support the **KSPROPSETID\_Wave** property set.

Create some new registry keys for the driver:


```C++
HKLM\SYSTEM\
  CurrentControlSet\Control
    DeviceClasses
      (decoder guid, eg 2721AE....)
        (Pnp id, eg ##?#VDGENDEV#...)
          #GLOBAL
            Device Parameters
              CLSID      REG_SZ   {17CCA...}
                FriendlyName   REG_SZ   WDM DVD Driver
                  Interfaces <--- create this key
                  {b9f8ac3e-0f71-11d2-b72c-00c04fb6bd3d} // Create this key.
    MediaInterfaces
      {b9f8ac3e-0f71-11d2-b72c-00c04fb6bd3d} // Create this key.
        (default)  REG_SZ   'KsProxy IBasicAudio handler' // Set this value.
        IID        REG_SZ   56 a8 68 b3 0a d4 11 ce b0 3a 00 20 af 0b a7 70 
                            // Create this key.
```



To implement volume control, the driver also must support **KSPROPSETID\_Wave**, along with KsProperty.Id = KSPROPERTY\_WAVE\_VOLUME. This property is passed to the driver through the [**IKsPropertySet::Get**](ikspropertyset-get.md) and [**IKsPropertySet::Set**](ikspropertyset-set.md) methods. The LeftAttenuation and RightAttentuation fields specify the left/right speaker volumes as linear values from 0x0000 to 0xffff.

## Related topics

<dl> <dt>

[Decoder Interfaces and Specifications](decoder-interfaces-and-specifications.md)
</dt> </dl>

 

 



