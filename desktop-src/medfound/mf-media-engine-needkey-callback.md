---
Description: Attribute which is passed in the IMFMediaEngineNeedKeyNotify to the media engine on creation.
ms.assetid: B9625B3C-00AC-4F46-BD76-5C77822F5829
title: MF\_MEDIA\_ENGINE\_NEEDKEY\_CALLBACK attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MEDIA\_ENGINE\_NEEDKEY\_CALLBACK attribute

Attribute which is passed in the [**IMFMediaEngineNeedKeyNotify**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediaengineneedkeynotify?branch=master) to the media engine on creation.

## Data type

**IMFMediaEngineNeedKeyNotify\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Remarks

The value of this attribute is a pointer to the [**IMFMediaEngineNeedKeyNotify**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediaengineneedkeynotify?branch=master) interface, implemented by the application.

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

 

 




