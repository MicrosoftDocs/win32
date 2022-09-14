---
description: The PKEY\_AudioEngine\_DeviceFormat property specifies the device format, which is the format that the user has selected for the stream that flows between the audio engine and the audio endpoint device when the device operates in shared mode.
ms.assetid: eb3c734f-0bb8-47cc-a01f-99569f472cde
title: PKEY_AudioEngine_DeviceFormat (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEngine\_DeviceFormat

The **PKEY\_AudioEngine\_DeviceFormat** property specifies the device format, which is the format that the user has selected for the stream that flows between the audio engine and the audio endpoint device when the device operates in shared mode. This format might not be the best default format for an exclusive-mode application to use. Typically, an exclusive-mode application finds a suitable device format by making some number of calls to the [**IAudioClient::IsFormatSupported**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-isformatsupported) method. For more information, see [Device Formats](device-formats.md).

The **vt** member of the **PROPVARIANT** structure is set to VT\_BLOB.

The **blob** member of the **PROPVARIANT** structure is a structure of type **BLOB** that contains two members. Member **blob.cbSize** is a **DWORD** that specifies the number of bytes in the format description. Member **blob.pBlobData** points to a **WAVEFORMATEX** structure that contains the format description. For more information about **BLOB**, see the Windows SDK documentation. For more information about **WAVEFORMATEX**, see the Windows DDK documentation.

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

 

 




