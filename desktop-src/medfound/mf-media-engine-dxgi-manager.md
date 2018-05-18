---
Description: 'Sets the Microsoft DirectX Graphics Infrastructure (DXGI) Device Manager on the Media Engine.'
ms.assetid: 'CB952492-0ACF-4501-BD8B-133E26FCE8F7'
title: 'MF\_MEDIA\_ENGINE\_DXGI\_MANAGER attribute'
---

# MF\_MEDIA\_ENGINE\_DXGI\_MANAGER attribute

Sets the Microsoft DirectX Graphics Infrastructure (DXGI) Device Manager on the Media Engine.

## Data type

**IMFDXGIDeviceManager\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md).

To set this attribute, call [**IMFAttributes::SetUnknown**](imfattributes-setunknown.md).

## Remarks

The value of this attribute is a pointer to the [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) interface.

In frame-server mode, this attribute enables the Media Engine to use hardware acceleration for video decoding and video processing. If the attribute is not set, the Media Engine uses software decoding and processing.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFMediaEngineClassFactory::CreateInstance**](imfmediaengineclassfactory-createinstance.md)
</dt> </dl>

 

 




