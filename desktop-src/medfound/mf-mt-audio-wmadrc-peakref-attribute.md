---
Description: Reference peak volume level of a Windows Media Audio file.
ms.assetid: bb762f9c-cf08-4d32-991e-490eb7b1f579
title: MF\_MT\_AUDIO\_WMADRC\_PEAKREF attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AUDIO\_WMADRC\_PEAKREF attribute

Reference peak volume level of a Windows Media Audio file.

## Data type

**UINT32**

## Remarks

This attribute applies to audio media types for Windows Media Audio codecs. It specifies the original peak volume level of the content. The decoder can use this value to perform dynamic range control.

The [**IMFASFContentInfo::ParseHeader**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-parseheader?branch=master) method adds this attribute to the media type if the ASF header contains the [**WM/WMADRCPeakReference**](wmformat.wm_wmadrcpeakreference) attribute. This attribute is documented in the Windows Media Format SDK documentation.

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

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFMediaType**](/windows/win32/mfobjects/nn-mfobjects-imfmediatype?branch=master)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




