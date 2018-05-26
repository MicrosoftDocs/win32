---
Description: Contains configuration properties for an encoder.
ms.assetid: f9bd8a50-e43e-4668-86a0-c9d5f517f4cf
title: MFT\_PREFERRED\_ENCODER\_PROFILE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_PREFERRED\_ENCODER\_PROFILE attribute

Contains configuration properties for an encoder.

## Data type

**[**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master)\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Applies to

[**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master)

## Remarks

This attribute can be set on the activation object returned by the [**MFCreateTransformActivate**](/windows/win32/mftransform/nf-mftransform-mfcreatetransformactivate?branch=master) function. The attribute applies only when the activation object is configured to create an encoder. The value of the attribute is a pointer to an attribute store, which itself contains properties to set on the encoder.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**MFCreateTransformActivate**](/windows/win32/mftransform/nf-mftransform-mfcreatetransformactivate?branch=master)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




