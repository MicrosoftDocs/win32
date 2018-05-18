---
Description: 'CLSID of a custom video mixer for the enhanced video renderer (EVR) media sink.'
ms.assetid: 'a3586e6f-a2a2-4932-8b43-a076f64c5958'
title: 'MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID attribute'
---

# MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID attribute

CLSID of a custom video mixer for the enhanced video renderer (EVR) media sink.

## Data type

**GUID**

## Remarks

If you are creating the EVR through an activation object, you can use this attribute to set a custom video mixer on the EVR. Use this attribute as follows:

1.  Call the [**MFCreateVideoRendererActivate**](mfcreatevideorendereractivate.md) function to create an activation object for the EVR. The function returns a pointer to the [**IMFActivate**](imfactivate.md) interface.

2.  Set this attribue on the [**IMFActivate**](imfactivate.md) pointer by calling [**IMFAttributes::SetGUID**](imfattributes-setguid.md). The value of the attribute is the CLSID of the application's custom video mixer.

If this attribute is set, the EVR calls **CoCreateInstance** with the specified CLSID to create the custom video mixer. The video mixer must expose the [**IMFTransform**](imftransform.md) interface. The mixer is created as an in-process COM server.

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

[**IMFAttributes::GetGUID**](imfattributes-getguid.md)
</dt> <dt>

[**IMFAttributes::SetGUID**](imfattributes-setguid.md)
</dt> <dt>

[**IMFActivate**](imfactivate.md)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 




