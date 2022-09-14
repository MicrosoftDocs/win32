---
description: The PKEY\_AudioEndpoint\_JackSubType property contains an output category GUID for an audio endpoint device.
ms.assetid: 5d712823-73e3-4872-a1ea-c166ed41ffa0
title: PKEY_AudioEndpoint_JackSubType (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_JackSubType

The **PKEY\_AudioEndpoint\_JackSubType** property contains an output category GUID for an audio endpoint device. The header file Ksmedia.h defines the GUIDs; each GUID specifies the type of connection. These GUIDs also have associated pin categories. For example, header file Ksmedia.h defines the GUID **KSNODETYPE\_DISPLAYPORT\_INTERFACE** for a display port that connects with the KS pin defined by the GUID **PINNAME\_DISPLAYPORT\_OUT**.

For more information, see the description of pin category properties in the Windows DDK documentation.

The **vt** member of the **PROPVARIANT** structure is set to **VT\_LPWSTR**.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains a category GUID.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Mmdeviceapi.h</dt> </dl> |



## See also

<dl> <dt>

[**Audio Endpoint Properties**](audio-endpoint-properties.md)
</dt> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> </dl>

 

 




