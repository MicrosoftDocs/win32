---
Description: 'Contains a pointer to the IMFMediaEngineExtension interface.'
ms.assetid: 'D2F3F41D-086A-4DEB-99D0-07574BC8F0D7'
title: 'MF\_MEDIA\_ENGINE\_EXTENSION attribute'
---

# MF\_MEDIA\_ENGINE\_EXTENSION attribute

Contains a pointer to the [**IMFMediaEngineExtension**](imfmediaengineextension.md) interface.

## Data type

**IMFMediaEngineExtension\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md).

To set this attribute, call [**IMFAttributes::SetUnknown**](imfattributes-setunknown.md).

## Remarks

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](imfmediaengineclassfactory-createinstance.md) method to initialize the Media Engine.

This attribute is optional. Use it to provide an object that implements the [**IMFMediaEngineExtension**](imfmediaengineextension.md) interface. This interface enables the application to load custom media resources.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




