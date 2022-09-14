---
description: The PKEY\_AudioEndpoint\_ControlPanelPageProvider property specifies the CLSID of the registered provider of the device-properties extension for the audio endpoint device.
ms.assetid: 429a7572-b609-46fd-946e-ee34ddd6cc5e
title: PKEY_AudioEndpoint_ControlPanelPageProvider (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_ControlPanelPageProvider

The **PKEY\_AudioEndpoint\_ControlPanelPageProvider** property specifies the CLSID of the registered provider of the device-properties extension for the audio endpoint device. The extension supplies the audio endpoint properties that are displayed in the device-properties page of the Windows multimedia control panel, Mmsys.cpl. For more information about Mmsys.cpl, see the Windows DDK documentation.

The **vt** member of the **PROPVARIANT** structure is set to VT\_LPWSTR.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains a GUID that identifies the provider of the control-panel extension.

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

 

 




