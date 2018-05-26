---
Description: Target average volume level of a Windows Media Audio file.
ms.assetid: f81158c8-b341-4b39-8fa4-b510c93b89fc
title: MF\_MT\_AUDIO\_WMADRC\_AVGTARGET attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MT\_AUDIO\_WMADRC\_AVGTARGET attribute

Target average volume level of a Windows Media Audio file.

## Data type

**UINT32**

## Remarks

This attribute applies to audio media types for Windows Media Audio codecs. It specifies the target average volume level of the content. The decoder can use this value to perform dynamic range control.

The [**IMFASFContentInfo::ParseHeader**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-parseheader?branch=master) method adds this attribute to the media type if the ASF header contains the [**WM/WMADRCAverageTarget**](wmformat.wm_wmadrcaveragetarget) attribute. This attribute is documented in the Windows Media Format SDK documentation.

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

 

 




