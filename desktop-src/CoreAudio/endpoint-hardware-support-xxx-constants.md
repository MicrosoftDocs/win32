---
description: The ENDPOINT\_HARDWARE\_SUPPORT\_XXX constants are hardware support flags for an audio endpoint device.
ms.assetid: 54032f75-2287-4589-bda5-e005ee077c41
title: ENDPOINT_HARDWARE_SUPPORT_XXX Constants (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ENDPOINT\_HARDWARE\_SUPPORT\_XXX Constants

The ENDPOINT\_HARDWARE\_SUPPORT\_XXX constants are hardware support flags for an audio endpoint device.



| Constant/value                                                                                                                                                                                                                                                                           | Description                                                              |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| <span id="ENDPOINT_HARDWARE_SUPPORT_VOLUME"></span><span id="endpoint_hardware_support_volume"></span><dl> <dt>**ENDPOINT\_HARDWARE\_SUPPORT\_VOLUME**</dt> <dt>0x00000001</dt> </dl> | The audio endpoint device supports a hardware volume control.<br/> |
| <span id="ENDPOINT_HARDWARE_SUPPORT_MUTE"></span><span id="endpoint_hardware_support_mute"></span><dl> <dt>**ENDPOINT\_HARDWARE\_SUPPORT\_MUTE**</dt> <dt>0x00000002</dt> </dl>       | The audio endpoint device supports a hardware mute control.<br/>   |
| <span id="ENDPOINT_HARDWARE_SUPPORT_METER"></span><span id="endpoint_hardware_support_meter"></span><dl> <dt>**ENDPOINT\_HARDWARE\_SUPPORT\_METER**</dt> <dt>0x00000004</dt> </dl>    | The audio endpoint device supports a hardware peak meter.<br/>     |



## Remarks

The [**IAudioEndpointVolume::QueryHardwareSupport**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-queryhardwaresupport) and [**IAudioMeterInformation::QueryHardwareSupport**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudiometerinformation-queryhardwaresupport) methods use the ENDPOINT\_HARDWARE\_SUPPORT\_XXX constants.

A hardware support mask indicates which functions an audio endpoint device implements in hardware. The mask can be either 0 or the bitwise-OR combination of one or more ENDPOINT\_HARDWARE\_SUPPORT\_XXX constants. If a bit that corresponds to a particular ENDPOINT\_HARDWARE\_SUPPORT\_XXX constant is set in the mask, then the meaning is that the function represented by that constant is implemented in hardware by the device.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mmdeviceapi.h</dt> </dl> |



## See also

<dl> <dt>

[Core Audio Constants](core-audio-constants.md)
</dt> <dt>

[**IAudioEndpointVolume::QueryHardwareSupport**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudioendpointvolume-queryhardwaresupport)
</dt> <dt>

[**IAudioMeterInformation::QueryHardwareSupport**](/windows/desktop/api/Endpointvolume/nf-endpointvolume-iaudiometerinformation-queryhardwaresupport)
</dt> </dl>

 

 




