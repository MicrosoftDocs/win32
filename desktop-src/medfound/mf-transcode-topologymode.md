---
Description: 'Specifies for a transcode topology whether the topology loader will load hardware-based transforms.'
ms.assetid: '33db8621-114a-4531-908f-f30034441973'
title: 'MF\_TRANSCODE\_TOPOLOGYMODE attribute'
---

# MF\_TRANSCODE\_TOPOLOGYMODE attribute

Specifies for a transcode topology whether the topology loader will load hardware-based transforms.

The topology mode specifies whether hardware transforms (such as hardware codecs) may be used in the transcode topology. The application can store this attribute in a transcode profile by calling [**IMFTranscodeProfile::SetContainerAttributes**](imftranscodeprofile-setcontainerattributes.md).

## Data type

**[**MF\_TRANSCODE\_TOPOLOGYMODE\_FLAGS**](mf-transcode-topologymode-flags.md)** stored as **UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

This attribute is optional. It must have one of the following values.



| Value                                              | Description                                                                                                                                                                                                                                                                       |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MF\_TRANSCODE\_TOPOLOGYMODE\_HARDWARE\_ALLOWED** | The Topology Loader will load hardware-based MFTs, such as hardware decoders, when available.<br/> The Topology Loader automatically falls back to software decoding if no hardware decoder is found, or if a hardware decoder fails to connect for some reason.<br/> |
| **MF\_TRANSCODE\_TOPOLOGYMODE\_SOFTWARE\_ONLY**    | The Topology Loader will load only software MFTs, including software decoders.                                                                                                                                                                                                    |



 

The default value is **MF\_TRANSCODE\_TOPOLOGYMODE\_SOFTWARE\_ONLY**.

If the Topology Loader inserts a hardware MFT into the topology, it sets the [MFT\_ENUM\_HARDWARE\_URL\_Attribute](mft-enum-hardware-url-attribute.md) attribute on the topology node. To check whether a hardware MFT is present, enumerate the nodes in the resolved topology and check whether this attribute is present.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transcode API](transcode-api.md)
</dt> <dt>

[**IMFTranscodeProfile::GetContainerAttributes**](imftranscodeprofile-getcontainerattributes.md)
</dt> <dt>

[**IMFTranscodeProfile::SetContainerAttributes**](imftranscodeprofile-setcontainerattributes.md)
</dt> </dl>

 

 




