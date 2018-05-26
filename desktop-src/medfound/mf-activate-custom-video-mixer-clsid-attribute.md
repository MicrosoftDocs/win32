---
Description: CLSID of a custom video mixer for the enhanced video renderer (EVR) media sink.
ms.assetid: a3586e6f-a2a2-4932-8b43-a076f64c5958
title: MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID attribute

CLSID of a custom video mixer for the enhanced video renderer (EVR) media sink.

## Data type

**GUID**

## Remarks

If you are creating the EVR through an activation object, you can use this attribute to set a custom video mixer on the EVR. Use this attribute as follows:

1.  Call the [**MFCreateVideoRendererActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatevideorendereractivate?branch=master) function to create an activation object for the EVR. The function returns a pointer to the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) interface.

2.  Set this attribue on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointer by calling [**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master). The value of the attribute is the CLSID of the application's custom video mixer.

If this attribute is set, the EVR calls **CoCreateInstance** with the specified CLSID to create the custom video mixer. The video mixer must expose the [**IMFTransform**](/windows/win32/mftransform/nn-mftransform-imftransform?branch=master) interface. The mixer is created as an in-process COM server.

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

[**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master)
</dt> <dt>

[**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master)
</dt> <dt>

[**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 




