---
description: ASF Attributes
ms.assetid: c1570669-6e9c-4614-af4d-2a148f12e36f
title: ASF Attributes
ms.topic: article
ms.date: 05/31/2018
---

# ASF Attributes

### Profile Attributes

The following attributes apply to ASF profiles.



| Attribute                                                                      | Description                                                  |
|--------------------------------------------------------------------------------|--------------------------------------------------------------|
| [**MF\_ASFPROFILE\_MAXPACKETSIZE**](mf-asfprofile-maxpacketsize-attribute.md) | Specifies the maximum packet size for an ASF file, in bytes. |
| [**MF\_ASFPROFILE\_MINPACKETSIZE**](mf-asfprofile-minpacketsize-attribute.md) | Specifies the minimum packet size for an ASF file, in bytes. |



 

### Stream Configuration Attributes

The following attributes apply to the ASF stream configuration object.



| Attribute                                                                              | Description                                                                   |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md) | Sets the average "leaky bucket" parameters for encoding a Windows Media file. |
| [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md) | Sets the peak "leaky bucket" parameters for encoding a Windows Media file.    |



 

### Media Buffer Attributes

The following attributes apply to media buffers for ASF packets.



| Attribute                                                                          | Description                                                                               |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**MFASFSPLITTER\_PACKET\_BOUNDARY**](mfasfsplitter-packet-boundary-attribute.md) | Specifies whether a buffer contains the start of an Advanced Systems Format (ASF) packet. |



 

### Presentation Descriptor Attributes

For a list of attributes that apply to ASF presentation descriptors, see [Presentation Descriptor Attributes](presentation-descriptor-attributes.md).

## Related topics

<dl> <dt>

[**IMFASFProfile**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfprofile)
</dt> <dt>

[**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 



