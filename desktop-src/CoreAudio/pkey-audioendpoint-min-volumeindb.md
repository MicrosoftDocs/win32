---
description: The PKEY\_AudioEndpoint\_Min\_VolumeInDb property indicates the minimum volume in dB for an audio endpoint device to be used by the OS volume implementation.
title: PKEY_AudioEndpoint_Min_VolumeInDb (Mmdeviceapi.h)
ms.topic: reference
ms.date: 03/04/2026
---

# PKEY\_AudioEndpoint\_Min\_VolumeInDb

The **PKEY\_AudioEndpoint\_Min\_VolumeInDb** property indicates the minimum volume in decibels for an audio endpoint device. This INF-supplied property is used by the OS volume implementation.

The **vt** member of the **PROPVARIANT** structure is set to VT\_I4.

The **lVal** member of the **PROPVARIANT** structure contains a float value expressed in fixed point 16.16 format.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Build 26100<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2025<br/>                                                           |
| Header<br/>                   | <dl> <dt>Mmdeviceapi.h</dt> </dl> |



## See also

<dl> <dt>

[**Audio Endpoint Properties**](audio-endpoint-properties.md)
</dt> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> <dt>

[**PKEY\_AudioEndpoint\_Max\_VolumeInDb**](pkey-audioendpoint-max-volumeindb.md)
</dt> </dl>

 

 




