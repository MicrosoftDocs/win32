---
Description: 'Enables the capture engine to use an encoder that has field-of-use restrictions.'
ms.assetid: '28421875-9629-4F14-8159-2D86012F517F'
title: 'MF\_CAPTURE\_ENGINE\_ENCODER\_MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute'
---

# MF\_CAPTURE\_ENGINE\_ENCODER\_MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute

Enables the capture engine to use an encoder that has field-of-use restrictions.

## Data type

**IUnknown\***

## Remarks

The value of this attribute is a pointer to the [**IMFFieldOfUseMFTUnlock**](imffieldofusemftunlock.md) interface, implemented by the caller. The caller's implementation of this interface is expected to perform a handshake with the encoder, as described in [Field of Use Restrictions](field-of-use-restrictions.md). Microsoft Media Foundation does not define the handshake—typically, it would involve some sort of cryptographic exchange.

Internally, the capture engine sets the [**IMFFieldOfUseMFTUnlock**](imffieldofusemftunlock.md) pointer on the encoder by setting the encoder's [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) attribute.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>Mfcaptureengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Capture Engine Attributes](capture-engine-attributes.md)
</dt> <dt>

[**IMFCaptureEngine::Initialize**](imfcaptureengine-initialize.md)
</dt> </dl>

 

 




