---
Description: Contains the identifier of the playlist element in the presentation.
ms.assetid: 355818cf-1e00-46ad-9ce1-ab3a178164f9
title: MF\_PD\_PLAYBACK\_ELEMENT\_ID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_PLAYBACK\_ELEMENT\_ID attribute

Contains the identifier of the playlist element in the presentation.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies to

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)

## Remarks

Media sources that deliver playlists can optionally set this attribute on their presentation descriptors.

When a media source delivers a playlist, it sends a [MENewPresentation](menewpresentation.md) event for each playlist element after the first. This event contains a presentation descriptor for the new playlist element. The media source can assign identifiers to the elements by setting the MF\_PD\_PLAYBACK\_ELEMENT\_ID attribute on each presentation descriptor, including the one created by [**IMFMediaSource::CreatePresentationDescriptor**](/windows/win32/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor?branch=master).

A media source might also send the [MENewPresentation](menewpresentation.md) event because of a dynamic stream switch or a change in the number of streams. In that situation, the value of MF\_PD\_PLAYBACK\_ELEMENT\_ID should remain the same across both presentations, to indicate that both presentations represent the same playlist element. If two consecutive presentations have the same value for this attribute, the Microsoft Media Foundation pipeline expects the time stamps to remain continuous across the transition. Therefore, the media source must not use the [MF\_EVENT\_SOURCE\_ACTUAL\_START](mf-event-source-actual-start-attribute.md) attribute when it transitions to the next presentation.

Media sources that implement [**IMFMediaSourceTopologyProvider**](/windows/win32/mfidl/nn-mfidl-imfmediasourcetopologyprovider?branch=master) should use the [MF\_TOPONODE\_SEQUENCE\_ELEMENTID](mf-toponode-sequence-elementid-attribute.md) attribute rather than the MF\_PD\_PLAYBACK\_ELEMENT\_ID attribute.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> </dl>

 

 




