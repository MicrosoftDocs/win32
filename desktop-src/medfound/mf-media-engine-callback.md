---
Description: 'Contains a pointer to the callback interface for the Media Engine.'
ms.assetid: '5FAEF29A-B978-410A-8F5B-EB6F7E35EE6D'
title: 'MF\_MEDIA\_ENGINE\_CALLBACK attribute'
---

# MF\_MEDIA\_ENGINE\_CALLBACK attribute

Contains a pointer to the callback interface for the Media Engine.

## Data type

**IMFMediaEngineNotify\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md).

To set this attribute, call [**IMFAttributes::SetUnknown**](imfattributes-setunknown.md).

## Remarks

The value of this attribute is a pointer to the [**IMFMediaEngineNotify**](imfmediaenginenotify.md) interface, implemented by the application.

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](imfmediaengineclassfactory-createinstance.md) method to initialize the Media Engine. The attribute is required.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFMediaEngineClassFactory::CreateInstance**](imfmediaengineclassfactory-createinstance.md)
</dt> <dt>

[**IMFMediaEngineNotify**](imfmediaenginenotify.md)
</dt> </dl>

 

 




