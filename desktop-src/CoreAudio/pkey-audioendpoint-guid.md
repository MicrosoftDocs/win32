---
description: The PKEY\_AudioEndpoint\_GUID property supplies the DirectSound device identifier that corresponds to the audio endpoint device.
ms.assetid: d3119504-9b6a-47b8-b3c6-15cb329929cb
title: PKEY_AudioEndpoint_GUID (Mmdeviceapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PKEY\_AudioEndpoint\_GUID

The **PKEY\_AudioEndpoint\_GUID** property supplies the DirectSound device identifier that corresponds to the audio endpoint device. The property value is a GUID that the client can supply as the device identifier to the **DirectSoundCreate** or **DirectSoundCaptureCreate** function in the DirectSound API. This value uniquely identifies the audio endpoint device across all audio endpoint devices in the system. For more information about DirectSound, see the DirectX SDK documentation.

The **vt** member of the **PROPVARIANT** structure is set to VT\_LPWSTR.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains a GUID that identifies the audio endpoint device in DirectSound.

As explained previously, the [MMDevice API](mmdevice-api.md) supports [device roles](device-roles.md). Although DirectSound does not directly support device roles, a DirectSound client can use the PKEY\_AudioEndpoint\_GUID property to select a DirectSound rendering or capture device based on its device role.

For example, a DirectSound application performs the following steps to create a DirectSound device that corresponds to the rendering endpoint device that the user has assigned the eMultimedia role to:

1.  Call the [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) method to get the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface of the rendering endpoint device that has the eMultimedia role.
2.  Call the [**IMMDevice::OpenPropertyStore**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-openpropertystore) method to obtain the **IPropertyStore** interface of the eMultimedia device. For more information about **IPropertyStore**, see the Windows SDK documentation.
3.  Call the **IPropertyStore::GetValue** method to obtain the PKEY\_AudioEndpoint\_GUID property value.
4.  Convert the property value from a GUID in string format to a 16-byte GUID structure.
5.  Call the **DirectSoundCreate** function with the GUID to create the device with the eMultimedia role.

> [!Note]  
> **PKEY\_AudioEndpoint\_GUID** is a read-only property regardless of the storage-access mode requested by the application in [**IMMDevice::OpenPropertyStore**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-openpropertystore). If an application attempts to set a value by using **IPropertyStore::SetValue**, this call fails with the E\_ACCESSDENIED error code.

 

Note that the 16-byte GUID generated in step 4 matches the device GUID that identifies the device during DirectSound device enumeration. The **DirectSoundEnumerate** function enumerates rendering endpoint devices, and the **DirectSoundCaptureEnumerate** function enumerates capture endpoint devices. In either case, the device GUID is the first parameter passed to the enumeration callback function. For more information about DirectSound enumeration, see the DirectX SDK documentation.

For a code example that uses the PKEY\_AudioEndpoint\_GUID property, see [Device Roles for DirectSound Applications](device-roles-for-directsound-applications.md).

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

 

 




