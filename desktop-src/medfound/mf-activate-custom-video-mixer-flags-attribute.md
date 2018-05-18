---
Description: 'Specifies how to create a custom mixer for the enhanced video renderer (EVR).'
ms.assetid: '00e65718-885f-4e1f-9b06-66c7f5786851'
title: 'MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_FLAGS attribute'
---

# MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_FLAGS attribute

Specifies how to create a custom mixer for the enhanced video renderer (EVR).

## Data type

**UINT32**

## Remarks

You can set this attribute on the [**IMFActivate**](imfactivate.md) pointer obtained from the [**MFCreateVideoRendererActivate**](mfcreatevideorendereractivate.md) function. The value of this attribute is a bitwise **OR** of the following values.



| Value                                      | Description                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MF\_ACTIVATE\_CUSTOM\_MIXER\_ALLOWFAIL** | If the [**IMFActivate::ActivateObject**](imfactivate-activateobject.md) method fails to create the application's custom mixer, it uses the default EVR mixer instead. By default, if the [**IMFActivate**](imfactivate.md) object fails when it tries to create the custom mixer, the **ActivateObject** method fails. |



 

Applications can use the [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID**](mf-activate-custom-video-mixer-clsid-attribute.md) attribute to specify a custom mixer for the EVR.

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 




