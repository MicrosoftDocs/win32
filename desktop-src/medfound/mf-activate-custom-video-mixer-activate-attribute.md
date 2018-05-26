---
Description: Specifies an activation object that creates a custom video mixer for the enhanced video renderer (EVR) media sink.
ms.assetid: 60484f87-7588-4b52-93aa-ef8fad66d971
title: MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_ACTIVATE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_ACTIVATE attribute

Specifies an activation object that creates a custom video mixer for the enhanced video renderer (EVR) media sink.

## Data type

**IUnknown\***

## Remarks

If you are creating the EVR through an activation object, you can use this attribute to set a custom video mixer on the EVR. Use this attribute as follows:

1.  Call the [**MFCreateVideoRendererActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatevideorendereractivate?branch=master) function to create an activation object for the EVR. The function returns a pointer to the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) interface.
2.  Set this attribute on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointer by calling [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master). The value of the attribute is a pointer to an activation object implemented by the caller. The caller's activation object must expose the **IMFActivate** interface.

If you set this attribute, the EVR calls [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master) to create the custom video mixer. The video mixer must expose the [**IMFTransform**](/windows/win32/mftransform/nn-mftransform-imftransform?branch=master) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
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

[**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master)
</dt> <dt>

[**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 




