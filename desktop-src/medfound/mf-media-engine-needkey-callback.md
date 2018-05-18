---
Description: 'Attribute which is passed in the IMFMediaEngineNeedKeyNotify to the media engine on creation.'
ms.assetid: 'B9625B3C-00AC-4F46-BD76-5C77822F5829'
title: 'MF\_MEDIA\_ENGINE\_NEEDKEY\_CALLBACK attribute'
---

# MF\_MEDIA\_ENGINE\_NEEDKEY\_CALLBACK attribute

Attribute which is passed in the [**IMFMediaEngineNeedKeyNotify**](imfmediaengineneedkeynotify.md) to the media engine on creation.

## Data type

**IMFMediaEngineNeedKeyNotify\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](imfattributes-getunknown.md).

To set this attribute, call [**IMFAttributes::SetUnknown**](imfattributes-setunknown.md).

## Remarks

The value of this attribute is a pointer to the [**IMFMediaEngineNeedKeyNotify**](imfmediaengineneedkeynotify.md) interface, implemented by the application.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                      |
| IDL<br/>                      | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




