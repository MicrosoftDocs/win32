---
description: The PKEY\_AudioEndpoint\_Association property associates a kernel-streaming (KS) pin category with an audio endpoint device.
ms.assetid: a20e082c-eddb-4b81-b851-49350b87e69a
title: PKEY_AudioEndpoint_Association (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_Association

The **PKEY\_AudioEndpoint\_Association** property associates a kernel-streaming (KS) pin category with an audio endpoint device. The .inf file that installs an audio adapter assigns a pin category to each KS pin in the adapter. A KS pin on an adapter device represents the point at which an audio stream enters or leaves the device. A pin category is a GUID that specifies the type of function performed by a KS pin. For example, header file Ksmedia.h defines pin-category GUID KSNODETYPE\_MICROPHONE to indicate a KS pin that connects to a microphone, and KSNODETYPE\_HEADPHONES to indicate a KS pin that connects to headphones. For more information, see the description of pin category properties in the Windows DDK documentation.

The **vt** member of the **PROPVARIANT** structure is set to VT\_LPWSTR.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains a KS pin category GUID.

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

 

 




