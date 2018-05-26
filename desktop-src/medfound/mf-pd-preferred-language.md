---
Description: Contains the preferred RFC 1766 language of the media source.
ms.assetid: 30f99804-6aea-473b-9bbf-e8c715501391
title: MF\_PD\_PREFERRED\_LANGUAGE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_PD\_PREFERRED\_LANGUAGE attribute

Contains the preferred RFC 1766 language of the media source.

## Data type

**WCHAR**

## Get/set

To get this attribute, call [**IMFAttributes::GetString**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getstring?branch=master).

To set this attribute, call [**IMFAttributes::Settring**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setstring?branch=master).

## Applies to

[**IMFPresentationDescriptor**](/windows/win32/mfidl/nn-mfidl-imfpresentationdescriptor?branch=master)

## Remarks

The MF\_PD\_PREFERRED\_LANGUAGE attribute is optional. An application can set this attribute on a media source (such as a network source) to specify its preferred language.

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

 

 




