---
Description: 'For a media type that describes an MPEG-2 transport stream (TS), specifies whether the transport packets contain Content Packet headers.'
ms.assetid: '527B965D-4330-4DCB-B6DA-32D6BCDF5515'
title: 'MF\_MT\_MPEG2\_CONTENT\_PACKET attribute'
---

# MF\_MT\_MPEG2\_CONTENT\_PACKET attribute

For a media type that describes an MPEG-2 transport stream (TS), specifies whether the transport packets contain Content Packet headers.

## Data type

**UINT32**



| Value                                                                                                | Meaning                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | No Content Packet headers are added.<br/>                                                                                                                                                                    |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | At 200–1000 millisecond intervals, a 14-byte Content Packet header is added to the beginning of the transport packet, as defined by the Association of Radio Industries and Businesses (ARIB) standard.<br/> |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




