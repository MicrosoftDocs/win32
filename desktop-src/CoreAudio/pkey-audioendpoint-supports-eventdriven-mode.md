---
description: The PKEY\_AudioEndpoint\_Supports\_EventDriven\_Mode property indicates whether the endpoint supports the event-driven mode.
ms.assetid: 9cffd9ae-710b-4d41-aa02-3ab1a065e544
title: PKEY_AudioEndpoint_Supports_EventDriven_Mode (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_Supports\_EventDriven\_Mode

The **PKEY\_AudioEndpoint\_Supports\_EventDriven\_Mode** property indicates whether the endpoint supports the event-driven mode.

The **vt** member of the **PROPVARIANT** structure is set to VT\_UI4.

The **uintVal** member of the **PROPVARIANT** structure is a **DWORD** that indicates if the endpoint supports the event-driven mode.

## Remarks

This property value is populated by an audio OEM in an .inf file to indicate that the HDAudio hardware supports event driven mode as per the WHQL requirement.

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

 

 




