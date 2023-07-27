---
description: The DVD Copy Protection property set provides authentication of copy protection information from hardware or software decrypters. Use this property set to prevent unauthorized copying from prerecorded DVD-Video.
ms.assetid: da3abefd-8f25-449d-8787-84d2cef928da
title: DVD Copy Protection Property Set (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Copy Protection Property Set

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The DVD Copy Protection property set provides authentication of copy protection information from hardware or software decrypters. Use this property set to prevent unauthorized copying from prerecorded DVD-Video.

Microsoft provides software that facilitates the authentication process required by the encryption scheme, thus enabling a DVD-ROM drive to authenticate and transfer keys with a DVD decrypter. Microsoft has no current plans to ship a DVD decrypter and, instead, is providing operating system code that will act as the agent to enable authentication of either hardware or software decrypters.

The DVD navigator initiates and controls the key exchange process. The DVD minidriver needs only to implement the following properties. Other components handle the rest.

Each DVD input stream will receive copy protection properties. This is true even if the same hardware controls all DVD streams.

The following information presents the necessary constants and data types to use for this property set in calls to [**IKsPropertySet**](ikspropertyset.md) methods. It provides values for the **GUID** (*guidPropSet*), property ID (*dwPropID*), and property data type (*pPropData*) parameters.



| Label | Value |
|-------------------|---------------------------|
| Property Set GUID | AM\_KSPROPSETID\_CopyProt |



 




| Property ID | Description | 
|-------------|-------------|
| <a href="am-property-copy-analog-component-property.md"><strong>AM_PROPERTY_COPY_ANALOG_COMPONENT</strong></a> | Queries whether the video output is standard-definition, analog component video. | 
| AM_PROPERTY_COPY_MACROVISION | This is a set-only property. This property sets the analog copy protection level for the NTSC encoder on the output end of the receiving pin. Uses <a href="/previous-versions/ms778996(v=vs.85)"><strong>AM_COPY_MACROVISION</strong></a>. | 
| AM_PROPERTY_DVDCOPY_CHLG_KEY | Both get and set operations are supported on this property. A get operation requests the decoder to provide its bus challenge key. A set operation provides the decoder with the bus challenge key from the DVD drive. The data passed in this property will be a structure of type <a href="/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-am_dvdcopy_chlgkey"><strong>AM_DVDCOPY_CHLGKEY</strong></a>. | 
| AM_PROPERTY_DVDCOPY_DEC_KEY2 | This is a get-only property. This property requests that the decoder's bus key 2 be transferred to the DVD drive. The data passed will be a structure of type <a href="/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-am_dvdcopy_buskey"><strong>AM_DVDCOPY_BUSKEY</strong></a>. | 
| AM_PROPERTY_DVDCOPY_DISC_KEY | Set-only property. This provides disc key. The key is a structure of type <a href="/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-am_dvdcopy_disckey"><strong>AM_DVDCOPY_DISCKEY</strong></a>. | 
| AM_PROPERTY_DVDCOPY_DVD_KEY1 | This is a set-only property. This property provides the DVD drive bus key 1 to the decoder. The data passed will be a structure of type <a href="/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-am_dvdcopy_buskey"><strong>AM_DVDCOPY_BUSKEY</strong></a>. | 
| AM_PROPERTY_DVDCOPY_REGION | Region code requests the region definition that the decoder is allowed to play in as defined by the DVD consortium. This region is defined as a <a href="/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-dvd_region"><strong>DVD_REGION</strong></a> structure. | 
| AM_PROPERTY_DVDCOPY_SET_COPY_STATE | Both get and set are supported on this property. Get is called first to determine if authentication is required. The set properties are indications as to which phase of copy protection negotiation the filter is entering. The data passed will be a structure of type <a href="/previous-versions/windows/desktop/api/Dvdmedia/ns-dvdmedia-am_dvdcopy_set_copy_state"><strong>AM_DVDCOPY_SET_COPY_STATE</strong></a>. | 
| AM_PROPERTY_DVDCOPY_SUPPORTS_NEW_KEYCOUNT | If this property is <strong>TRUE</strong>, the DVD Navigator does not send <strong>AM_UseNewCSSKey</strong> samples before negotiating the disc key. See <a href="/windows/win32/api/strmif/ns-strmif-am_sample2_properties"><strong>AM_SAMPLE2_PROPERTIES</strong></a>.<br /> Read-only. The property data is a <strong>BOOL</strong> value.<br /><blockquote>[!Note]<br />Applies to Windows 7.</blockquote><br /> | 
| AM_PROPERTY_DVDCOPY_TITLE_KEY | This is a set-only property. This provides title key from current content. The key is a structure of type <a href="/previous-versions/windows/desktop/api/Dvdmedia/ns-dvdmedia-am_dvdcopy_titlekey"><strong>AM_DVDCOPY_TITLEKEY</strong></a>. | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 




