---
Description: Core Audio Structures
ms.assetid: 92585cd4-baa9-4f75-816e-b83f5badad37
title: Core Audio Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Core Audio Structures

This section describes the structures that are used by the Core Audio APIs in Windows Vista and later.



| Structure                                                                     | Description                                                                                                                                                         |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AUDIO\_VOLUME\_NOTIFICATION\_DATA**](/windows/win32/Endpointvolume/ns-endpointvolume-audio_volume_notification_data?branch=master)   | Describes a change in the volume level or muting state of an audio endpoint device.                                                                                 |
| [**DIRECTX\_AUDIO\_ACTIVATION\_PARAMS**](/windows/win32/Mmdeviceapi/ns-mmdeviceapi-tagdirectx_audio_activation_params?branch=master) | Specifies the initialization parameters for a DirectSound stream.                                                                                                   |
| [**KSJACK\_DESCRIPTION**](/windows/win32/Devicetopology/ns-devicetopology-__midl___midl_itf_devicetopology_0000_0000_0009?branch=master)                             | Retrieved through [**IKsJackDescription::GetJackDescription**](/windows/win32/Devicetopology/nf-devicetopology-iksjackdescription-getjackdescription?branch=master); describes an audio jack.                                 |
| [**KSJACK\_DESCRIPTION2**](/windows/win32/Devicetopology/ns-devicetopology-_tagksjack_description2?branch=master)<br/>                | Retrieved through [**IKsJackDescription2::GetJackDescription2**](/windows/win32/Devicetopology/nf-devicetopology-iksjackdescription2-getjackdescription2?branch=master); describes an audio jack. <br/>                 |
| [**KSJACK\_SINK\_INFORMATION**](/windows/win32/Devicetopology/ns-devicetopology-_tagksjack_sink_information?branch=master)<br/>       | Retrieved through [**IKsJackSinkInformation::GetJackSinkInformation**](/windows/win32/Devicetopology/nf-devicetopology-iksjacksinkinformation-getjacksinkinformation?branch=master); describes an audio jack sink.<br/> |
| [**LUID**](/windows/win32/Devicetopology/ns-devicetopology-_luid?branch=master)<br/>                                               | Stores the video port identifier.<br/>                                                                                                                        |



 

## Related topics

<dl> <dt>

[Programming Reference](programming-reference.md)
</dt> </dl>

 

 




