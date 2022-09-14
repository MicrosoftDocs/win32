---
description: Recovering from an Invalid-Device Error (Spatial Sound)
title: Recovering from an Invalid-Device Error (Spatial Sound)
ms.topic: article
ms.date: 10/29/2020
---

# Recovering from an Invalid-Device Error (Spatial Sound)

Many of the methods of the Microsoft Spatial Audio API, such as [ISpatialAudioClient](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient), [ISpatialAudioObjectRenderStream](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobjectrenderstream), and [ISpatialAudioObject](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobject), return error codes if the audio endpoint device that the client application is using becomes invalid or the spatial audio rendering format is changed on the endpoint. These error codes indicates that the endpoint device has been unplugged, or that the audio hardware or associated hardware resources have been reconfigured, disabled, removed, spatial audio mode is changed or otherwise made unavailable for use. Frequently, the application can recover from this error.

Error codes that indicate an invalid-device error include the following:

- SPTLAUDCLNT_E_DESTROYED
- AUDCLNT_E_DEVICE_INVALIDATED
- AUDCLNT_E_RESOURCES_INVALIDATED
- AUDCLNT_E_UNSUPPORTED_FORMAT
- SPTLAUDCLNT_E_INTERNAL

## Strategies for handling invalid-device errors

The recommended strategy for recovering from an invalid-device error depends on whether the application automatically selects a specific device based on internal requirements or it allows the user to explicitly select a device from a list of available devices. 

### Default audio device

If the application automatically selects the default device, use the following steps to recover.

1. Release the [ISpatialAudioObjectRenderStream](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobjectrenderstream) and [ISpatialAudioClient](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) interface and any other spatial audio interfaces that are used for rendering. 
1. Call [IMMDeviceEnumerator::GetDefaultAudioEndpoint](/windows/win32/api/mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) to get the current default audio device.
1. Attempt to activate **ISpatialAudioClient** on the audio device.
1. Activate **ISpatialAudioObjectRenderStream**. 

### Specifically selected audio device

If the application selects a specific audio device, use the following steps to recover.

1. Release the ISpatialAudioObjectRenderStream interface and any other spatial audio interfaces that are used for rendering, but don't release **ISpatialAudioClient**.
1. Use the current **ISpatialAudioClient** instance to activate **ISpatialAudioObjectRenderStream**.

Note that for both strategies listed above, the same steps can be applied to applications that use the [ISpatialAudioObjectRenderStreamForMetadata](/windows/win32/api/spatialaudiometadata/nn-spatialaudiometadata-ispatialaudioobjectrenderstreamformetadata) or [ISpatialAudioObjectRenderStreamForHrtf](/windows/win32/api/spatialaudiohrtf/nn-spatialaudiohrtf-ispatialaudioobjectrenderstreamforhrtf) interfaces. Simply replace **ISpatialAudioObjectRenderStream** in the above steps with the metadata or Hrtf interfaces.


## Related topics

<dl> <dt>
[Recovering from an Invalid-Device Error](recovering-from-an-invalid-device-error.md)
[Stream Management](stream-management.md)
</dt> </dl>

 

 



