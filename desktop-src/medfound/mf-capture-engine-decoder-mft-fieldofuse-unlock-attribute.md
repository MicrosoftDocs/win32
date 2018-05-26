---
Description: Enables the capture engine to use a decoder that has field-of-use restrictions.
ms.assetid: EDE6D207-FD84-4DEB-9BF5-0952C454B00F
title: MF\_CAPTURE\_ENGINE\_DECODER\_MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_CAPTURE\_ENGINE\_DECODER\_MFT\_FIELDOFUSE\_UNLOCK\_Attribute attribute

Enables the capture engine to use a decoder that has field-of-use restrictions.

## Data type

**IUnknown\***

## Remarks

The value of this attribute is a pointer to the [**IMFFieldOfUseMFTUnlock**](/windows/win32/mfidl/nn-mfidl-imffieldofusemftunlock?branch=master) interface, implemented by the caller. The caller's implementation of this interface is expected to perform a handshake with the decoder, as described in [Field of Use Restrictions](field-of-use-restrictions.md). Microsoft Media Foundation does not define the handshake—typically, it would involve some sort of cryptographic exchange.

Internally, the capture engine sets the [**IMFFieldOfUseMFTUnlock**](/windows/win32/mfidl/nn-mfidl-imffieldofusemftunlock?branch=master) pointer on the decoder by setting the decoder's [MFT\_FIELDOFUSE\_UNLOCK\_Attribute](mft-fieldofuse-unlock-attribute.md) attribute.

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

[**IMFCaptureEngine::Initialize**](/windows/win32/mfcaptureengine/nf-mfcaptureengine-imfcaptureengine-initialize?branch=master)
</dt> </dl>

 

 




