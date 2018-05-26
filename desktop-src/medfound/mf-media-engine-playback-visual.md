---
Description: Sets a Microsoft DirectComposition visual as the playback region for the Media Engine.
ms.assetid: C381D28E-B7A1-4A1A-9F8D-42A4ABB1C633
title: MF\_MEDIA\_ENGINE\_PLAYBACK\_VISUAL attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MEDIA\_ENGINE\_PLAYBACK\_VISUAL attribute

Sets a Microsoft DirectComposition visual as the playback region for the Media Engine.

## Data type

**IDCompositionVisual\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Remarks

For more information on DirectComposition, see [DirectComposition](directcomp.directcomposition_portal) and [**IDCompositionVisual**](directcomp.idcompositionvisual).

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/win32/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance?branch=master) method to initialize the Media Engine.

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

 

 




