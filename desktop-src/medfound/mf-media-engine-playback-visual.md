---
Description: Sets a Microsoft DirectComposition visual as the playback region for the Media Engine.
ms.assetid: C381D28E-B7A1-4A1A-9F8D-42A4ABB1C633
title: MF\_MEDIA\_ENGINE\_PLAYBACK\_VISUAL attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MEDIA\_ENGINE\_PLAYBACK\_VISUAL attribute

Sets a Microsoft DirectComposition visual as the playback region for the Media Engine.

## Data type

**IDCompositionVisual\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown).

## Remarks

For more information on DirectComposition, see [DirectComposition](https://msdn.microsoft.com/40e2d02b-77e8-425f-ac5e-3dcddef08173) and [**IDCompositionVisual**](https://msdn.microsoft.com/462dfc20-ad5a-425c-94b5-f21ab05f5af8).

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance) method to initialize the Media Engine.

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

 

 




