---
description: The PKEY\_AudioEndpoint\_FormFactor property specifies the form factor of the audio endpoint device. The form factor indicates the physical attributes of the audio endpoint device that the user manipulates.
ms.assetid: f49cb7da-3b50-47e2-90b4-1a885001b5d7
title: PKEY_AudioEndpoint_FormFactor (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_FormFactor

The **PKEY\_AudioEndpoint\_FormFactor** property specifies the form factor of the audio endpoint device. The form factor indicates the physical attributes of the audio endpoint device that the user manipulates.

The **vt** member of the **PROPVARIANT** structure is set to VT\_UI4.

The **uintVal** member of the **PROPVARIANT** structure contains an enumeration value that is cast to type UINT. It is set to one of the following [**EndpointFormFactor**](/windows/win32/api/mmdeviceapi/ne-mmdeviceapi-endpointformfactor) enumeration values:

-   RemoteNetworkDevice
-   Speakers
-   LineLevel
-   Headphones
-   Microphone
-   Headset
-   Handset
-   UnknownDigitalPassthrough
-   SPDIF
-   HDMI
-   UnknownFormFactor

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mmdeviceapi.h</dt> </dl> |



## See also

<dl> <dt>

[**Audio Endpoint Properties**](audio-endpoint-properties.md)
</dt> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> </dl>

 

 




