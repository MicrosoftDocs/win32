---
description: The PKEY\_AudioEndpoint\_StableId property supplies an opaque identifier for an audio endpoint. Windows attempts to preserve this identifier across operating system and audio driver updates.
title: PKEY_AudioEndpoint_StableId (Mmdeviceapi.h)
ms.topic: reference
ms.date: 08/26/2026
---

# PKEY\_AudioEndpoint\_StableId

The **PKEY\_AudioEndpoint\_StableId** property supplies an additional, opaque identifier for an audio endpoint.  Windows attempts to preserve this identifier across operating system updates and audio driver updates.

The ordinary endpoint ID that is returned by [**IMMDevice::GetId**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-getid) is not stable. An operating system update or an audio driver update can cause the same physical peripheral to be assigned a different endpoint ID. As a result, an app cannot use the ordinary endpoint ID to reliably track a physical audio endpoint. The **PKEY\_AudioEndpoint\_StableId** property, when available, can be used to track a physical audio endpoint. An example scenario is a communications app that remembers the microphone or speaker that the user selected and restores that selection in a later session.

The **vt** member of the **PROPVARIANT** structure is set to VT\_LPWSTR.

The **pwszVal** member of the **PROPVARIANT** structure points to a null-terminated, wide-character string that contains the stable identifier for the audio endpoint device. If the endpoint has no stable ID, the property value is VT\_EMPTY. Not every endpoint is guaranteed to have a stable ID.

## Remarks

Treat the property value as an opaque, case-sensitive string, and compare it case-sensitively. Do not modify, normalize, reconstruct, or parse the value, and do not extract or rely on any internal substring. The internal format of the string is an implementation detail. Cache the value only to identify the same endpoint again later.

Do not treat the stable ID as an immutable identifier for all characteristics of the device. Other endpoint properties—for example, the friendly name and the format characteristics—can change while the stable ID stays the same. After you resolve the device from a cached stable ID, re-query any mutable properties that your app depends on.

The stable ID is more durable than the ordinary endpoint ID, but it is not guaranteed to never change. Windows attempts to preserve it across operating system and audio driver updates. Windows' ability to preserve this value depends on the behavior of the audio driver, the peripheral firmware, the bus type (for example, USB and Bluetooth), and the information that the peripheral exposes. A small percentage of peripherals might receive a different stable ID after an operating system or driver upgrade.

An app must handle each of the following cases:

-   The property value is VT\_EMPTY.
-   The property-store read fails.
-   A cached stable ID no longer resolves to an endpoint through [**IMMDeviceEnumerator::GetDevice**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdevice).

### Retrieving the stable ID

To retrieve the stable ID for the endpoint that the user selected, do the following:

1.  Start with an [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface for the selected endpoint.
2.  Call the [**IMMDevice::OpenPropertyStore**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-openpropertystore) method with the STGM\_READ flag.
3.  Call the **IPropertyStore::GetValue** method with the PKEY\_AudioEndpoint\_StableId property key.
4.  If the **vt** member of the returned **PROPVARIANT** is VT\_LPWSTR, persist the entire **pwszVal** string.
5.  If the property is unavailable or is not VT\_LPWSTR (for example, on an older version of Windows, or when the value is VT\_EMPTY), you can optionally fall back to [**IMMDevice::GetId**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-getid). Note that the fallback value is less durable and can become stale after operating system or audio driver updates.

The following example retrieves and persists the stable ID.

```C++
wil::unique_cotaskmem_string deviceId;
wil::com_ptr_nothrow<IPropertyStore> propertyStore;
if (SUCCEEDED(userSelectedEndpoint->OpenPropertyStore(STGM_READ, &propertyStore)))
{
    wil::unique_prop_variant var;
    if (SUCCEEDED(propertyStore->GetValue(PKEY_AudioEndpoint_StableId, &var)))
    {
        if (var.vt == VT_LPWSTR)
        {
            deviceId.reset(var.release().pwszVal);
        }
    }
}
```

### Restoring the device later

To restore the device in a later session, create an **MMDeviceEnumerator** object by calling **CoCreateInstance**, and then pass the cached stable-ID string as the *pwstrId* argument to the [**IMMDeviceEnumerator::GetDevice**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdevice) method to get the [**IMMDevice**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdevice) interface back. Handle the failure case in which no matching endpoint is found.

```C++
HRESULT GetUserAudioEndpoint(_In_ PCWSTR endpointStableId, _COM_Outptr_ IMMDevice** userSelectedEndpoint)
{
    *userSelectedEndpoint = nullptr;
    wil::com_ptr_nothrow<IMMDeviceEnumerator> enumerator;
    RETURN_IF_FAILED(CoCreateInstance(__uuidof(MMDeviceEnumerator), nullptr, CLSCTX_ALL, IID_PPV_ARGS(&enumerator)));
    RETURN_IF_FAILED(enumerator->GetDevice(endpointStableId, userSelectedEndpoint));
    return S_OK;
}
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 24H2 (build 26100) \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2025 (build 26100) \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mmdeviceapi.h</dt> </dl> |



## See also

<dl> <dt>

[**Audio Endpoint Properties**](audio-endpoint-properties.md)
</dt> <dt>

[Core Audio Properties](core-audio-properties.md)
</dt> <dt>

[**IMMDevice::OpenPropertyStore**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-openpropertystore)
</dt> <dt>

[**IMMDeviceEnumerator::GetDevice**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdevice)
</dt> <dt>

[**IMMDevice::GetId**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-getid)
</dt> <dt>

[Endpoint ID Strings](endpoint-id-strings.md)
</dt> </dl>

 

 




