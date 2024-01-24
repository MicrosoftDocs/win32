---
description: Specifies an activation object that creates a custom video mixer for the enhanced video renderer (EVR) media sink.
ms.assetid: 60484f87-7588-4b52-93aa-ef8fad66d971
title: MF_ACTIVATE_CUSTOM_VIDEO_MIXER_ACTIVATE attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_ACTIVATE attribute

Specifies an activation object that creates a custom video mixer for the enhanced video renderer (EVR) media sink.

## Data type

**IUnknown\***

## Remarks

If you are creating the EVR through an activation object, you can use this attribute to set a custom video mixer on the EVR. Use this attribute as follows:

1.  Call the [**MFCreateVideoRendererActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatevideorendereractivate) function to create an activation object for the EVR. The function returns a pointer to the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface.
2.  Set this attribute on the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointer by calling [**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown). The value of the attribute is a pointer to an activation object implemented by the caller. The caller's activation object must expose the **IMFActivate** interface.

If you set this attribute, the EVR calls [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) to create the custom video mixer. The video mixer must expose the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Enhanced Video Renderer Attributes](enhanced-video-renderer-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown)
</dt> <dt>

[**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 




