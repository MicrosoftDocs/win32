---
description: Configures a camera device source to be in either controlling mode or sharing mode.
title: MF_DEVSOURCE_ATTRIBUTE_FRAMESERVER_SHARE_MODE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/09/2022
---

# MF\_DEVSOURCE\_ATTRIBUTE\_FRAMESERVER\_SHARE\_MODES attribute

Configures a camera device source represented by an instance of [IMFMEdiaSource](/windows/win32/api/mfidl/nn-mfidl-imfmediasource) to be in either controlling mode or sharing mode.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

When this attribute is either not set or set to 0 value, the camera device source is configured in controlling mode.  This is the default mode for camera sources.  When in controlling mode, all camera operations are available and the application may change media types and/or extended camera controls.

Only one controlling mode instance of **IMFMediaSource** can be in an active state at any time. An **IMFMediaSource** is not considered active after it has been created an initialized. The media source only becomes active after the stream has been started, with a call to [IMFMediaSource::Start](/windows/win32/api/mfidl/nf-mfidl-imfmediasource-start), or after a camera control value is set either by the issuing of a camera control by calling [IKsControl::KsProperty](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-ikscontrol-ksproperty) with the property set [KSPROPERTYSETID_ExtendedCameraControl](/windows-hardware/drivers/stream/kspropertysetid-extendedcameracontrol) or by using the [IMFExtendedCameraControl](/windows/win32/api/mfidl/nn-mfidl-imfextendedcameracontrol) interface. For information on getting instance of **IMFExtendedCameraControl**, see [IMFExtendedCameraController](/windows/win32/api/mfidl/nn-mfidl-imfextendedcameracontroller)

Attempting to render active an **IMFMediaSource** instance when another controlling mode instance is already active will result in a sharing violation.

At any time there can be an arbitrary number of active sharing mode instances of **IMFMediaSource** and newly created sharing mode instances can be activated while a controlling mode instance is active. Sharing mode instances cannot change media types and must use the current media type in use. Sharing mode instances cannot change **KSPROPERTYSETID_ExtendedCameraControl** controls.  Legacy camera controls such as [PROPSETID_VIDCAP_CAMERACONTROL](/windows-hardware/drivers/stream/propsetid-vidcap-cameracontrol) and [PROPSETID_VIDCAP_VIDEOPROCAMP](/windows-hardware/drivers/stream/propsetid-vidcap-videoprocamp) and OEM/IHV-specific controls can be changed by sharing mode instances.

To configure a camera source to be in Sharing mode, the attribute must be set at the time of **IMFMediaSource** creation. 

### Configure sharing mode using MFCreateDeviceSource

The following code example illustrates creating an instance in sharing mode using [MFCreateDeviceSource](/windows/win32/api/mfidl/nf-mfidl-mfcreatedevicesource).

```cpp
HRESULT
SampleCreateSharedModeCamera(
    _In_z_ LPCWSTR cameraSymbolicName,
    _COM_Outptr_ IMFMediaSource** cameraSource
    )
{
    wil::com_ptr_nothrow<IMFAttributes>     initAttributes;

    RETURN_HR_IF_NULL (E_INVALIDARG, cameraSymbolicName);
    RETURN_HR_IF_NULL (E_POINTER, cameraSource);
    *cameraSource = nullptr;

    RETURN_IF_FAILED (MFCreateAttributes(&initAttributes, 3));
    RETURN_IF_FAILED (initAttributes->SetGUID(MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE, MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_GUID));
    RETURN_IF_FAILED (initAttributes->SetString(MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_SYMBOLIC_LINK, cameraSymbolicName));
    RETURN_IF_FAILED (initAttributes->SetUINT32(MF_DEVSOURCE_ATTRIBUTE_FRAMESERVER_SHARE_MODE, 1));
    RETURN_IF_FAILED (MFCreateDeviceSource(initAttributes.get(), cameraSource));

    return S_OK;
}
```

### Configure sharing mode using IMFActivate

The following example illustrates creating an **IMFMediaSource** instance using [IMFActivate](/windows/win32/api/mfobjects/nn-mfobjects-imfactivate). Note that The **IMFActivate** object will internally cache a newly created **IMFMediaSource** from the call to [ActivateObject](/windows/win32/api/mfobjects/nf-mfobjects-imfactivate-activateobject).  So if **ActivateObject** is called again before a call to [DetachObject](/windows/win32/api/mfobjects/nf-mfobjects-imfactivate-detachobject) is made, the cached instance will be returned and any changes to the attributes will be ignored.

```cpp
HRESULT
SampleCreateSharedModeCameraFromActivate(
    _In_ IMFActivate* activate,
    _COM_Outptr_ IMFMediaSource** cameraSource
    )
{
    RETURN_HR_IF_NULL (E_INVALIDARG, activate);
    RETURN_HR_IF_NULL (E_POINTER, cameraSource);
    *cameraSource = nullptr;

    RETURN_IF_FAILED (activate->SetUINT32(MF_DEVSOURCE_ATTRIBUTE_FRAMESERVER_SHARE_MODE, 1));
    RETURN_IF_FAILED (activate->ActivateObject(IID_PPV_ARGS(cameraSource)));

    return S_OK;
}
```

### Configure sharing mode using IMFCaptureEngine

To activate the **IMFMediaSource** in sharing mode using [IMFCaptureEngine](/windows/win32/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengine), the **IMFActivate** passed in for the camera source must have the **MF_DEVSOURCE_ATTRIBUTE_FRAMESERVER_SHARE_MODE** attribute. As stated above, after **IMFActivate::ActivateObject** is called, **DetachObject** must be called for any attribute changes to be reflected in the activated object.

### Configure sharing mode using MediaCapture

When accessing the camera using the [MediaCapture](/uwp/api/windows.media.capture.mediacapture) class, set sharing mode using the [MediaCaptureInitializationSettings.SharingMode](/uwp/api/windows.media.capture.mediacaptureinitializationsettings.sharingmode) property.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, build 26100<br/>                                         |
| Minimum supported server<br/> | Windows Server<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Audio/Video Capture](audio-video-capture.md)
</dt> <dt>

[Capture Device Attributes](capture-device-attributes.md)
</dt> </dl>

 

 




