---
description: Sets the Microsoft DirectX Graphics Infrastructure (DXGI) Device Manager on the Media Engine.
ms.assetid: CB952492-0ACF-4501-BD8B-133E26FCE8F7
title: MF_MEDIA_ENGINE_DXGI_MANAGER attribute (Mfmediaengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MEDIA\_ENGINE\_DXGI\_MANAGER attribute

Sets the Microsoft DirectX Graphics Infrastructure (DXGI) Device Manager on the Media Engine.

## Data type

**IMFDXGIDeviceManager\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown).

## Remarks

The value of this attribute is a pointer to the [**IMFDXGIDeviceManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfdxgidevicemanager) interface.

In frame-server mode, this attribute enables the Media Engine to use hardware acceleration for video decoding and video processing. If the attribute is not set, the Media Engine uses software decoding and processing.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFMediaEngineClassFactory::CreateInstance**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance)
</dt> </dl>

 

 




