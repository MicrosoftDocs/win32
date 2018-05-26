---
Description: Specifies how to create a custom presenter for the enhanced video renderer (EVR).
ms.assetid: 40893e13-bf2e-4424-ae43-2b253fc0b622
title: MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_FLAGS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_FLAGS attribute

Specifies how to create a custom presenter for the enhanced video renderer (EVR).

## Data type

**UINT32**

## Remarks

You can set this attribute on the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointer obtained from the [**MFCreateVideoRendererActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatevideorendereractivate?branch=master) function. The value of this attribute is a bitwise **OR** of the following values.



| Value                                          | Description                                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MF\_ACTIVATE\_CUSTOM\_PRESENTER\_ALLOWFAIL** | If the [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master) method fails to create the application's custom presenter, it uses the default EVR presenter instead. By default, if the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) object fails when it tries to create the custom presenter, the **ActivateObject** method fails. |



 

Applications can use the [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_PRESENTER\_CLSID**](mf-activate-custom-video-presenter-clsid-attribute.md) attribute to specify a custom presenter for the EVR.

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

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> <dt>

[How to Write an EVR Presenter](how-to-write-an-evr-presenter.md)
</dt> </dl>

 

 




