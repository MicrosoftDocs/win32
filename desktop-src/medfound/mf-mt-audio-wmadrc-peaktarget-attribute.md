---
Description: 'Target peak volume level of a Windows Media Audio file.'
ms.assetid: '73f4e763-dcb7-48cd-ab80-37635d973da0'
title: 'MF\_MT\_AUDIO\_WMADRC\_PEAKTARGET attribute'
---

# MF\_MT\_AUDIO\_WMADRC\_PEAKTARGET attribute

Target peak volume level of a Windows Media Audio file.

## Data type

**UINT32**

## Remarks

This attribute applies to audio media types for Windows Media Audio codecs. It specifies the target peak volume level of the content. The decoder can use this value to perform dynamic range control.

The [**IMFASFContentInfo::ParseHeader**](imfasfcontentinfo-parseheader.md) method adds this attribute to the media type if the ASF header contains the [**WM/WMADRCPeakTarget**](wmformat.wm_wmadrcpeaktarget) attribute. This attribute is documented in the Windows Media Format SDK documentation.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFMediaType**](imfmediatype.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




